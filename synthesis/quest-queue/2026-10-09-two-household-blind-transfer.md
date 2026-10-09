---
name: Quest Card — Two-Household Blind Transfer Test
description: "Aetherforce-branded quest card testing the claim that a claimed non-local transmitter (a torsion-field generator, or a home-replicable pulse-excited LED) changes the properties of a water sample in a SEPARATE household at a distance, with the receiver blind to which of N modes the transmitter is running. Primary source: SRCAA 'Zond' (Kyiv) meeting minutes 279, 2020-07-15 — a blinded 3,572 km Kyiv→Tomsk transfer test (operator K switched 3 generator modes; operator T measured water blind; 'full 100% correlation'); convergence source: the scalarwave.cc 2.2 km LED-generator-vs-EIS experiment. The queue's first card whose two ends are a sender and a receiver in separate households with independent power, its first whose discriminator is a blind mode identification scored against chance, and its first that tests a distance claim as a distance claim. Community domain (shared-infra knowledge — the neighbourhood replication node); Community mirror (community-domain complement)."
---

# ⚡ Aetherforce — Community

**Guild:** Aetherforce — Community
**Quest Line:** ⚡ Aetherforce · Community complement
**Tier:** sand
**Domain:** community (shared-infra knowledge — a distributed, two-household replication; the neighbourhood replication node)
**Status:** proposed
**Created:** 2026-10-09

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-09-two-household-blind-transfer` · authored_at `2026-10-09` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Community",
  desc: "In 2020 a research society in Kyiv ran an experiment with a partner 3,572 km away in Tomsk. One operator switched a torsion-field generator between three modes; the other, in a different country, measured the properties of eight litres of water in a bucket — and did not know which mode was running. When the two sheets were compared afterwards, the minutes record 'full 100% correlation.' The same community reports a shorter version: a pulse-excited LED in one place, a water sensor 2.2 km away, the transmitter run from a battery precisely so nobody could say the signal travelled through the mains. This is the claim this quest tests, and it is the one claim a neighbourhood can test that a single household cannot — because it needs two homes, two people, and one sealed list of modes. The design is the whole point: the receiver must not know whether the transmitter is off or on, or which mode is running, and must say which they think it is. Score that against chance. If the receiver's guesses land on the right mode more often than chance, and it repeats, you have something extraordinary that needs a second pair of households. If the guesses land at chance — the expected result — then a claim that has circulated for decades without a blind trial has been tested by two families with a battery, an LED and a strip of litmus paper. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Two-Household Blind Transfer Test — Can a Sender Reach a Receiver Who Cannot Know the Mode?",
    "FIRST pre-register before any trial: write down both households and their approximate separation, the transmitter and its N modes (at least three: off / A / B), the link (a printed photograph of the receiver's water sample), the water source and volume, the pH method, the number of trials (at least 12), the timing schedule, the chance model (1/N), and the scoring rule - photograph the sheet, and seal the mode list with the sender. Then run the trials: the sender randomly picks one mode per trial from the sealed list, runs it for the fixed interval, and records the mode and the time; the receiver, at the scheduled time, measures the pH of their water sample and records BOTH the reading and which mode they believe is running - with no communication during the run and independent power at each end (the transmitter runs from its own battery, never from the mains). Repeat for all trials, varying the times so no pattern can be learned. Only after the last trial, open the sealed sheets and compute the receiver's blind mode-identification accuracy against the 1/N chance baseline, and the pH reading per trial against the sender's mode. Then repeat the whole session once with a fresh sealed list. Measurable outcome: the receiver's blind mode-identification accuracy (correct guesses out of N trials) against the 1/N chance baseline, and the pH reading per trial plotted against the sender's mode. Target: accuracy above chance at p<0.05 that repeats in the second session = the claim survives and needs a second pair of households; accuracy at chance with pH not tracking the mode = the claim is refuted (the expected, complete result). Include off-mode trials so ordinary drift can be separated from a transfer.",
    ["Science", "Community", "Measurement"],
    "🏘️"
  ],
  source_doc: "translations/2026-10-09-srcaa-zond-meeting-minutes-279-uk.md — SRCAA 'Zond' (Kyiv) minutes 279, 2020-07-15, the blinded 3,572 km Kyiv→Tomsk transfer test (3 generator modes, blind receiver, 'full 100% correlation'); convergence: translations/2026-10-09-2point2km-nonlocal-led-torsion-generator-eis-scalarwave-zh.md — the 2.2 km pulse-excited-LED vs water-EIS experiment",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-10-09-dossier-077-two-household-blind-transfer.md",
  pass_fail: "PASS (claim survives - the surprise): the receiver's blind mode-identification is ABOVE the 1/N chance baseline at p<0.05 (binomial) AND the direction repeats in a second session AND at least one second pair of households reproduces it - requires independent replication before it is believed | PASS (claim refuted - the expected, complete result): the receiver's blind mode-identification is AT chance and the pH readings do not track the sender's mode - the two-household transfer is not reproduced (Skeptic's Star) | FAIL: the blinding was broken (the receiver knew or could infer the mode), the two ends shared mains power, the mode list was not sealed, or the pH method changed between trials | VOID: Phase 0 failed (the transmitter did nothing the household could verify, or the receiver's baseline noise exceeded the effect sought), or a reading was taken outside the pre-registered schedule - a VOID is not a NULL | ARTIFACT: the receiver's readings track a mundane shared variable (time of day, temperature, a shared water delivery) rather than the sender's mode - detected by the off-mode trials and the baseline",
  evidence: "Photo of the pre-registration sheet (both households, separation, transmitter, modes, link, water, pH method, trials, timing, chance model, scoring rule) taken before the first trial + a photograph of the transmitter and of the link (the printed photograph of the receiver's sample) + the sealed mode list and the sender's per-trial record (mode + time) + the receiver's per-trial record (pH reading + the mode they believed was running), kept blind + the three baseline readings with the transmitter off + the scoring sheet (blind accuracy vs 1/N, the pH-per-trial table, and the second session's repeat) + a one-paragraph verdict (supports / refutes / inconclusive) with the numbers and the chance calculation shown"
}
```

