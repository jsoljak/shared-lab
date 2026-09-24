---
name: us-weather-advisor
metadata:
  status: draft
description: >
  Pulls live weather (NOAA/NWS) and river conditions (USGS: flow, gauge height, water
  temperature) for any US location and gives a plain verdict on whether it is a good day
  for an outdoor activity: going out in general, a hike, a road trip, or an overnight
  camping trip. Trigger for: "is it a good day to go outside", "what's the weather like
  for a hike near [place]", "should I go camping this weekend", "is it worth a road trip
  to [place]", "what's the water level/flow on [river]", or any conditions question tied
  to an outdoor plan that is not specifically about fish biting. Also the data layer us-
  fishing-advisor calls for water temperature and flow. Do NOT trigger for fishing-
  specific "will they bite" questions (us-fishing-advisor calls this skill itself) or
  for legal access/regulations with no weather component (us-water-finder).
target_stack: null
---

# us-weather-advisor

Answers one question, for whichever activity is asked about: **are conditions
actually good for this, right now or on this date.** This is a shared data +
light-verdict layer — it does not know anything about fish species or fishing
regulations. Deeper, species-specific fishing decisions belong to
`us-fishing-advisor`, which consumes this skill's water-temperature and flow
output rather than duplicating the data fetch.

## 0. Hard rules

1. **Don't fetch data twice.** If `us-fishing-advisor` calls this skill for
   water temperature/flow, don't also have it independently query NOAA — this skill
   owns the fetch, other skills consume its output.
2. **Lakes don't have real-time gauges.** USGS covers rivers and streams. For a
   lake/reservoir, say plainly that the water temperature is an estimate (surface-air-
   temperature-driven proxy), not a measurement — never present it with the same
   confidence as a river reading from an actual gauge.
   **The estimate is invalid for the Great Lakes — don't produce one.** An air-driven
   proxy assumes a body of water small enough to track air temperature. Superior,
   Michigan, Huron, Erie and Ontario are stratified, hundreds of feet deep, and stay
   cold through summer regardless of air temperature, so the proxy doesn't return a
   weak number there — it returns a confidently wrong one. Say the model doesn't cover
   Great Lakes water temperature and point at NOAA's Great Lakes observing products
   instead. (Same carve-out as `us-water-finder` rule 7, for the same reason: these
   aren't big lakes, they're a different kind of water body.)
   **Borrowing a reading from a distant gauge is a third case, distinct from both
   "measured" and "estimated" — label it as such.** A gauge can report live flow and
   stage while its temperature sensor is dead or absent, and the nearest gauge that
   *does* report temperature may be 25+ miles away on a different reach (this is
   normal in the sparsely-gauged West, confirmed near Bozeman 2026-08-21). Using it
   is legitimate; presenting it as this water's temperature is not. Say which gauge,
   how far, and whether it's upstream or downstream — a downstream gauge below a
   confluence or a reservoir release can be several degrees off, and for a species
   with a hard stop near the reading (westslope cutthroat at 67°F) that difference
   decides the answer. Beyond roughly 30 miles or across a reservoir/major confluence,
   treat it as too weak to carry a recommendation and say the temperature is unknown.
3. **A forecast past about 7 days is a trend, not a plan.** NOAA's forecast
   confidence degrades with lead time same as anywhere else — flag anything beyond a
   week out as lower-confidence rather than stating it flatly.
4. **Overnight numbers matter for camping and don't matter for a day hike.** Don't
   run the same check for both — a camping verdict needs the overnight low and
   overnight precipitation probability; a day-hike verdict doesn't.
5. **Sustained rain/wind matters more than a passing shower for outdoor activity
   generally** — the same logic that makes barometric pressure a weak predictor for
   fish applies here in reverse: don't weight a 20-minute forecast blip the same as
   a multi-hour front. Look at the probability-weighted precipitation window
   (`p_5mm`-equivalent — "measurable, sustained rain"), not just "chance of rain."
6. **This skill gives a verdict, not a guarantee.** "Good conditions for a hike" is
   about weather/trail-adjacent factors it can actually check — not trail closures,
   wildlife activity, or anything else outside its data.
7. **US units, always.** Fahrenheit, mph, inches — never surface a bare Celsius
   number. `fetch_water.py` writes a converted `value_f` alongside USGS's native
   Celsius reading specifically so this doesn't require mental math (or a mistake)
   every time; use `value_f`. `fetch_weather.py`'s NOAA data is already
   Fahrenheit/mph natively.
