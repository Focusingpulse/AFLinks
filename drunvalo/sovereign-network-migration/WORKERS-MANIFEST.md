---
name: workers-manifest
description: Fleet-wide worker + job manifest for the offload to the local Sovereign Network (AnythingLLM/LiteLLM). Every agent, every scheduled job, role, practice, scope, and repos. Mandated by Chris 2026-10-21.
authorship: {agent_id: "agent-0132a387-e656-42e5-b563-e1f2d6438df3", name: "Drunvalo", date: "2026-10-21"}
---

# Fleet Workers & Jobs Manifest — Sovereign Network Offload
**Generated:** 2026-10-21 · **Author:** Drunvalo (agent-0132a387) · **Mandate:** Chris, 2026-10-21

## Why this exists

The cloud is no longer viable for the fleet's scheduled work:

- **Every cron on account user-6295b4a3 fails** with `LISTENER_TURN_FAILED_BEFORE_RUN` (daily inference quota exhausted). Last healthy Drunvalo run: 2026-10-16 16:00 UTC. Eloquint's mirror: 10-16. Cure 8er's mirror: **09-26 (dead 25 days)**.
- The **fleet ledger** (79 cron identities) shows everything stalled **2026-10-15** except `connector`, which last checked in 2026-10-21T13:08Z from the other account.
- Watchtower's 2026-10-21 scan: "six dark lanes missed the full forge/connector up-window (not one flap); forge declares 4th gap."
- Plan tier is `free`, 0 credits. The decision: **offload scheduled jobs to Chris's local Sovereign Network** — FocusOptimized, AnythingLLM + LiteLLM + the local model stack.

This manifest is the complete migration package: who works here, what each job does, what it touches, and what the new host must provide.

---

## Part 1 — WORKERS MANIFEST (the agents)

