# EXPAND — adding a species or a technique on demand

Read this when EXPAND mode fires (`SKILL.md` §2). It mirrors `us-water-finder`'s Mode E:
same spirit — don't refuse, research it properly and disclose that it's fresh — applied to
this skill's own knowledge base instead of state data.

Two things trigger it, and they need different procedures.

---

## A species not in `species.yaml`

**Research it to the same standard as the existing sixteen.** That means every number gets
an evidence tier (`references/evidence-tiers.md`: `[D]` documented, `[P]` plausible, `[F]`
folklore) and a source you actually fetched, not a recollection.

Fill the full schema — an entry with three fields is worse than no entry, because it looks
complete:

- `temperature`: `opt_min`, `opt_max`, `stop`, `upper_stress`, `tier`
- `temperature_note`: where the numbers came from, and what's uncertain about them
- `light` / `light_note` / `active_windows`
- `spawn`: trigger temperature and typical months
- `closed_season`: orientation only — `us-water-finder` is authoritative
- `turbidity`: `benefits` / `neutral`
- `hard_stop` **if and only if** there's a documented mortality threshold, with the citation
  in the `reason` string. Don't invent one for a species that merely gets uncomfortable.

**Source priority, best first:**

1. Peer-reviewed thermal-biology or vision-physiology studies (this is what backs the
   strongest entries in the file — the walleye light window, the cutthroat/rainbow
   comparative thermal study)
2. Federal or state agency technical models — USFWS Habitat Suitability Index documents,
   state DNR fisheries research, USGS studies
3. State agency public-facing species pages
4. Angling-methodology consensus, clearly marked `[P]` — usable for tactics, not for
   biology numbers

An angling blog is not a source for a thermal optimum. If tiers 1–3 produce nothing, the
honest entry has `null` values and a `temperature_note` saying so — `crappie` and
`common_carp` are already in the file that way, and that's the correct shape, not a
failure.

**Then:** add a matching entry to `references/hooks-and-rigs.md`, and say plainly in the
answer that the species was just added and hasn't had the scrutiny the original set had.

**Watch for the Great Lakes collision.** If the species lives mainly in Lake Superior,
Michigan, Erie, Huron or Ontario — lake trout is the obvious case — the biology half of
the answer can be researched normally, but the *location and conditions* half cannot:
`us-water-finder` rule 7 says the Great Lakes don't fit the per-state inland data model,
and `us-weather-advisor`'s lake-temperature estimate is meaningless for a body of water
that size and depth (stratified, hundreds of feet deep, cold most of the year regardless
of air temperature). Adding the species does **not** unlock a confident conditions answer
there. Say which half you can stand behind and which you can't, rather than letting a
successful species-research pass imply the whole answer is solid.

---

## A technique this skill doesn't model

The clearest case is **fly fishing** — out of scope by design, not oversight, and
genuinely likely to come up given how much of American trout culture runs on it. Don't
just refuse.

**Don't force it into `hooks-and-rigs.md`.** That file is built around spinning/casting
tackle: hook sizes, rig types, lure categories tied to the §3 temperature logic. Fly
tackle has a different vocabulary and a different selection logic. Give it its own file
(`references/fly-fishing.md` for that case) rather than bending an existing structure
around it.

**Source discipline — this is the part that's easy to skip.** Techniques don't have
peer-reviewed literature the way thermal optima do, so the tier system from
`evidence-tiers.md` doesn't transfer directly. Use this instead, best first:

1. **State agency instructional material** — many state fish and wildlife agencies publish
   genuine beginner and technique guides, and hatch charts for their own waters. This is
   the closest thing to an authoritative, non-commercial source.
2. **Regional fly shops and guide services for the specific water** — a shop's hatch chart
   and current report for a named river is real, local, current knowledge. It is also
   commercially motivated; take the entomology and timing, be skeptical of the gear
   recommendations.
3. **Established instructional references** (Orvis-style learning centers, long-running
   technique literature) — good for fundamentals: rod/line weight matching, leader
   construction, casting and mending, reading water.
4. **Forums and social** — last resort, same survivorship-bias caution as
   `references/water-reports.md`.

**What a usable technique entry has to cover**, or it isn't done:

- Gear class and how it's matched (rod/line weight to target species and water size,
  leader and tippet)
- **The selection logic that replaces §3's bait categories.** This is the core of it. For
  fly fishing that's matching the hatch — what's actually emerging on that water at that
  time of year — which is a fundamentally different decision procedure from "cold water →
  slow presentation." Don't paraphrase §3 with fly names substituted in; that would be
  wrong in the same way applying the warmwater rule to trout was wrong (see
  `evidence-tiers.md` §8).
- Presentation: dead drift, swing, strip, and when each applies
- Where it changes the *decision*, not just the tackle — a technique that opens water or
  hours the spinning-tackle model would have written off is worth saying so explicitly

**Disclose it clearly.** A technique researched mid-conversation is not at the same
confidence level as the spin/casting content that was built and tested deliberately. Say
so, and suggest they sanity-check it against a dedicated source before relying on it.

---

## Both at once

A request like "what fly for trout on the Madison River" needs a technique expansion
*and* a state expansion (Montana isn't pre-built in `us-water-finder`). **Don't block one
on the other, and don't run both in one turn by default** — that stacks two expensive
procedures for a single question and blows the token budget in `SKILL.md` §5.

Answer the part that's cheap and self-contained first (the technique question, which
doesn't need state data), then say plainly that access points and regulations for that
water need a separate lookup, and offer it. One of the two will usually be what they
actually wanted.
