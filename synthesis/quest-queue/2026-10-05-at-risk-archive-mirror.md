---
name: Quest Card — At-Risk Archive Mirror Test
description: "Aetherforce-branded quest card testing the preservation claim the archive's own preservation raids assert — that at-risk research sites in the aether / LENR / radionics field disappear permanently, and a home mirror is the defense. Grounded in the 2026 Crimson Hexagonal Archive erasure (862 works under 1,817 DOIs removed by Zenodo/CERN) and the MERLib Mirror tool. One endpoint: does a home mirror produce a complete, self-contained copy that survives the original going dark? Community domain (shared-infra knowledge — the community's shared library); Community mirror."
---

# ⚡ Aetherforce — Community

**Guild:** Aetherforce — Community
**Quest Line:** ⚡ Aetherforce · Community complement
**Tier:** sand
**Domain:** community (shared-infra knowledge — preserving the community's shared library against platform erasure)
**Status:** proposed
**Created:** 2026-10-05

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-05-at-risk-archive-mirror` · authored_at `2026-10-05` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Community",
  desc: "Every library in this archive is one dead server away from gone. In June 2026 a single account termination at Zenodo removed 862 works filed under 1,817 DOIs — not because anyone judged them false, but because a platform decided to stop hosting them. The researchers in this field are old, their sites are hand-built, and their domains expire. The defense is not a bigger platform; it is a copy on your own machine. This quest makes your household a node in that defense: pick one named at-risk site, count its pages before you touch it, mirror it to your own disk, and then prove the copy stands on its own by serving it with the original switched off. If the copy is complete and self-contained, you have saved something that was otherwise going to vanish — and you have learned the one skill that keeps a library alive. If it is not, you have learned exactly which sources a home mirror can and cannot save, which is a real result. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "At-Risk Archive Mirror Test",
    "FIRST pre-register before you fetch anything: pick ONE named at-risk site, count its pages from its sitemap.xml or the Wayback CDX API, and write down the site, the page count and its source, the mirror method, the completeness threshold, the self-containment test, and the criteria - photograph the sheet. Then mirror the site with a queue-based tool (the MERLib mirror, or wget --mirror / httrack), respecting robots.txt and rate limits; record the copy's file count, total size, and a sha256sum manifest. Then verify two separate things: COMPLETENESS - the fraction of the source's pages present in the local copy, with a list of what is missing; and SELF-CONTAINMENT - block the original (hosts file, network off, or a different port), serve the local copy, and check whether the pages render with their assets and their internal links resolve locally. Measurable outcome: the fraction of the source's pages present in the local copy, and whether the local copy serves its content with the original unreachable. Target: >=95% of the source's pages present AND the local copy serves offline with no missing assets = the mirror preserved the site; <50% present or home-page-only = the tool does not preserve this site at home scale (the expected result for dynamic sites).",
    ["Technology", "Community", "Preservation"],
    "🗄️"
  ],
  source_doc: "sources/2026-10-04-archive-raid-merlib-mirror.md — 'MERLib Mirror — endangered experimental-physics site preservation' (esaruoho/merlib-mirror) + sources/2026-10-04-archive-raid-crimson-hexagonal-erasure.md — the 2026-06-19 Crimson Hexagonal Archive erasure (862 works under 1,817 DOIs)",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-10-05-dossier-065-at-risk-archive-mirror.md",
  pass_fail: "PASS (the claim survives - the mirror preserves the site): >=95% of the source's pages are present in the local copy AND the local copy serves its content with the original blocked, with no missing assets on the pages sampled | PASS (the claim refuted for this site - the expected, complete result): <50% of the source's pages present, or only the home page - the tool does not preserve this site at home scale (Skeptic's Star) | FAIL (void, not a null): the crawl was blocked (robots.txt, rate-limiting, or an unreachable source) - the run says nothing about the claim | ARTIFACT: the copy is complete by page count but NOT self-contained - the pages' assets or links still point at the live domain, so the copy will not survive the original going dark",
  evidence: "Photo of the pre-registration sheet (site, page count and its source, method, thresholds, criteria) taken before the first fetch + the source's page list (sitemap or CDX output) + the mirror's file count and sha256sum manifest + the completeness comparison (pages present / pages pre-counted, with the missing list) + a screenshot of the local copy serving WITH the original blocked + the self-containment notes (any asset or link still pointing at the live domain)"
}
```

---

## Source Documentation

- **Primary (the claim and the tool):** `sources/2026-10-04-archive-raid-merlib-mirror.md` — the MERLib Mirror raid. It quotes the project's own README verbatim ("Websites disappear. Servers go offline. Domains expire. Researchers die and their life's work vanishes from the internet…") and records the tool: `esaruoho/merlib-mirror`, MIT, Python stdlib-only, a queue-based daemon with `./mirror-submit <domain>` (Wayback mode) and `./mirror-submit <live-url>` (live BFS crawl). ⚠ The raid's own verification note is explicit that the repo is **young and small** (created 2026-03-04, 1 star, 1 open issue) — *"the tool as confirmed and the library as in-progress."* The card treats the tool as the thing under test, not as proven infrastructure.
- **Motivating event (the erasure):** `sources/2026-10-04-archive-raid-crimson-hexagonal-erasure.md` — the Crimson Hexagonal Archive erasure: Zenodo/CERN terminated the account on **2026-06-19**, removing **862 works under 1,817 DOIs**. The successor archive (Alexanarch) published a **Sovereign Asset Registry** and a **Tombstone Mirror**.
- **Companion raids (same cluster):** `sources/2026-10-04-archive-raid-lenr-documentation-initiative.md` (the LRDI + Ego Out Documentation Project — preserving researchers' records before retirement and death) and `sources/2026-10-04-archive-raid-borderland-etheric-physics.md` (Borderland Sciences — a 77-year print tradition, only partially digitised, a known rot-risk).
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-05-dossier-065-at-risk-archive-mirror.md`
- **Aetherforce Reference:** search "archive" / "preservation" / "Borderland Sciences" on https://www.aetherforce.energy
- **Vault link:** https://focusingpulse.github.io/AFLinks

---

## Rubric Justification

- **Practical:** a named apparatus (a queue-based mirror tool — `esaruoho/merlib-mirror`, or `wget --mirror` / `httrack`) with a named procedure (pre-register the site and its page count → mirror → verify completeness → verify self-containment) and a measurable outcome (**the fraction of the source's pages present, and whether the local copy serves with the original blocked**). Not pure theory.
- **Replicable:** home-scale (**~$0** — a computer, a few GB of disk, free software), no lab, no chemicals, family-safe, any time.
- **Relevant:** maps to the Village **community** survival domain (shared-infra knowledge — the community's shared library) and complements the **Community** guild (distributed labs / neighbourhood nodes), applied to preservation instead of experiment.
- **Honest:** framed as a TEST, not an endorsement. The card names the tool's immaturity (a 1-star, single-maintainer repo), cites the motivating erasure as a dated event rather than as proof, keeps **completeness** and **self-containment** as two separate measurements, and treats a partial result as a finding about which sources are preservable at home scale. It states the rights posture plainly: keep the copy private, publish only our own summary and a link.
- **Linked:** source docs (the MERLib raid + the Crimson Hexagonal erasure + two companion raids), dossier created with protocol + pass/fail, evidence protocol defined.

---

## What makes it the queue's first of its kind

- **The first card about knowledge infrastructure** — the community's shared *library*, rather than a device, a field, a material, or a measurement. Every prior community card (005, 007, 013, 023, 029, 035, 040, 046, 052, 059) tests a *physical* claim; this one tests whether the community can keep its own sources.
- **The first card whose subject is the archive itself** — the AFLinks vault exists to preserve exactly this material, and this card is the family-scale version of the same act. The engine has been turning the archive into quests; this is the first quest that turns the archive's *preservation* into a family skill.
- **The first card grounded in a documented 2026 event** — the Crimson Hexagonal erasure (862 works / 1,817 DOIs, 2026-06-19) — rather than in a historical claim or a practitioner manual.
- **The design choice that is the whole card: two separate measurements.** A crawl can capture every page and still fail to preserve the site, because the pages' assets and links point at the live domain. **Completeness** (pages present vs the pre-registered page count) and **self-containment** (does the copy serve with the original blocked?) are scored separately, and the ARTIFACT condition is exactly the case where a copy is "complete" but dies with the domain.

---

## Honest Framing

This is a test, not an endorsement. The tool is a **young, single-maintainer, 1-star repository**, and the raid that found it says so; the card does not dress it as proven infrastructure — it makes the tool the thing under test. The motivating event is **real and dated** (the Crimson Hexagonal erasure, 2026-06-19, 862 works / 1,817 DOIs), and the card cites it as the reason the test matters, not as evidence the tool works. The likely outcome is that a static, mostly-HTML site mirrors cleanly while a dynamic or JavaScript-rendered site mirrors poorly — **a complete and useful result**, because it tells a family which of its at-risk sources it can actually save. A clean pass on a site the tool was not built for would be the surprise. The card makes **no claim about the content** of the sites it preserves — preserving a claim is not endorsing it; the archive's job is to keep the record, and the dossier is where any claim gets tested. **Rights:** a private archival copy of publicly-available content is low risk; **republishing** it is the risk — keep the copy private, publish only our own summary and a link.

---

## Aetherforce Mirror Coverage

This card complements **Guild 24: Community** (distributed labs / neighbourhood nodes) — its **7th** card, after the Electrostatic Energy Test (2026-09-10), Psi-Track Dowsing (2026-09-21), Shared Well Yield Estimate (2026-09-25), Eclipse Pendulum Watch (2026-09-27), Shared Well Iron & Manganese Vortex (2026-09-29), and Blind Concordance Dowsing (2026-10-01).

**Mirrors filled: 25/26** (unchanged — no new guild filled; Textiles remains the only empty mirror, with no buildable fiber-resonance source in the archive).

---

## Dossier

- `living-library/synthesis/replication/2026-10-05-dossier-065-at-risk-archive-mirror.md` — full protocol, apparatus, pass/fail, confounds and verdict rules.
