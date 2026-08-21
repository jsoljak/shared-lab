# Roadmap — what's not done yet

## Done
- Live, tested Indiana access-point fetch (`fetch_indiana.py` against the DNR
  `Fish_Access_RO` FeatureServer — confirmed working, includes species/fee/amenity
  fields).
- Live, tested Michigan access-point fetch (`fetch_michigan.py` against the DNR's
  MRBIS boating/fishing access layer — confirmed working, though it's a different
  field shape than Indiana's, boating/amenity-focused rather than species/fee).
- Michigan closed-season pattern documented (`michigan-regulations.md`) as the one
  genuine seasonal-closure case among the five states.
- Mode E (EXPAND) procedure documented. **2026-08-20: scope widened from a fixed
  five-state list to any US state** — the procedure itself (find the open-data
  pattern, pull access/rules/license/stocking, write `reference-data/states/<state>.json`,
  disclose it as unverified) didn't change, only the artificial gate on when it's
  allowed to run. Also renamed from `midwest-water-finder`.
- **2026-08-20: `maps_url` added to every fetch script's output** (Indiana, Michigan,
  Ohio) — a real gap a live test surfaced: results had names and coordinates but no
  way to actually get there without the person looking the place up themselves.
  Format: `https://www.google.com/maps/search/?api=1&query=<lat>,<lon>`. SKILL.md
  §3 now makes carrying this through the answer a hard rule, not optional polish.
- **2026-08-20: Indiana Mode B (RULES) built** — `reference-data/states/indiana.json`, full
  size/bag limits, license fees, and reciprocity for the 11 warmwater species modeled
  at the time (trout added 2026-08-21, see below), via a
  real research pass (not Mode E, since Indiana isn't outside the five-state scope —
  same underlying procedure, applied to a state that already had Mode A). Found and
  corrected a real gap in prior research: the Wabash River is also Indiana↔Illinois
  reciprocal water, not just the Ohio River and Calumet Harbor.
- **2026-08-20: Mode E run live for the first time, against Ohio.** Worked, but
  needed real judgment calls the written procedure didn't anticipate — folded
  those back into SKILL.md Step 1/2 (state DNR data split across divisions with
  no cross-index; verify "no login required" claims by fetching, don't trust the
  state's own referral copy). Produced `reference-data/states/ohio.json` (access points
  partial/river-only, regulations solid, stocking identified but login-gated —
  contradicts this file's earlier claim that Ohio had "the strongest stocking
  dataset of the five," now corrected in SKILL.md's data-source table) and
  `scripts/fetch_ohio.py`. Also corrected SKILL.md's Status section, which
  overstated Indiana/Michigan as "full" — neither actually has a Mode B
  (regulations) data file; only the Mode A access-point layer is real for either.

- **2026-08-20: `license_summary` made a required field**, not optional, in
  `references/data-schema.md` and Mode E Step 2 — what to buy, where, and the
  cost in USD, not just abstract regulation text. Indiana's file already had this
  (added organically during its research pass); the schema now requires it going
  forward for Michigan/Illinois/Kentucky too.
- **2026-08-20: general scraping fallback added** (rule 10 since 2026-08-21, was rule 9) — not just an
  Illinois-specific note anymore. Any state/water with no confirmed API gets a
  targeted web search before "no data" is the answer, labeled as scraped
  (lower confidence) rather than presented like a FeatureServer result.

- **2026-08-21: audit fixes.** `where_to_buy` was **missing from both state files**
  despite being a required schema field with its own rationale ("a cost number with no
  purchase path isn't actionable") — added for Indiana and Ohio from verified official
  sources. **Trout/salmon regulations added to both states**, closing a gap the trout
  species addition had opened the day before: `species.yaml` could score a species the
  legal layer had nothing to say about. Both states turned out to regulate trout as one
  combined group rather than per species, and Ohio's Lake Erie tributaries are a separate
  seasonal zone — recorded as such rather than merged. `data-schema.md`'s species list
  was stale (11 keys vs. 16 in `species.yaml`) and is now pinned to reading species.yaml
  directly. New hard rule 9 + `references/emergency-restrictions.md` for drought and
  temperature-triggered closures (see below). Rule 2 now states the US-only boundary
  explicitly instead of leaving it to be inferred, and Mode A warns that its documented
  field list does not hold outside the states already built.
- **2026-08-21: emergency/drought closures covered** (`references/emergency-restrictions.md`).
  Montana had active hoot-owl restrictions during the audit's own Montana test window and
  nothing in the toolkit would have surfaced them — a real "recommended water is legally
  closed" failure. Deliberately NOT a data field: current status has a useful life of days,
  and a stale "no restrictions" value would read with the same confidence as a verified
  size limit. Durable trigger thresholds are recorded; current status is always live or
  explicitly unknown. Research found three traps a naive rule would have hit: Idaho's
  agency publicly opposes the mechanism, Wyoming's and Colorado's versions are voluntary
  rather than legal, and Utah's drought response is inverted (raising bag limits).

## Known gaps
0. **Every state outside Indiana/Michigan/Ohio/Illinois/Kentucky is completely
   untouched** — Mode E has never actually run against a state whose primary
   fish/wildlife agency isn't called "DNR" (Montana's is FWP, and several other
   Western states use a different naming pattern too — SKILL.md Step 1 now flags
   this but it hasn't been tested against a real one yet). The first live run
   against a genuinely different agency-naming pattern is likely to surface real
   friction the same way Ohio's first Mode E run did.
1. **Indiana's Mode B is done (2026-08-20, `reference-data/states/indiana.json`); Michigan's
   still isn't.** Michigan has only the closed-season pattern in
   `michigan-regulations.md` — no size/bag-limit or license-info data file yet.
   This is now the single biggest asymmetry between the two "primary" states.
2. **Stocking data fetch is not built** — both states publish stocking dashboards.
   Indiana's was confirmed genuinely public (no login wall, unlike Ohio's) during
   the 2026-08-20 Mode B research, but nothing pulls from it into a fetch script yet.
3. **Illinois and Kentucky have no `reference-data/states/` file yet** — Ohio's is done
   (2026-08-20, see above); Illinois in particular has no confirmed API at all
   (per-waterbody HTML scraping), so expect its Mode E run to be the roughest of
   the three remaining states.
4. **Emergency-restriction current status can't be checked for every state.** Montana,
   Wyoming and Colorado have real current-status pages; California, Oregon, Washington and
   Utah do not, so for those the honest output is "in the risk window, couldn't confirm,
   check the agency" rather than a yes/no. No multi-state aggregator exists.
5. **Great Lakes shorelines aren't handled** beyond the flag in `SKILL.md` rule 7 —
   no actual data source identified yet for Great Lakes-specific zoned regulations.
   Ohio's Mode E pass explicitly did not research Lake Erie.
6. **Ohio's access-point layer only covers rivers/streams**, not lake/reservoir
   shoreline — the Division of Watercraft paddling-access layer used is the closest
   real data found, but it's not a fishing-access feed and has a 1000-row server
   cap (query by county/waterbody, not statewide, to avoid silent truncation).
