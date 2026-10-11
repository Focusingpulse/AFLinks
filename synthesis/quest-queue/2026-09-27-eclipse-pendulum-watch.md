---
name: Eclipse Pendulum Watch
description: "Build a paraconical/Foucault pendulum, measure its own baseline precession and period on ordinary days, then run the identical session during the next solar eclipse — and pool the result across households. Community-domain card (the queue's first distributed, simultaneous, multi-household measurement — the neighborhood replication node); ~$50-100; Community mirror. Tests the contested Allais eclipse-pendulum claim, whose modern replications are mostly null."
---

# ⚡ Aetherforce — Community

**Guild:** Aetherforce — Community
**Quest Line:** ⚡ Aetherforce · Community complement
**Tier:** straw
**Domain:** community (a distributed, simultaneous, multi-household measurement — the neighborhood replication node; the phenomenon tested is an eclipse-time pendulum anomaly)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-27-eclipse-pendulum-watch` · authored_at `2026-09-27` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Community",
  desc: "In 1954 the economist Maurice Allais released a pendulum every 14 minutes for thirty days — and during a solar eclipse its swing plane turned 13.5 degrees off its normal path. Replications since have been mixed: a 1970 torsion pendulum saw the period shift, a 2010 automated Foucault pendulum saw nothing, and the modern literature calls the effect unproven. That is exactly why it belongs to a neighborhood rather than a laboratory. Build a pendulum, measure its own baseline on ordinary days — that is your null — then run the identical session during the next eclipse visible from where you live, and have your neighbors do the same. One home can only ever have one eclipse; several homes measuring the same event the same way is the only thing that can settle it. If the eclipse day looks like every other day, you have measured a null on your own rig and joined the modern result — which is worth just as much. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Eclipse Pendulum Watch",
    "Build a pendulum: a 1-5 kg bob on a 2-3 m low-twist line, released from a fixed recorded plane. State which geometry you built — a fixed pivot (Foucault, whose signature is the precession of the swing plane) or a ball-and-socket/knife-edge support (paraconical, Allais's own design). Read the swing-plane azimuth every 5 minutes against a protractor ring, from a phone on a tripod, for a 2-hour session; record the period as the mean of at least 20 swings. First run at least 3 BASELINE sessions on ordinary days at the SAME clock time as the coming eclipse's local maximum, and compute your baseline precession rate and period with their scatter — that scatter is your null and your resolution. Then run the identical session on eclipse day, starting 1 hour before first contact and ending 1 hour after last contact, changing nothing. Recruit at least 2 neighboring households to run the same protocol and post their own baseline and eclipse series. Measurable outcome: the eclipse-day precession rate and period versus each site's OWN baseline, in units of that site's baseline scatter. PASS: a deviation of at least 3x the baseline scatter, in the same direction, across at least 2 of 3 sessions or 2 of 3 households. FAIL: every site within its own baseline scatter — the expected result, matching the modern null literature (Skeptic's Star). VOID: your baseline scatter is larger than the effect you are trying to see — report the resolution achieved, not a verdict. NEVER look at the sun without ISO 12312-2 eclipse glasses.",
    ["Science", "Measurement", "Community", "Family"],
    "🌑"
  ],
  source_doc: "sources/2026-09-20-scout-a-langs-1.md#entry-3 (scout find: Alexander N. Ivanov, 'Gravitational Anomaly of Solar Eclipses' — practical_applicability true [buildable, reproducible]; ties the Chinese 1997 eclipse gravimeter report to Fatio 1690 and Allais's paraconical pendulum)",
  source_url: "https://alexandar.info/zatmeniya/",
  dossier: "living-library/synthesis/replication/2026-09-27-dossier-046-eclipse-pendulum-watch.md",
  pass_fail: "PASS: eclipse-day precession rate (and/or period) deviates from the site's own baseline by >= 3x the baseline scatter, same direction, in >= 2 of 3 sessions OR across >= 2 of 3 households at the same eclipse. FAIL: the eclipse-day series is within the baseline scatter at every site and session - the pendulum does not see the eclipse at this scale; a complete result (Skeptic's Star) and the expected one. INCONCLUSIVE: fewer than 3 baseline sessions; baseline scatter exceeds the effect size (the rig cannot resolve it); the eclipse arm was not run at the same clock time; the geometry or release changed between arms. VOID: the eclipse was not visible from the site; the rig was disturbed mid-session; the reader knew which arm they were in; the protocol was changed after first contact. ARTIFACT: the deviation tracks indoor temperature rather than the eclipse; or it appears on a non-eclipse day at the same clock time; or it disappears when the observer is removed from the room.",
  evidence: "Photo of the rig and its stated geometry (line length, bob mass, release method, pivot type, azimuth scale) + the pre-registration sheet (session times, thresholds, scoring rule, geometry) + the 3+ baseline series with their scatter + the full eclipse-day series + the indoor temperature log for every session + the video of the azimuth scale + the per-household sheets if pooled + the eclipse-visibility record for each site + the void/artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the archive find):** `living-library/sources/2026-09-20-scout-a-langs-1.md`, **entry 3** — Alexander N. Ivanov, *Гравитационная аномалия солнечных затмений* (Gravitational Anomaly of Solar Eclipses), https://alexandar.info/zatmeniya/ — a fragile personal research archive (host-stability: fragile, flagged preservation-candidate) tying the Chinese 1997 eclipse gravimeter report to Fatio de Duillier's 1690 kinetic-gravity model and Maurice Allais's paraconical-pendulum work. The scout flag is explicit: *"eclipse-day gravimeter measurements are cheap, instrumented, and repeatable at every eclipse — an open replication window for anyone with a gravimeter."*
- **The claim in the source's own terms:** that a pendulum's behaviour during a solar eclipse departs from classical prediction — the azimuth of the oscillation plane (Allais) and/or the period (Saxl & Allen; Jeverdan) — and that eclipse-day measurement is a cheap, repeatable window open to anyone.
- **External literature (context and the honest ledger — not held in the archive):** Allais's 1954 paraconical-pendulum observations (~13.5° azimuth excursion over ~2.5 h against a normal ~0.19°/min Foucault precession; repeated 1959); Jeverdan, Rusu & Antonescu (1961, period); Saxl & Allen, *Phys. Rev. D* **3**:823–825 (1971, torsion-pendulum period +0.037 %); Duif (2004 review — conventional explanations fail); **nulls:** Ullakko et al. (1990 Finland, no effect within error) and Salva, *Phys. Rev. D* **83**, 067302 (2011, automated Foucault pendulum — no evidence; would have seen >0.3°/h).
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-27-dossier-046-eclipse-pendulum-watch.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "eclipse", "Allais", "paraconical pendulum", "gravimeter", "Kozyrev"
- **Aetherforce Reference:** Search "gravity", "Allais", or "eclipse" on https://www.aetherforce.energy
- **Related cards:** 005 (Blind Geopathic Zone Mapping — a pendulum/rod instrument against ground truth), 034 (Neutral Pendulum Discrimination Test — a pendulum as a measurement skill), 021 (Earth-Energy Grid Instrument Scan), 041 (Spin-Weight Anomaly Test — the queue's other already-refuted-claim card)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (a bob, a low-twist line, a defined pivot, an azimuth scale, a timer) with a named procedure (3+ baseline sessions at the eclipse's clock time → identical eclipse-day session → per-site scatter → pooled across households) and a measurable outcome (**eclipse-day precession/period deviation in units of the site's own baseline scatter**). Not pure theory. |
| **Replicable** | YES — Home, straw: ~$50–100 (bob, line, release, protractor ring, timer). No mains, no chemicals, no heat. The demanding requirements are **discipline** (pre-registration before the eclipse, identical clock time, unchanged protocol) and **patience** (the eclipse arm is scheduled). |
| **Relevant** | YES — Community domain, and the fit is the **distributed protocol itself**: the card's value is that several households measure the same event the same way simultaneously — the "neighborhood replication node" the Community guild's complement names. **This is the queue's first card that requires multiple homes and a scheduled external event.** The phenomenon is a gravity/pendulum anomaly; the *practice* is community coordination. |
| **Honest** | YES — the claim is framed as a claim and the card is a test, not an endorsement. The **modern null literature is named in advance** (Ullakko 1991, Salva 2011), the **expected result is stated as a null**, the **baseline scatter is the discriminator** (not the eclipse deviation alone), and the confounds (tilt of the vertical, thermal drift, time-of-day, observer airflow) are each named as explicit ARTIFACT tests. Clean FAIL / INCONCLUSIVE / VOID paths. |
| **Linked** | YES — a scout find, the source URL, the external literature, a pre-registered replication dossier, and cross-links to four related cards. |

**Mirror choice, stated:** the card's domain is **community**, and **Community** is the honest fit — its complement is named *"distributed labs / Uber-for-labs — neighborhood replication nodes,"* and this card is the queue's first literal instance of that node (several homes, one event, one pre-registered protocol). **Oddball** ("cross-field bridges / suppressed-science re-try") was the closest alternative and was not chosen because the card's defining feature is its *distributed protocol*, not its subject matter; **Rocket** and **Electricity** were considered for the gravity/energy subject and rejected because they already carry three cards each and because the card's outcome is a coordinated community measurement, not a device.

---

## The honest framing (the spine of the card)

**This card cannot settle the Allais effect, and it says so.** One home gets one eclipse; that is one data point, and the effect is contested precisely because single-site results have been contradictory. What the card *can* do is what no single laboratory has managed: get several households to measure the same eclipse the same way, each against its own pre-registered baseline, and pool. That is the only shape of evidence that could ever move this question.

**The baseline is the card.** The eclipse arm is the headline, but the *measurement* is the family's own pendulum on ordinary days — its precession rate, its period, and their scatter. Without that number there is nothing to compare the eclipse to, and the run is VOID. This is the queue's first card where the control is the family's own instrument on ordinary days.

**The departure from the scout flag, written down:** the scout entry describes eclipse-day **gravimetry** (an instrument family the archive does not hold and a family cannot build). The card is **narrower than the source**: it tests the same claim with a **pendulum** — the apparatus Allais actually used, and the one a home can build — and it says so. The gravimeter version is deferred to the instrument tier.

**Under-promise:** a null is the expected result. The modern literature is mostly null, and the card is built so that a null is a *complete* result (Skeptic's Star), not a failure. The card's real product is the distributed protocol and the discipline of pre-registering before a scheduled event.

**Hard condition carried from the source context:** the eclipse is only usable if it is **visible from the site**, and **no one may look at the sun without ISO 12312-2 eclipse glasses.** Both are stated in the card, not implied.

---

## Next eclipse windows (verified 2026-09-27, NASA)

- **6 Feb 2027** — annular; visible in parts of South America and Africa (Chile, Argentina, Uruguay, Brazil, Ivory Coast, Ghana, Togo, Benin, Nigeria), partial across much of South America, Africa and Antarctica.
- **2 Aug 2027** — total; visible in southern Spain, North Africa (Morocco, Algeria, Tunisia, Libya, Egypt), Saudi Arabia, Yemen; **partial** across most of Europe, much of Africa, the Middle East, and **northern Maine in the U.S.**
- **26 Jan 2028** — annular; **partial** across the United States (annularity not visible from the U.S.).
- Source: NASA *Future Eclipses* (science.nasa.gov/eclipses/future-eclipses/) and NASA GSFC eclipse pages. **A family should confirm the local circumstances for its own location before pre-registering** — the eclipse must be visible from the site or the run is VOID.

**Lead time, stated plainly:** the next eclipse visible from most of North America is **2 Aug 2027 (~11 months)**. The card is therefore a **standing protocol**: Phase 1 (build + baseline) is immediate and produces the family's own null now; Phase 2 is scheduled. A family that would rather not wait can run the baseline phase as a standalone Foucault-pendulum measurement, or join a household nearer an eclipse.
