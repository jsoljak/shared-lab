# State Data File Schema

Used whenever a state's regulation/license/stocking layer gets built or refreshed —
via Mode E (EXPAND) for a new state, or a direct research pass for a state that
already has Mode A (like Indiana, 2026-08-20). Write to `reference-data/states/<state>.json`
following this shape, so Mode A/B/C can read it the same way regardless of which
state it came from. This is the real, current shape (Indiana's and Ohio's files both
follow it) — earlier versions of this doc had a thinner example; `license_summary`
in particular is REQUIRED, not optional, per below.

```json
{
  "state": "ohio",
  "source_note": "Freeform note on where this came from and its confidence level — e.g. 'pulled via Mode E on 2026-09-01, access points confirmed against data.ohio.gov, regulations not yet cross-checked against the full PDF booklet'",
  "confirmed": ["access_points", "stocking"],
  "unconfirmed": ["regulations_full_text", "closed_seasons"],
  "access_points_source": "URL or API endpoint used",
  "access_points_caveat": "Free text — what the access-point layer actually covers and doesn't (e.g. rivers only, no lake shoreline; wrong division; row-count caps). Optional but strongly recommended whenever the layer isn't a clean, purpose-built fishing-access feed.",
  "regulations_source": "URL — usually a PDF booklet unless a structured feed was found",
  "regulations_summary": {
    "<species_key>": "Plain-language size/bag limit for this species, matching the keys in us-fishing-advisor/references/species.yaml. As of 2026-08-21 that is 16 species: largemouth_bass, smallmouth_bass, crappie, bluegill, common_carp, catfish_channel, catfish_blue, catfish_flathead, walleye, northern_pike, muskellunge, rainbow_trout, brown_trout, brook_trout, cutthroat_trout, kokanee_salmon. Read species.yaml rather than trusting this list — it is a convenience copy and has already gone stale once (the trout/salmon group was added to species.yaml on 2026-08-20 and this list wasn't updated until a day later, which meant a state built from the schema in between would have silently skipped trout entirely). If a rule differs between lakes and rivers/streams, say so explicitly in the same entry — don't record only one and imply it covers both (a real gap caught for Indiana bass, 2026-08-20: the first research pass only recorded the lakes number). MANY STATES REGULATE TROUT AS ONE COMBINED GROUP rather than per species (confirmed for both Indiana and Ohio) — when that's the case, record the combined rule once under a `trout_combined` key and point the individual species keys at it, rather than duplicating or inventing per-species numbers. A species genuinely not present/regulated in the state gets an explicit 'NOT FOUND, do not infer' entry, not silence.",
    "water_specific_examples_found": ["A handful of named-water overrides — doesn't need to be exhaustive, but should be sourced from the actual regs text, not invented."]
  },
  "stocking_source": "URL or API endpoint used — and CONFIRM by fetching whether it's actually public, don't trust a referral page's 'no login required' claim (Ohio's stocking data claimed no login and was in fact gated; verify don't assume).",
  "closed_seasons": {
    "note": "Only Michigan has genuine statewide closed seasons for walleye/pike/musky among these five states — for any other state, this should normally be empty/null. If Mode E finds evidence otherwise, flag it clearly rather than assuming the Michigan pattern applies."
  },
  "license_summary": {
    "resident_1yr": "Cost in USD",
    "resident_1day": "Cost in USD, if offered",
    "nonresident_1yr": "Cost in USD",
    "nonresident_1day": "Cost in USD, if offered",
    "where_to_buy": "How Max actually gets one — official state license-sales site/app, in-person retailer, or both. A cost number with no purchase path isn't actionable.",
    "notes": "Anything else that changes what to buy — a trout/salmon stamp requirement, a youth/senior tier, license-year start date, etc.",
    "source": "URL — cross-check against the regs PDF, don't rely on one source alone if the fee schedule has its own page."
  },
  "reciprocity": "Free text — named boundary waters where a neighboring state's license is also valid, if any (see SKILL.md rule 5 for the toolkit-wide list this should stay consistent with). If a new reciprocal water is found here, add it to SKILL.md rule 5 too, not just this file.",
  "great_lakes_note": "Free text — if this state touches a Great Lake, flag that it has its own regulatory layer not covered by this file's inland/statewide summary (SKILL.md rule 7), even if not researched in depth.",
  "known_gaps": ["whatever wasn't confirmed in this pass"]
}
```

**Why `license_summary` is required, not optional:** the regulations and access-point
layers tell someone where they can go and what they can keep — but without knowing
what to buy, where, and for how much, none of that is actionable for someone who
isn't already a resident angler. This is exactly the kind of thing a toolkit built
for a specific person (not a generic reference) has to get right by default, not on
request.

**Why `confirmed`/`unconfirmed` exists:** Indiana and Michigan's access-point data
came from a dedicated research pass with live-tested endpoints. A state added on the
fly via Mode E — or a regulations/license layer built after the fact, like Indiana's
— has NOT had the same scrutiny as a multi-pass review. This field is what lets
`SKILL.md` rule 3 ("never present a Mode E result as equally authoritative") actually
be enforced in the answer, rather than being a rule nobody checks.
