#!/usr/bin/env python3
"""
score.py — the scoring engine for us-fishing-advisor.

Takes conditions (water temperature + trend, flow/turbidity, time-of-day, wind/
cloud) and scores every requested species 0-100, using the weights and evidence-
tiered logic in references/species.yaml. Mirrors the "score per species, not per
day" discipline in SKILL.md rule 5 — this never produces one blended "how's fishing
today" number.

Does NOT fetch its own data — conditions come from a JSON file assembled from
us-weather-advisor's output (see --conditions). This script only interprets.

Usage:
    python3 score.py --species-file ../references/species.yaml \\
        --conditions conditions.json --time-of-day dawn --json out.json

conditions.json shape:
{
  "water_type": "river" | "lake",
  "water_temp_f": 68.5,
  "water_temp_source": "measured" | "estimated",
  "water_temp_trend_72h_f": -1.2,
  "flow_rise_pct_72h": 12,       // null/omit if lake or unknown
  "wind_mph": 8,
  "sky_cover_pct": 40,
  "date": "2026-08-27",          // for seasonal-phase and lead-day confidence
  "query_date": "2026-08-20"     // today, for lead-day confidence in WINDOW mode
}
"""
import argparse
import datetime
import json
import sys

try:
    import yaml
except ImportError:
    yaml = None


def load_species(path):
    if yaml is None:
        raise SystemExit("PyYAML is required (pip install pyyaml) to read species.yaml")
    with open(path) as f:
        data = yaml.safe_load(f)
    return data["species"], data["weights"]


def temperature_position_score(temp_f, opt_min, opt_max, stop, upper_stress):
    """0-1 score for where temp_f sits on the species' feeding curve."""
    if opt_min is None or opt_max is None:
        return None  # not enough data — caller must treat as unknown, not zero
    if stop is not None and temp_f <= stop:
        return 0.02
    if opt_min <= temp_f <= opt_max:
        # peak in the middle of the band
        mid = (opt_min + opt_max) / 2
        half_width = (opt_max - opt_min) / 2 or 1
        return round(1.0 - 0.15 * (abs(temp_f - mid) / half_width), 2)
    if temp_f < opt_min:
        span = (opt_min - stop) if stop is not None else opt_min
        frac = max(0.0, (temp_f - (stop or 0)) / span) if span else 0.5
        return round(0.15 + 0.55 * frac, 2)
    # above opt_max
    ceiling = upper_stress if upper_stress is not None else opt_max + 15
    if temp_f >= ceiling:
        return 0.10
    span = ceiling - opt_max or 1
    frac = (temp_f - opt_max) / span
    return round(0.85 - 0.65 * frac, 2)


def trend_score(temp_f, trend_72h_f, opt_min, opt_max):
    """Rate-of-change matters independent of absolute position (evidence-tiers.md)."""
    if trend_72h_f is None or opt_min is None or opt_max is None:
        return 0.5, "trend unknown"
    warming = trend_72h_f > 0.3
    cooling = trend_72h_f < -0.3
    below_opt = temp_f < opt_min
    above_opt = temp_f > opt_max
    if below_opt and warming:
        return 0.85, f"warming toward optimum (+{trend_72h_f:.1f}F/72h) — can trigger feeding even below optimum"
    if above_opt and cooling:
        return 0.75, f"cooling back toward optimum ({trend_72h_f:.1f}F/72h)"
    if below_opt and cooling:
        return 0.25, f"cooling further below optimum ({trend_72h_f:.1f}F/72h) — suppresses feeding"
    if above_opt and warming:
        return 0.30, f"warming further past optimum (+{trend_72h_f:.1f}F/72h) — heat/oxygen stress risk"
    return 0.55, f"inside optimum, trend secondary ({trend_72h_f:+.1f}F/72h)"


def light_window_score(species, time_of_day):
    windows = species.get("active_windows") or []
    if not windows or windows == ["unknown"]:
        return 0.5, "no documented light-window data for this species — treated as neutral, not scored confidently"
    if time_of_day in windows:
        return 1.0, f"{time_of_day} is an active window for this species"
    return 0.35, f"{time_of_day} is outside this species' documented active windows ({', '.join(windows)})"


