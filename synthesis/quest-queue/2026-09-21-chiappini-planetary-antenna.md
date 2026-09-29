---
name: Quest Card — Chiappini Planetary Antenna (D-Field VHF Antenna)
description: Aetherforce-branded quest card testing the D-field "Planetary Antenna" claim — that a 49 cm VHF antenna built from electric-displacement theory matches or beats a conventional reference antenna in the 2 m amateur band — via a home build with SWR and range endpoints. Electricity guild complement, energy domain.
---

# ⚡ Aetherforce — Chiappini Planetary Antenna

**Guild:** Aetherforce — Power (complements Electricity)
**Quest Line:** ⚡ Aetherforce · Electricity complement
**Tier:** sand
**Domain:** energy (radio / RF — off-grid communications)
**Status:** proposed
**Created:** 2026-09-21

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-21-chiappini-planetary-antenna` · authored_at `2026-09-21` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Power",
  desc: "An Argentine radio amateur asked a question his textbooks skipped: why does the teaching of radio propagation leave out the electric displacement field, the very term Maxwell needed to make his equations complete? Working it through, he found a set of geometric constants and bent a single 63 cm piece of wire into the wireframe of a tiny planet — four meridians and an equator — and mounted it on a coax connector. Total radiating length: 49 cm. He reports that this little 'Proton' antenna, 5 m up and running 1 W from a cheap handheld, reaches 25 km across a city — and he is unusually honest that he never published an SWR measurement, and tells you to take your own. That is the quest: build it, sweep it, and compare it head-to-head against a plain reference antenna on the same day, same power, same spots. If it holds up, you have a tiny, cheap, off-grid antenna and a genuine anomaly worth telling the world about. If it doesn't, you have retired a claim honestly and you now understand resonance, SWR, and polarization in your hands instead of on a page. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "The Proton Antenna",
    "Cut 63 cm of stiff messenger wire and mark it from one end: 10 cm for the connector, then 4.1 cm, 16.3 cm, 4.1 cm, then three × 8.2 cm. Bend the segments around a ~5.2 cm form into four meridians and an equator — a wireframe sphere — keeping the meridian planes perpendicular and each meridian advancing in the equator's direction. Solder on a PL259 with the south pole 8.3 mm from the connector, leaving ~1.5 cm of excess wire to trim in tenths of a millimeter while watching performance. Then measure: sweep SWR at 144.0, 145.0, 146.0, 147.0 and 148.0 MHz with a NanoVNA, in the final mounting position, and do the same for a reference antenna (the handheld's stock rubber-duck or a quarter-wave ground-plane). Finally, with a second station, transmit at 1 W on the same day from the same two locations and record the maximum distance each antenna stays intelligible, averaged over at least 3 runs. Measurable outcome: SWR below 2.0 across the band AND range equal to or better than the reference antenna, reproducing on a second build = the D-field design holds up on your bench; SWR above 2.0 in every position, or range clearly worse than the reference = the claim is retired honestly.",
    ["Science", "Engineering", "Self-Reliance"],
    "📡"
  ],
  source_doc: "translations/2026-09-18-planetary-antenna-d-field-chiappini-es.md — 'Antena Planetaria (Planetary Antenna),' Carlos Alejandro Chiappini's full construction guide and D-field theory appendix (viXra:2110.0093, 2021-10-17)",
  source_url: "https://www.aetherforce.energy",
  dossier: "living-library/synthesis/replication/2026-09-21-dossier-030-chiappini-planetary-antenna.md",
  pass_fail: "PASS: SWR < 2.0 across 144–148 MHz in the final mounting position AND range at 1 W equal to or greater than the reference antenna (same day, same locations, ≥ 3 runs) AND the result reproduces on a second build | FAIL: SWR ≥ 2.0 across the band in every mounting position (the author's own discard criterion), or range clearly worse than the reference, or the antenna cannot be tuned into the band — honest negative, Skeptic's Star | INCONCLUSIVE: SWR acceptable but range comparison not run (unlicensed, or no second station), fewer than 3 range runs, or build accuracy too poor to be a fair test",
  evidence: "Photos of the marked wire before bending and the finished 4-meridian + equator shape on the PL259; the antenna in its final mounting position with height and surroundings visible; NanoVNA or SWR-meter screen photos at each frequency for both the Planetary Antenna and the reference; the range log (date, time, power, frequency, both antennas, distance, intelligibility) for each run; a build-accuracy note recording how closely the measurements were held"
}
```

