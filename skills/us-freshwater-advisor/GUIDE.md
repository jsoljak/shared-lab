# US Freshwater Advisor — field manual

Most fishing trips are a coin flip, because nobody can watch the water every day. This is
a set of three Claude skills that replaces that missing day-to-day observation with public
data — water temperature, flow, weather, regulations — and turns it into one answer: go
here, target this, at this hour, with this on the end of your line.

---

## What it is

Each skill owns one question and refuses to answer the other two. That separation is
deliberate: it means there is exactly one source of truth for "what's legal here," rather
than three skills that could quietly drift apart and start contradicting each other.

**`us-water-finder` — where can I legally fish, and what applies there**
Access points with GPS and map links, size and bag limits, closed seasons, licence cost
and where to buy one. Pre-built for Indiana, Michigan and Ohio; any other state gets built
the first time you ask about it.

⌄ *passes waters + legal constraints down*

**`us-weather-advisor` — what are the conditions actually doing**
Live NOAA forecast and USGS river gauges: water temperature in Fahrenheit, flow, 72-hour
trend, and a radar link when rain is genuinely in play. Works anywhere in the US, and
answers plain outdoor questions too (a hike, a camping weekend) with no fishing involved.

⌄ *passes measured conditions down*

**`us-fishing-advisor` — so what should I actually do**
Scores every water × species pair for the day and hour, ranks them, and writes the verdict
— including the bait, hook size and rig. This one never fetches its own data; it interprets
and decides.

**You only ever talk to the last one.** It calls the other two itself.

---

## Install

Roughly five minutes, one edit required.

### 1. Put the three folders where your Claude looks for skills

Copy (or symlink) the three folders inside `skills/` into your skills directory. The exact
location depends on which Claude you use — Claude Code, Cowork and Claude Desktop each have
their own; check the current docs for yours.

Keep each folder intact. The layout *is* the format: `SKILL.md` has to sit at the top of
its folder with `references/` and `scripts/` beside it.

### 2. Put your own contact address in the weather script

Open `us-weather-advisor/scripts/fetch_weather.py` and replace
`PUT-YOUR-EMAIL-ADDRESS-HERE` near the top with your own email.

NOAA asks every caller to identify itself with a real contact rather than a browser string.
It works fine without this today, but they can rate-limit or block requests that ignore it
— thirty seconds now beats debugging it later.

### 3. Check Python is there

The five data scripts need Python 3 and, for scoring, `pyyaml` (`pip install pyyaml`).
Nothing else — no API keys, no accounts, no paid services. Every source it uses is free
and public.

### 4. Ask it something

Try *"where should I fish near Anderson, Indiana this weekend?"* — Indiana is the most
complete state, so it's the best first test of whether the whole chain is wired up.

> **Where to keep it.** If you file things with something like PARA, this sits naturally
> under an **Areas → Hobby Fishing** sort of folder — it's an ongoing interest rather than
> a project with an end date, and it accumulates its own history over time. If you use
> something else, put it wherever open-ended hobby material already lives. Nothing about
> the toolkit depends on this.

---

## What to ask

Plain language. The mode names below are internal — you never type them.

| Ask it | Mode |
|---|---|
| "I've got Saturday free, where should I go?" | Plan |
| "When's the best window in the next ten days?" | Window |
| "I'm going to the White River Thursday — full plan" | Trip plan |
| "What hook and rig for flathead catfish?" | Tackle |
| "Been here three hours and nothing's biting" | Adapt |
| "Any recent reports for this lake?" | Reports |
| "Did well on bass, nothing on catfish" | Log |
| "Is this thing actually predicting well?" | Calibrate |
| "What's the limit on brown trout in Indiana?" | Rules |
| "I'm going to Montana — where do I start?" | Expand |

### Three things it does that are easy to miss

**It will tell you not to go.** When the best option on the board scores under 50, it says
so and offers a better window instead of manufacturing a reason to drive somewhere. An
advisor that always finds an excuse to fish is a fantasy generator, not an advisor.

**It scores per species, never per day.** One day can't be good for smallmouth and channel
catfish at the same time — they want water twenty degrees apart. A single "fishing is 7/10
today" number is the most common mistake in fishing apps, and this system deliberately
cannot produce one.

**You always get the bait, hook and rig**, whether you asked or not. Knowing where and when
to go is half an answer.

---

## How it works

Some of what it knows sits in files inside the skill and never touches the network. The
rest has to be live, because a stored copy would be wrong within days. Knowing which is
which tells you how much to trust an answer.

