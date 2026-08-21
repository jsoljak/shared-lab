# Roadmap — what's not done yet

*Built 2026-08-20 as a from-scratch US rebuild of a Czech personal fishing-decision
system, for Indiana (primary) and Michigan (secondary), with an on-demand expansion
mode for Ohio, Illinois, and Kentucky. Renamed from `midwest-fishing-advisor` and
widened to a nationwide scope later the same day — see the dated entry below.*

## Done
- Scoring engine: temperature position/trend, light window, season, flow/turbidity,
  wind/cloud, weighted per `species.yaml`, evidence-tiered per `evidence-tiers.md`.
- Eight species groups, including the three-way catfish split (channel/blue/flathead
  behave differently enough to need separate handling — not one generic "catfish")
  and the coldwater trout/salmon group added 2026-08-20 (see below).
- WINDOW mode (scan a date range, confidence degrades past ~5-6 days out) and the
  "don't bother today" / high-water-redirect discipline (`SKILL.md` rules 6-7).
- Bait/lure logic plus hook-size and rig recommendations per species
  (`hooks-and-rigs.md`) — new relative to the Czech original, which only covered
  bait category.
- Anti-scope boundaries (no cooking/recipe content; non-US destinations declined).
  Fly fishing and unmodeled species are deliberately NOT anti-scope — they route to
  EXPAND (`references/expand-procedure.md`), which researches and adds them rather
  than refusing. The frontmatter `description` says so explicitly, since that is what
  routing logic reads first and it previously implied a flat refusal.
- **2026-08-20: Token economy section added to SKILL.md** (§5) — one mode per
  query, score only the species in play (not all 11 by default), reuse
  already-fetched data instead of re-calling scripts, WINDOW capped at ~10-14
  days. Added after the end-to-end dry run (see `us-weather-advisor/
  references/roadmap.md`) showed a routine single-trip question could cost
  20+ tool calls chained across all three skills — necessary given Max isn't on
  an unlimited plan.
- `score.py` — live-tested against `species.yaml` with two synthetic condition sets:
  a moderate river/dawn case (sensible ranking: smallmouth/largemouth top, pike
  lowest given a 68.5F reading below its preferred window) and a hot-lake/day case
  that confirmed the muskellunge 79F hard-stop actually fires (score forced to 0,
  confidence "n/a — hard stop", full Bieber & Suski 2024 citation in the message)
  independently of whether temperature_position itself could be scored — muskellunge
  has no documented opt_min in `species.yaml` (only the 79F ceiling is `[D]`-tier),
  so temperature_position correctly falls back to "unknown" while the hard-stop still
  fires off water_temp directly. Confidence-degradation (lead-time + estimated-source)
  also confirmed working via the min-rank combination.

- **2026-08-20: the 72h water-temp/flow trend `score.py`'s `trend_score()` and
  `turbidity_score()` expect (`water_temp_trend_72h_f`, `flow_rise_pct_72h`) now
  has a real source** — `us-weather-advisor/scripts/fetch_water.py` gained
  `--trend-days`/history support (see its roadmap for detail). Before this, the
  dry run showed those fields could only ever be passed as `null`, which the
  scoring code handles gracefully but silently drops a factor the model is
  supposed to weigh.

