# Friction log

Append-only. This is NOT about fishing — that's `lessons.md`. This is about the
**toolkit itself** not working smoothly for you: a script erroring, an answer that
was confusing or wrong, data that should have been there and wasn't, a mode that
didn't fit what you actually asked. Every one of these three skills was built and
tested before you got it, but "tested" isn't the same as "used for months by a real
person" — this file is how the gap between those two gets tracked instead of just
silently annoying you every time it happens.

## When to write here

Any time something genuinely didn't work as expected — not every minor "estimated"
caveat the skill already flags honestly (that's working as designed), but a real
friction point: an error, a wrong or missing answer, an instruction that was unclear
enough that the skill had to guess what you meant, a state/species/mode gap that
came up in an actual question. Write one entry per incident, right when it happens —
don't try to remember it for later.

## Entry format

```
### YYYY-MM-DD — one-line summary
What was asked: ...
What went wrong: ...
Suggested fix: [specific, concrete — which SKILL.md rule/section, which script,
  what data file — not just "improve this"]
```

## What to do with these entries

When asked something like "how's this been working," "any issues," or periodically
if a handful of entries have piled up unreviewed: read through this file and
summarize the real patterns — not every single entry restated, but what keeps
coming up. Turn that into a short, concrete list of proposed fixes (specific
SKILL.md/script/reference changes), the same level of specificity as the fixes made
during this toolkit's own testing phase. You can apply small, safe fixes yourself
(a clarifying sentence in a SKILL.md rule, a missing field in a data file) the same
way earlier fixes were made in this project — but flag anything that changes actual
scoring logic, adds a new data dependency, or touches more than one file, rather
than quietly changing it, since those are exactly the kind of change that should be
visible, not silent.

## Seed (empty — starts filling in once this ships)
