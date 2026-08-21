# Evidence Tiers

Read this when a score needs defending or a "why" question comes up. For routine
answers, `SKILL.md` + `species.yaml` are enough.

**Tiers:** `[D]` documented (peer-reviewed or direct field/telemetry study) ·
`[P]` plausible (mechanism makes sense, evidence is thinner or indirect) ·
`[F]` folklore (repeated widely, doesn't hold up or is unsupported).

---

## Decision layering

| Layer | What | How it enters |
|---|---|---|
| 1 | Closed seasons, size/bag limits, legal water access | **binary filter** — excludes the species/water entirely |
| 2 | Water temperature and its trend, light/time-of-day, season | ~70% of score weight |
| 3 | Flow and turbidity, wind and cloud cover | ~30% of score weight |
| 4 | **Barometric pressure, moon phase** | **do not enter the score** |

---

## 1. Water temperature — strongest predictor, `[D]`

Fish are ectotherms. Metabolism and digestion speed scale with temperature (Q10 ≈
2-3× per +10°C). Feeding rate vs. temperature is a dome-shaped curve — rises to an
optimum, then drops sharply as oxygen demand outstrips supply. Score the position
on the species' curve, not the raw number.

Key contrasts (full values in `species.yaml`):
- Smallmouth bass (field preference ~70°F) vs. channel catfish (optimal digestion
  80-85°F) — one day can't be great for both.
- Bluegill spawns in repeated bouts through the whole summer (4-11 per season,
  documented) — not one spring event like most species.
- Muskellunge has a hard, telemetry-measured upper danger threshold (26°C/79°F)
  tied to post-release mortality risk, not just reduced feeding.

**Rate of change is its own factor.** A warming trend can trigger feeding even below
nominal optimum; a cooling trend suppresses it even inside the optimum band.

## 2. Oxygen and thermal stratification — `[D]` as a habitat constraint

Lakes stratify seasonally; the deep layer (hypolimnion) can lose oxygen. Predators
including walleye concentrate in the upper, oxygenated layer even when they'd
otherwise hold deeper — below the thermocline, they generally aren't catchable
regardless of temperature match. Largemouth bass actively avoid hypoxic water,
selecting cooler, better-oxygenated water when the surface gets too warm — this is
the real mechanism behind the "warm water hurts bass fishing" observation, not heat
itself. `[D]`.

## 3. Light, time of day, turbidity — `[D]` for walleye and largemouth specifically

- **Walleye**: has a tapetum lucidum (light-reflecting eye layer) — directly measured
  in a 2025 study. Reaction distance and foraging success peak specifically between
  nautical and civil twilight, not in full darkness or bright daylight. This is the
  strongest single citation in this knowledge base — `[D]`, directly usable as a
  light-window weight.
- **Largemouth bass**: foraging success measurably higher at low/moderate light than
  bright midday sun (direct study). `[D]`.
- **Northern pike**: daytime ambush predator, limited by temperature and cover more
  than light. `[P]` — behaviorally documented, not a vision-physiology study like
  walleye's.
- **Crappie**: strong, near-universal angler consensus on low-light/night activity
  (dock-light feeding is a well-known pattern), plausible given large, light-sensitive
  eyes similar in principle to walleye — but no controlled vision study found.
  `[P]`, not `[D]`.
- **Bluegill**: a dedicated literature review (Wisconsin DNR, synthesizing multiple
  peer-reviewed studies) explicitly found *no* documented light-preference data —
  treat any dawn/dusk claim for bluegill as `[P]` at best, and say so.

## 4. Flow, turbidity, and catfish chemoreception — `[D]`

Catfish have amino-acid-specific olfactory detection and enormous numbers of taste
receptors distributed over the body and barbels — detection keys specifically on
amino acids released from fish flesh/slime, not on blood as such (blood is a
secondary signal, not the primary one — this directly contradicts common angler
belief and is worth surfacing when it comes up). Temperature governs how far a scent
plume travels (hundreds of feet warm, under 30 feet near-freezing) — cold-water
catfishing should tighten bait spacing rather than assume the fish "went off the
bite." `[D]` for the mechanism; the exact numeric ranges reported come from a single
non-academic source and should be treated as directionally right rather than
citation-grade precise.

Turbidity favors scent/vibration-oriented feeding generally (catfish chemoreception,
bass and walleye lateral-line/vibration detection) over sight-oriented presentation.
`[D]` for bass (lateral line) and walleye (jig-spinner performance in cloudy water),
`[P]`/indirect for catfish (turbidity often correlates with the flow/temperature
shifts that matter more than the murk itself).

## 5. Barometric pressure — `[F]` as a predictor

A passing weather front is a pressure change of roughly 10-30 hPa — a fish achieves
the same pressure change by moving 10-30 cm up or down in the water column. Fish can
sense pressure (swim bladder, Weberian apparatus in cyprinids), but the case for a
small barometric shift *by itself* triggering feeding is thin; what actually
correlates is the wind, cloud cover, and temperature drop that come with the same
front — and those are already scored. Cold-front feeding suppression is genuinely,
repeatedly field-documented in bass fishing (multiple named Bassmaster/Elite Series
pros describe the same 1-2 day post-front slump and the same fix: downsize, slow
down, fish heavier cover) — but model that as a short-term post-front modifier, not
as "pressure" entering the score directly.

## 6. Moon phase — `[F]`

Solunar theory has no controlled freshwater study that survives scrutiny; outdoor
media itself is split on it. The only defensible remnant: moon phase changes night
light level, which matters for the same species where low light already matters
(walleye, catfish, night crappie) — that's a light factor, not a "moon phase" factor,
and it should be modeled as such if at all.

## 7. Season and spawn — `[P]`/`[D]`

Pattern: pre-spawn feeding surge (well-documented, especially bass) → spawn-period
lull → 1-3 week recovery → strong post-spawn window. Spawn timing is
temperature-triggered, not calendar-triggered — the dates in `species.yaml` are
typical for Indiana/Ohio Valley latitude and will shift in an unusually warm or cold
year. Legal closed seasons (Michigan specifically) are a hard filter regardless of
what the biology says — see `us-water-finder`.

## 8. Trout and salmon are a genuinely different curve, not a colder version of the same one

Every warmwater species in §1-§7 shares one underlying shape: cold water suppresses
feeding, warm water (up to a stress ceiling) drives it. Trout and kokanee invert
that — their whole thermal niche sits in the 50s-60s°F, well below where warmwater
species even start feeding well, and there's no "stop" temperature the way bass has
one (`species.yaml`'s brook and cutthroat trout entries both have `stop: null` for
exactly this reason — cold water near freezing is normal operating range for this
group, not a shutdown condition). Applying the "cold=slow" bait-logic backbone rule
(SKILL.md §3) to trout is a real mistake, not a simplification — it would mean
downsizing and slowing down exactly when the fish are most comfortable and active.
`[D]` for the thermal-niche shape itself (Raleigh 1982 USFWS brook trout model,
McMahon MSU rainbow/cutthroat comparative study, Elliott brown trout growth model —
see Sources below); `[P]` for the specific claim that forage-matching (not
temperature) is the dominant presentation driver for this group, since that's
angling-methodology consensus rather than a controlled study.

**Cutthroat vs. rainbow is the sharpest species-specific contrast in this whole
knowledge base for a within-group comparison.** Same study, same protocol, same
water: rainbow tolerates sustained temperatures to 24.3°C/75.7°F, westslope
cutthroat's equivalent threshold is 19.6°C/67.3°F — a full 5°C/9°F lower, not a
rounding difference. That's directly relevant to why rainbow trout displace native
cutthroat as water warms, and why a marginal-temperature cutthroat water is a real
biological risk to the fish specifically, not just a lower score for the angler.

**Brown trout is the one fall spawner in this group** — rainbow and cutthroat both
spawn in spring, brook trout also spawns fall like brown trout does. Don't default
to "trout = spring spawner" without checking which species is actually being asked
about.

**Kokanee's forage is plankton, not a larger prey item** — the "match the hatch"
logic that drives trout lure selection doesn't really apply; small, flashy
attractors behind a dodger/flasher are the actual working presentation (`[P]`,
angling-methodology consensus, not a controlled feeding study). Kokanee are also
functionally a stillwater species — their only real river/stream relevance is a
short fall spawning-run window into tributaries, and that window is frequently
gear-restricted specifically to protect the spawning population.

## 9. "Cold water = smaller/stronger-scent bait" — the US carp/catfish parallel

US carp-angling culture is largely imported European methodology (the hair rig
itself wasn't IGFA-approved for records until 2007). The available US sources
support a soft version of the same rule the Czech original documents: cold water
lowers a fish's tolerance for a large caloric/protein load while raising the value of
a strong, fast-diffusing scent signal, favoring a smaller, higher-attractor bait over
a large "food value" bait — `[P]`, mechanism-consistent, not a taste-preference claim.
"Warm water prefers sweet flavor" specifically is weaker — treat as closer to `[F]`,
same as the Czech original's treatment of the same folk claim. One clean,
well-sourced debunk: corn does **not** damage a fish's digestive system (a
persistent myth) — the only real corn restriction in the entire five-state region is
Rhode Island's, which is outside this toolkit's scope anyway; most "corn is illegal"
claims online are themselves folklore.

---

## Sources

Coutant, C.C. — *Responses of Bass to Natural and Artificial Temperature Regimes*
(Oak Ridge National Laboratory). Michels et al. 2025, *Visual sensitivity, foraging
behavior, and success of walleye*, Environmental Biology of Fishes 108. Bieber &
Suski 2024, *Spatial ecology and thermal preferences of muskellunge within a Midwest
impoundment*, Aquaculture, Fish and Fisheries 4. Wisconsin DNR Bluegill Literature
Review. Nevada Division of Environmental Protection, Channel Catfish Thermal
Tolerance Analysis. McMahon & Holanov 1995, J. Fish Biol. (bass light-intensity
foraging).

**Trout/salmon group (added 2026-08-20):** McMahon et al., *Comparative Thermal
Requirements of Westslope Cutthroat and Rainbow Trout*, Montana State University
(Transactions of the American Fisheries Society) — direct comparative UUILT/growth
study, the primary source for both `rainbow_trout` and `cutthroat_trout` thermal
values. Elliott, J.M. — brown trout growth-temperature model (via Wild Trout Trust
thermal biology paper) — the primary source for `brown_trout`'s growth-range and
zero-growth thresholds. Raleigh, R.F. 1982, *Habitat Suitability Index Models: Brook
Trout*, USFWS Biological Services Program (the standard federal reference for this
species) — primary source for `brook_trout`. Mullen, J.W. 1958 (feeding-activity
temperature range, secondary/older source for brook trout, doesn't fully agree with
Raleigh — flagged as such in `species.yaml`). Multiple USGS thermal-acclimation
studies on brook trout, 2024-2025 (species-sensitivity confirmation, not the primary
numeric source). *Effects of Light Intensity and Photoperiod on the Feeding Behavior
of Rainbow Trout*, Fishes 11(3):183, 2025 — rainbow trout light-window source.
Washington Dept. of Fish & Wildlife kokanee species page — kokanee temperature/depth
citation (cross-regional, not Montana-specific, flagged `[P]` in `species.yaml`).
Montana Field Guide (fieldguide.mt.gov) — kokanee spawn timing, westslope cutthroat
spawn timing/temperature trigger. Vermont Fish & Wildlife Dept. rainbow trout page —
spawn timing/incubation temperature. Full citation list and URLs: see the toolkit's
build research notes.