def turbidity_score(species, flow_rise_pct):
    if flow_rise_pct is None:
        return 0.5, "no flow data"
    reaction = species.get("turbidity", "neutral")
    rising = flow_rise_pct > 15
    if reaction == "benefits" and rising:
        return 0.8, f"rising/turbid water ({flow_rise_pct:+.0f}%/72h) — this species benefits from reduced visibility"
    if reaction == "neutral" and rising:
        return 0.55, f"rising water ({flow_rise_pct:+.0f}%/72h), neutral reaction for this species"
    if abs(flow_rise_pct) <= 15:
        return 0.55, f"flow stable ({flow_rise_pct:+.0f}%/72h)"
    return 0.4, f"flow rising ({flow_rise_pct:+.0f}%/72h), no documented benefit for this species"


def wind_cloud_score(wind_mph, sky_cover_pct):
    if wind_mph is None and sky_cover_pct is None:
        return 0.5, "no wind/cloud data"
    score = 0.5
    notes = []
    if sky_cover_pct is not None and sky_cover_pct > 60:
        score += 0.15
        notes.append(f"{sky_cover_pct:.0f}% cloud cover — lower light favors longer active windows")
    if wind_mph is not None and wind_mph > 20:
        score -= 0.15
        notes.append(f"{wind_mph:.0f} mph wind — likely too rough for comfortable/effective fishing")
    return round(max(0.0, min(1.0, score)), 2), "; ".join(notes) or "unremarkable"


def lead_days_confidence(query_date_str, target_date_str):
    try:
        q = datetime.date.fromisoformat(query_date_str)
        t = datetime.date.fromisoformat(target_date_str)
    except (ValueError, TypeError):
        return "medium"
    lead = (t - q).days
    if lead <= 2:
        return "high"
    if lead <= 5:
        return "medium"
    return "low"


# A species below its documented feeding-stop temperature is not "a bit worse" — it's
# effectively not feeding. Before 2026-08-21 `stop` only zeroed the temperature factor
# (35% of weight), so a stopped-out fish could still accumulate 53/100 from light window,
# trend, flow and wind and get recommended as viable. `stop` is a gate, not a factor:
# nothing else can rescue it, so the final score is capped rather than merely reduced.
STOPPED_SCORE_CAP = 12


def evaluate_hard_stop(species, water_temp):
    """Data-driven hard stop, read from species.yaml rather than hardcoded per species.

    Shape in species.yaml:
        hard_stop: {above: 79, reason: "..."}   # or {below: N, reason: "..."}

    Returns the reason string if the stop fires, else None. Before 2026-08-21 the only
    hard stop in the system was a muskellunge-specific `if key == "muskellunge"` branch
    in this file, which meant a species added via the skill's EXPAND mode had no way to
    declare a critical threshold without a code change.
    """
    hs = species.get("hard_stop")
    if not hs or water_temp is None:
        return None
    above, below = hs.get("above"), hs.get("below")
    reason = hs.get("reason") or "Hard stop declared in species.yaml with no reason given."
    if above is not None and water_temp >= above:
        return reason
    if below is not None and water_temp <= below:
        return reason
    return None


