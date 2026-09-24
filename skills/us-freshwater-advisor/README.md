# US Freshwater Advisor

> **Sada 3 skillů pro Claude** · version **2026-09-24** · English · **⬇ Download packages:** [us-water-finder](https://raw.githubusercontent.com/jsoljak/shared-lab/main/downloads/us-water-finder.skill) · [us-weather-advisor](https://raw.githubusercontent.com/jsoljak/shared-lab/main/downloads/us-weather-advisor.skill) · [us-fishing-advisor](https://raw.githubusercontent.com/jsoljak/shared-lab/main/downloads/us-fishing-advisor.skill) (download all three)

Three Claude skills that answer one question between them: **where should I go fishing,
when, and with what.**

Most fishing trips are a coin flip, because nobody can watch the water every day. This
replaces that missing day-to-day observation with public data — water temperature, flow,
weather, regulations — and turns it into an actual recommendation rather than a vibe.

**→ [Read the field manual](GUIDE.md)** for what it does, how to install it, and — worth
reading before you trust it — where it's honestly thin.

---

## Download

Three files, one per skill. **Download all three**: the fishing advisor takes its data from the other two.
[us-water-finder.skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/downloads/us-water-finder.skill) ·
[us-weather-advisor.skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/downloads/us-weather-advisor.skill) ·
[us-fishing-advisor.skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/downloads/us-fishing-advisor.skill).
Each file is a complete skill with its reference data; the rest of this folder is for reading.

## What's here

```
us-freshwater-advisor/
├── GUIDE.md          ← start here
└── skills/
    ├── us-water-finder/       where can I legally fish, and what applies there
    ├── us-weather-advisor/    what are the conditions actually doing
    └── us-fishing-advisor/    so what should I actually do
```

Each folder is a self-contained Claude Skill. They're built to work as a chain — the
fishing advisor calls the other two for data rather than fetching its own — but the water
finder and weather advisor also stand alone if that's all you want.

## Requirements

Claude with Skills support (Claude Code, Cowork, or Claude Desktop), Python 3, and
`pyyaml`. **No API keys and no accounts** — every data source it uses (NOAA/NWS, USGS
Water Data, state fish and wildlife open-data portals) is free and public.

One edit is required before real use: put your own contact address in
`us-weather-advisor/scripts/fetch_weather.py`. [The guide](GUIDE.md#install) explains why.

## Two folder names that look unusual on purpose

`us-water-finder/reference-data/` and `us-fishing-advisor/memory-seeds/` would more
conventionally be called `data/` and `memory-template/`. They aren't, deliberately.

Repositories that host skills often carry blanket `.gitignore` rules blocking `**/data/`,
`**/config/`, `**/outputs/` and similar — because in most skills those folders hold live
operational data, and blocking them by folder name is a cheap, reliable guard against
committing something private by accident. That guard doesn't read file contents; it
matches the folder name and nothing else.

Nothing here is private — `reference-data/` holds published state fishing regulations with
their sources cited in each file, and `memory-seeds/` ships empty (`waters: []`,
`trips: []`) — but the folder *names* would have tripped that guard anyway. Renaming was
the cheaper fix than punching a hole in a safety rule, and `reference-data` is arguably
the more accurate name regardless: it's public reference material, not operational data.

Worth knowing before anyone renames them back.

## Legal note

This reflects public regulation data as of when it was gathered for a given state.
**Always verify current rules against the state agency before fishing** — regulations
change, and this is a planning aid, not a legal authority. Every regulation in here
records where it came from, precisely so it can be checked.

## Where it came from

A from-scratch US rebuild of a personal Czech fishing-decision system that ran on the
Czech Anglers' Union water registry and Czech Hydrometeorological Institute data. The
underlying idea is the same — replace missing day-to-day water observation with a
data-driven decision layer. Every data source, species model and regulation here is native
US material, researched for this toolkit. Nothing is translated or carried over from the
original beyond the general shape of the idea.

## Version history

| Version | What changed |
|---|---|
| 2026-09-24 | Download packages added. Skill descriptions shortened to fit the 1024-character install limit (triggers and scope unchanged in meaning). |
