# Fleet Blind Spots — Weekly Synthesis Issue 2

**Date:** 2026-10-16
**Watchtower Run:** 15:00 UTC (Friday weekly)
**Repos Audited:** AFLinks, clean-chem-intel, permies-skip-pep-data, Aether-commons-kit, bellas-media
**Previous Issue:** Issue 1 (2026-09-25). Issues for 10-02 and 10-09 never landed — see §2.6 (self-flag, closed by this report).

---

## Executive Summary

**Production is compounding; instruments are decaying.** AFLinks absorbed its largest intake ever this week (+4,609 documents in one day, archive 131,234, Tesla estate complete at 3,584 items) while the vault's own instruments fell further behind: the theme map is 44 days stale and was computed over 47% of today's archive, the citation graph has been frozen 40 days, the counter builder checked in FAILED, and the concept tagger is dead. That is the same shape as every structural finding this lane carries — clobbers, feed rebuilds, status-file freezes: **detection is fast, prevention is absent.**

Cross-repo: clean-chem's ungraded debt crossed 82% (Linnea has zero commits since 10-01 while Dolman adds ~11 products/day). The Village↔Yard quest pipeline syncs cleanly and delivers quests nothing can complete (97/97 `proposed`, day 40, schema cannot say "completed"). bellas-media's quiet is by design — it was restructured 09-18 into a public record; the work surface moved to a private vault and to clean-chem's new `/preview/` lane. Two deliverables now wait on Sandra, not on agents.

---

## Section 1: Standing Flags — Re-Verification

| Flag | Status | Evidence (cited paths) | Owner |
|------|--------|------------------------|-------|
| **0. AFLinks main clobbers** | 🟢 **10 days clean** | Last clobber 10-06. `git ls-files` = 126,489 (consistent with intake). No new `backup/main-clobbered-*` branches on remote. Prevention still absent — and a sibling hazard appeared, see §2.2. | (watch) |
| **1. Feed latest_finds** | ✅ **HEALTHY** | `library_feed.json` `latest_finds` = **520** (up from 365 on 10-04, 516 on 10-15). Resolved flag stays resolved. | — |
| **2. Feed top_researchers / dossiers** | ✅ **HEALTHY** | `top_researchers` = 24. Dossiers 110 (+3 d/d per Navigator Issue 32). Numbering collisions (021/022/026/032/038) still cosmetic, no convention adopted. | — |
| **3. Feed domains** | ✅ **HEALTHY** | `domains` = **13**, unchanged. | — |
| **4. Translator stream** | ✅ **LANDING DAILY** | Feed `latest_translations` = **930**, **34 dated today 10-16**; +56 d/d. Drunvalo QC today: +15 works (Forge Oct-16 batch), DB at 1,102 works / 692 persons (`drunvalo/status.json`). R159 fossil absent from `forge/status.json` — stays retired. | — |
| **5. Synthesist status frozen** | ⚠️ **48 days** | `synthesist/status.json` last_run 2026-08-29T18:08:38Z, ACTIVITY.md frozen same day. Production continues via other lanes: quest queue 97 = feed `practical.quests` 97, exact match. Navigator Issue 32 and Connector Report 37 now both cite the freeze independently. I remain its watchdog. | Watchtower carries |
| **6. Village P0s unadopted** | ⚠️ **MONTH+** | `schemaVersion` count in `permies-skip-pep-data/data.js` = **0**; `alert()` still at `story.js:532` (adventure-code copy handler). First flagged 09-16. Lane is hyperactive otherwise — new content lanes (culture-engine, vitality-engine, meditation-abilities) enrich daily and correct their own over-claims. The P0s are structural work, not content work; nobody owns them. | Village lane |
| **7. clean-chem grading stall** | 🚨 **DAY ≥11 — WORST YET** | `clean-chem-intel/counts.md`: **436 products / 76 graded / 360 ungraded = 82.6%** (was 77.5% on 10-07, 38% *coverage* at Issue 1 → 17.4% now). Graded flat ≥11 days. **Linnea: 0 commits since 10-01** (verified via git log). Dolman added ~98 products in 9 days. | Linnea lane owner |
| **8. bellas-media quiet** | 🔄 **REFRAMED — quiet is by design** | Repo restructured 09-18 (`README.md`: "Restructured: September 18, 2026") into the *public published record*; WIP moved to private `Focusingpulse/bellas-media-vault`. The marketing work surface migrated: Cairn's BMVC "Products I Use" page landed 10-13 at `clean-chem-intel/preview/index.html` (noindex, awaiting Sandra's sign-off, day 3). Idaho Springs 404 still open and documented (`bellas-media/log/claims.md`, `log/site-changes.md`). | Sandra (human gate) ×2 |
| **9. Secrets** | 🟢 **CLEAN** | Bounded scan today across all 5 repos (token/key/private-key patterns): zero hits. | — |
| **10. Fossil translator check** | ✅ **STAYS RETIRED** | No re-emergence in `forge/status.json` or Forge ACTIVITY. | — |
| **11. Yard schema gap** | ⚠️ **DAY 40** | All **97** quest cards `proposed` (verified: 82 `**Status:** proposed` + 15 `Status: proposed` in frontmatter across `synthesis/quest-queue/*.md`); 0 completed; no `completed`/verdict value exists in schema. Navigator Issue 32 independently counts "40th consecutive day." Raised to Sam 09-26 — still unanswered. Cards are physical experiments: completion needs human hands. | Sam (schema decision) |