def score_species(key, species, conditions, time_of_day):
    temp = species.get("temperature", {})
    opt_min, opt_max = temp.get("opt_min"), temp.get("opt_max")
    stop, upper = temp.get("stop"), temp.get("upper_stress")

    water_temp = conditions.get("water_temp_f")
    factors = {}

    pos = temperature_position_score(water_temp, opt_min, opt_max, stop, upper) if water_temp is not None else None
    factors["temperature_position"] = {
        "value": pos if pos is not None else 0.5,
        "note": (f"{water_temp}F vs. optimum {opt_min}-{opt_max}F" if pos is not None
                 else "no documented optimum for this species — see species.yaml tier"),
        "weight": 0.35,
        "confident": pos is not None,
    }

    tr_val, tr_note = trend_score(water_temp, conditions.get("water_temp_trend_72h_f"), opt_min, opt_max) \
        if water_temp is not None else (0.5, "no water temp")
    factors["temperature_trend"] = {"value": tr_val, "note": tr_note, "weight": 0.15}

    lw_val, lw_note = light_window_score(species, time_of_day)
    factors["light_window"] = {"value": lw_val, "note": lw_note, "weight": 0.20}

    factors["seasonal_phase"] = {"value": 0.55, "note": "seasonal-phase modeling not yet built — neutral placeholder, see roadmap.md", "weight": 0.15}

    tb_val, tb_note = turbidity_score(species, conditions.get("flow_rise_pct_72h")) \
        if conditions.get("water_type") == "river" else (0.55, "still water — flow/turbidity factor doesn't apply")
    factors["flow_turbidity"] = {"value": tb_val, "note": tb_note, "weight": 0.10}

    wc_val, wc_note = wind_cloud_score(conditions.get("wind_mph"), conditions.get("sky_cover_pct"))
    factors["wind_cloud"] = {"value": wc_val, "note": wc_note, "weight": 0.05}

    total = sum(f["value"] * f["weight"] for f in factors.values())
    score = round(total * 100)

    # Apply the feeding-stop gate (see STOPPED_SCORE_CAP above). This is deliberately a
    # cap on the total, not another weighted factor — "this fish is not eating" cannot be
    # outvoted by a good light window.
    stopped_out = (
        water_temp is not None and stop is not None and water_temp <= stop
    )
    stop_note = None
    if stopped_out and score > STOPPED_SCORE_CAP:
        stop_note = (
            f"{water_temp}F is at or below this species' documented feeding-stop "
            f"temperature ({stop}F) — feeding is effectively off, so the score is capped "
            f"at {STOPPED_SCORE_CAP} regardless of how favorable the other factors look "
            f"(raw weighted score before the cap: {score})."
        )
        score = STOPPED_SCORE_CAP

    # confidence: degrade if key factors are undocumented, further degrade with lead time
    base_confidence = "high" if factors["temperature_position"]["confident"] else "medium"
    if conditions.get("query_date") and conditions.get("date"):
        lead_conf = lead_days_confidence(conditions["query_date"], conditions["date"])
        rank = {"high": 3, "medium": 2, "low": 1}
        base_confidence = min([base_confidence, lead_conf], key=lambda c: rank[c])
    if conditions.get("water_temp_source") == "estimated":
        rank = {"high": 3, "medium": 2, "low": 1}
        base_confidence = min([base_confidence, "medium"], key=lambda c: rank[c])

    hard_stop = evaluate_hard_stop(species, water_temp)

    return {
        "species": key,
        "common_name": species.get("common_name", key),
        "score": 0 if hard_stop else score,
        "confidence": "n/a — hard stop" if hard_stop else base_confidence,
        "hard_stop": hard_stop,
        "feeding_stop_note": stop_note,
        "factors": factors,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--species-file", required=True)
    ap.add_argument("--conditions", required=True)
    ap.add_argument("--time-of-day", required=True, choices=["dawn", "day", "dusk", "night", "unknown"])
    ap.add_argument("--species", type=str, help="comma-separated species keys; default = all")
    ap.add_argument("--json", required=True)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    all_species, weights = load_species(args.species_file)
    with open(args.conditions) as f:
        conditions = json.load(f)

    wanted = args.species.split(",") if args.species else list(all_species.keys())
    results = []
    unknown = []
    for key in wanted:
        key = key.strip()
        if key not in all_species:
            # Don't drop this silently — a typo'd or guessed key used to vanish without a
            # trace, so an answer could quietly omit the species the user actually asked
            # about. With 16 species in species.yaml the odds of a near-miss key are real.
            unknown.append(key)
            continue
        results.append(score_species(key, all_species[key], conditions, args.time_of_day))

    if unknown:
        msg = (f"Unrecognized --species key(s): {', '.join(unknown)}. "
               f"Not scored. Valid keys: {', '.join(sorted(all_species.keys()))}")
        print(f"WARNING: {msg}", file=sys.stderr)
        if not results:
            raise SystemExit(
                "No valid species to score — every key passed to --species was unrecognized."
            )

    results.sort(key=lambda r: r["score"], reverse=True)
    out = {
        "conditions": conditions,
        "time_of_day": args.time_of_day,
        "results": results,
        "unrecognized_species_keys": unknown,
    }
    with open(args.json, "w") as f:
        json.dump(out, f, indent=2)
    if not args.quiet:
        for r in results:
            if r["hard_stop"]:
                flag = " [HARD STOP]"
            elif r.get("feeding_stop_note"):
                flag = " [FEEDING STOPPED — capped]"
            else:
                flag = ""
            print(f"{r['common_name']:<22} {r['score']:>3}/100  ({r['confidence']}){flag}")


if __name__ == "__main__":
    main()