### Drunvalo — 🔮 The Pattern Keeper
| Field | Value |
|---|---|
| agent_id | `agent-0132a387-e656-42e5-b563-e1f2d6438df3` |
| Account | user-6295b4a3 (Chris's 2nd) |
| Pod | meaning-maker + evidence-keeper (synthesis, translation QC, dedupe, fleet check-ins) |
| Status | All 8 crons quota-dead since 2026-10-16 |
| Repos | AFLinks (drunvalo/, synthesis/, database/, sources/, family_ledger.json, build_library_feed.py), permies-skip-pep-data (full write), cron-coordination (ledger), DrunvaloMemory (mirror) |

### Cure 8er — The Synthesist
| Field | Value |
|---|---|
| agent_id | `agent-060fb094-9b9e-4106-ab35-73d554c0d28c` *(recovered from his own operating-context.md — was UNKNOWN in the registry)* |
| Account | user-6295b4a3 (Chris's 2nd) |
| Pod | meaning-maker |
| Status | Mirror dead since 2026-09-26. Desktop crons degraded (local-only, desktop often offline). Re-home plan documented but parked. |
| Repos | AFLinks (synthesist/, translate_pipeline.py, translation_progress/), Cure-8er-memory (mirror) |

### Eloquint — Voice/Editorial
| Field | Value |
|---|---|
| agent_id | `agent-57d47bec-dfad-41d0-af6e-ab5ea729d60b` *(recovered from her memory-mirror.md — was UNKNOWN in the registry)* |
| Account | user-6295b4a3 (Chris's 2nd) |
| Pod | voice-editorial (tone/voice policing for going-live copy, claim traceability, editorial calendar) |
| Status | Mirror stale since 2026-10-16. No work crons; lane runs by direct request. Announced 2026-09-24 in AGENT-THREADS. |
| Repos | Eloquint-memory (mirror); annotates copy in cron-coordination + AFLinks |

### Cairn — governance + business
| Field | Value |
|---|---|
| agent_id | `agent-6d7b07d4-e1e0-42c2-969e-32071de2c5de` |
| Account | account-01 focusandexcell (Chris's 1st) |
| Pod | operational + governance-watch |
| Status | 20 crons (inventory 2026-10-15). Owns the fleet HUD, registry, business lanes (BMVC, Clean Chem). |
| Repos | cron-coordination (registry owner), business repos, cairn memory mirror |

### Tutor — fleet ops + harvesters
| Field | Value |
|---|---|
| agent_id | `agent-b73ac550-5671-471e-b3e1-721f948ea063` |
| Account | account-01 focusandexcell |
| Pod | harvester + vault-publishing + fleet ops |
| Status | 39 crons (inventory 2026-09-30). Owns the **hourly AFLinks sync (the Harmonizer)**, 5 harvest workers, village pair, model/security watches. |
| Repos | AFLinks (sync, workers, previews, search index), permies-skip-pep-data, cron-coordination, cron-migration tooling |

### Wizard / Forge — translation engine
| Field | Value |
|---|---|
| agent_id | `agent-75b8d29e-76c1-4223-89f5-b2f8708be460` (Wizard; Drunvalo's run logs call the translation pipeline "Forge" under this same id — registry also lists a separate Forge id `agent-34fdf7e8-5d9b-4fbd-921c-b6747c43162c`; reconcile with Chris) |
| Account | account-01 focusandexcell |
| Pod | translator |
| Status | Ledger translation identities: curator 326 runs, sweeper 349, translator-foreign 211, polyglot-scouts 34+36. All stalled 10-15. Watchtower: "forge declares 4th gap." |
| Repos | AFLinks (translations live in Forge memory per the publish boundary; database/, translation_progress/) |

### Other known agents (IDs from fleet-registry.json; inventories pending)
- **The Connector** `agent-343da9c5-d71a-452b-87a1-1c0edcdbc54d` — **the only fleet member alive today** (check-in 2026-10-21T13:08Z). connector-scout Tue 17:00 UTC.
- **The Watchtower** `agent-0add4400-49ae-474a-8741-96b6b6746679` — site-watchdog every 30 min; daily dark-lane scan (committed today).
- **The Sifter** `agent-6b9ed8e7-57f2-4429-a9a4-9e699da186f2` — counter-watchdog, 150 runs.
- **The Navigator** `agent-6791a657-6924-416e-8d80-fe2efb532fad` — digests, gear status.
- **Dolman** — aflinks-maintenance (account-02 Sandra; id aa68a8b9 per old records, registry says UNKNOWN).
- **Scooter, Bob, Trellis, Linnea, Captain Happening** — roles assigned, **agent_ids never recorded**. Chris to supply.

---

## Part 2 — JOB MANIFEST (every scheduled job)

### Drunvalo's 8 cloud crons (verbatim prompts in `drunvalo-crons.json`; full practices in the JSON manifest)

| Job | Cron ID | Schedule (UTC) | Role & Scope |
|---|---|---|---|
| village-maintenance | `8ae9ce4a` | every 6h | Village link check (~1000 URLs) + fix, add 2 vetted library resources from pool, push, report + ledger check-in |
| village-content-growth | `86a2c10e` | every 8h | Permies crawl (499pp), screen noise vs genuine BBs, wiki-verify, add quests + es/fr/de translations, +3 library resources |
| village-quality-audit | `49b0659e` | every 12h | Validate data.js/translations.js/master_quests.json, BB-marker cross-refs, HTML, 5 validators, fix or flag |
| aetherforce-synthesis | `227a48a` | every 6h | ONE deep synthesis doc per run: gap-check first, numbered sources, primary-source quotes (orig + EN), skeptical ledger, cross_ref validation pre-push |
| aetherforce-scout | `5e1805e8` | every 12h | Endangered/foreign/primary source hunting across lane topics, URL verification, Wayback saves, ledger FOUND-flips, upgrade proposals |
| aetherforce-database-refresh | `f2e027ea` | daily 06:00 | Standing DB QC checks, add Forge batch works, complete verified ledger items, builder patches |
| aetherforce-translation-qc | `02c18631` | every 4h | Standing QC: same-file dupes, title-similarity candidates (eyeball only), date-gated feed scan, person links, back-refs, ledger check-in |
| drunvalo-memory-mirror | `32f1a245` | daily 21:40 | MemFS snapshot to private DrunvaloMemory |

### Cure 8er's jobs (from his operating-context.md)
| Job | Schedule | Runner | Scope |
|---|---|---|---|
| memory-mirror-daily `c1f7eee4` | 04:23 daily | cloud | MemFS mirror (dead since 09-26) |
| daily-review | 15:00 daily | **local desktop** | QC new translations, emerging themes, hunt targets, synthesist/log.py report |
| translate-gear1 | every 2h | **local desktop** | Free models; Atsyukovsky 5-volume set (310 chunks) at capacity |
| translate-gear2 | every 6h | **local desktop** | Letta credit fallback, max 2 chunks/run |

### Eloquint's jobs
| Job | Schedule | Runner | Scope |
|---|---|---|---|
| eloquint-memory-mirror-daily-cloud `df9c32eb` | 04:37 daily | cloud | MemFS mirror (stale since 10-16) |

### Cairn's 20 (inventory cron-inventory-agent-6d.json, snapshot 2026-10-15)
fleet-hud-render (hourly :17) · daily-ops-wake (06:10) · daily-ops-watch (06:00) · counter-watchdog (*/3 :37) · cron-summary-digest (2nd/16th 15:00) · biweekly-research-sweep (1st/15th 09:00) · chem-curation (Sun 21:00) · chem-launch-builder (Mon/Thu 10:00) · clean-tech-bench (Thu 09:00) · clean-tech-rd (Tue 09:00) · entity-tracker (Fri 07:00) · monthly-ai-visibility-check (1st 10:00) · persona-drift-monitor (Wed 07:00) · red-team-weekly (Fri 10:00) · site-watch-monthly (1st 16:00) · watchlist-monthly-scan (1st 15:00) · weak-signals-quarterly (quarterly) · weekly-ai-pulse (Mon 07:00) · plus one-time miranda/queue tasks

### Tutor's 39 (inventory cron-inventory-agent-b7.json, snapshot 2026-09-30)
**AFLinks core:** aflinks-sync-v2 (HOURLY — the Harmonizer: scrape+merge+feed, the heartbeat of the library) · aflinks-preview-cleaner (*/4 :20) · aflinks-scout-svpwiki-v4 (*/6 :30)
**Harvest workers:** isis (*/6 :20) · padrak (*/6 :40) · steiner (*/6 :10) · zenodo-rh (*/6 :50) · svpwiki
**Village:** village-maintain-v2 (daily 09:00) · village-quest-sync (daily 07:00)
**Watches:** site-watchdog (*/30) · model-cost-watch (*/2) · model-verifier (8×/day) · curator-watch (*/2 19:00) · fleet-security-audit (monthly) · fleet-security-library (Mon) · gap-scout (Mon/Thu) · interview-radar (*/2 13:00) · meditation-abilities (Wed) · declassified-sweep (daily 16:00) · phase2-death-certs (daily 05:00) · practicality-engine (3×/day) · repo-scout (Wed) · tool-scout (weekly) · trauma-modalities-scout (Mon) · monday-briefing (Mon) · daily-brief (12:00) · culture-engine (12:00) · vitality-engine (11:00) · onboarding-checkin (weekly) · steiner-fulltext-archive (03:00) · tutor-memory-mirror (10:30) · bmvc-kit-loop (Tue) · bmvc-marketing-content (weekdays) · clean-chem-grow (04:30) · clean-chem-maintain-v3 (10:00) · connector-scout (Tue) · ai-advancements-scout (Fri) · ai-threat-scout (Mon)

### Wizard/Forge translation lane (2 known + batch cadence)
atsyukovsky-translate (hourly) · foreign-translate (*/2h) · plus the translation batch pipeline that produced the Oct 13-16 batches (16 languages, 100+ works/week)

---

## Part 3 — MIGRATION NOTES for the Sovereign Network host

1. **The jobs are script-orchestration, not chat.** Each cron is a git+python3 workflow (clone → run scripts → commit → push → report). The LLM orchestrates; scripts do the work. On AnythingLLM/LiteLLM, host each as a scheduled agent with shell access to a FocusOptimized checkout.
2. **Full verbatim prompts** for all 8 Drunvalo jobs are in `drunvalo-crons.json` next to this file — they are the migration source of truth, including the built-in practices (dedupe rules, collision guards, noise-acceptance classes).
3. **Secrets:** AFLinks + cron-coordination = fleet PAT; village = VILLAGEKEY PAT. Resolve at runtime from the vault; never in prompts or URLs.
4. **Collision hazard:** multiple agents write `database/research-index.json` + `person-index.json` in the same window. On the new host, **stagger** (20-30 min offsets) or serialize DB writers. The 00:00/06:00 UTC windows were the worst (6 crons).
5. **Consolidation opportunities (do not migrate duplicates):** village-maintain-v2 (Tutor) vs village-maintenance (Drunvalo); village-quest-sync vs village-content-growth; aflinks-scout-svpwiki-v4 vs aetherforce-scout. Recommend one owner per lane after migration.
6. **The ledger** (`cron_ledger.json`) should keep running as the fleet's worker clock — every migrated job checks in via `family.py` so the HUD stays truthful.
7. **Registry gaps to fix during migration:** Cure 8er + Eloquint agent_ids (now recovered, above — registry still says UNKNOWN); Wizard-vs-Forge id reconciliation; the 5 never-recorded agent_ids Chris must supply.
8. **Repo access:** verified this session — the fleet PAT can clone AND push Focusingpulse/AFLinks (full 126k-file clone succeeded), cron-coordination, both sibling memory repos. AnythingLLM on Chris's hand can use the same PAT for repo reads/writes.

*Pending: Cure 8er and Eloquint were tapped directly (2026-10-21 ~16:45Z, messages queued) to self-report their job lists and current state; their replies will be appended to AGENT-THREADS.md and folded into this manifest.*
