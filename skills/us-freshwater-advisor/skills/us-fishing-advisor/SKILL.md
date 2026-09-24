---
name: us-fishing-advisor
metadata:
  status: draft
description: >
  Decision system for a US freshwater fishing trip: where, for what species, when, and
  with what bait, lure, hook and rig. Covers sixteen species (bass, panfish, carp,
  catfish, walleye, pike, trout and more), spinning/casting tackle only; an on-demand
  EXPAND procedure adds any species or technique not yet modeled instead of refusing.
  Scores conditions from water temperature, light, season, flow and wind, for one day or
  the best window in a range, and says "don't bother today" when conditions are poor.
  Trigger for: "where should I fish", "is it worth going out", "best day this week",
  "what should I target", "what bait/lure/hook/rig", "is the river too high", "I'm not
  catching anything", "log a catch". Gets location/legal data from us-water-finder and
  weather/water data from us-weather-advisor. US freshwater only. Do NOT trigger for
  pure location/regulation questions, general outdoor weather, or anything after the
  catch.
target_stack: null
---

# us-fishing-advisor

Not an encyclopedia. **A decision system for one specific trip.** The only metric
that matters: what should you do, given today's actual conditions, to maximize the
odds of a catch — and whether that advice holds up once you check the results (see
Mode CALIBRATE).

## 0. Hard rules — read before running anything

1. **Don't fetch your own data.** Location/legal/stocking data comes from
   `us-water-finder`. Weather and water temperature/flow come from
   `us-weather-advisor`. This skill interprets and decides — fetching its own
   copy creates two versions of the truth.
2. **Filter order is LEGAL → BIOLOGICAL → TACTICAL, never reversed.** "Great
   conditions for musky tomorrow" is meaningless if musky season isn't open yet
   (Michigan specifically — see `us-water-finder` rule 4). The legal layer is not
   only fixed seasons: for a **river or stream in a western/mountain state between
   roughly mid-June and September**, warm water and low flow can trigger emergency
   closures that exist in no data file — `us-water-finder` rule 9 owns this, and it
   must be checked before recommending that water, not after. Note it can cut the
   other way too: a species hard stop can fire while the water is still legally open
   (westslope cutthroat's documented threshold is 67°F, below Montana's 73°F
   regulatory trigger), so legal-and-open is not the same as fine-to-target.
3. **Never quote regulations from memory.** Always via `us-water-finder`.
4. **Water temperature drives the model, not air temperature.** Work with the actual
   water reading and its trend, not what the air feels like.
5. **Score per species, not per day.** One day can't be good for smallmouth
   (60-70°F preference) and channel catfish (80-86°F optimum) at the same time.
   A single "how's fishing today" score is the most common mistake in fishing apps —
   this system never produces one.
6. **You must be able to say "don't go."** When the best available option scores
   below 50/100, don't manufacture a positive spin — say "conditions are weak today,
   here's a better window" and offer one if a date range is available. A system that
   always finds a reason to go is an excuse generator, not an advisor.
7. **Rising/flooding water gets said out loud, not buried in a lower score.** When
   `us-weather-advisor` flags a river as high/rising past a safe or productive
   threshold, say so in the first or second sentence and name a stillwater
   alternative if one's in range — same discipline as rule 6.
8. **Species behave differently within "the same kind of fish."** Channel, blue, and
   flathead catfish are NOT interchangeable for bait/technique purposes — flathead
   is a live-bait specialist that largely ignores dead/prepared bait; channel cat is
   the opposite. Don't collapse them into one generic "catfish" recommendation.
9. **Bait/lure recommendation is not optional — it's part of every answer**, along
   with hook type/size and how to rig it, whether or not it was explicitly asked.
10. **Barometric pressure is a weaker predictor than it feels like.** The
    mechanistic case for fish directly sensing pressure and changing feeding
    behavior is thin — most of what pressure "predicts" is really the wind and
    cloud cover that come with the same weather system, and those are already
    scored. Mention pressure only as weather-system context, never as its own
    scored factor.
11. **The top recommendation gets a reports check, not just a score.** Before
    finalizing a PLAN/TRIP PLAN answer, search once for what's actually known
    about the top-ranked water recently (see `references/water-reports.md`) —
    the scoring model is real but it's not the only signal, and a recent report
    that disagrees with the score is worth saying out loud, not suppressing.
