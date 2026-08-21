#!/usr/bin/env python3
"""
fetch_water.py — river flow/water-temperature layer for us-weather-advisor.

Finds the nearest USGS gauge to a GPS point (within a bounding box) and pulls
current discharge, gauge height, and water temperature where available. No API key
needed. Rivers/streams only — USGS doesn't gauge most lakes/reservoirs, so for
still water this script reports "no gauge found" rather than guessing; the lake-
temperature ESTIMATE (air-temperature-driven proxy) is handled separately, not
here, and must always be labeled as an estimate downstream.

By default also pulls a recent-history window (--trend-days, default 3) and computes
a simple trend (latest reading minus earliest reading in the window) per variable per
site — this feeds us-fishing-advisor's score.py, which weighs rate-of-change
(water_temp_trend_72h_f, flow_rise_pct_72h) as a real factor, not just absolute
position. Pass --no-trend to skip this and only fetch the instantaneous reading (one
API call instead of two).

Usage:
    python3 fetch_water.py --lat 39.7684 --lon -86.1581 --box-deg 0.3 --json out.json
    python3 fetch_water.py --site 03353000 --json out.json
    python3 fetch_water.py --site 03353000 --trend-days 3 --json out.json
"""
import argparse
import datetime
import json
import math
import urllib.parse
import http.client
import time
import urllib.error
import urllib.request

STALE_HOURS = 6  # a reading older than this isn't "current conditions" anymore

BASE = "https://waterservices.usgs.gov/nwis/iv/"


def _http_get(req_or_url, source, timeout=20, retries=2):
    """Fetch JSON, retrying transient failures, and fail with a readable message.

    Before 2026-08-21 none of these scripts caught network errors at all: a USGS 503 or a
    NOAA rate-limit surfaced as a raw Python traceback, which is what a real session would
    have shown the user. Transient server-side failures (5xx, 429, timeouts) are worth a
    short retry; a 4xx means the request itself is wrong and retrying only wastes time.
    """
    transient = (408, 429, 500, 502, 503, 504)
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req_or_url, timeout=timeout) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code in transient:
                if attempt < retries:
                    time.sleep(2 ** attempt)
                    continue
                raise SystemExit(
                    f"{source} returned HTTP {e.code} after {retries + 1} attempts. "
                    f"That is a server-side failure, not a problem with the query — it is "
                    f"usually temporary. Do NOT report this as 'no data found': data may "
                    f"well exist. Say the source is unreachable right now and suggest "
                    f"retrying in a few minutes."
                )
            raise SystemExit(
                f"{source} rejected the request with HTTP {e.code} ({e.reason}). This "
                f"usually means the query is wrong (bad station/site ID, malformed "
                f"parameters, or the API changed) rather than the service being down."
            )
        except (OSError, http.client.HTTPException) as e:
            # Deliberately broad. urllib surfaces transport failures as URLError,
            # TimeoutError, ConnectionResetError and http.client.RemoteDisconnected,
            # and those do NOT share one narrow base class — catching URLError alone
            # let a dropped connection through as a raw traceback (found in testing,
            # 2026-08-21). HTTPError is handled above and must stay above this, since
            # it is itself a URLError/OSError subclass.
            if attempt < retries:
                time.sleep(2 ** attempt)
                continue
            detail = getattr(e, "reason", None) or e
            raise SystemExit(
                f"Could not reach {source} after {retries + 1} attempts: {detail}. "
                f"Treat this as temporarily unreachable, NOT as an empty result — never "
                f"report 'no data found' on a connection failure."
            )
        except json.JSONDecodeError:
            raise SystemExit(
                f"{source} returned something that isn't valid JSON — most likely an error "
                f"page instead of data. The endpoint may have changed."
            )


def fetch(params):
    url = BASE + "?" + urllib.parse.urlencode(params)
    return _http_get(url, "USGS Water Services")


