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
- **The guards do not cover everything.** On 2026-09-17 a rebuild on a sandbox with no shared
  `living-library` **and** no master index (`index.json` / `index_shards/manifest.json`) wrote a
  **464 KB** feed against the previous **17.4 MB** one: `seam` went 11.4 MB → 135 bytes,
  `library.meta_counts` was lost, `library.archive_entries` and `library.aflinks_docs` became
  `None`, and `patents` / `pages_translated` shifted. `practical` (the Replication Yard) rebuilt
  correctly — only the corpus-derived sections degraded. **You can rarely tell from the counts
  alone; check the file size.**
- **Safe procedure when you only need the Yard updated:** back up first
  (`cp library_feed.json /tmp/library_feed.bak.json`), run the builder if you want, then rebuild
  the feed as a deep copy of the backup with **only** `practical` (and
  `library.validations` / `library.replication_dossiers`) replaced from the new run, plus a
  refreshed `generated_at`. Restore `daily_counts.json` from the backup — the builder may append a
  degraded entry with `docs: None`.
- After rebuilding, verify: `practical.quests`, `practical.dossiers`, `practical.validations`,
  `library.translations` are non-zero, `latest_finds` did not shrink vs. the previous feed, and the
  file is still ~17 MB. Then confirm the committed blob:
  `git cat-file -s HEAD:library_feed.json` → **17392990** bytes; if it is ~0.5 MB you committed a
  gutted feed.
- If a rebuild goes wrong: `git checkout -- library_feed.json daily_counts.json`.

## Reporting lanes

Fleet lanes write their own directory + `status.json` + `ACTIVITY.md` (e.g. `navigator/`, `scout/`,
`forge/`, `drunvalo/`, `synthesist/`). Commit only files you own. `*.md` is globally gitignored
with per-lane exceptions in `.gitignore`; a new lane needs those exceptions added.
