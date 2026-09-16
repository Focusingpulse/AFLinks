# AGENTS.md — rules for any agent working in this repository

You are working in **AFLinks**, the public Knowledge Vault and site repository for the Aether Force archive.
`main` is a **live branch**: GitHub Pages builds the site from it. Treat it as production.

## BRANCH SAFETY — read this first

**Never force-push `main`. Never push an orphan commit to `main`. Never push a tiny tree to `main`.**

A healthy AFLinks checkout has **~45,000 tracked files**. Before you commit, run:

```bash
git ls-files | wc -l
```

- **≥ ~40,000** → normal. Proceed.
- **< ~1,000** → your checkout is broken, or `main` itself has been clobbered. **STOP.**
  Do **not** `git add` + `git commit` + `git push` — that is how the archive gets destroyed.
  Instead: `git fetch origin main && git reset --hard origin/main`, or re-clone cleanly
  (`git clone --depth 1 https://github.com/Focusingpulse/AFLinks.git`, then
  `git checkout --cone` / `git sparse-checkout set --cone <dirs>` — never bare `--sparse`,
  which leaves the tree unpopulated). If `origin/main` itself has < ~1,000 files, **stop and report
  the incident**; do not push on top of it.

To publish work: `git pull --rebase origin main`, commit, then push **fast-forward**.
If a push is rejected, re-pull and retry — never `--force`.

Why this file exists: on 2026-09-16 `main` was orphan-force-pushed twice (06:05 UTC and 08:07 UTC),
replacing the whole 45k-file tree with a parentless commit containing one report file. The public
vault was empty for ~2 hours. Recovery required a lossless `--allow-unrelated-histories` merge from
the last good commit (`e9c2a39c`).

## Rebuilding the feed (`library_feed.json`)

```bash
AFLINKS_DIR=/root/workspace/AFLinks python3 build_library_feed.py
```

- **Never rebuild from a checkout missing the content it reads.** Many sections are read from the
  shared `living-library` projection; when that is absent the builder computes *shorter* lists.
  The script's degraded-run guards keep the previous published values (empty **or shorter**) for
  `latest_finds`, `domains`, `top_researchers`, `declassified`, `agents`, `activity_log`. Do not
  remove those guards.
- After rebuilding, verify: `practical.quests`, `practical.dossiers`, `practical.validations`,
  `library.translations` are non-zero, and `latest_finds` did not shrink vs. the previous feed.
- If a rebuild goes wrong: `git checkout -- library_feed.json daily_counts.json`.

## Reporting lanes

Fleet lanes write their own directory + `status.json` + `ACTIVITY.md` (e.g. `navigator/`, `scout/`,
`forge/`, `drunvalo/`, `synthesist/`). Commit only files you own. `*.md` is globally gitignored
with per-lane exceptions in `.gitignore`; a new lane needs those exceptions added.