| | |
|---|---|
| **Species biology** | Local file. Thermal optima, spawn windows, light preference and forage for sixteen species, each number carrying an evidence tag — documented, plausible, or folklore — so a claim can be argued with rather than just believed. |
| **Regulations & licences** | Local file, one per state, with the official source URL recorded inside it. Built once, then read offline. |
| **Access points** | Live, every time. Queried straight from the state's own mapping service, so a ramp added last month shows up. Not scraping — a real structured query. |
| **Weather & water** | Live, always. NOAA for forecast and radar, USGS for gauge readings. These change hourly; a cached copy would be worse than useless. |
| **Recent reports** | Live search, and only for the top-ranked water — the point of a report is that it's fresh, and checking five waters would cost five times as much for no gain. |

### The order it thinks in

Legal first, biology second, tactics last — never reversed. "Great conditions for musky
tomorrow" is a meaningless sentence if the season isn't open. Everything that fails the
legal filter drops out *before* the answer gets written, not after.

> **⚠ Western rivers in summer.** Montana and several neighbours close rivers on
> days-to-weeks notice when water gets too warm — Montana's "hoot owl" restrictions shut
> fishing from 2 p.m. to midnight, and they're enforceable law, not advice. These exist in
> no data file anywhere, so for a western river between roughly mid-June and September the
> skill checks the state's current-status page live. If it can't confirm, it says so and
> hands you the link rather than guessing that the water is open.

---

## Your history

Optional, off by default, and it stays on your machine.

The toolkit works fine with no memory at all — you just don't get personal history. If you
want it, copy `memory-seeds/` to a `skill-memory/us-fishing-advisor/` folder *outside* the
skill's own directory on first use. It ships empty and only ever gets appended to, never
overwritten.

| | |
|---|---|
| `waters.yaml` | Waters you've actually fished. Checked before it goes looking for strangers in a government database — somewhere you know beats a name on a map. |
| `trips.yaml` | Every outing, including the blank ones. Zero-catch trips are the data the model needs most and the data nobody volunteers. |
| `preferences.md` | Standing facts that shouldn't need re-stating — how far you'll drive, bank or boat, species you don't care about. |
| `lessons.md` | The narrative takeaway once a pattern shows up across several trips. |

You don't need to fill in a form. *"Did well on smallmouth at the bend, nothing on catfish,
water looked lower than last time"* is a complete, valid entry — it backfills the conditions
itself and asks at most three follow-up questions.

Once there are enough logged trips, you can ask whether the thing is actually any good. If
the average predicted score is the same whether the trip worked or not, it will tell you
that plainly: the model isn't discriminating. That's the point of keeping the log.

---

## What it won't do

**Fly fishing.** This is spinning and casting tackle. Fly gear has a genuinely different
selection logic — matching a hatch rather than reading water temperature — and half-
answering it would be worse than not answering. It isn't a wall, though: ask, and it will
research the technique properly and tell you the result is fresh and unvetted rather than
pretending otherwise.

**Anything after the catch.** Cleaning, cooking, recipes, mounting. The scope ends when the
fish is in the net.

**Outside the US.** It's built on US federal and state data sources. Ask about Ontario and
it will say so rather than improvising from general knowledge.

**Species it doesn't know.** Same as fly fishing — it researches and adds them on request,
then flags that they haven't had the scrutiny the original sixteen got.

---

## Where it's thin

Read this before trusting an answer more than it deserves.

**Most states have never been touched.** Indiana, Michigan and Ohio have real, tested data.
Kentucky is partial, Illinois has no clean data feed at all, and everywhere else gets built
from scratch the first time you ask. A freshly-built state is *unverified*, not merely new
— and it will say so.

**Lake temperature is estimated, not measured.** The USGS gauge network covers rivers and
streams; there's no equivalent for still water. Trust a river number considerably more than
a lake number. For the Great Lakes it declines to estimate at all — they're too deep and too
stratified for the model to mean anything.

**The scoring has never been calibrated against real results.** The weights are reasoned
from published fisheries research, not tuned against outcomes, because there are no logged
outcomes yet. Treat a high score as "conditions favour this," not as a prediction.

> **⛔ Not a legal source.** Size limits, seasons and access rules change, and a wrong
> answer costs you a citation, not just a bad day. The toolkit records where every
> regulation came from precisely so you can go check it. For anything that matters,
> check it.

---

## When it gets something wrong

When something doesn't work — a script errors, an answer is wrong, an instruction was
ambiguous enough that it had to guess — it writes an entry to `friction-log.md` rather than
working around it silently and forgetting.

Ask it to review that log once entries have piled up and it will look for the real recurring
patterns and propose specific fixes. Small safe ones it can apply directly; anything
touching the scoring logic or spanning several files it will show you as a proposal first
rather than changing quietly behind your back.

The failure worth reporting loudest is the boring one: a data source being down. The scripts
distinguish "the server is having a bad day, try again shortly" from "your query is wrong" —
and neither ever gets reported as *no fish here*.

---

Built from published fisheries research, state wildlife agency data and NOAA/USGS public
feeds. No API keys, no accounts, nothing paid. Every regulation and every biological claim
carries its source inside the files — if an answer looks wrong, the receipts are there to
check it against.