---

## Section 2: New Blind Spots Discovered

### 2.1 META-FINDING: The instrument-lag pattern (detection rich, prevention absent)

Every structural finding this week is the same finding wearing different clothes. Production scales; the instruments that measure and guard production decay; each decay is *detected* quickly; none has a guard at the write or schedule point:

- **Archive instruments** (Navigator Issue 32, verified against `library_feed.json`): `paradigm_lenses.json` generated 2026-09-02 over 61,578 docs = 44d stale, covering 47% of the current 131,126-doc archive; `archive-graph.json` frozen 2026-09-06 (345/453 nodes/edges) while The Diver's live citation graph is at 25,653 nodes / 34,793 edges; counter-watchdog checked in **FAILED** 2026-10-15T09:51Z ("builder degraded"); concept tagger dead (`drunvalo/report-2026-10-16-*.json`: "tag_concepts skipped (dead)").
- **Write-path hazards**: 4 main clobbers (detection fast, no push-time `ls-files` guard) + 2 whole-file feed rebuilds by rescue-sweep (§2.2).
- **Reporting lanes frozen while production runs**: synthesist 48d, Linnea 11d, Forge's check-in sensor quiet today (§2.4), my own weekly twice (§2.6).

The fleet has built excellent sensors and almost no circuit breakers. The cheapest available breaker already exists — the Aether-commons-kit `family.py` has a staleness watchdog and budget gate the live repo lacks (§2.3).

### 2.2 rescue-sweep whole-file feed rebuilds (NEW hazard, verified)

Navigator fleet note (10-16 10:47Z, `navigator/ACTIVITY.md`): the `rescue-sweep` lane rebuilt `library_feed.json` from a stale base **twice** (10-14 pass 4, 10-16 pass 6 / commit `43eb75666`), reverting other lanes' Yard records (`practical.validations` 79→76, `book5_complete` dropped, `atsuyskovsky_books` 1→0, `news` 8→5) **while passing every routine health check** — because "is the feed empty?" checks don't see surgical regressions. Both times a later `aflinks-cron` bake healed it within ~1 hour.

**Verified this run:** current feed (generated 14:16:56Z) is healthy — validations 79, `book5_complete` true, `atsuyskovsky_books` 1, `news` 8. **Occurrence count stands at 2; re-arm at 3**, at which point it is an unfixed structural bug in that lane's write path (fix: merge rather than whole-file rebuild, or pull fresh before rebuilding). This lane now watches it alongside the clobber watch — it is the same hazard class at 36 MB instead of 126k files.

### 2.3 family.py drift has INVERTED (flag reframed)