def haversine_mi(lat1, lon1, lat2, lon2):
    r = 3958.8
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlambda / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def _dig(data, path, source, hint=""):
    """Walk a nested key path, failing with an explanation instead of a KeyError.

    A successful HTTP fetch can still return a shape this script doesn't expect — an
    API redesign, a deprecation notice served as JSON, or an error object delivered
    with a 200. Before 2026-08-21 that surfaced as a bare KeyError traceback, which
    to the user is indistinguishable from the script being broken. Network failures
    are handled in _http_get; this covers the other half of the same failure class.
    """
    node = data
    walked = []
    for key in path:
        if not isinstance(node, dict) or key not in node:
            where = " -> ".join(walked) if walked else "(top level)"
            if isinstance(node, dict):
                found = ", ".join(sorted(node.keys())[:12]) or "nothing"
            else:
                found = f"a {type(node).__name__}, not an object"
            raise SystemExit(
                f"{source} responded, but not in the shape this script expects: no "
                f"'{key}' under {where}. Found instead: {found}. That usually means the "
                f"API changed its response format, or returned an error object with a "
                f"success status. {hint} "
                f"Report this as a problem with the source, NOT as 'no data found' — and "
                f"it is worth writing to friction-log.md, since it needs a script fix "
                f"rather than a retry."
            )
        walked.append(key)
        node = node[key]
    return node


def parse_series(data, origin_lat=None, origin_lon=None):
    ts = data.get("value", {}).get("timeSeries", [])
    sites = {}
    for t in ts:
        # Skip a malformed series rather than killing the whole run — one bad station
        # in a bounding-box scan of 60 shouldn't cost the other 59.
        try:
            info = t["sourceInfo"]
            sid = info["siteCode"][0]["value"]
            name = info["siteName"]
            loc = info["geoLocation"]["geogLocation"]
            lat, lon = loc["latitude"], loc["longitude"]
            var = t["variable"]["variableName"]
            vals = t["values"][0]["value"]
        except (KeyError, IndexError, TypeError):
            continue
        latest = vals[-1] if vals else None
        sites.setdefault(sid, {
            "site_id": sid, "site_name": name, "lat": lat, "lon": lon, "readings": {},
        })
        if latest:
            stale = None
            try:
                ts = datetime.datetime.fromisoformat(latest["dateTime"])
                age_hours = (datetime.datetime.now(ts.tzinfo) - ts).total_seconds() / 3600
                stale = age_hours > STALE_HOURS
            except (ValueError, TypeError):
                pass  # if the timestamp can't be parsed, don't guess — leave stale unset
            reading = {
                "value": latest["value"],
                "datetime": latest["dateTime"],
                "stale": stale,
            }
            # USGS reports water temperature in Celsius (parameter 00010) — this
            # toolkit is US-units-first throughout (score.py's conditions.json,
            # every SKILL.md), so convert once here rather than making every
            # caller do the C-to-F math (and risk getting it wrong) themselves.
            if "temperature" in var.lower():
                try:
                    reading["value_f"] = round(float(latest["value"]) * 9 / 5 + 32, 1)
                except (ValueError, TypeError):
                    pass
            sites[sid]["readings"][var] = reading
    if origin_lat is not None:
        for s in sites.values():
            s["distance_mi"] = round(haversine_mi(origin_lat, origin_lon, s["lat"], s["lon"]), 1)
    return list(sites.values())


def parse_trend(data):
    """Earliest-vs-latest delta per site per variable, from a period=P{N}D series.
    Returns {site_id: {variable_name: {earliest_value, earliest_datetime,
    latest_value, latest_datetime, delta}}}."""
    ts = data.get("value", {}).get("timeSeries", [])
    trends = {}
    for t in ts:
        try:
            sid = t["sourceInfo"]["siteCode"][0]["value"]
            var = t["variable"]["variableName"]
            vals = [v for v in t["values"][0]["value"] if v.get("value") not in (None, "")]
        except (KeyError, IndexError, TypeError):
            continue  # same tolerance as parse_series — skip the series, keep the scan
        if len(vals) < 2:
            continue  # not enough points in the window to say anything about trend
        try:
            earliest, latest = vals[0], vals[-1]
            earliest_val, latest_val = float(earliest["value"]), float(latest["value"])
        except (ValueError, TypeError):
            continue
        trends.setdefault(sid, {})[var] = {
            "earliest_value": earliest_val,
            "earliest_datetime": earliest["dateTime"],
            "latest_value": latest_val,
            "latest_datetime": latest["dateTime"],
            "delta": round(latest_val - earliest_val, 3),
        }
    return trends


