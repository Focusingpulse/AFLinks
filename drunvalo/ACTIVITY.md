# Translation-QC 2026-09-15 04:00 UTC

## Summary

**Root cause identified and fixed**: The Harmonizer's `cron_job.sh` had a git stash/pop dance that, on a clean tree, pops a leftover stash from a previously killed run — restoring stale pre-QC files, which `git add -A` then commits back. This resurrected 6 duplicate translations and reverted goethe mojibake fixes from the 00:20 QC run.

**Fixes pushed this run**:
1. Patched `cron_job.sh`: removed stash/pop, added dirty-tree abort gate. Commits: d4eb33d4
2. Deleted 6 duplicate translation files (re-added by 01:24 sync). Commits: 6 individual deletes
3. Re-fixed goethe mojibake (45 sequences, cp1252 round-trip). Commit: ce69749a
4. Annotated dead publisher URL (editionschristineclaire.com permanently closed) with Wayback link. Commit: 01575662
5. Remapped 15 dead file refs in `person-index.json` to canonical translations. Commit: f6257a63
6. Deduped 16 duplicate ids in `research-index.json`. Commit: 3a8c0e26

**QC of 5 most recent translations**:
- All 5 files: well-formed markdown, valid frontmatter, correct language tags, no mojibake, no untranslated passages
- 1 URL dead (publisher site permanently closed) — annotated with Wayback snapshot
- All other referenced URLs validated (7/7 reachable with browser UA)

**Database integrity**:
- `person-index.json`: 172 entries, 124 file refs, all now resolve
- `research-index.json`: 211 unique work ids (was 227 with 16 dupes)

**Next steps**:
- Monitor next Harmonizer sync run (should abort on dirty tree if stash left behind)
- Consider adding content-hash fingerprints to translations to detect re-emission of already-translated sources (open item from 2026-09-13)
- LFS migration still blocked pending Chris approval for >100MB files

## Files checked/modified

- `translations/2026-09-03-compendium-vortex-physics-de.md` — DELETED (dup)
- `translations/2026-09-11-compendium-of-vortex-physics-schauberger-de.md` — DELETED (dup)
- `translations/2026-09-11-schauberger-water-blood-of-the-earth-de.md` — DELETED (dup)
- `translations/2026-09-11-theorie-phi-scalar-field-baryonic-matter-fr.md` — DELETED (dup)
- `translations/2026-09-11-torsion-physics-newton-to-present-ru.md` — DELETED (dup)
- `translations/Wilhelm_Reich_Ether_Physics_and_Orgone_Experiments_EN.html.md` — DELETED (dup)
- `translations/2026-09-12-goethe-scientific-works-complete-it.md` — FIXED mojibake
- `translations/2026-09-14-frandeau-fortuna-major-patent-fr-en.md` — ANNOTATED dead URL
- `cron_job.sh` — PATCHED stash-ban + dirty-tree gate
- `database/person-index.json` — REMAPPED 15 dead refs
- `database/research-index.json` — DEDUPED 16 duplicate ids

## Commits this run

1. Delete duplicate: translations/2026-09-03-compendium-vortex-physics-de.md
2. Delete duplicate: translations/2026-09-11-compendium-of-vortex-physics-schauberger-de.md
3. Delete duplicate: translations/2026-09-11-schauberger-water-blood-of-the-earth-de.md
4. Delete duplicate: translations/2026-09-11-theorie-phi-scalar-field-baryonic-matter-fr.md
5. Delete duplicate: translations/2026-09-11-torsion-physics-newton-to-present-ru.md
6. Delete duplicate: translations/Wilhelm_Reich_Ether_Physics_and_Orgone_Experiments_EN.html.md
7. ce69749a — Re-fix goethe mojibake
8. 01575662 — Annotate dead publisher URL
9. d4eb33d4 — Patch cron_job.sh stash-ban
10. f6257a63 — Remap person-index dead refs
11. 3a8c0e26 — Dedupe research-index ids

**Status**: OK