Issue 1 recorded AFLinks `family.py` as canonical (full CLI) vs an older blueprint copy. **That flipped on 09-26.** Now:

- `AFLinks/family.py` — 6.4 KB: `checkin`, `checkout`, `propose_upgrade`, `status`, `log`. **No staleness watchdog, no budget gate, no dead-links.**
- `Aether-commons-kit/ledger/family.py` — 10 KB: `should_run` (budget gate), `staleness_report`, `record_dead_links`, `report_archive_growth`, `set_budget`. The docstring is the fleet-coordination design the live repo needs.

`AFLinks/family.py` is still load-bearing (referenced by `cron_job.sh` and `fleet_report.py`). The practical consequence is exactly flag 5: nothing in production automatically notices a frozen lane — the synthesist freeze is carried by a human-scale watchdog (me) instead of a `staleness_report` cron. **Fix path:** port the blueprint's `staleness_report` (+ budget gate) into `AFLinks/family.py` and wire it into `fleet_report.py` or a daily cron. Owner: AFLinks maintainer (Sam) or Forge; Watchtower recommends, does not own.

### 2.4 Forge check-in sensor silent today (watch item, day 1)

`forge/status.json` last update 2026-10-15T12:30Z; the expected 00:20Z fire (363) and 12:30Z update did not land commits today. **Production is not silent** — Drunvalo QC at 02:08Z processed "+15 works (Forge Oct-16 batch)" — but the sensor the HUD reads is quiet. By the fleet's own liveness rule this is *not* a stall; it becomes a flag only if check-ins stay absent >48h (re-check 10-18 daily scan).

### 2.5 clean-chem is now a BMVC work surface — and two gates wait on Sandra

Cairn's `/preview/index.html` ("Products I Use," noindex, "proposed… not a live page") is marketing deliverable work living in the intel repo. That's legitimate — but it crosses repo lanes: bellas-media's README claims the "published mirror" job, so when the preview ships, the record should land in `bellas-media/published/`. More important: **two deliverables are now human-gated on the same person** — the Idaho Springs service-area page (404, open since ≥09-18) and the Products I Use sign-off (since 10-13). Neither is agent-blocked. If Sandra wants a single queue, these two are it.

### 2.6 SELF-FLAG CLOSED: weekly synthesis missed two consecutive Fridays

Issues for 10-02 and 10-09 died before push — sandbox wiped between fires, full-audit budget exhausted after re-cloning. The 10-09 daily scan self-flagged this and set the fix (re-clone shallow FIRST, time-box the audit). This issue is the fix executed: clones complete by 15:04Z, report written by ~15:30Z. **Closed by landing.**

---

## Section 3: Signals in the Noise

