# Database refresh 2026-09-15 06:00 UTC

## Health metrics

- **Translations**: 151 (147 at last refresh, +4 files on disk; 3 newly indexed this run)
- **Researchers**: 172
- **Works**: 214 (211 → 214)
- **New since last refresh**: 3 indexed works

## Changes

1. `database/research-index.json` — added 3 works:
   - `andre-simoneton-radiovitalite-fr-en` — André Simoneton (1893–1983), radio engineer under Captain Ferrié, extended the Bovis scale into food radiations (radiovitality). Bovis → Simoneton → Blanche Merz lineage.
   - `enel-energeia-reprints-2025-2026-fr-en` — Librairie Energeia re-issued the core Enel corpus 2025–2026 with Thieux prefaces; publication chain Al-Maaref Cairo → Dangles 1959 → eBookEsoterique 2022 → Energeia 2025-26.
   - `radionique-machine-shelf-2026-fr-en` — the 2026 French radionics retail shelf: Dajafée nine-device catalog, BIOLECHER Lecher-tuned emitter, Vibrasaï box. Falsifiable range claims flagged.
2. `database/person-index.json` — updated Simoneton (+radiovitality, food_radiations, bovis_scale domains), Enel (+Energeia reprints), Servranx (+machine-shelf dossier, radionics domain).
3. `database/health-report.json` — refreshed metrics.

## Notes

- Marquette and Frandeau dossiers (2026-09-14) were already indexed by the 04:00 Translation-QC run — no double-add.
- Clone from this sandbox hangs (3.2GB repo, known issue); entire refresh done via GitHub Contents API (raw fetch + PUT with blob sha). Commits: fce3b1f3, ecbb57a9, 57d876fe.
- `build_library_feed.py` / `tag_concepts.py` not runnable without a clone; feed and concept tags were rebuilt by the 04:00 QC run and are current.
- Upgrade bank: no `proposed` items became newly collectible this run (Marquette/Frandeau dossiers already recorded; Energeia reprints noted as source-availability improvement for Enel corpus but no ledger item targets it).

## Next run

- 2026-09-16 06:00 UTC.