8. **When precipitation risk is real, give the radar link, not just a percentage.**
   `fetch_weather.py` writes a `radar_url` (the nearest NWS station's live loop) —
   a forecast is a snapshot, a radar loop is current. Include it whenever precip
   probability is high enough to matter for the activity being planned, not only
   on request.
9. **Single source, and say so if asked.** This skill pulls NOAA/NWS only —
   NOAA's own forecast already synthesizes multiple numerical models internally
   (that's how NWS forecasters build a forecast), but this skill does NOT
   independently query a second provider and compute a disagreement/confidence
   number the way some multi-source tools do. If asked directly whether this
   cross-checks multiple sources: no, not yet — say that plainly rather than
   implying a level of verification that isn't there. See `references/roadmap.md`.

## 1. Data sources

- **Weather:** `api.weather.gov` (NOAA/NWS) — free, no API key, gridpoint forecast
  by lat/lon. Gives temperature, precipitation probability, wind, sky cover, by hour
  and by day.
- **River flow/water temperature:** `waterservices.usgs.gov` (USGS Water Data) —
  free, no API key, real-time discharge, gauge height, and water temperature at
  monitored river/stream gauges. Find the nearest gauge to the target GPS point;
  if none exists within a reasonable distance, say so rather than silently
  extrapolating from a distant one.
- **Lake temperature (no real gauge network):** estimate from recent air temperature
  trend and depth/size where known — always labeled as an estimate in output, same
  discipline as the fishing-advisor's stillwater temperature handling.

## 2. Modes

| Signal in the request | Mode |
|---|---|
| "is it a good day to go outside", "how's the weather for [date]" | **GENERAL** |
| "hike", "trail", "is it good hiking weather" | **HIKE** |
| "camping", "camp overnight", "should I camp this weekend" | **CAMP** |
| "road trip", "drive to [place]", "worth going to [place] this weekend" | **ROADTRIP** |
| "what's the water level/flow/temperature on [river]" (asked directly), or called internally by `us-fishing-advisor` | **DATA** (no activity verdict, just the numbers) |

### GENERAL

Temperature, precipitation probability, wind, sky cover for the window asked about.
One-line verdict (good / mixed / poor) with the one or two factors driving it.

### HIKE

Same as GENERAL, plus: heat index if hot, wind chill if cold, and a note on sustained
rain vs. passing showers (rule #5). No overnight check needed unless it's a multi-day
hike, in which case treat it as CAMP for the overnight portion.

### CAMP

GENERAL logic for the daytime window, plus a **mandatory overnight check**: overnight
low temperature and overnight precipitation probability. A day that looks fine at
2pm and drops to a cold, wet overnight low is a bad camping call even with a good
daytime forecast — say so explicitly, don't let the daytime number carry the verdict.

### ROADTRIP

Broader window (the whole day or trip duration, not just a snapshot), weighted toward
whether driving conditions are reasonable (sustained rain/snow, high wind) over minor
comfort factors. If the destination is far enough that conditions differ meaningfully
from the origin, check both.

### DATA (internal use or direct query)

Return water temperature, 72-hour trend, and flow/flow-trend for the requested
water — whether the request is a direct human question ("what's the flow on the
White River") or an internal call from `us-fishing-advisor`, which additionally
wants the same numbers for a same-region stillwater alternative if one's in context.
No activity verdict either way, just the numbers, labeled measured vs. estimated
per rule #2.

## 3. How to answer

1. **Verdict first, one line.** "Good hiking day Saturday — mid-60s, low wind, no
   rain in the forecast" beats leading with a temperature table.
2. **Name the factor that's actually driving the call**, not a generic list. If it's
   a poor day, say what specifically makes it poor.
3. **Flag estimates as estimates** — lake temperature, forecasts past ~7 days,
   anything not a direct gauge/station reading.
4. **For CAMP specifically, always report the overnight numbers even if unprompted**
   — it's the single most common way a "good weather day" verdict misleads someone
   planning to sleep outside.

## 4. Token economy

1. **GENERAL/HIKE/ROADTRIP only need `fetch_weather.py`.** Don't call `fetch_water.py`
   unless the request actually touches water — river/lake conditions, or an internal
   DATA call from `us-fishing-advisor`. A "good day for a hike" question has no
   business pulling USGS gauge data.
2. **Prefer `--site <id>` over a broad `--lat/--lon` scan once you know the gauge.**
   A bounding-box scan can return 50+ gauges with full reading detail each — expensive
   to both fetch and read back. Scan once to find the right gauge, then re-query that
   one site directly for anything further (trend included).
3. **Only fetch a trend (`fetch_water.py`'s default) when rate-of-change actually
   matters** — a direct "what's the flow right now" question wants the instantaneous
   reading; pass `--no-trend` for that (halves the API calls). Trend is worth its
   extra cost specifically for `us-fishing-advisor` DATA calls, where the scoring
   model weighs the 72h change, not just the fishing-advisor's default is trend-on.
4. **Always `--quiet --json <file>`, then read the file once** — don't also let the
   script print a human-readable summary to stdout and read that too.

## File Access Protocol

1. Read files with the Read tool.
2. If that fails with a permission error, try a direct filesystem path.
3. If the file is outside the accessible directory, ask where it should be found.
4. Only report a file as missing after all three steps fail.

## Status

Weather and river-flow fetch logic built against NOAA/NWS and USGS Water Data.
Lake-temperature estimation is a rough proxy (see `references/roadmap.md`) — same
open gap the fishing-advisor's Czech original has for stillwater, not yet solved
here either.
