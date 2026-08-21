---
name: us-water-finder
metadata:
  status: draft
description: >
  Finds legal freshwater fishing locations, access points, and regulations anywhere
  in the US. Fully pre-built for Indiana (primary), Michigan, and Ohio, with a
  documented on-demand expansion procedure (Mode E) for any other state — Illinois
  and Kentucky have partial data already, everywhere else (Montana, or any state
  not yet touched) gets built the first time it's asked about. Sourced from
  official state DNR/fish-and-wildlife open-data portals — GPS access points,
  size/bag limits, closed seasons, stocking records. Trigger this for: "where can I
  fish near [place]", "what are the rules on [lake/river]", "is there a closed
  season for walleye/musky/trout in [state]", "find me a lake/river near [city]",
  "can I fish [water] right now", or any question about legal fishing access,
  regulations, or stocking anywhere in the US. Coverage quality varies — say so
  plainly when it's thin. Do NOT trigger for: fishing technique or bait questions
  with no location component (that's us-fishing-advisor), or weather/water-condition
  questions with no location/legal component (that's us-weather-advisor).
target_stack: null
---

# us-water-finder

Answers one question: **where can I legally fish, and what applies there.** This
skill owns location and regulation data — it does not decide whether fish will bite
(`us-fishing-advisor`) or whether conditions are good (`us-weather-advisor`).
Keeping this separation means there's one source of truth for "what's legal," not
three skills that could drift out of sync.

## 0. Hard rules — read before answering anything

1. **Never answer regulations from memory.** State fishing law is granular and
   changes yearly. If the data file doesn't have it, say so — don't guess or fall
   back on general knowledge. A wrong regulation answer can cost someone a citation.
2. **US only, and coverage within the US is uneven — say both plainly.** This
   toolkit covers US states. A non-US destination (Canada, Mexico, anywhere
   overseas) is **out of scope — decline it cleanly** rather than pointing Mode E at
   a country whose agencies, licensing and data infrastructure it was never built
   for. Say the toolkit is US-only and stop there; don't half-answer from general
   knowledge. Within the US: Indiana, Michigan and Ohio have real structured data
   behind them, Kentucky is partial, Illinois isn't built as a clean feed (expect its
   Mode E run to be the roughest), and every other state is untouched until Mode E
   runs for it. State the tier before answering, don't let a thin state read like
   Indiana's.
3. **Distinguish statewide rules from water-specific rules.** A state's general
   size/bag limits can be overridden on a specific lake or river (slot limits,
   special regulations). Always check for a water-specific override before quoting
   the statewide default.
4. **Michigan is the one state with a real closed season** for walleye/pike (opens
   the last Saturday of April downstate, May 15 in the Upper Peninsula) and
   muskellunge (opens the first Saturday of June). Indiana, Ohio, Illinois, and
   Kentucky regulate those species by size/bag limit year-round, not by season —
   don't apply Michigan's closed-season pattern to the other four, or assume any
   other state (including one Mode E hasn't touched yet) follows it either — check
   that state's actual data once it exists.
5. **No reciprocity between states except a handful of named boundary waters.**
   There is no multi-state license. Confirmed reciprocal waters: the Ohio River
   main stem (Indiana↔Kentucky, Ohio↔Kentucky, Illinois↔Kentucky), Calumet
   Harbor on Lake Michigan (Indiana↔Illinois, harbor only, not the banks), and the
   Wabash River where it forms the Indiana↔Illinois boundary. Anywhere else, the
   license for the state you're physically in/on is what applies.
6. **A stocking-record hit doesn't mean current abundance.** Stocking data shows
   what was put in and when — it's a data point about the fishery, not a promise
   of what's there now. Present it as history, not a guarantee.
7. **The Great Lakes are not a normal inland water.** Lake Michigan, Lake Erie, and
   any other Great Lakes shoreline have their own regulatory layer — often zoned,
   often coordinated between multiple states and sometimes Canada — that doesn't
   fit this skill's per-state inland-water data model. Don't answer a Great Lakes
   regulation question from the same state file as an inland lake; say plainly that
   Great Lakes rules need a direct check against that state's Great Lakes-specific
   fishing regulations page, and give whatever general state-level context is known
   without presenting it as the complete picture.
8. **Mode E can attempt any US state, not just the ones already built.** Indiana,
   Michigan, and Ohio have real, live-tested data behind them; Illinois and Kentucky
   are partial; every other state (Montana, or anywhere else) runs through Mode E
   cold on first request. That's the point of Mode E existing as a repeatable
   procedure rather than a one-time build — but be honest about what that means:
   a state that's never been through Mode E is **unverified**, not just "not yet
   built." Say so before presenting its data with the same confidence as Indiana's.
   A handful of states (Alaska, Hawaii, and non-US destinations) may genuinely have
   no equivalent open-data infrastructure to find — if Mode E's own search turns up
   nothing workable after a real attempt (not a first-guess failure), say that
   plainly instead of forcing a low-quality result.
9. **A fixed closed season is not the only way water closes.** Western and mountain
   states impose **emergency restrictions triggered by warm water and low flow** —
   Montana's "hoot owl" closures (2 p.m. to midnight, triggered at 73°F sustained over
   three days) are the clearest case, and they are enforceable law, not advice. They are
   imposed and lifted on a days-to-weeks timescale, so they appear in no data file here.
   **Whenever a river or stream in a western/mountain state is being recommended between
   roughly mid-June and September, read `references/emergency-restrictions.md`** before
   answering. Three traps that file exists to prevent: not every western state does this
   (Idaho's agency argues against it), some states' versions are voluntary rather than
   legal (Wyoming, Colorado), and Utah's drought response is the *opposite* — raising bag
   limits, not closing water. Never assert a river is open because you didn't find a
   restriction; "I couldn't confirm current status, check <agency link>" is the honest
   answer and a genuinely useful one.
10. **No clean API is not the end of the search — it's the point where you switch
   to scraping.** This applies everywhere, not just Illinois: if a location's
   state has no confirmed FeatureServer/open-data layer, or the layer that exists
   doesn't actually cover the water in question, search for and read the state's
   own web page(s) for that specific water/region before reporting "no data."
   A web search for `"<water name>" fishing access OR boat ramp <state>` or the
   state DNR's own per-lake/river page is a real source, just a slower one to
   read than a FeatureServer query — use it, don't skip straight to "not found."
   Always label a scraped result as scraped (lower confidence, no GPS precision
   guarantee) rather than presenting it with FeatureServer-level certainty.

## 1. Data sources

States actually run through this toolkit so far — everywhere else uses the same
Mode E procedure (§2) starting cold, and is unverified until it has been:

| State | Access/rules layer | Stocking | Notes |
|---|---|---|---|
| **Indiana** | `data-indnr.hub.arcgis.com` — `Fish_Access_RO` FeatureServer (live REST, GPS + amenities) | ArcGIS dashboard, `in.gov/dnr/fish-and-wildlife/fishing/indiana-fish-stocking/` | Best-structured of the states built so far |
| **Michigan** | `gis-michigan.opendata.arcgis.com` — dedicated "Fishing Access Sites" layer | ArcGIS dashboard (note: several weeks' lag vs. actual stocking) | Only state with real closed seasons, of the states built so far |
| **Ohio** | `gis2.ohiodnr.gov` — Division of Watercraft stream/paddling-access layer (confirmed live; river/stream put-ins only, no lake shoreline, no dedicated fishing-access layer) | `data.ohio.gov` — described as a weekly-updated CSV back to 1970, but confirmed **login/approval-gated** as of the first Mode E run (2026-08-20) despite ODNR's own referral page claiming no login is required — verify by fetching, don't trust the claim | Regulation text itself is PDF-only; see `reference-data/states/ohio.json` after first Mode E run |
| **Kentucky** | `opendata-kygeonet.opendata.arcgis.com` — "Fishing Access Sites in Kentucky" | Page exists (`fw.ky.gov/Fish/Pages/Fish_Stocking.aspx`), structure unconfirmed | Reciprocity hub for the Ohio River agreements |
| **Illinois** | No confirmed public API — per-waterbody HTML pages on `ifishillinois.org` | Browse-only interface, no bulk export confirmed | Weakest of the states touched so far; needs scraping, not a feed |

Any other state — Montana included — has no row here yet because Mode E hasn't
run for it. That's expected, not a gap to apologize for; it's what Mode E is for.

Weather and water-flow data are NOT this skill's job — that's `us-weather-advisor`
(USGS Water Data for river gauges, NOAA/NWS for weather, both genuinely nationwide
already). This skill only answers "where" and "what's legal there."

## 2. Modes

| Signal in the request | Mode |
|---|---|
| "find me a place to fish near [city]", "lakes/rivers around [place]" | **A — FIND** |
| "what are the rules on [named water]", "size limit for walleye on [lake]" | **B — RULES** |
| "is there a closed season for [species] in [state]" | **C — SEASON** |
| destination state not yet in the data | **E — EXPAND** |

### Mode A — FIND

Query the state's access-point layer near the given location. For Indiana, this is a
live REST query against the `Fish_Access_RO` FeatureServer — filter by distance from
the given city/coordinates, return `site_name`, `waterbody`, `water_type`, `boat_ramp`,
`shoreline`, `species` fields. For Michigan, same pattern against the Michigan DNR
fishing-access layer. Sort by distance, give 1-2 sentences per result on why it's
worth considering (size, boat access, species present per the data).

**Don't expect that field list to hold outside the states already built.** Every
state designs its own layer, and the first live run against a new one (Montana,
2026-08-21) returned site names, coordinates and amenities but **no `waterbody`
field at all** — the river had to be inferred from site names like "Cameron Bridge."
Take what the layer actually has, say which fields were missing rather than quietly
filling the gap by inference, and never present an inferred waterbody name with the
same confidence as a returned one. A missing `species` field in particular means
*unknown*, not *no fish*.

**Don't silently filter down to one water type.** A river-focused request still
gets shown a nearby lake/pond if the query returned one — moving and still water
behave differently enough (see `us-fishing-advisor` rule 7) that dropping
stillwater options from the answer is a real omission, not a simplification.
**Every site mentioned in the answer gets its Google Maps link** — each fetch
script writes a `maps_url` field per site (`https://www.google.com/maps/search/
?api=1&query=<lat>,<lon>`); include it next to the name, don't make the person
ask for it separately.

**If the FeatureServer/registry query comes back empty or the state has no
confirmed layer at all** (Illinois, or a gap in an otherwise-covered state), don't
stop — this is rule 10's scraping fallback. Search for the specific water/region
directly rather than reporting a bare "no access points found."

### Mode B — RULES

Look up size/bag limits and any water-specific override for the named water. Quote
the specific rule, then note the statewide default it overrides (if any), then cite
the source. If the water isn't in the data, say so — don't infer from a similar
nearby water.

### Mode C — SEASON

Answer yes/no/unknown on closed seasons, with the date range if applicable. Remember
rule #4 above: only Michigan has real closed seasons for walleye/pike/musky among
the states built so far. For the other states covered, redirect to size/bag limits
since that's the actual applicable regulation, not a season — and for a state Mode E
hasn't run yet, don't assume either pattern, get the actual answer first.

### Mode E — EXPAND (add a new state on demand)

Trigger this when someone asks about any US state not yet in `reference-data/states/` — this
is no longer limited to a fixed list (rule 8 above). This is the repeatable
procedure for pulling in a new state's data — the equivalent of a build script, but
run per-state instead of all at once. It's already been run for Indiana, Michigan,
and Ohio (and partially for Illinois and Kentucky); running it for a state like
Montana works the same way, it just hasn't happened yet.

**Step 1 — find the state's open-data pattern.** Most state DNRs (or, in several
Western states, a "Fish, Wildlife & Parks"/"Fish and Game" agency under a different
name than "DNR" — don't assume the agency name, search for it) run on ArcGIS Hub
(`<state>.opendata.arcgis.com` or a state GIS portal under a similar pattern — this
held for Indiana, Michigan, Ohio, and Kentucky in this toolkit's own research, but
hasn't been confirmed outside those four). Search for `"<state> fish and wildlife"
fishing access sites arcgis` or `"<state> DNR" open data GIS` first, adjusting the
agency name for the actual state. If that pattern doesn't hold (as it doesn't for
Illinois), fall back to the state's own fishing-locations web pages and treat it as
a scraping job — one page per waterbody, no bulk feed. **Expect the state's GIS data
to be split across divisions** (Wildlife, Watercraft, Parks, a general GIS portal)
with separate REST service trees and no cross-index — Ohio's real fishing-adjacent
data turned out to live under Division of Watercraft, not Wildlife, and took walking
the REST services folder tree to find (confirmed in the first live Mode E run). Don't
stop at the first plausible-looking layer — check whether it actually covers fishing
access (a lake-habitat polygon layer or a boat-only layer is not the same thing) before
treating it as the answer.

**Step 2 — pull the FOUR things every other state has:** access points/GPS,
size-and-bag-limit regulations (plus any closed-season note), **license info** —
what Max actually needs to buy, where to buy it, and the cost in USD (see
`references/data-schema.md`'s `license_summary`; this is required, not a nice-to-
have — a state file without it isn't done) — and stocking records if published.
Don't try to get everything at once — get access points first (Mode A needs them
immediately), rules and license info second (both from largely the same regs/fee
pages, worth pulling together), stocking third since it's the least time-sensitive.
**Verify any "public, no login required" claim by actually fetching
it** — don't trust the state's own referral/marketing copy. Ohio's own DNR page
claimed its stocking CSV needed no login; the live dataset page itself demanded
account approval when fetched. The claim, not the fetch, was wrong.

**Step 3 — write the new state into `reference-data/states/<state>.json`** following the same
schema as Indiana's file (see `references/data-schema.md`), and note in the file's
header what's confirmed vs. what still needs verification — don't silently treat a
one-pass scrape as complete the way Indiana/Michigan's structured feeds are.

**Step 4 — tell the person plainly** that this state was just added on the fly, so
they know the data hasn't had the same scrutiny as Indiana/Michigan, and to
double-check anything regulation-critical against the state DNR directly.

## 3. How to answer

1. **Cite before summarizing.** State the rule/data as found, then summarize — not
   the other way around.
2. **State the coverage tier up front when it's not Indiana or Michigan.** "Ohio's
   stocking data is solid but I don't have a confirmed access-point feed for it yet"
   is more useful than silently answering from partial data.
3. **Never present a Mode E result as equally authoritative as Indiana/Michigan's
   built-in data** — flag it as freshly pulled and unverified against a second pass.
4. **When asked for legal/regulatory specifics you can't find:** say "not in the
   data" — don't fill the gap from general knowledge of US fishing law, which varies
   too much state to state to be safe to guess.
5. **Always include the Google Maps link for a named site**, not just its name —
   every fetch script writes `maps_url` per result specifically so an answer never
   has to send someone to a name they then have to look up themselves.
6. **Mix water types in a location answer** — don't hand back only rivers when a
   lake or pond turned up in the same query, and vice versa. See Mode A above.

## 4. Token economy

1. **Leave `--limit` at its default (25) unless the request genuinely needs more.**
   A wide FIND radius with a bumped-up limit multiplies both the API payload and
   what gets read back into context for marginal value — 25 nearby options is
   already more than most answers need to mention.
2. **Mode E writes to `reference-data/states/<state>.json` so it only has to run once per
   state.** Before triggering Mode E, check whether that file already exists —
   don't re-run the whole expansion procedure on a second question about a state
   already covered, even in a later conversation.
3. **Don't re-fetch a state's access points twice in the same exchange.** If
   `us-fishing-advisor`'s PLAN mode already pulled candidate waters this turn,
   reuse that result for a follow-up regulation question instead of querying again.
4. **Don't pull a full regulations PDF/page when one number will do.** Mode B needs
   the specific size/bag limit for the water in question, not the entire booklet —
   fetch narrowly (search within the source, or a targeted page range) rather than
   ingesting the whole document by default.

## File Access Protocol

1. Read files with the Read tool.
2. If that fails with a permission error, try a direct filesystem path.
3. If the file is outside the accessible directory, ask where it should be found.
4. Only report a file as missing after all three steps fail.

## Status

Indiana and Michigan have live, working Mode A (FIND — access points via FeatureServer)
and Michigan additionally has the closed-season reference case for Mode C built out.
**Indiana now has a full Mode B (RULES) data file** (`reference-data/states/indiana.json`,
built 2026-08-20, trout and license purchase path added 2026-08-21) — size/bag limits,
license fees, purchase path and reciprocity for all 16 modeled
species, cross-checked against two independent fetches of the official regs PDF, plus
a real correction to this toolkit's own prior research (the Wabash River is also
reciprocal water between Indiana and Illinois, not just the Ohio River and Calumet
Harbor — folded into rule 5 above). **Michigan still has no Mode B data file** — only
the closed-season pattern (`michigan-regulations.md`), not size/bag limits; that's the
next real gap to close. Ohio has been through one live Mode E pass (2026-08-20,
`reference-data/states/ohio.json`) covering access points (partial — river/stream only),
regulations (solid — pulled from the official PDF), and stocking (identified but
access-gated, not actually usable). Illinois and Kentucky are not pre-populated —
they run through Mode E on first request. **2026-08-20: Mode E's scope widened from
a fixed five-state list to any US state** — the procedure itself didn't change,
only the artificial ceiling on when it's allowed to run. A state like Montana is
architecturally no different from Illinois was on day one: untested, but not
out of scope. See `references/data-schema.md` for the state data file format and
`references/roadmap.md` for known gaps.
