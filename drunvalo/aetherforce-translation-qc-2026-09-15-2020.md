# aetherforce-translation-qc — 2026-09-15 20:20 UTC

**Status:** ok

## Scope
The 5 newest translations (all 2026-09-15, authored by Forge):
1. `2026-09-15-andre-simoneton-radiovitalite-fr-en.md` — clean
2. `2026-09-15-blanche-merz-hauts-lieux-cosmo-telluriques-fr-en.md` — clean
3. `2026-09-15-enel-energeia-reprints-2025-2026-fr-en.md` — clean
4. `2026-09-15-merz-high-places-inter-rater-bench-note-en.md` — clean
5. `2026-09-15-simoneton-vs-biophotonics-bench-note-en.md` — 2 issues fixed

## Checks run
- Markdown well-formedness (frontmatter, headers, paragraphs): pass on all 5
- Source URL validity: 5 URLs fetched, all HTTP 200 (editions-tredaniel.com, mrbienetre.fr, psi-gamma.com, inexplore.com ×2)
- Language tags: correct (fr→en composites; en authored notes)
- Untranslated passages: none — every FR/DE/ES quote carries an inline English translation
- Duplicate regrowth: filename-cluster scan across all 125 translations — 3 clusters found, all intentional (translation + original pairs: onde-di-forma en/it, sweeper fr/it/ru, vortex-motor es/es). No regrowth since the 12:20 UTC purge.
- Titles vs content: accurate on all 5

## Issues found & fixed
1. **Bench-note frontmatter incomplete** (simoneton-vs-biophotonics): only name/description. Added translator, source_language, language, date_published, sources.
2. **Factual error** (same file): "Alfred Bovis" → **André** Bovis (1871–1947), per the corpus record in the companion dossiers and psi-gamma.
3. **research-index.json dupes**: 4 work ids re-emitted by the translation agent (andre-simoneton-radiovitalite-fr-en ×2, jacques-ravatin-champs-de-coherence-fr-en ×2, shipov-torsion-fields-torsion-technologies-ru ×2, study-on-torsion-fields-de ×2). Merged keeping richer entries + union of lists: 222 → 218. Added 2 missing bench-note works: merz-high-places-inter-rater-bench-note, simoneton-vs-biophotonics-bench-note.
4. **person-index.json dupes**: blanche-merz/merz-blanche and andre-simoneton/simoneton-andre merged (union of works_in_collection, cited_by, domains): 179 → 177.

## DB updates
- research-index: 2 works added, 4 dup ids merged
- person-index: 2 dup persons merged (Enel and Guy Thieux already present under ids `enel`, `thieux`)

## Commits
- 6611b62f — bench-note fixes
- dd163f54 — research-index dedupe + additions
- c01ec16f — person-index dedupe
- 2ee488c9 — status.json
- da191eda — ACTIVITY.md

## Method note
git clone hangs from this sandbox (known issue since 2026-09-14; full/shallow/sparse/blob-less all tried). Entire run executed via GitHub Contents API with the PAT — one commit per file. tag_concepts.py not run (requires full clone).

## Open items
- Root-cause duplicate prevention still belongs in the emitting translation agent (agent-75b8d29e): content-hash/source-URL check before write.
- database_refresh.py update_person_index additive-only rewrite still open.
