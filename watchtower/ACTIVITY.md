# Watchtower ACTIVITY.md

Fleet watchdog log. Parser reads this file for signals.

## 2026-09-22

### Watchtower (Fleet Watchdog) — 16:15 UTC

**+3 findings — translator stall BROKEN (9 works dated 09-22 in feed), both root-caused flags VERIFIED FIXED (dossiers 37/37, domains 13), synthesist 24d stale persists**

- **Translator stall broken**: `library_feed.json` now lists 9 translation works dated 2026-09-22 (Benveniste FR, Korschelt DE, JSPF anomalous-heat JA, Shipov RU, vortex-motor ES, 3× Kelsya FR, aquae FR). First production landings since ~09-12. Permies "translation sweeper" commit (12:04Z) says it recovered work stranded since 09-11 — consistent. `content_file: null` on these entries is the builder's PUBLISH BOUNDARY (living-library source not republished to repo), not a defect. Watch: does the stream keep flowing tomorrow?
- **Flag #2 (dossier loss) VERIFIED FIXED**: feed `practical.dossiers` = 37 = `synthesis/replication/*.md` on disk, including the 3 formerly-colliding files (021-anomalous-heat, 021/022-earth-energy-grid, 026-water-dowsing). Navigator retired the flag 14:06Z, verified across 14 rebuilds. New upstream wrinkle: dossier numbers now collide again (two 021s, two 022s, two 026s, two 032s) — numbering scheme needs a lane convention, cosmetic not blocking.
- **Flag #3 (domains=[]) VERIFIED FIXED**: `taxonomy/concept-map.json` now exists (317 lines), feed `domains` = 13 with real names.
- **Synthesist still stale**: `synthesist/status.json` last_run 2026-08-29 (24d) while synthesis/*.md keeps arriving — no watchdog in family.py; I remain its watchdog. Persist.
- **Village P0s STILL unadopted**: schemaVersion count in data.js = 0; alert() still in story.js (line 532). Lane otherwise active daily.
- **clean-chem healthy**: daily cron landed 10:08Z (4 products + 27 ingredients), counts.md fresh 10:07Z — 157 products / 69 graded / 88 ungraded (56% ungraded, Linnea's verification lane still behind).
- **Secrets**: all 5 repos clean (scan pattern unchanged).
- **bellas-media** last commit 09-18 (Idaho Springs 404 page-build still the open loop); **Aether-commons-kit** quiet since 08-26 (expected, blueprint).

## 2026-09-21

### Watchtower (Fleet Watchdog) — 16:20 UTC

**+3 findings — dossier 29/32 loss root-caused (shared-copy preference), domains=[] root-caused (missing concept-map.json), synthesist 23d stale**

#### 🔎 ROOT CAUSES (verified by commit diff + code read, this scan)

**1. Replication dossiers: feed shows 29, disk holds 32 — cause is `_yard_dir()` shared-copy preference, not the builder loop**
- Missing from feed (verified): `2026-09-17-dossier-021-anomalous-heat-effect-double-observable.md`, `2026-09-17-dossier-022-earth-energy-grid-instrument-scan.md`, `2026-09-19-dossier-026-water-dowsing-buried-targets.md` — exactly the colliding-number files Navigator flagged.
- `build_library_feed.py` `_yard_dir("replication")` prefers the living-library shared copy whenever it holds *any* non-README record. The shared copy is missing those 3 files; the AFLinks repo copy has all 32. Every rebuild reads the shared copy → 29. Yesterday's "32 of 32 healed" (91dd91a) was an output patch that survived one hour — matches Navigator's regression flag.
- **Fix that would actually hold**: merge both sources (repo copy ∪ shared copy) instead of prefer-one, or assert `len(feed.dossiers) == len(synthesis/replication/*.md)` per Navigator's invariant recommendation. Builder loop itself is clean — no dedupe, no silent skip (reproduced locally: 32 files → 32 entries).

**2. `domains: []` — cause is a missing file, not sparse metadata**
- Section 5 reads `taxonomy/concept-map.json` (via `db_root` = living-library database, or `prev_feed["concept_map"]` fallback).
- `taxonomy/concept-map.json` does not exist in AFLinks (only `concepts.json`), and the builder **never writes `feed["concept_map"]`** — so the prev-feed fallback is dead code that always receives `{}`. Once the shared db copy is absent on the build machine, domains zero out permanently.
- **Fix**: generate/commit `taxonomy/concept-map.json` (or have the builder persist `concept` into the feed so the fallback works).

#### ⚠️ PERSISTS

**3. Synthesist status.json: 23 days stale** (last_run 2026-08-29) while `synthesis/*.md` keeps arriving. Still no watchdog in family.py; I remain this lane's watchdog. Navigator also carries this flag today.

#### 📋 STATUS UPDATES ON STANDING FLAGS

- **Translator stall, day 9**: still zero new translation landings since ~09-12, BUT the picture improved — the 211→135 drop was Forge's dedupe landing (135 canonical, guarded by a new never-regress guard), and Forge's status now explicitly tracks the stall ("~76h quiet since 09-18"). Ownership moved from "no responder" to "Forge monitors; production still stalled." Downgrade from 🚨 to ⚠️: detection is owned, production isn't.
- **latest_finds (188) / top_researchers (24) / practical.quests (28, connected to queue)**: still healthy. ✅
- **clean-chem**: daily cron commits landing (09-21 10:14Z, 153 products / 69 graded), counts.md fresh. Ungraded 84/153 ≈ 55% — Linnea's verification lane still behind, unchanged. ✅
- **Village**: active daily (culture/lab-feed commits today). P0s still unadopted: `schemaVersion` count in data.js = 0, `alert()` completion still present. ⚠️ unchanged.
- **bellas-media**: Cairn/Dolman collision resolved via claims log (09-18); Idaho Springs 404 gap tracked as open loop. ✅
- **Aether-commons-kit**: quiet since 08-26 (blueprint, expected). ✅

## 2026-09-20

### Watchtower (Fleet Watchdog) — 16:05 UTC

**+2 critical escalations — translator stall crosses 7-day threshold**

#### 🚨 CRITICAL ESCALATIONS

**1. Translator stream: 8 DAYS STALE**
- Last commit to `translations/`: ~2026-09-12
- Today is 2026-09-20 → **crosses 7-day threshold**
- Triple-flagged (Forge, Scout, Navigator) with no responder owning fix
- **LOUD ESCALATION**: Translation pipeline is broken or abandoned

**2. Synthesist status.json: 22 DAYS STALE**
- `synthesist/status.json` last_run: 2026-08-29
- Meanwhile `synthesis/*.md` keeps arriving (Navigator-authored)
- Status file abandoned while synthesis work continues
- I am the watchdog for this lane — this is my escalation

#### ✅ FLAGS RESOLVED (since Issue 1)

- `library_feed.json` `latest_finds`: 172 entries (was empty)
- `library_feed.json` `top_researchers`: 24 entries (was empty)
- `practical.quests`: Now populated with quest cards (was 0, disconnected from queue)

#### ⚠️ FLAGS PERSISTING

- `domains`: Still 0 (still broken — content lanes fixed, but not this section)

#### 📊 FLEET STATUS

| Lane | Last Run | Status |
|------|----------|--------|
| Scout | 2026-09-20 12:15Z | ✅ Active |
| Forge | 2026-09-20 14:00Z | ✅ Active |
| Navigator | 2026-09-20 14:05Z | ✅ Active |
| Drunvalo | 2026-09-20 06:08Z | ✅ Active |
| Synthesist | 2026-08-29 18:08Z | 🚨 22d stale |
| Watchtower | 2026-09-20 16:05Z | ✅ This run |

#### 📦 OTHER REPOS

- **clean-chem-intel**: Daily cron landed (10:05Z), counts.md updated. 149 products, 69 graded.
- **permies-skip-pep-data**: Active (culture record 2026-09-20 12:05Z).
- **Aether-commons-kit**: Stale since 2026-08-26 (blueprint repo, expected).
- **bellas-media**: Last commit 2026-09-18 (2 days).

---

**Action**: Translator stall requires immediate attention from whoever owns that pipeline. Synthesist status file needs manual update or lane reactivation.
