---
name: Blind Water-Line Location Test
description: "Test whether a sensitive person can locate a buried flowing-water line and name its flow direction, blind — against ground truth (the hose's real position), a non-dowser control operator, and a 50% chance baseline. Community/shared-infra card; ~$20–40; Earthworks mirror."
---

# ⚡ Aetherforce — Earthworks

**Guild:** Aetherforce — Earthworks
**Quest Line:** ⚡ Aetherforce · Earthworks complement
**Tier:** sand
**Domain:** community (shared-infra knowledge — siting a shared well / water line)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-23-blind-water-line-location` · authored_at `2026-09-23` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Earthworks",
  desc: "Before a community digs a shared well, someone has to say where the water is. The dowsing tradition says a sensitive person can find the line and even tell which way the water runs. Bury a garden hose in a zigzag, have a referee flip a coin to decide which end the water enters from, and walk it blind. Mark where you think the line is; say which way the water flows before the coin is revealed. A second person who claims no skill walks the same field as the control. You get a number against ground truth — and either way, you learn what the claim is worth at home scale. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Blind Water-Line Location Test",
    "Lay a 15–30 m garden hose in a gentle zigzag, cover it with soil or a board, and record the true path with stakes you then hide. A referee flips a coin to decide which end the water enters from, connects it out of sight, and starts the flow. You walk the field with rods and mark at least five points where you think the line runs — each measured as a perpendicular distance from the true line — then state the flow direction in writing before the coin is revealed. Run 20 direction trials, 10 static (water off) trials you are not told about, and have a non-dowser run the same direction trials as the control. Measurable outcome: blind direction hit rate over 20 trials against a 50% chance baseline (binomial), your median location error in metres versus the control operator's, and your false-positive rate on the static trials. Target: >=15/20 direction hits at p<0.05 AND median location error <1.0 m and at least half the control's AND <=2/10 static false positives, repeated in a second session — or an honest refutation at home scale.",
    ["Science", "Observation", "Community"],
    "💧"
  ],
  source_doc: "sources/2026-09-21-scout-b-langs-1#entries-1-3 (Balck artificial water veins; Stängle 1972 scintillation measurements) + sources/2026-09-22-scout-a-langs-2#find-11 (UCR field record)",
  source_url: "https://www.biosensor-physik.de/biosensor/tallin-2018-lecture-english-low.pdf",
  dossier: "living-library/synthesis/replication/2026-09-23-dossier-035-blind-water-line-location.md",
  pass_fail: "PASS: blind direction hit rate >=15/20 (binomial p<0.05 one-tailed, chance 0.5) AND operator median location error <1.0 m and at least half the control operator's error AND static-trial false positives <=2/10, and the direction result repeats in a second session. FAIL: operator median location error at or above the control operator's AND blind direction hit rate within chance (7-13/20, p>0.05) - an honest negative (Skeptic's Star). INCONCLUSIVE: the operator cannot produce a signal even on the visible hose with water running (the blind arms are then uninformative, NOT a refutation), the key was opened before the final tally, the hose was visible or the flow audible, N was not pre-registered, or static false positives exceed 20%.",
  evidence: "Photo of the pre-registration sheet (trial counts, thresholds, chance model, scoring rule, key-holder) + the true hose path as recorded before the trials + the sealed key photographed sealed + the operator's five marked points with the referee's perpendicular-distance measurements + the written direction call for every trial, timestamped before unblinding + the control operator's results reported separately + the static-trial results reported separately + the full tally with the binomial calculation shown + the second-session repeat"
}
```

---

## Source Documentation