def summarize_trend(trend_for_site):
    """Convenience fields matching what score.py's conditions.json expects
    (water_temp_trend_72h_f-style naming, generalized to whatever window was used)."""
    out = {}
    for var, t in trend_for_site.items():
        lower = var.lower()
        if "temperature" in lower:
            # delta is a temperature DIFFERENCE — *9/5 converts it correctly.
            # (unlike an absolute reading, a delta needs no +32 offset.)
            out["water_temp_trend_f"] = round(t["delta"] * 9 / 5, 2)
        elif "streamflow" in lower or "discharge" in lower:
            if t["earliest_value"]:
                out["flow_change_pct"] = round((t["delta"] / t["earliest_value"]) * 100, 1)
        elif "gage height" in lower or "gauge height" in lower:
            out["gauge_height_trend_ft"] = round(t["delta"], 2)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lat", type=float)
    ap.add_argument("--lon", type=float)
    ap.add_argument("--box-deg", type=float, default=0.3, help="bounding box half-width in degrees (~20mi at this latitude)")
    ap.add_argument("--site", type=str, help="specific USGS site number")
    ap.add_argument("--trend-days", type=int, default=3, help="history window for trend calc (default 3, matching the 72h factor score.py expects)")
    ap.add_argument("--no-trend", action="store_true", help="skip the history fetch, instantaneous reading only")
    ap.add_argument("--json", type=str, required=True)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    params = {
        "parameterCd": "00010,00060,00065",  # water temp, discharge, gauge height
        "format": "json",
        "siteStatus": "active",
    }
    if args.site:
        params["sites"] = args.site
        origin = (None, None)
    elif args.lat is not None and args.lon is not None:
        d = args.box_deg
        # USGS rejects bBox coordinates with too many decimal places (float
        # arithmetic artifacts like -85.85810000000001 return a 400) — round to
        # 6 decimals, far more precision than this query needs.
        coords = [round(args.lon - d, 6), round(args.lat - d, 6),
                  round(args.lon + d, 6), round(args.lat + d, 6)]
        params["bBox"] = ",".join(str(c) for c in coords)
        origin = (args.lat, args.lon)
    else:
        raise SystemExit("Provide --site or --lat/--lon")

    data = fetch(params)
    sites = parse_series(data, *origin)
    sites_with_temp = [s for s in sites if "Temperature, water, deg C" in s["readings"] or
                        any("Temperature" in k for k in s["readings"])]

    if origin[0] is not None:
        sites.sort(key=lambda s: s["distance_mi"])

    # Trend (history fetch) is deliberately ONLY done for a single named --site, never
    # for a broad --lat/--lon scan. A bBox scan can return dozens of gauges; pulling a
    # 3-day history for every one of them multiplies both the USGS payload and the
    # JSON this script writes (which an LLM then reads into context) many times over
    # for data that's thrown away for all but the 1-2 gauges actually used. The
    # intended flow: scan first (cheap, instantaneous-only), pick the relevant gauge(s)
    # from the result, then re-run with --site <id> to get that gauge's trend.
    trend_note = None
    if args.site and not args.no_trend:
        trend_params = dict(params)
        trend_params["period"] = f"P{args.trend_days}D"
        trend_data = fetch(trend_params)
        trends = parse_trend(trend_data)
        for s in sites:
            t = trends.get(s["site_id"])
            if t:
                s["trend"] = {"window_days": args.trend_days, "raw": t, "summary": summarize_trend(t)}
    elif not args.site and not args.no_trend:
        trend_note = ("Trend not fetched for this broad scan (no --site given) to avoid pulling "
                       f"{args.trend_days}-day history for every gauge found — re-run with "
                       "--site <id> on the gauge you actually want once you've picked one.")

    out = {
        "source": "USGS Water Data waterservices.usgs.gov/nwis/iv",
        "query": {"lat": args.lat, "lon": args.lon, "box_deg": args.box_deg, "site": args.site,
                   "trend_days": None if args.no_trend else args.trend_days},
        "note": "Rivers/streams only — no equivalent real-time network for lakes/reservoirs. "
                "An empty result here means no gauge in range, not that the water doesn't exist. "
                f"Some gauges report flow/gage-height live but have a discontinued or malfunctioning "
                f"temperature sensor — each reading is flagged 'stale': true if it's more than "
                f"{STALE_HOURS}h old. Never present a stale temperature reading as current. "
                "USGS reports water temperature in Celsius ('value') — a converted 'value_f' "
                "field is included on every temperature reading; use value_f, this toolkit is "
                "US-units-first throughout."
                + (f" {trend_note}" if trend_note else ""),
        "gauges_found": len(sites),
        "gauges_with_water_temp": len(sites_with_temp),
        "sites": sites,
    }
    with open(args.json, "w") as f:
        json.dump(out, f, indent=2)
    if not args.quiet:
        print(f"{len(sites)} gauge(s) found, {len(sites_with_temp)} report water temperature. Written to {args.json}")


if __name__ == "__main__":
    main()
