# Roadmap — what's not done yet

## Done
- **2026-08-21: audit fixes.** All network calls in `fetch_weather.py` and
  `fetch_water.py` (and the three `us-water-finder` fetch scripts) were completely
  unguarded — a USGS 503, reproduced live during the audit, produced a raw Python
  traceback. Added a shared `_http_get` helper: retries transient failures (5xx, 429,
  timeouts) with backoff, fails fast on 4xx since those mean the query is wrong, and
  returns a message that explicitly tells the caller not to report a connection failure
  as "no data found." Testing caught a second gap — `http.client.RemoteDisconnected` is
  not a `URLError` subclass and was leaking through — so the handler now catches `OSError`
  and `http.client.HTTPException` broadly. **Response-shape failures covered too** — a
  successful fetch can still return an unexpected structure (API redesign, an error
  object served with a 200, a retired layer), which previously raised a bare `KeyError`;
  a `_dig` helper now names the missing key, lists what was actually returned, and says
  explicitly not to report it as "no data found." `parse_series`/`parse_trend` skip a
  malformed series instead of dying, so one bad station can't cost a 60-gauge scan, and
  the ArcGIS scripts detect a 200 with no `features` key. Both classes of message tell
  the caller to log it to `friction-log.md`, since a shape change needs a script fix
  rather than a retry. Rule 2 gained two cases it didn't cover: the
  air-driven lake estimate is invalid (not merely weak) for the Great Lakes, and
  borrowing a temperature reading from a distant gauge is a third confidence class
  distinct from measured and estimated, with a ~30-mile / no-reservoir-between limit.
- **2026-08-20: renamed from `midwest-weather-advisor`, description corrected to
  say "any US location."** No code change needed — NOAA/NWS and USGS Water Data
  were already nationwide; the old name and description text were the only thing
  actually scoped to the Midwest. Confirmed by grepping both fetch scripts for any
  state-specific logic: none found.
- `fetch_weather.py` — live, tested against NOAA/NWS, pulls daily periods
  (including overnight, needed for CAMP mode) and next-48h hourly detail.
  User-Agent is a placeholder marked `PUT-YOUR-EMAIL-ADDRESS-HERE` (deliberately not
  written in email form, so repo secret scanners don't read it as a leaked address) —
  swap in a real contact per NOAA's usage policy before real use.
- `fetch_water.py` — live, tested against USGS Water Data, finds nearby gauges by
  bounding box, pulls water temperature/discharge/gauge height. Includes a
  staleness check discovered during testing: some gauges report live flow/gage-
  height but have a discontinued temperature sensor (one test case had a water-
  temperature reading four years old on an otherwise-live station) — every reading
  is now flagged `stale: true/false` rather than trusting the presence of a value.
  **2026-08-20: added trend support** (`--trend-days`, default 3) — a second fetch
  using USGS's `period=P{N}D` param, computing earliest-vs-latest delta per
  variable. This closes a real gap an end-to-end dry run surfaced: SKILL.md and
  `us-fishing-advisor`'s `score.py` both expect a 72h water-temp/flow trend,
  but nothing fetched one before this. Deliberately scoped to single-`--site`
  queries only (not broad bBox scans) to avoid multiplying API payload and
  context-read cost across dozens of gauges — see the new §4 Token economy
  section in SKILL.md.
- **2026-08-20: full end-to-end dry run**, 6 scenarios run through fresh agents
  with no memory of the build (simulating exactly what Max's Claude would see —
  only the SKILL.md files, no prior context). Covered: full 3-skill chain for an
  Indiana trip, muskellunge hard-stop against real live August water-temp data,
  anti-scope (cooking question correctly ignored), direct DATA-mode query
  (river flow, no fishing context), Mode E's first live run (Ohio — see
  `us-water-finder/references/roadmap.md`), and CAMP mode with a
  dual-intent ("camping + should I bring a rod") message. All 6 passed on the
  substance; findings that needed fixing are listed above and in the other two
  skills' roadmaps, not repeated here.

## Known gaps
1. **Lake/reservoir temperature estimation isn't built** — `fetch_water.py`
   correctly returns nothing for still water (no gauge network exists), but there's
   no fallback estimate script yet. Needs its own small model (recent air-
   temperature trend, maybe depth/size where known) before CAMP/lake-fishing
   verdicts can say anything about lake water temperature beyond "unknown."
2. **GENERAL/HIKE/CAMP/ROADTRIP verdict logic itself isn't written yet** — the two
   fetch scripts pull raw data; the mode-specific interpretation logic
   (`SKILL.md` §2) needs a script or needs to be handled by the calling model
   directly from the fetched JSON. Given how much of this is genuinely
   interpretive (is this wind "reasonable for a hike" — no universal number), that
   interpretation may belong in `SKILL.md` prose rather than a deterministic
   script — worth a design decision before building further.
3. **No test yet of a multi-day WINDOW-style scan** — `fetch_weather.py` returns
   the full 14-period forecast in one call, so the data is there, but nothing
   yet consumes it the way `us-fishing-advisor`'s WINDOW mode will need to.