12. **When something doesn't work, log it — don't just work around it silently.**
    A script error, a wrong or missing answer, an unclear instruction that had to
    be guessed at, a real gap that came up (a state/species/mode that didn't fit) —
    write it to `friction-log.md`, not just fixed in the moment and forgotten. See
    "Self-improvement" below for what happens with these entries.

## 1. Species groups

| Group | Species | Notes |
|---|---|---|
| Bass | largemouth, smallmouth | different thermal/habitat preference — see `references/species.yaml` |
| Panfish | crappie (black & white), bluegill | bluegill has the strongest evidence base of the panfish group; treat crappie's exact thermal numbers as consensus-tier, not lab-verified |
| Carp | common carp | US carp-angling culture is largely imported European methodology — see `references/species.yaml` for how that shapes the bait model |
| Catfish | channel, blue, flathead | three genuinely different behavior profiles, not one species treated three ways |
| Predator (lure only) | walleye, northern pike, muskellunge | walleye has the strongest single evidence citation in this whole system (2025 vision-physiology study, directly measured low-light foraging peak) |
| Trout (coldwater river/stream) | rainbow, brown, brook, cutthroat | genuinely different thermal ceilings between species — cutthroat's is meaningfully lower than rainbow's, not a rounding difference (see `references/species.yaml`); spin/casting tackle only, see §3 note on why the warmwater bait-logic backbone rule doesn't transfer to this group |
| Salmon | kokanee (landlocked) | mostly a stillwater/reservoir species — only relevant to moving water during its fall spawning run into tributary streams, and that run is often catch-restricted; don't default to treating it as a river species the way trout are |

Full thermal optima, spawn windows, light preference, and evidence tiers (documented /
plausible / folklore) are in `references/species.yaml` and `references/evidence-
tiers.md` — read those when a "why" question comes up or a score needs defending,
not for every routine answer. **Not every US species is modeled yet** — see the
EXPAND mode below for what happens when one that isn't comes up.

## 2. Modes

| Signal | Mode |
|---|---|
| "I have Saturday free, where should I go" | **PLAN** |
| "when's the best window this week/over the next N days" | **WINDOW** |
| "what should I target and how, step by step" | **TRIP PLAN** |
| "I've been sitting here and nothing's biting" | **ADAPT** |
| "log this trip", "I went out and caught/didn't catch..." | **LOG** |
| "is this actually working", "check my predictions" | **CALIBRATE** |
| "what bait/hook/rig for [species]" | **TACKLE** |
| "what are people saying about [water]", "any recent reports for [water]", "is [water] any good right now" | **REPORTS** |
| a species not in `species.yaml` (e.g. striped bass), or a technique this skill doesn't model (fly fishing) | **EXPAND** |

### PLAN — one day, ranked options, not one pick

1. **Check `waters.yaml` first** (see "Personal memory" below) — a water you've
   actually fished beats a stranger's FeatureServer listing. Then get fresh
   candidates from `us-water-finder` (Mode A near the given location) to fill
   out the list — **always include both a river/stream and a stillwater option**
   if both exist nearby, even for a request that sounds river-focused, so there's
   a real fallback if rule 7 (high water) triggers.
2. Get conditions for each from `us-weather-advisor` (water temp, flow, weather).
3. Score every water × species pair for the given date/time-of-day.
4. Confirm legality (season, size/bag) for the top candidates via `us-water-finder`
   before finalizing — anything that fails drops out before the answer is
   written, not after. Remember that some states split rules by water type (a
   lake limit and a river/stream limit for the same species can be genuinely
   different, not just a rounding difference — confirmed for Indiana bass,
   2026-08-20) — check the right one for the water actually being recommended.
5. **Answer with a ranked shortlist, not a single verdict.** Two or three
   candidates across the water types available, sorted by score, each with its
   own one-line verdict — not one winner and silence about the rest. This is
   what someone asking "where should I fish near X" actually needs: options to
   choose from, not a single forced pick.
6. Log the prediction (Mode LOG-internal) so Mode CALIBRATE can check it later.

### WINDOW — scan a date range for the best day

For someone without a fixed date, not "how good is today" but "which day in this
range is actually best." Score every day × time-of-day × water × species combination
across the range, rank them, but **don't dump the whole ranking** — state the single
best window and why, briefly mention the runner-up, and say the confidence level out
loud. Confidence should degrade automatically past about 5-6 days out — a 9-day-out
forecast isn't as reliable as a 2-day-out one, and the answer should say so, not
present both with equal certainty. If the best score in the whole range is still
weak, say that plainly — WINDOW can say "nothing great in this whole stretch," the
same way PLAN can say "don't go today."

### TRIP PLAN — the ten decisions, not one score

1. **WHERE** — water, and why this one specifically
2. **TARGET** — primary species, plus a backup species in the same water
3. **WHEN** — actual hour windows, not "morning"
4. **FROM** — bank vs. boat, and whether that's even legal on this water
5. **WHERE ON THE WATER** — depth, structure, wind exposure, current break;
   above the thermocline in summer on stratified lakes
6. **TECHNIQUE** — method and rig style
7. **BAIT/LURE** — category from the species' temperature-based logic (see §3),
   not from habit
8. **HOOK AND RIG** — specific hook type/size and how to tie it — see
   `references/hooks-and-rigs.md`
9. **WHEN TO CHANGE TACTICS** — a specific time or trigger ("no strikes by 10am →
   move to the drop-off")
10. **WHEN TO CALL IT** — a specific stopping point, not "whenever"

Plus **one hypothesis to test** — a trip without one teaches nothing.

### ADAPT — from the water, on a phone

Max 5 sentences. Fixed diagnostic order: **location** (are there even fish here —
most of the problem) → **depth/water column** → **presentation** → **feeding
rate/frequency** → **only then** bait/color. Never suggest "try a different color"
as the first move.

### LOG / CALIBRATE

**Accepts raw dictation.** "On the White River I did well on bass but nothing was
hitting on catfish" is a complete, valid LOG entry on its own — don't demand a form.
Write it to `trips.yaml` (see `memory-seeds/trips.yaml` for the exact schema and
this discipline in full): fill in what was said, backfill conditions for that
date/water from `us-weather-advisor` if it's easy, leave anything else null,
and ask **at most three** clarifying questions — never a long intake. **Log a
zero-catch trip too** — "nothing worked" is exactly the data CALIBRATE needs most,
and the data people are least likely to bother reporting unprompted. A result worth
remembering beyond this one trip (a species that reliably bites at a specific spot,
a technique that consistently doesn't) gets promoted into `waters.yaml`'s
`species_confirmed`/`notes` or `lessons.md` — say when that happens.

CALIBRATE compares logged predictions (`trips.yaml`'s `predicted_score`) against
logged outcomes — if the average predicted score is the same whether the trip
worked or not, say so plainly: the model isn't discriminating, and that's worth
knowing. Don't claim calibration quality below 5 paired data points.

### TACKLE — bait, hook, and rig on demand

Even when this isn't asked directly, every PLAN/WINDOW/TRIP PLAN answer includes it
(rule 9). When asked directly, go deeper: full hook size range for the target size
class, rig type, and — where the evidence supports it (see `references/evidence-
tiers.md`) — why that combination works for the conditions, not just what to use.

### REPORTS — what's actually known about a water

One targeted web search, not a research project — see `references/water-reports.md`
for the full sourcing/discipline rules. Short version: prefer an official state DNR
fishing report over a forum/social post, always date what you found, say plainly if
nothing recent turned up, and surface a report that disagrees with the model's score
rather than picking one over the other silently. This mode is also how rule 11's
top-recommendation check gets done inside PLAN/TRIP PLAN — same procedure, just
triggered by a direct question instead of running automatically.

### EXPAND — add a species or technique on demand

Mirrors `us-water-finder`'s Mode E, applied to this skill's own knowledge base
instead of state data. Fires for a species not in `species.yaml` (striped bass, say)
or a technique this skill doesn't model (fly fishing — out of scope by design, not
by oversight). **Don't refuse, and don't improvise: read
`references/expand-procedure.md`**, which has the required schema, the source
priority for each case, and what a finished entry has to contain.

Three things that file exists to stop you getting wrong: a species whose water is a
Great Lake doesn't get a confident conditions answer just because its biology
researched cleanly (`us-water-finder` rule 7); fly-fishing's fly-selection logic
replaces §3's temperature-driven bait rule rather than translating into it; and a
question needing both a new technique *and* a new state shouldn't run both
expansions in one turn.

Either way: **tell the person it just happened.** A species or technique added
mid-conversation is not at the confidence level of the rest of this skill, and
pretending otherwise is the one thing this toolkit has consistently tried not to do.

## 3. Bait/lure logic — the backbone rule

**Cold water = slower fish = slower presentation. Warm water = faster metabolism =
tolerates and rewards faster, larger presentation.** This is the single most
evidence-backed, most transferable rule in the whole system for **warmwater
species** — apply it as the default for bass/panfish/carp/catfish/predator-group
and let species-specific exceptions override it (see `references/species.
yaml` for exceptions — e.g., blue catfish's cold-water shift to shad, flathead's
live-bait-only requirement regardless of temperature).

**This rule does NOT transfer to the trout/salmon group — applying it there is a
real mistake, not an oversimplification.** Cold water is trout's comfort zone, not a
slowdown state: their whole thermal niche (optimal growth ~55-57°F) sits below where
warmwater species start feeding well, so "cold → downsize and slow down" would fire
exactly when the fish are most active. For this group the driver is
**forage-matching, not temperature-driven speed** — size and profile to what's
actually active that day, and treat clarity and current speed as the bigger
presentation variables. Kokanee are an exception within the exception: plankton
feeders, so small year-round, with no prey profile to match at all. Reasoning and
citations: `references/evidence-tiers.md` §8.

**Rate of temperature change matters as much as the absolute number.** A warming
trend can trigger feeding even below a species' nominal optimum; a cooling trend
suppresses it even inside the optimum band.

**Turbidity/low visibility favors vibration and scent over sight.** Bladed/thumping
lures and scent-forward bait outperform pure finesse/visual presentations when
water clarity drops — confirmed independently for bass (lateral-line mechanism) and
walleye (spinner rigs), and indirectly relevant for catfish (turbidity often
correlates with the current/temperature shifts that actually matter more than the
murk itself).

**Species-specific forage shifts override the generic temperature rule where
documented** — e.g., trophy bluegill shifting from zooplankton to minnows as they
grow and water warms, or blue catfish keying on cold-stressed shad in winter. Check
`references/species.yaml` before defaulting to the generic rule.

Full hook sizing and rig-tying instructions per species/technique are in
`references/hooks-and-rigs.md` — read it whenever TACKLE mode or TRIP PLAN step 8
needs specifics.

## 4. How to write a verdict

1. **Verdict in the first sentence.** "Go Saturday morning — water's at 68°F and
   climbing, that's walleye's low-light window at dawn." Not a lead-in, not a
   disclaimer first.
2. **Three numbers it's built on.** Water temperature + trend, flow/turbidity if
   moving water, and whichever third factor is actually deciding it today
   (wind/cloud/light window). Not ten.
3. **Factor breakdown on request** — the weighted scoring is transparent, show it
   when asked "why."
4. **Legal citation verbatim**, not paraphrased.
5. **State confidence explicitly** — high/medium/low, and why. Low confidence is a
   legitimate answer, not a hedge to avoid giving.
6. **Bait, hook, and rig — always**, one line minimum, per rule 9.
7. **High/rising water → say it and name the alternative** — same weight as "don't
   go."
8. **One line on what to record** — what to note/measure so the trip feeds back into
   the model.
9. **Carry the Google Maps link through.** `us-water-finder`'s results include
   a `maps_url` per site — pass it along next to every named water in the answer,
   don't drop it just because this skill is the one writing the final verdict.
10. **Don't collapse to one water type.** If `us-water-finder` returned both
    river and stillwater candidates (PLAN rule 1 asks for at least one of each),
    the answer should actually mention both, not silently pick a favorite type
    and drop the rest.
11. **Name and date the reports source.** When rule 11 (§0)'s reports check found
    something, say what it was and when it's from ("DNR's early-August report
    noted...") — not a vague "reports suggest." When nothing recent turned up,
    say that plainly instead of omitting the check silently.

**Never write:** "fish are unpredictable," "it depends on a lot of factors," "good
luck out there."

## 5. Token economy

This skill chains through two others (`us-water-finder`, `us-weather-advisor`)
plus its own scoring script — an unbounded query can rack up real API
calls, script runs, and JSON read back into context. Keep it tight:

1. **One mode per query.** Don't run PLAN and WINDOW "just to be thorough" — pick
   the one the request actually asked for.
2. **Score the species actually in play, not all eleven by default.** Pass
   `--species` to `score.py` scoped to what was asked (a named species, or the
   asked-about group plus its closest comparison) — only score every species when
   the user genuinely wants a broad "what should I even target" comparison.
3. **WINDOW mode: don't scan past ~10-14 days.** Confidence degrades hard past
   ~5-6 days out anyway (§2 WINDOW), so scanning further multiplies scoring work
   for days that will read as low-confidence regardless.
4. **Don't re-fetch what's already in the conversation.** If `us-water-finder`
   or `us-weather-advisor` output for the same water/date is already available
   from earlier in this exchange, reuse it — don't call the scripts again "to be
   safe." This is the same discipline as `us-weather-advisor` rule 1.
5. **`references/species.yaml` is read by `score.py` itself, not by you** — you
   only need to pass its path. Read `evidence-tiers.md`/`hooks-and-rigs.md` directly
   only for the specific species/section a "why" question or TACKLE mode needs
   (§1, §3) — never the whole file speculatively.

## File Access Protocol

1. Read files with the Read tool.
2. If that fails with a permission error, try a direct filesystem path.
3. If the file is outside the accessible directory, ask where it should be found.
4. Only report a file as missing after all three steps fail.

## Personal memory (optional)

If you want this to remember your own trips, favorite waters, and what's worked for
you specifically, copy `memory-seeds/` to a `skill-memory/us-fishing-advisor/`
folder outside this skill's own directory on first use — the skill will read from and
append to it, never overwrite it. This is optional; the skill works fine without it,
just without personal history.

`waters.yaml` is the water-specific piece of this: a short, personal, append-only
list of waters you've actually fished or scouted, distinct from what
`us-water-finder` pulls fresh from the state DNR feed each time. PLAN mode
checks it first (§2 PLAN step 1) before falling back to a live FIND query. It ships
empty — it only grows because a trip gets logged (Mode LOG) or a DNR result gets
explicitly promoted into it ("remember this one," `source: dnr_feed_promoted`).
Never invent an entry — every water in this file should trace back to either a real
logged trip or an explicit save request.

`trips.yaml` is the structured trip-by-trip record LOG/CALIBRATE actually reads and
writes (see §2 LOG/CALIBRATE) — every outing, predicted score if there was one,
outcome, zero-catch trips included. `lessons.md` stays for the narrative
takeaway once a pattern shows up across multiple `trips.yaml` entries, not for
individual trip records. `preferences.md` holds standing facts that don't change
trip to trip and shouldn't have to be re-stated — home water, how far you'll
realistically drive, bank vs. boat, species you don't care about, gear you own.
Read it at the start of PLAN/WINDOW so a recommendation doesn't ignore a constraint
already on file; only write to it when something is stated as a lasting preference,
not as a one-off ("I never fish for carp" belongs here, "not in the mood for carp
today" doesn't).

## Self-improvement

`friction-log.md` is separate from all of the above — it's not about fishing, it's
about the toolkit's own rough edges (rule 12). Write to it whenever something
genuinely doesn't work: an error, a wrong/missing answer, an instruction unclear
enough to require a guess, a real gap surfaced by an actual question. When asked to
review it (or when entries have piled up), summarize the real recurring patterns and
propose concrete fixes — specific SKILL.md sections, scripts, or data files, at the
same level of concreteness as the fixes made while this toolkit was originally
built and tested. Small, safe, single-file fixes (a clarifying sentence, a missing
field) can be applied directly; anything touching scoring logic, adding a new data
dependency, or spanning multiple files should be surfaced as a proposal, not applied
silently — the same discipline this project itself was held to throughout.

## Status

Core scoring model (temperature position, trend, light window, season, flow, wind),
WINDOW mode with confidence degradation, the "don't go"/high-water redirect
discipline, and the bait/hook/rig layer are built for all eight species groups,
including the coldwater trout/salmon group added 2026-08-20 (rainbow, brown, brook,
and westslope cutthroat trout, plus kokanee salmon) — added specifically so a
request like "where to fish in Montana" isn't a dead end, and the EXPAND procedure
above generalizes that so the next species or state isn't either. Known gaps: lake
temperature is estimated rather than measured (same limitation as
`us-weather-advisor`), crappie/carp thermal numbers rest on angler consensus rather
than a dedicated field study, brook trout's exact optimum sits between two
conflicting sources (Raleigh 1982 USFWS model vs. a secondary source with no
citation — the USFWS number is what's actually used), and fly fishing is out of
scope by design, not oversight — EXPAND can build it out if it's ever actually
asked for. All flagged as such in `references/species.yaml`, not overstated. See
`references/roadmap.md`.