---

## Source Documentation

- **Primary (the seed record):** `translations/2026-10-09-srcaa-zond-meeting-minutes-279-uk.md` — the full English translation of *Minutes of the Session of the SRCAA "Zond" No. 04 (279)*, Ukrainian Research Centre for the Study of Anomalies "Zond", Kyiv, 2020-07-15 (uk→EN, 9 chunks, complete). The load-bearing passage, verbatim: *"The T operator in Tomsk made multiple measurements of water properties (8 litres in a conventional galvanized bucket) without knowing which TFG mode of operation the K operator used at this moment in Kyiv. After the end of the experiment, the operating modes of TFG in Kyiv and the properties of water in the bucket in Tomsk were compared. Full 100% correlation was found."* The same minutes record a shorter, home-scale version: *"the transfer of the acid-alkaline properties of water over a distance of about 40 cm was carried out. The transfer was monitored with litmus papers. The indicator values changed from pH 5...6 to pH 8...9 over 20 min."* ⚠ The minutes are a **research society's own record** — a deposited article, not a peer-reviewed paper.
- **Convergence (the home-replicable transmitter):** `translations/2026-10-09-2point2km-nonlocal-led-torsion-generator-eis-scalarwave-zh.md` — the full English translation of *2.2-km-Distance Non-local Action Experiment — LED Torsion Generator vs EIS*, scalarwave.cc (zh→EN). It supplies the home-buildable transmitter (a **pulse-excited LED**, described by its own author as "a relatively weak torsion generator") and the design principle the card adopts: the transmitter run from a **12 V battery** so the two ends are "two absolutely independent systems".
- **The archive's own counterweight:** `translations/2026-10-09-radionica-skepsis-museum-nl.md` — the Dutch skeptical encyclopedia's entry on radionics, which names the lineage's origin (Albert Abrams) and the standing objection ("what does not exist does not harm, yet we heal with what does not exist"); and `translations/2026-10-09-does-water-have-memory-provereno-media-factcheck-ru.md` — a Russian fact-check of the water-memory claim. Both are cited because the card's honesty depends on them.
- **Track rule:** the archive's own standard (see `sources/emf-biology/README.md`) — *"Record claims as claims … The negative half is required."* The card obeys it: the counterweight is cited in the card itself.
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-09-dossier-077-two-household-blind-transfer.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "torsion field", "non-local", "radiesthesia", "water memory", "biolocation"
- **Aetherforce Reference:** search "torsion", "non-local", "scalar", or "radionics" on https://www.aetherforce.energy

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — a named apparatus (a claimed non-local transmitter, a water sample, a pH measurement) with a named procedure (pre-register N modes, run blinded trials, score against chance) and a measurable outcome (blind mode-identification accuracy against the 1/N baseline, and pH per trial). Not pure theory. |
| **Replicable** | YES — home, ~$20–60 (a pH meter or litmus paper, water, and a transmitter built from an LED, a resistor and a battery). The one requirement a single household cannot meet is the **second household** — which is the point of the card. No mains work; the transmitter runs from its own battery. |
| **Relevant** | YES — Community domain: the **neighbourhood replication node** the community guild's complement names. It maps to the **Witness** villager role too — the household that measures blind and records honestly. |
| **Honest** | YES — framed as a TEST, not an endorsement. The card states plainly that the primary source is a society's minutes with no trial count and no chance model, that the convergence source is a practitioner's own page, that no mechanism is proposed, and that the **expected result is the null**. It cites the archive's own counterweight, makes **no health claim**, and labels the claim as extraordinary. Clean FAIL, VOID and ARTIFACT paths. |
| **Linked** | YES — the two source translations (with the load-bearing passages quoted), the archive's own counterweight, a pre-registered replication dossier, and the Vault + Aetherforce search pointers. |

