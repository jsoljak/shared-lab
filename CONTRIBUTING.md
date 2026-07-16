# Contributing

This is a public repo — only general, non-personal content belongs here.

## One-time setup after cloning

The repo has a pre-commit safety check that blocks commits containing sensitive data.
It doesn't activate on its own — run this once after cloning:

```bash
git config core.hooksPath hooks
chmod +x hooks/pre-commit
```

Check it worked: `git config --get core.hooksPath` should print `hooks`.

## What the check blocks

Before each commit, it scans staged files (including the contents of `.skill` archives)
and blocks the commit if it finds:

- emails, phone numbers, rate/fee figures
- casual references to me by name (my formal `Jiří Soljak` + LinkedIn attribution is
  the only allowed exception)
- a few other internal-only markers

## If it blocks a commit

1. **It's right** → clean up the flagged content, commit again.
2. **False positive** → override deliberately: `git commit --no-verify -m "intentional: <reason>"`.
