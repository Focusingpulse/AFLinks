---
name: Dossier 065 — At-Risk Archive Mirror Test
description: "Replication dossier for the preservation claim the archive's own preservation raids assert — that at-risk research sites in the aether / LENR / radionics field disappear permanently, and a home mirror is the defense. Grounded in the 2026 Crimson Hexagonal Archive erasure (862 works under 1,817 DOIs removed by Zenodo/CERN, 2026-06-19) and the MERLib Mirror tool (esaruoho/merlib-mirror, MIT, queue-based Wayback + live crawl). One endpoint: does a home mirror produce a complete, self-contained copy that survives the original going dark? Community card (shared-infra knowledge — the community's shared library); ~$0; Community mirror."
---

# Dossier 065 — The At-Risk Archive Mirror Test

**Status:** protocol
**Domain:** community (shared-infra knowledge — preserving the community's shared library against platform erasure)
**Tier:** sand (home/homelab, ~$0 — a computer and free software)
**Created:** 2026-10-05
**Source docs:**
- `living-library/sources/2026-10-04-archive-raid-merlib-mirror.md` — the MERLib Mirror raid (esaruoho/merlib-mirror; a queue-based daemon that mirrors disappearing personal research sites in LENR, zero-point energy, electrogravitics and advanced EM). Source: https://github.com/esaruoho/merlib-mirror.
- `living-library/sources/2026-10-04-archive-raid-crimson-hexagonal-erasure.md` — the Crimson Hexagonal Archive erasure (Zenodo/CERN terminated the account on 2026-06-19, removing 862 works under 1,817 DOIs; the successor archive published a Sovereign Asset Registry and a Tombstone Mirror). The motivating event.
- `living-library/sources/2026-10-04-archive-raid-lenr-documentation-initiative.md` — the LENR Research Documentation Initiative + Ego Out Documentation Project (preserving researchers' records before retirement and death).
- `living-library/sources/2026-10-04-archive-raid-borderland-etheric-physics.md` — Borderland Sciences (a 77-year print tradition, only partially digitised — a known rot-risk).

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-05-at-risk-archive-mirror` · authored_at `2026-10-05` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The claim (as asserted by the source)

The MERLib Mirror raid quotes the project's own README verbatim:

> "Websites disappear. Servers go offline. Domains expire. Researchers die and their life's work vanishes from the internet. In fields like LENR, zero-point energy, electrogravitics, and advanced electromagnetic research, this happens constantly."

The Crimson Hexagonal raid documents the same claim as an event rather than a worry: a repository-scale erasure on 2026-06-19 in which **862 works under 1,817 DOIs** were removed when Zenodo/CERN terminated an account. The successor archive (Alexanarch) published a **Sovereign Asset Registry** and a **Tombstone Mirror** — i.e. even the recovery apparatus is itself a small, single-party project.

The operational claim under test — the one a family actually cares about — is: **can a home mirror make a named at-risk site survive the original going dark?** The sources assert the risk and name the tool; neither asserts that a home mirror *works*. That is what the card measures.

**What is being tested, in one sentence:** when a family mirrors a named at-risk research site to its own machine, is the resulting copy complete enough and self-contained enough that the site's content still serves with the original unreachable?

## Honest status of the claim

The archive holds the **claim and the tool, and no home test of either.** A grep for `mirror`, `Wayback`, `archive node`, `preservation` across `living-library/synthesis/quest-queue/` and `living-library/synthesis/replication/` returns **no card and no dossier** on home-scale preservation. Every community card in the queue tests a *physical* claim (dowsing, wells, tools, a pendulum); **none tests the preservation of the knowledge itself.**

Four things the card must say out loud:

1. **The tool is young and small, and the card says so.** The MERLib repo was created 2026-03-04, is MIT-licensed, has **1 star** and **1 open issue**, and is a single-maintainer project. The raid's own verification note is explicit: *"the tool as confirmed and the library as in-progress."* A card that treats a 1-star repo as proven infrastructure is over-claiming; the card treats it as **the thing under test**.
2. **The motivating event is real and dated.** The Crimson Hexagonal erasure is a documented 2026-06-19 event with counts (862 works / 1,817 DOIs). The card cites it as the *reason the test matters*, not as proof the tool works.
3. **"Complete" and "self-contained" are two different measurements, and the card keeps them apart.** A crawl can capture every page and still fail to preserve the site, because the pages' assets and links point at the live domain. The card scores both — completeness against the source's own page list, and self-containment against the original being blocked.
4. **A partial result is a real result.** If the tool preserves some sites and not others, that is a finding about *which* sites are preservable at home scale — not a failure of the run.

**Under-promise, stated plainly:** the likely outcome is that a static, mostly-HTML site mirrors cleanly (≥95% complete, self-contained) while a dynamic or JavaScript-rendered site mirrors poorly. **That is a complete, useful result** — it tells a family which of its at-risk sources it can actually save, and it files the queue's first home test of the archive's own preservation claim. A clean pass on a site the tool was not built for would be the surprise.

## Why it matters

- It is the queue's **first card about knowledge infrastructure** — the community's shared *library*, rather than a device, a field, a material, or a measurement. Every prior community card tests a physical claim; this tests whether the community can keep its own sources.
- It is the queue's **first card whose subject is the archive itself** — the AFLinks vault exists to preserve exactly this material, and this card is the family-scale version of the same act.
- It is the queue's **first card grounded in a documented 2026 event** (the Crimson Hexagonal erasure) rather than in a historical claim.
- It is genuinely **community-scale**: one household mirrors one site, and a neighbourhood that pools its mirrors becomes a distributed archive — the same "distributed node" shape as the Community guild's neighbourhood replication nodes, applied to preservation instead of experiment.

## Replicability: `home`

- Build/obtain cost: **~$0** — a computer, a few GB of disk, and free software (the MERLib tool is Python stdlib-only; `wget`/`httrack` are acceptable alternatives, and the Wayback Machine is a fallback source).
- Safety: **low.** No chemicals, no mains wiring, no voltage. The only cautions are (a) respect the source site's `robots.txt` and rate limits — a mirror is not a DoS, and (b) do not mirror anything you are not permitted to keep privately; a private archival copy of publicly-available web content is low risk, **republishing** it is the risk.
- Accessibility: an afternoon. Pre-counting the source's pages takes minutes (a sitemap or the Wayback CDX API); the crawl runs unattended; verification is a file count and one offline serve.

## Apparatus (Bill of Materials)

- **A computer** with a few GB of free disk and Python 3 (stdlib only).
- **The mirror tool** — `esaruoho/merlib-mirror` (MIT): `./mirror-submit <domain>` for Wayback mode (CDX discovery + multi-timestamp fallback), `./mirror-submit <live-url>` for a live BFS crawl. Acceptable alternatives: `wget --mirror`, `httrack`, or a manual Wayback pull.
- **A page-count source** — the target site's `sitemap.xml`, or the Wayback CDX API (`http://web.archive.org/cdx/search/cdx?url=<domain>&output=json&fl=original&collapse=urlkey`) for a pre-registered page list.
- **A checksum tool** — `sha256sum` (or equivalent) to record a manifest of the local copy.
- **A way to block the original** — edit `/etc/hosts`, disconnect the network, or serve the local copy on a different port — to prove self-containment.
- **A camera/phone** — to photograph the pre-registration sheet and the offline serve.

## Protocol (pre-registered home-mirror preservation test)

**Phase 1 — pre-register, before anything is fetched.**
1. **Pick ONE named at-risk site** and write it down. The MERLib raid names three examples — `cheniere.org` (Tom Bearden), `riess.org`, `amasci.com` (Bill Beaty) — but any site the family judges at risk qualifies. Record the URL and the date.
2. **Pre-count the source's pages** from its `sitemap.xml` or the Wayback CDX API and **record the number and the method**. This is the denominator; without it, "complete" is unmeasurable.
3. **Write the pre-registration sheet:** the site, the page count and its source, the mirror method (tool + mode), the completeness threshold, the self-containment test, and the criteria below. **Photograph it before the first fetch.**

**Phase 2 — mirror.**
4. **Run the mirror** against the site (Wayback mode or live crawl). Respect `robots.txt` and rate limits; a blocked crawl is a **void** run, not a failure of the claim.
5. **Record the output:** the local copy's file count, total size, and a `sha256sum` manifest.

**Phase 3 — verify completeness.**
6. **Count the pages actually captured** and compare against the pre-registered page count. Report the **fraction present**.
7. **List what is missing** (pages in the source list but not in the copy) — the missing list is part of the result.

**Phase 4 — verify self-containment.**
8. **Block the original** (hosts file, network off, or a different port) and **serve the local copy**. Open the home page and follow links.
9. **Score self-containment:** do the pages render with their assets, and do the internal links resolve locally, with the original unreachable? Record every broken asset or link that still points at the live domain.

## Pass / fail (pre-registered)

- **PASS (the mirror preserves the site — the claim survives):** **≥95% of the source's pages are present** AND the local copy **serves its content with the original blocked**, with no missing assets on the pages sampled. Report as the claim holding for this site.
- **PASS (the mirror is not sufficient — the claim refuted for this site):** **<50% of the source's pages present**, or only the home page — the tool does not preserve this site at home scale. Reported as the expected result for dynamic sites, not a failure (Skeptic's Star).
- **FAIL (void, not a null):** the crawl was **blocked** (`robots.txt`, rate-limiting, or an unreachable source) — the run says nothing about the claim.
- **ARTIFACT:** the copy is "complete" by page count but **not self-contained** — the pages' assets or links still point at the live domain, so the copy will not survive the original going dark.

## Evidence

Photo of the pre-registration sheet (site, page count and its source, method, thresholds, criteria) taken before the first fetch + the source's page list (sitemap or CDX output) + the mirror's file count and `sha256sum` manifest + the completeness comparison (pages present / pages pre-counted, with the missing list) + a screenshot of the local copy serving **with the original blocked** + the self-containment notes (any asset or link still pointing at the live domain).

## Confounds (named in advance)

- **The source changed between the pre-count and the mirror.** Pages can be added or removed mid-run. **Record both timestamps; treat a small drift as expected.**
- **The page list is itself incomplete.** A sitemap may omit pages; the CDX may not cover everything. **Name the list's source and its limits.**
- **"Complete" without "self-contained" is not preservation.** A copy whose assets point at the live domain dies with the domain. **Score both, separately.**
- **A blocked crawl is a void, not a refutation.** Rate-limiting and `robots.txt` are not evidence about the claim. **Record the block and stop.**
- **The tool is young.** A failure on a site the tool was not built for is a statement about the tool's scope, not about preservation in general. **Say which.**
- **Rights.** A private archival copy of publicly-available content is low risk; **republishing** it is the risk. **Keep the copy private; publish only our own summary and a link.**

## Verdict rules

≥95% of pages present AND the copy serves offline with the original blocked → **the claim survives for this site.** <50% present or home-page-only → **the claim is refuted for this site** (the expected result for dynamic sites). A blocked crawl → **void, not a null.** A copy that is complete by count but not self-contained → **an artifact, not a pass.** Fewer than one full crawl, or no pre-registered page count → **inconclusive.**
