---
name: Quest Card — Egely Wheel Vital-Force Test
description: "Aetherforce-branded quest card for the queue's first vital-force-instrument test: a light rotor on a low-friction bearing is said to spin when a person holds a hand near it, and the spin rate (the 'VQ' vitality quotient) is said to read the person's state of health and fitness. The device is a commercial product (Egely, 1994–present) with a patent (WO910870); the manufacturer ran his own heat and wind controls and the Hungarian Skeptic Society holds a replication protocol (heated iron spins it, an airflow-blocking plate stops it). This card builds the wheel and runs the matched-distance thermal control and the airflow-blocked control the two sides disagree about. Natural Medicine mirror (vital-force measurement), health domain."
---

# ⚡ Aetherforce — Natural Medicine

**Guild:** Aetherforce — Natural Medicine
**Quest Line:** ⚡ Aetherforce · Natural Medicine complement
**Tier:** sand
**Domain:** health (vital-force instrumentation — does a person's hand spin a wheel, and does the spin rate read their state of health?)
**Status:** proposed
**Created:** 2026-09-28

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-28-egely-wheel-vital-force` · authored_at `2026-09-28` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Natural Medicine",
  desc: "A Hungarian engineer built a wheel that spins on a needle point, so light it coasts on almost nothing, and claimed that holding your hand near it makes it turn — and that how fast it turns reads how alive you are. He called the number a vitality quotient, calibrated it against a thousand people, and reported that sick people could barely move it while fit ones spun it fast. He also knew what you are already thinking: a warm hand carries heat and air. So he wore gloves, built glass boxes to kill the drafts, and set warm metal tanks shaped like hands beside the wheel. The warm tanks, he said, managed only a tenth of what a man could do. A skeptic society in Budapest built the same wheel and reported the opposite: a heated iron spins it with nobody there, and a plate that blocks the airflow stops it. Both sides ran controls. They disagree about what the controls show. That is the experiment. Build the wheel, run the hand, then run a hand-shaped cup of body-temperature water at exactly the same distance, then run the hand again with a clear plate blocking the air. If the hand beats the warm cup and survives the blocked air, the claim lives. If not, you have measured heat and draft — and you will know exactly what a vitality meter is worth. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Egely Wheel Vital-Force Test",
    "Build a light rotor on the lowest-friction bearing you can make: a flat non-ferromagnetic disc of 0.3–0.8 g (thin card, balsa, or cut aluminium) with a marking on the edge for counting turns, balanced on a sewing-needle point (or a magnetic bearing). Verify it coasts — record how long it takes to stop on its own; if it stops in under a second, friction is too high and nothing can be measured. Then run four arms in randomized order, same distance and height, in a still room: A, your open hand at a recorded distance (not touching); B, a hand-shaped vessel of water held at 37–40 °C at the same distance and height (the heat control); C, your hand at the same distance with a clear plate between hand and wheel blocking the airflow (the air control); D, nothing (baseline). Count turns per minute for each, log room and object temperature, and repeat on at least 3 separate days with at least 2 operators. Measurable outcome: turns per minute per arm, and whether the hand (A) exceeds the warm cup (B) and the airflow-blocked hand (C) repeatably. PASS: A beats B and C in >= 2 of 3 sessions and across >= 2 operators — the claim survives both its heat control and its air control. FAIL: the warm cup matches or beats the hand, or the airflow block removes the spin — a complete result (Skeptic's Star): the archive's own skeptic protocol is confirmed at home and the 'vitality' reading is a heat/airflow reading. ARTIFACT: the spin tracks the temperature difference rather than the object's identity, or follows drafts, breathing or the operator's expectation. Then blind it once: have someone else set either the warm cup or the hand without telling you, and see whether the reading can tell them apart.",
    ["Science", "Biology", "Measurement"],
    "🎡"
  ],
  source_doc: "sources/2026-09-27-scout-b-langs-1.md#find-4 (scout find: 'Egely Kutató-Fejlesztő Kft. — Egely Wheel manufacturer primary source', egely.hu; practical_applicability buildable — 'the device is trivially buildable (bearing-mounted light wheel) and the skeptic replication protocol (see find 5) makes it a cheap, fully-testable vital-force claim — exactly the library's T2 class') + #find-5 (scout find: 'Härtlein Károly — Merő vitalitás', Hungarian Skeptic Society, BME — 'the wheel turns under a heated iron (no vitality required), stops under an airflow-blocking plate')",
  source_url: "https://egely.hu/vitalitasmero/",
  dossier: "living-library/synthesis/replication/2026-09-28-dossier-051-egely-wheel-vital-force.md",
  pass_fail: "PASS: the hand (A) produces a repeatable spin that is absent in the baseline (D), larger than the matched warm object (B), and larger than the airflow-blocked hand (C), reproduced in >= 2 of 3 sessions and across >= 2 operators - the claim survives both its heat control and its air control. FAIL: no repeatable difference between arms, or the hand's spin is matched or exceeded by the warm object (B) and/or removed by the airflow block (C) - a null, a complete result (Skeptic's Star). INCONCLUSIVE: bearing friction too high to coast; distance or height not matched between arms; arm order not randomized; fewer than 3 sessions or fewer than 2 operators; room not draft-free. ARTIFACT: the spin tracks the temperature difference between hand/object and room rather than the object's identity; the spin follows air currents (hand movement, breathing, door drafts); the spin follows the operator's expectation (unblinded); the reading tracks the meter's warm-up or the room's thermal drift.",
  evidence: "Photo of the built rotor, bearing and stand with a ruler + the free-spin decay time + the pre-registration sheet (arm order, distance, duration, thresholds) photographed before the first trial + the full turns-per-minute log for all four arms across all sessions with the temperature column + the operator identities (>= 2) + the blind trial result + the void/artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the archive finds):** `living-library/sources/2026-09-27-scout-b-langs-1.md`, **§ Hungarian, find 4** — *"Egely Kutató-Fejlesztő Kft. — Egely Wheel manufacturer primary source"*, https://egely.hu/vitalitasmero/ (product) · https://egely.hu/oneletrajz/ (autobiography) — Hungarian, Hungary (Budapest region), work type **prototype (commercial device, 1994–present)**. Scout flag: `Practical Applicability: flag — fields: buildable, reproducible; note: the device is trivially buildable (bearing-mounted light wheel) and the skeptic replication protocol (see find 5) makes it a cheap, fully-testable vital-force claim — exactly the library's T2 class`. Scout verification: `search-result verified (manufacturer pages retrieved)`.
- **Primary (the counter-claim):** same file, **find 5** — *"Härtlein Károly — 'Merő vitalitás'"*, Hungarian Skeptic Society (BME), http://szkeptikus.bme.hu/borsohanyo/vitalitas.pdf — Hungary (Budapest, BME skeptic society), work type **experimental (replication/debunk)**. Scout flag: `flag — fields: reproducible, verified; note: this is the experimental protocol that makes the Egely claim testable — a ready-made T1/T2 pairing`. Content: *"the wheel turns under a heated iron (no vitality required), stops under an airflow-blocking plate, and Iván Gábor's repeatable-experiment study is cited as the systematic refutation."*
- **Primary URL (manufacturer) — the inventor's own account.** Egely's *"The Story of the Egely Wheel (Vitality Meter)"* (Budakeszi, 1994) states the claim and reports his own controls: gloves to exclude heat, glass boxes to exclude wind, and hand-shaped metal tanks filled with warm water (up to 113 °F) that produced *"at most 10% of the good results with men."*
- **Archive mirror (fetched and verified 2026-09-28):** https://www.rexresearch.com/egely/egely.htm — Rex Research carries the same account plus the abstract of patent **WO910870**, *"Apparatus and method for detecting effects indicating physical state of health and fitness"*: *"a rotor (3) arranged rotatably on a frame (11), of the mass of 0.1 and 2.0 g, more accurately 0.3 to 0.8 g, with at least one marking (19) on the edge being suitable for reading number of turns, wherein magnetic permeability is less than 50, furtheron optionally the rotor (3) and the frame (11) are connected to each other by a spring means."* The patent gives the buildable spec the card uses.
- **The VQ scale, in the source's terms:** a 0–400% vitality quotient calibrated against **1,000+ measured persons**, average adult baseline **9 rpm**; the inventor reports Ernő Rubik's best at **35 rpm ≈ VQ 600%**. KERMI 1994 licensing is noted by the scout.
- **Database mirror:** `living-library/database/research/research-index.json` → `works/egely-wheel` (*Egely-kerék / Egely Wheel Vitality Meter*); `database/research/practical-applications.json` → `works/egely-wheel`; `database/persons/person-index.json` → `persons/György Egely` (`egely-g`, Egely Kutató-Fejlesztő Kft.); `database/entities/researcher-index.json` → `Gyoergy Egely` / `Gyorgy Egely` (Rex Research sources).
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-28-dossier-051-egely-wheel-vital-force.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "Egely", "vitality meter", "bioenergy", "radiesthesia"
- **Aetherforce Reference:** search "vitality" / "bioenergy" / "Egely" on https://www.aetherforce.energy
- **Related cards:** 034 (Neutral Pendulum Discrimination — the *blinding*-controlled subtle-energy measurement; this card is its *physical-control* counterpart), 045 (Palm Thermal Control — the practitioner's own body as the object, with a temperature readout), 041 (Spin-Weight Anomaly — a card that carries an already-refuted claim honestly)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — a named apparatus with a buildable spec (patent WO910870: a non-ferromagnetic rotor of 0.3–0.8 g with an edge marking, on a low-friction bearing) and a measurable outcome (**turns per minute per arm, and whether the hand exceeds the matched warm object and the airflow-blocked hand**). Not pure theory. |
| **Replicable** | YES — Home, sand: **under $50** (rotor ~$1, bearing/needle ~$1, stand ~$5, a hand-shaped warm-water vessel ~$5, a clear baffle ~$3, stopwatch/thermometer ~$10). No chemicals, no heat above hand-warm, no mains wiring. The demanding requirement is **discipline** (matched distance, randomized arms, draft-free room, ≥2 operators). |
| **Relevant** | YES — Health domain, squarely: the claim is that a reading of a person's **general state of health and fitness** can be taken from a spinning wheel. It is also the queue's **first card whose control is a thermal/convective physical mechanism** for a bioenergy claim — the first to separate "the person" from "the person's heat and air." |
| **Honest** | YES — the claim is framed as a claim and the card is a test, not an endorsement. Four things are stated in advance: the source says the mechanism is **unknown**; the archive holds a **documented skeptic replication** (heated iron, airflow plate); the leading physical explanation is **thermal convection and air currents**, which the card makes separable; and the FAIL path is a complete result (Skeptic's Star). |
| **Linked** | YES — two scout finds (claim + counter-claim), the manufacturer primary source, the Rex Research archive mirror with the patent abstract, four database index entries, a pre-registered replication dossier, and cross-links to three related cards. |

**Mirror choice, stated:** the claim is that a **person's own vital state** is read from a device, so **Natural Medicine** ("Health / human physiology") is the honest complement and the family label is `Aetherforce — Natural Medicine`. This is the mirror's **eighth** card, and the pairing is deliberate: **034 (Neutral Pendulum) controls by hiding the target; 051 controls by replacing the hand with a warm object and blocking the air.** Together they are the two ways to test a bioenergy claim. **Oddball** ("odd instruments") was the closest alternative and was not chosen because the *claim* is health (measuring vitality), not the instrument's oddness; the device is the means, the health reading is the subject.

---

## The honest framing (the spine of the card)

**Both sides ran controls, and they disagree about what the controls show.** This is the rare card where the archive already holds the claim *and* its refutation, in one language, from the same decade. The manufacturer (find 4) reports a commercial device, a patent, a 1,000-person calibration, and his own heat/wind controls — gloves, glass boxes, warm hand-shaped tanks — and says the effect is not heat or wind. The Hungarian Skeptic Society (find 5) reports the opposite: a heated iron spins the wheel with nobody there, and an airflow-blocking plate stops it. **The card runs the experiment the disagreement is actually about** — the matched warm object and the airflow block — at home.

**The leading explanation is physical, and the card says so up front.** A hand near a light rotor on a near-frictionless bearing supplies **thermal convection** (a warm object drives an air plume) and **air currents** (a hand is a moving object). Egely knew this and tried to exclude it; the skeptics say the exclusions do not hold. The card makes the alternatives separable and pre-registered, and its honest expectation is that a hand-shaped warm object at the same distance will spin the wheel.

**A control for "the person" is not a control for "the person's heat."** This is the card's transferable lesson, and it is the same error class the fleet keeps finding: *the instrument answers the question it was built around, and that was a different question.* A card that only compared "hand" to "no hand" would answer *"is anything there?"* — it could not answer *"is it the person?"* The warm object and the airflow block are what turn a demonstration into a test.

**The friction is the instrument's honesty.** A rotor that stops in under a second cannot measure a hand's influence at all — it measures its own bearing. The card requires a **recorded free-spin decay time** before any trial, because a high-friction wheel would manufacture a null (or a noise-shaped reading), and a card that cannot say what its instrument was doing is not a test.

**Under-promise:** the most likely outcome is that the warm object matches the hand and the airflow block removes the spin — which would confirm the skeptic protocol at home and file a real finding about the archive's own holdings. A hand that beats the warm object *and* survives the blocked air would be genuinely surprising and would justify a harder follow-up. The card is written so that either outcome is a complete result.