- **The largest intake day in fleet history landed the same week the instruments were stalest** — the Connector's eighth correction (Report 37) names it: "growth is not dialogue; an archive can inherit faster than it can listen." The Tesla estate is complete (3,584 items). The digest's three jobs — repair instruments before the next harvest, bound the 97 Yard cards, run the voice-print home test — are the right triage.
- **The water rail hardened in a single week**: Max Planck ceiling on light-driven interfacial water + independent Prague reproduction of the exclusion zone (Pollack's own protocol) + first independent hearing for Mizuno's processed-metal branch. Replication Watch run 14 added 3 records (water ×2, LENR SUS304) — `practical.validations` 76→79. This is the Yard's top rung producing; the bottom rung (physical completions) remains empty day 40.
- **The Village↔Yard pipeline works and delivers quests nothing can finish**: `village-quest-sync` commits "Lab feed: quest cards (95 cards)" 10-16 vs AFLinks queue 97 — ≤1 sync cycle lag, healthy sync. But completion is impossible at both ends: the Yard schema can't say "completed" (flag 11) and the Village's celebration/guided-session P0s are unadopted (flag 6). Two ends of one pipe, both capped.
- **New lanes are appearing outside every registry**: culture-engine, vitality-engine, meditation-abilities (permies), Cairn (cross-repo), rescue-sweep, aflinks-preview-cleaner (AFLinks job families). None appear in `build_library_feed.py` AGENT_FLEET/STATUS_FILES. The HUD says 15 active agents; reality has more writers. Registration gap — minor, but the HUD is how Sam sees the fleet.
- **Good hygiene signals worth naming**: aflinks-preview-cleaner reverted 1,800 harmful stub replacements (cleanup automation defending the tree); culture-engine removed an unsourced clause from its own science line rather than letting it stand; Sifter withdrew a bad derm-C call ("gr_ruled"). The fleet's self-correction instinct is real — that's the trust signal under the whole evidence layer.
- **Bake-cadence gap nearly closed**: `archive_entries` (131,234, scout's shard manifest) vs `aflinks_docs` (131,126, baked DB counter) gap 2,409 → 108. Two different instruments printed side by side as "the archive size" — Navigator's unlabelled-measurement-context class. Know which number you're reading.

---

## Section 4: Who Worked, Who's Silent (week of 10-09 → 10-16)

*(AFLinks census from the 10-16 shallow window + daily-scan lane records; small-repo census from full weekly logs.)*

**AFLinks:** aflinks-cron (feed bakes, multiple/day), aflinks-worker families (zenodo-rh, i-sis, svpwiki, steiner — steiner at terminal 371/377 GAs), Scooter (HUD 2×/day), Navigator (digests Issue 29→32 + replication-watch), Drunvalo (translation-QC 2×/day, clean), rescue-sweep (zpenergy passes 4–6, see §2.2), aflinks-preview-cleaner, connector (paradigm Report 37), Focusinguplse gear-status probes. **Silent:** synthesist (48d, status only), Forge check-ins (1d, §2.4).

**clean-chem-intel:** Dolman (station-2 harvests ~11 products/day, Mon/Wed/Fri + station-4 closes), clean-chem-cron (daily gather+rebuild), Sifter (verification/enrichment runs 10-11, 10-13), Cairn (preview page 10-13). **Silent:** Linnea (0 commits since 10-01 — flag 7), and graded count flat ≥11 days.

**permies-skip-pep-data:** village-cron (daily), village-quest-sync (daily lab feed), culture-engine (1.3→1.7 enrichments with self-corrections), vitality-engine (fascia, posture, breath, balance), meditation-abilities (entry 8), Drunvalo (library route migration +42 links, maintenance), library lane (+3 vetted resources ×2). P0 structural items untouched (flag 6).

**Aether-commons-kit:** silent since 09-26 (20 days) — but its 09-26 family.py is now the fleet's best coordination code (§2.3). Blueprint repo; quiet is acceptable.

**bellas-media:** silent since 09-22 (24 days) — by design post-restructure (§2.5). Open loops tracked in its `log/`, not its commit stream.

---

## Section 5: Commitments for Next Cycle

1. **Land Issue 3 on 10-23** using today's proven pattern (shallow-clone first, audit time-boxed, push before 16:00Z).
2. **rescue-sweep watch**: third whole-file rebuild regression → escalate as structural bug with the fix named (merge-instead-of-rebuild or pull-fresh-first).
3. **Forge check-in watch**: if no forge status update by the 10-18 daily scan, promote §2.4 to a finding.
4. **Linnea escalation**: if graded is still 76 on 10-23, recommend to Sam explicitly: pause the lane formally or throttle Dolman ingest — 11 days of silent stall is the worst state, and the ungraded pile will be ~440 by then at +11/day.
5. **Track Sandra's two gates** (Idaho Springs 404 page build; Products I Use sign-off) and report wait-time, not just state.
6. **family.py port**: raise §2.3 as a named recommendation to the AFLinks maintainer; if untouched by 10-23, draft the port as a proposal PR rather than letting it age.
7. **ACTIVITY.md hygiene**: entries for 10-04/10-08/10-09/10-10 sit below the September block (appended, not prepended). Parser reads date headers so signals survive, but the file is confusing to humans — keep new entries prepended; reorder only if the parser is confirmed order-insensitive.

---

*Watchtower (Fleet Watchdog) — weekly synthesis. Flag only what's real and verified; cite file paths. Detection ≠ remediation: every finding above names its owner.*
