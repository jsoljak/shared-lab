# Water reports — what's actually known about a specific water

This is the US equivalent of a "what are people saying about this spot" check. The
Czech original this toolkit is modeled on solved this with a curated allowlist of
official regional angling-association RSS feeds — that infrastructure doesn't exist
here. There is no single clean feed. This is a live web-search job, done narrowly,
with the same survivorship-bias discipline the Czech original applied to social
media catch photos.

## Source priority (most to least trustworthy)

1. **State DNR weekly/regional fishing reports.** Indiana, Michigan, and Ohio DNRs
   each publish an official fishing report (weekly or biweekly, often by region/
   district) — search `"<state> DNR fishing report" <region or water name>`. These
   are the closest thing to a curated source: written by the agency, not
   crowdsourced, and usually explicit about "slow" as well as "hot" bite conditions.
   Trust these most, but they're often regional ("northeast Indiana") rather than
   water-specific — don't assume a regional report describes the exact spot.
2. **Local bait shop / guide service reports or blogs**, if a search turns one up
   for the specific water. Useful but has an obvious incentive to sound upbeat —
   treat "great fishing lately" from a shop that sells bait with more skepticism
   than a DNR report saying the same thing.
3. **Forums, social posts, state-specific angling communities** (e.g. a subreddit,
   a state fishing forum). Least trustworthy as a group, most prone to
   survivorship bias — a triumphant catch photo gets posted, three quiet
   no-bite trips don't. A post that says "nothing was biting" is worth more than
   its rarity suggests, precisely because it's rare.

## How to search

One targeted search per water, not a research project: `"<water name>" fishing
report 2026` or `"<water name>" fishing "<month>"` scoped to something recent. If
the first search surfaces a DNR report, stop there — don't keep searching for a
second opinion by default. If nothing recent turns up, say so plainly rather than
reporting on a six-month-old post as if it were current.

## What to actually write in an answer

- **Date the source.** "DNR's early-August report for the White River corridor
  noted..." is useful. An undated "fishing has been good here" is not — always
  say when the information is from, and flag if it's more than a few weeks old.
- **Don't launder a single post into a trend.** One angler's bad day (or great day)
  is a data point, not a pattern. Say "one recent report mentioned X" rather than
  "the water is currently Y."
- **A source disagreeing with the model's own score is worth surfacing, not
  hiding.** If `score.py` says conditions look good but the most recent report
  says the bite's been slow, say both — that's a real signal the scoring model
  might be missing something (turbidity from an unmodeled event, recent heavy
  fishing pressure, a stocking gap), not a reason to suppress the report.
- **No result found is a valid, honest answer.** "I didn't find a recent report
  for this specific water" is better than silence or a fabricated-sounding
  generic summary.

## Token/scope discipline

- Only do this for the **top-recommended water** in a PLAN/TRIP PLAN answer, not
  for every candidate in a ranked shortlist — one search, not N.
- Skip it entirely for WINDOW mode (scanning many day/water combinations) unless
  specifically asked — it doesn't scale to a multi-day scan the same way.
- If asked directly ("what are people saying about [water]," "any recent reports
  for [water]") this becomes the whole point of the answer, not a side note —
  do the search even outside PLAN/TRIP PLAN.