---

## Source Documentation

- **Primary source:** `translations/2026-09-18-planetary-antenna-d-field-chiappini-es.md` — a full ES→EN translation of Carlos Alejandro Chiappini's viXra preprint (viXra:2110.0093, 2021-10-17). It gives the full construction guide (wire marking, bending sequence, connector spacing, tuning), the reported performance (25 km at 1 W in the city; 10 km noise-free at 1 W), the author's explicit acknowledgement that no SWR data is included, and a theory appendix deriving the length series `s = λ/2π` and `s3 = λ/(2π)³ ≈ 8.278 mm` from the electric displacement field D⃗.
- **Origin URL:** https://vixra.org/pdf/2110.0093v1.pdf (verified live 2026-09-21: HTTP 200, 687,183 bytes)
- **Scout find:** `sources/2026-09-18-scout-a-langs-1.md` §6 — flagged `practical_applicability: true, fields [buildable, reproducible]`; noted "viXra preprint, single author, 0 citations — claims unverified; value is as a buildable experiment protocol, not validated theory."
- **Companion card (Tesla / radiant, Electricity mirror):** `synthesis/quest-queue/2026-09-08-tesla-radiant-receiver.md` (merged) — the other Electricity-mirror card; a power-reception claim rather than an antenna claim.
- **Companion card (load-bearing geometry):** `synthesis/quest-queue/2026-09-19-drbal-pyramid-blade-retention.md` (dossier 027, Metalworking) — another card where a specific geometry is the claim under test.
- **Replication Dossier:** `synthesis/replication/2026-09-21-dossier-030-chiappini-planetary-antenna.md`
- **Aetherforce Reference:** search "antenna" / "Tesla" / "radiant" / "radio" on https://www.aetherforce.energy
- **Vault link:** https://focusingpulse.github.io/AFLinks

---

## Rubric Justification

- **Practical:** named apparatus (a 49 cm wire antenna on a PL259) with a measurable outcome (SWR across 144–148 MHz; intelligible range at 1 W versus a reference antenna) and a specific construction guide.
- **Replicable:** home-scale (~$15–30 for wire, connector, and solder; the SWR meter / NanoVNA is the main instrument, ~$30–50). No lab equipment, no exotic materials. Transmitting requires an amateur license; the SWR/geometry half needs none.
- **Relevant:** maps to the Village **energy** survival domain (off-grid radio / RF) and complements the **Electricity** guild (radiant / Tesla / LMD — the Village's electromagnetism home).
- **Honest:** framed as a TEST of a single-author, unrefereed, uncited claim, not an endorsement. The author's own missing SWR data is stated up front; the quarter-wave confound is named; the author's own discard criterion (SWR ≥ 2) is adopted as the FAIL condition; a null is presented as an equally valuable outcome.
- **Linked:** source doc (translation + verified origin URL), dossier created with protocol + pass/fail, evidence protocol defined.

---

## Honest Framing

This is a test, not an endorsement. The Planetary Antenna comes from a single-author
viXra preprint with no peer review and no citations, and the author himself publishes
**no SWR data** — he asks the builder to measure it. His range figures (25 km at 1 W)
are one operator's anecdote, not a controlled comparison. There is also a real confound:
at 49 cm the radiating length is numerically almost exactly a quarter-wave in the 2 m
band, so a good SWR would show the antenna *works*, not that the D-field theory is
correct. The value of the card is that a family can build it in an afternoon, measure
it against a plain reference antenna, and get their own answer — including the honest
null. **Never transmit with SWR ≥ 2; test on receive first, and only transmit on the
amateur bands if licensed.**

---

## Status

**Proposed** — awaiting Chris approval before merge into Village quest data.