**Mirror choice, stated:** the card's **domain is community** (the rotation's next field), and its **guild complement is Community** — whose complement in the mirror map is *"Distributed labs / Uber-for-labs — neighborhood replication nodes."* This card **is** that complement: it cannot be run by one household. The alternative domain (water) would have made it a third water-transfer card and missed the design's actual subject, which is the **two-household structure** rather than the water.

**Overlap, stated not hidden:** this card is in the same broad family as **dossier 067 (Water-to-Water Information Transfer Test)** — both test a non-contact transfer into water. They differ in structure (one room vs two households), discriminator (direction vs blind mode identification), endpoint (dried-drop pattern vs pH), and what they isolate (the sender's state vs the distance and independence of the two ends). The engine permits multiple cards per family; the overlap is recorded rather than concealed.

---

## What makes it the queue's first of its kind

- **The first card whose two ends are a sender and a receiver in separate households with independent power** — every prior transfer or dowsing card runs both ends under one roof. This is the first that makes the distance and the independence of the two ends part of the design, and the first the source itself designed that way (the transmitter on a battery so the signal cannot travel the mains).
- **The first card whose discriminator is a blind mode identification** — the receiver must **name which of N modes** the sender is running, scored against a 1/N chance baseline, rather than compare two arms.
- **The first card that tests a distance claim as a distance claim** — the separation is a stated, recorded number between two addresses, not a bench gap.
- **The first card that is itself the neighbourhood replication node** — the community guild's own complement. It needs two households by construction, and the protocol is the thing they share.

---

## The honest framing (the spine of the card)

The card tests a claim, not a tradition. The torsion/radiesthesia lineage is not being asked to prove anything — it is being asked what it says the transmitter does, and the one part of that answer two families can establish is whether a blind receiver's reading tracks the sender's mode.

Three things the card keeps in front of the family:

1. **The claim is extraordinary and the sources are weak.** The primary source is a research society's minutes with no trial count and no chance model; the convergence source is a practitioner's own page whose author himself concedes a skeptic might call it coincidence. The card says so before the family starts.
2. **The hard endpoint is the blind identification, and the pH is the secondary record.** "Did the receiver name the right mode more often than chance, and did it repeat" is countable and pre-registerable. The pH table is the corroborating record. The card keeps them separate.
3. **A null is a complete result.** A receiver at chance means a claim that has circulated for decades without a blind trial has been tested by two families with a battery, an LED and a strip of litmus paper — a real, useful finding (Skeptic's Star), not a failed experiment.

**Under-promise, stated plainly:** the likely outcome is that the receiver's guesses land at chance and the pH readings drift without tracking the sender's mode. That is the honest verdict, and the card is designed to reach it cleanly.

---

## Safety and rights notes

- **Safety: none.** Battery-powered transmitter only; no mains work, no chemicals, no electrical hazard. The one caution is the ordinary one: do not short the battery, and keep the pH meter's probe clean between readings.
- **Rights posture:** the source translations are **our own** (P2 — publishable). The underlying SRCAA minutes and the scalarwave.cc page are third-party works and are **cited and linked** with only short attributed quotations. Any harvested media transcript is **P0 — never publish**.