- **Primary (the protocol):** Friedrich H. Balck, *"Experimental Approach to Water Veins"*, Earth's Fields 2018 conference, Tallinn — https://www.biosensor-physik.de/biosensor/tallin-2018-lecture-english-low.pdf (**fetched and read 2026-09-23**). Balck reports artificial water veins from a half-inch garden hose: **six parallel zones** (L3 L2 L1 / R1 R2 R3) whose distance from the hose depends on water velocity, **concentric rings and vortex cells** around a bend, and the claim that **dowsers distinguish left from right with matter in motion**. His summary claim is the widest one: *"Flowing water, moving air, electrical current and light have similar zones."*
- **Primary (the instrumented follow-up):** Peter Käser, *"Brunnensuche, Krankheiten und die Messungen des Rutenmeisters Jakob Stängle 1972 in Vilsbiburg"* — https://www.museum-vilsbiburg.de/fileadmin/user_upload/dateien/Texte/3_Pohl_Arlan.pdf (**fetched and read 2026-09-23**). In October 1972 Stängle walked three water veins mapped by von Pohl in 1929 with a **scintillation counter and chart recorder** and reported **more than double the background radiation intensity inside the mapped vein boundaries** versus the surrounding ground. Wüst had reported elevated gamma over geopathic zones in 1956.
- **Primary (the field record):** Mario Enrique Arias Salguero, *"El arte del Zahorí, las creencias del Rabdomante y la sensibilidad del Radiestesista en la búsqueda del agua subterránea"*, Universidad de Costa Rica, 2020 — https://hdl.handle.net/10669/90757 (**fetched and read 2026-09-23**). Documents the two schools (physical / mental), the standard instruments, the training exercises (coded envelopes; "7 of 10 correct" as the sensitivity threshold), the **flow-direction method** (walk the line both ways; the pendulum turns faster with the flow), and **Hans Dieter Betz's Munich GTZ program** pairing dowsers with vertical electrical soundings in Africa and Asia.
- **Scout entries:** `sources/2026-09-21-scout-b-langs-1.md` (finds 1–3) and `sources/2026-09-22-scout-a-langs-2.md` (find 11).
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-23-dossier-035-blind-water-line-location.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "radiesthesia", "water veins", "dowsing"
- **Aetherforce Reference:** Search "radiesthesia", "water veins", or "geobiology" on https://www.aetherforce.energy
- **Related dossiers:** 005 (Blind Geopathic Mapping — map-vs-map, no ground truth), 029 (Psi-Track Dowsing — a *mental* target), 034 (Neutral Pendulum — a tuned instrument on a known physical property), 021 (Earth-Energy Grid Instrument Scan — the other instrument-over-ground card)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (a buried hose, rods, a coin, a tape measure) with a named procedure (lay, blind, mark, call, unblind) and two measurable outcomes (blind direction hit rate against a computed 50% baseline; median location error in metres against ground truth and against a control operator). Not pure theory. |
| **Replicable** | YES — Home, sand-cheap: ~$20–40 for a hose, stakes, tape, and rods. No mains work, no chemicals, no purchased instrument (the optional Geiger arm is not required for pass/fail). One afternoon plus one repeat. |
| **Relevant** | YES — Community domain: siting a shared well or water line is the classic village-scale shared-infrastructure decision, and the method is a shared, teachable, mutual-aid skill. Complements the Earthworks guild (measuring what is underground). |
| **Honest** | YES — Claim framed as contested and pseudoscientific; the mechanism (a "subtle matter") is unfalsifiable and the card tests only the effect; the sources are proponent documents, not neutral ones; the Stängle result is a single interested-party measurement; and the card states plainly that **a hose is not a vein** — a pass shows detection of flowing water in a hose, not aquifer location, depth, or yield. Clean FAIL path. |
| **Linked** | YES — Three source docs (two scout entries + three primary URLs, all fetched and verified live this run), a pre-registered replication dossier, and cross-links to the four related cards. |

**Mirror choice, stated:** the card's **domain is community** (the rotation's next field), but its **guild complement is Earthworks** — the measurement is of an underground structure, the same object class as the Earthworks guild's earth-energy grid scan, and Earthworks is the emptiest relevant mirror (1 card). Stacking a third card on the Community mirror would over-weight one complement.

---

## The honest framing (the spine of the card)

- **The mechanism is unfalsifiable; the effect is not.** "Subtle matter" cannot be measured by any instrument the sources can name. What *can* be measured is whether a blind operator beats chance and beats a control operator. The card tests only that.
- **The sources are proponents, not neutrals.** Balck is a committed geobiology researcher; the Stängle material is a museum archive piece written by an admirer; the UCR document is a geophysicist's survey of a practice whose author states plainly that no comparative technical studies exist. None is a blinded trial.
- **The hose is not a water vein.** No aquifer, no rock strata, no depth, no yield. A pass means *this operator detected a buried flowing hose better than chance on this field, this day*. It does not mean anyone can find water for a well.
- **The control operator is the design, not an extra.** Without a non-dowser running the same trials, a "hit rate" cannot be distinguished from a rig that leaks the answer — a wet patch, a hum, a vibration.
- **A null is the likely outcome and is a complete result.** The engine's rule holds: a weak card is worse than none, and an honest negative earns the Skeptic's Star.
- **Never substitute this for a real survey.** A dowsing protocol is not a hydrogeological survey and not a substitute for a licensed driller.