- **2026-08-20: personal water registry, ranked shortlists, and a reports check
  added**, all from live-testing feedback: `memory-seeds/waters.yaml` (a
  personal known-water list PLAN checks before falling back to a fresh
  `us-water-finder` query — ships empty, grows via logged trips or explicit
  saves), PLAN mode now answers with a ranked shortlist across water types
  instead of one forced pick, and a new REPORTS mode/rule 11 does one targeted
  web search for what's actually known about the top-recommended water
  (`references/water-reports.md` — DNR reports preferred over forum posts,
  same survivorship-bias discipline as the Czech original's `teren-reporty.md`,
  scoped to the top pick only so it doesn't multiply cost across a shortlist).

- **2026-08-20: renamed from `midwest-fishing-advisor`, scope widened to
  nationwide, coldwater trout/salmon group added.** Triggered by realizing
  `us-weather-advisor`'s data sources (NOAA/USGS) were already nationwide with no
  code changes needed, and `us-water-finder`'s Mode E was architecturally general
  but artificially capped to five states — "Midwest" was a misleading name for a
  toolkit whose weather layer already worked anywhere in the US. Added five new
  species with the same evidence-tier research discipline as the original eleven:
  rainbow, brown, brook, and westslope cutthroat trout, plus kokanee salmon —
  researched via direct fetches of primary sources (Montana State University's
  comparative rainbow/cutthroat thermal study, the classic Elliott brown-trout
  growth model, the USFWS Raleigh 1982 brook trout Habitat Suitability Index, a
  2025 rainbow-trout light-intensity study, Washington DFW/Montana Field Guide for
  kokanee and cutthroat specifics) rather than generic angling-blog consensus.
  Documented in `evidence-tiers.md` §8 that this group's thermal logic is inverted
  from every warmwater species already modeled (cold = normal operating range, not
  a slowdown state) and that the SKILL.md §3 backbone bait rule does not transfer
  to it. Added a new EXPAND mode (mirrors `us-water-finder`'s Mode E) so the next
  species or an eventual fly-fishing request doesn't require another from-scratch
  session — explicitly requested as forward preparation, not built out today
  (fly fishing stays out of scope until it's actually asked for).

- **2026-08-21: full audit and fix pass** (3 fresh-agent scenario tests + mechanical
  reference check + live run of all five scripts + schema validation). Fixed here:
  **the `stop` threshold was decorative** — it only zeroed one 35%-weight factor, so a
  species documented as "feeding effectively off" scored 53/100 with high confidence and
  would have been recommended (largemouth at 45F, reproduced live). `stop` is now a gate
  that caps the total at 12, and the raw pre-cap score is reported so the reasoning stays
  visible. **Hard stops moved from code into data** — `score.py` had a literal
  `if key == "muskellunge"` branch, meaning any species added via EXPAND had no way to
  declare a critical threshold without a code change; `hard_stop: {above|below, reason}`
  is now read generically from `species.yaml`, and two evidence-backed ones were added
  (brook trout 68F per Raleigh 1982, westslope cutthroat 67F per the MSU 60-day UUILT).
  **Unknown `--species` keys now warn** instead of silently vanishing from the answer,
  and an all-unknown list fails loudly rather than returning an empty result. EXPAND's
  detail moved to `references/expand-procedure.md`, which adds the source discipline the
  technique branch was missing (fly fishing had "research it the same way" with no
  sourcing rules) and the Great-Lakes collision warning. `preferences.md` was an orphan —
  shipped but never mentioned in SKILL.md — now documented.

## Known gaps
1. **Lake/reservoir water temperature is estimated, not measured** — same USGS gap
   as the Czech original's ČHMÚ gap for stillwater. No fix without a satellite/
   modeled-temperature data source, which would need its own research pass.
2. **Crappie and common carp thermal numbers rest on angler consensus, not a
   dedicated field study** — flagged `[P]` in `species.yaml` rather than `[D]`.
   Worth a follow-up literature search if this becomes a real dependency.
3. **Score calibration is untested against real outcomes** — there's no equivalent
   yet of the Czech system's CALIBRATE mode having real logged trip data behind it.
   LOG/CALIBRATE modes exist in `SKILL.md` but need actual use before their output
   means anything.
4. **Hook/rig recommendations are practitioner-consensus, not evidence-tiered** —
   genuinely useful but a different kind of claim than the biology in
   `evidence-tiers.md`; don't present them with the same confidence level.
4b. **`SKILL.md` runs ~412 lines, modestly over the toolkit's 400-line soft limit.**
   The 2026-08-21 audit pass moved EXPAND's detail out to a reference file, which
   bought back most of what the trout/salmon and emergency-closure additions cost.
   What's left inline is hard rules and mode procedure — trimming further would mean
   cutting safety content to hit a round number, which is the wrong trade. Revisit if
   it drifts past ~450.
5. **No Great Lakes-specific regulatory handling yet** beyond flagging that it's
   different (`us-water-finder` rule 7) — a real Great Lakes fishing trip would
   need that built out properly, not just flagged.
6. **Kokanee's temperature band is a Washington citation, not a Montana one** —
   the mechanism (thermocline-following near 50°F) is well-established for the
   species generally, but the exact 47-53°F range hasn't been checked against a
   Montana-specific source. Worth a follow-up if kokanee becomes a real dependency.
7. **Fly fishing is fully out of scope** — not started, by explicit design decision
   (2026-08-20), not partially built. The EXPAND mode's technique-addition path is
   designed for this specifically but hasn't been exercised yet.
8. **Score calibration still untested against real outcomes** — the 2026-08-21 audit
   fixed how `stop` and `hard_stop` behave, but the weights themselves (0.35 temperature
   position, 0.20 light window, etc.) have never been checked against logged results.
   The 12-point cap for a stopped-out species is a judgment call, not a calibrated
   number. CALIBRATE mode needs real trips before any of this is more than reasoned.
