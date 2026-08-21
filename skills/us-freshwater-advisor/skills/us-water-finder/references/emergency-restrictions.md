# Emergency (drought/temperature-triggered) fishing restrictions

Read this whenever a **river or stream in a western/mountain state** is being recommended
**between roughly mid-June and September**. This is a legal layer the per-state
`reference-data/states/*.json` files deliberately do NOT carry — see "Why this isn't a data field"
at the bottom.

**What this covers:** restrictions imposed and lifted on a days-to-weeks timescale when
water gets too warm or flows drop too low, to protect heat-stressed trout. Montana calls
them "hoot owl" restrictions. They are **not** fixed calendar closed seasons (those live
in `closed_seasons` in the state file) and they are **not** the high-water/flood situation
`us-fishing-advisor` rule 7 handles — the trigger is the opposite, low and warm rather
than high and rising.

---

## The three things that make this easy to get wrong

**1. Not every western state does this, and one does the opposite.** A rule shaped like
"western states close rivers in summer" would be confidently wrong in specific,
user-harming ways. Idaho's fish and wildlife agency has publicly argued the *contrary*
position — that heat and low water do not by themselves justify closing Idaho fisheries.
Utah's drought response is to **raise** daily bag limits at specific reservoirs, to
encourage harvest before a die-off. Don't generalize from Montana.

**2. "Restriction" means different things legally in different states.** Montana's are
enforceable regulatory closures. Wyoming's and Colorado's are framed by the agencies
themselves as **voluntary**. Calling a Wyoming advisory a "closure" overstates it; calling
a Montana hoot-owl restriction "voluntary" could get someone cited. Use the state's own
framing, which is recorded per state below.

**3. The time-of-day boundary is not universal.** Montana's hoot-owl window is 2 p.m. to
midnight. Wyoming's guidance is to stop catch-and-release at **noon**. Don't quote 2 p.m.
as a general rule.

---

## Per state

| State | Uses this mechanism? | Legal status | Published trigger | Current-status source |
|---|---|---|---|---|
| **Montana** | Yes — "hoot owl" | **Regulatory (enforceable)** | Daily max water temp ≥ **73°F for at least part of the day on 3 consecutive days**. Flow triggers are set per named river section in absolute cfs at specific gauges, not one statewide number. Escalates to full all-day closure if hoot-owl proves inadequate. | `fwp.mt.gov/news/current-closures-restrictions/waterbody-closures` |
| **Wyoming** | Yes — no fixed brand name; "fishing in the heat" | **Voluntary/advisory** | ≥65°F: harvest rather than release encouraged. ≥70°F: stop catch-and-release for the day. >75–80°F: described as potentially fatal to trout. Guidance is sunrise–**noon** only. | `wgfd.wyo.gov/fishing-boating/fishing-heat` |
| **Colorado** | Yes — "voluntary fishing closures" | **Voluntary** per CPW (though press coverage describes some as effectively mandatory in practice on named stretches) | Water temp **≥71°F** as the coldwater-stress threshold; also low streamflow/reservoir storage, evaluated per water body rather than one statewide number. | Hub: `cpw.state.co.us/fishing`. Actual current list is a published Google Sheet titled "2026 Weather and Drought Closures" — find it linked from the hub rather than hardcoding the sheet URL, which is not a durable link. |
| **Idaho** | **No — do not assume otherwise** | n/a | IDFG has publicly taken the opposite position: that heat/low water alone doesn't justify closures. No equivalent current-status page found. | n/a |
| **Oregon** | Unconfirmed | Emergency closures exist but are not distinguishable from routine seasonal ones in ODFW's own listing | No numeric trigger program confirmed. ODFW publishes softer "dry year outlook" advisories. | `myodfw.com/articles/regulation-updates` — mixes emergency and routine closures under identical wording; **do not treat a closure found here as drought-triggered without checking why**. |
| **Washington** | Unconfirmed | WDFW uses general emergency rulemaking as the vehicle; no temperature-specific program confirmed | None published | `wdfw.wa.gov/fishing/regulations/emergency-rules` |
| **California** | Ad hoc only | Mixed — has issued both *voluntary* "hoot-owl style" guidance and *formal* emergency regulations closing named river stretches, in drought years | No standing numeric threshold; invoked year to year at agency/Commission discretion | **No reliable single current-status URL found.** `wildlife.ca.gov/fishing/inland/closures` exists but showed no drought content when checked. Weakest state here — check CDFW news and the Fish and Game Commission's emergency regulations, and say plainly that you could not confirm current status. |
| **Utah** | **Inverted mechanism** | Regulatory, but in the opposite direction | Low reservoir levels trigger **emergency increases to daily bag limits**, to encourage harvest ahead of a die-off — not closures | Posted as dated news items at `wildlife.utah.gov/news/`, not as a running status page |

**Scope, across every confirmed case:** rivers and streams only — no confirmed instance of
a hoot-owl-style restriction on a lake or reservoir. (Utah's inverted bag-limit changes are
the exception and *are* reservoir-specific.) Season is roughly mid-June through September.
Restrictions are generally a time-of-day closure on a whole named river segment rather than
species-selective, even though the stated purpose is protecting trout.

**There is no multi-state aggregator.** No structured feed, no shared source. This is
strictly per-state, each with its own terminology, page and update cadence.

---

## How to actually use this

1. **Is it in the risk window?** Western/mountain state + river or stream + roughly
   mid-June to September. If not, this whole file is irrelevant — don't spend calls on it.
2. **Does the state even use the mechanism?** Check the table. Idaho: no. Utah: inverted.
   Don't check a page for a program that doesn't exist.
3. **Try the current-status page** for the states that have a real one (Montana, Wyoming,
   Colorado). One fetch, not a research project.
4. **If you can't confirm current status — say so, don't guess in either direction.**
   For California, Oregon, Washington and Utah there is no dependable current-status page,
   so the honest output is: *"this is in the seasonal window where <state> can impose
   emergency restrictions; I couldn't confirm current status — check <agency link> before
   you go."* That is a genuinely useful answer. "No restrictions found" is not, because it
   reads as "it's open" when what you actually established is "I didn't find a page."
5. **Never assert a river is open based on absence of evidence.** The asymmetry matters:
   recommending a legally closed river is a compliance problem for the user; an
   unnecessary "verify before you go" costs them one click.

## Anticipating risk from data already fetched

Montana's trigger (73°F sustained) is a published number, and `us-weather-advisor`'s
`fetch_water.py` already returns water temperature in Fahrenheit with a 72h trend. That
means a warming trend approaching 73°F on a Montana river is a **predictable** risk, not
just a thing to look up after the fact — worth flagging to the user proactively ("water's
at 71°F and climbing; Montana imposes hoot-owl restrictions at 73°F sustained, so this
could close before your trip").

Treat the **trigger thresholds as durable** (they don't change year to year, and are safe
to rely on from this file) and **current status as never durable** (always live, always
caveated).

Note that a species-level hard stop can fire *below* the regulatory trigger: westslope
cutthroat's documented lethal threshold is 67°F, well under Montana's 73°F. Water can be
legally open and still be biologically wrong for the target species — see
`us-fishing-advisor/references/species.yaml`.

## Why this isn't a data field

An earlier design instinct was to add an `emergency_restrictions` field to
`reference-data/states/*.json`. That would be worse than nothing. The information has a useful life
measured in days, during exactly the season it matters, and a stale "no restrictions"
value in a data file would be read with the same confidence as a verified size limit —
producing a confidently wrong legal claim. Durable trigger criteria live here in prose;
current status is fetched live or explicitly declared unknown.
