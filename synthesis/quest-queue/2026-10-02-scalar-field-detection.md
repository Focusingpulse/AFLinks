---
name: Scalar Electromagnetic Field Detection Test
description: "Test whether an oscillating charged sphere produces a scalar (monopole) electromagnetic field — the field Tesla said his instruments radiated, and which Maxwell–Lorentz electrodynamics says cannot exist — by looking for the source's own signature: an anomalous rotation of a brass ring suspended in the sphere's equatorial plane. Energy card; homelab, ~$150–400; Power mirror (Electricity complement). The queue's first card on the scalar / monopole field, and its first whose discriminator is a material-swap control."
---

# ⚡ Aetherforce — Power

**Guild:** Aetherforce — Power (complements Electricity)
**Quest Line:** ⚡ Aetherforce · Electricity complement
**Tier:** straw
**Domain:** energy (a claimed monopole / scalar electromagnetic field — Tesla's "non-Hertzian" radiation)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-02-scalar-field-detection` · authored_at `2026-10-02` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Power",
  desc: "Tesla was asked what field his instruments radiated and received. He said: not Hertzian electromagnetic waves. A century later the claim is still untested at home — that a charged sphere whose charge oscillates radiates a scalar (monopole) field that Maxwell–Lorentz electrodynamics says cannot exist. This card builds the source's own apparatus and looks for its own signature: a brass ring, hung in the sphere's equatorial plane, that rotates when the sphere is driven. The trap is that a 5000-volt sphere makes corona, and corona makes ion wind, and ion wind pushes a light ring. So the card hangs a second ring — same size, same weight, not metal — and screens a third run behind a grounded mesh. If the brass ring rotates and the plastic one does not, something is there. If they both rotate, you have measured the wind. Either way you have an answer, and the source never had one. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Scalar Electromagnetic Field Detection Test",
    "Build the source's apparatus — a Tesla transformer (6-turn 5 mm aluminium primary, 1500-turn 0.35 mm copper secondary on a 50 mm polyethylene tube) driven at ~10 MHz by a Brovin generator to ~5000 V, feeding a metal sphere on an insulating stand. Suspend a thin brass ring by a nylon thread in the sphere's equatorial plane, free to rotate. Then run four pre-registered arms, 60 s each, three times in randomised order: (A) driven sphere + brass ring; (B) driven sphere + a MATCHED INSULATING ring of the same size and mass; (C) static (undriven) charged sphere + brass ring; (D) driven sphere + brass ring with a grounded fine mesh between them. Measurable outcome: the ring's angular displacement in degrees per 60 s for each arm. If the brass ring rotates and the plastic one does not, and the grounded mesh does not stop it, you have a conductor-specific, non-shieldable, oscillation-dependent torque — the source's claim, and a genuinely anomalous result needing independent replication. If both rings rotate, the effect is ion wind and the scalar-field reading is refuted — the expected result, and a complete one. Adult-only; ~5000 V at 10 MHz.",
    ["Science", "Physics", "Measurement"],
    "🧲"
  ],
  source_doc: "translations/2026-10-02-fizicheskii-vakuum-torsionnye-polya-tesla-shipov-ru.md (G.I. Shipov, 'Physical Vacuum, Torsion Fields, Quantum Mechanics and the Experiments of N. Tesla', trinitas.ru) + sources/2026-10-02-scout-a-langs-1.md#find-4",
  source_url: "https://trinitas.ru/rus/doc/0231/008a/1081-sh.pdf",
  dossier: "living-library/synthesis/replication/2026-10-02-dossier-060-scalar-field-detection.md",
  pass_fail: "PASS (refutation — the expected result): the brass ring rotates in Arm A AND the matched insulating ring rotates comparably in Arm B, and/or the grounded mesh blocks it in Arm D — the rotation is ion wind / conventional EM, not a scalar field. PASS (anomaly — a surprising result): the brass ring rotates in Arm A, the matched insulating ring does NOT in Arm B, the grounded mesh does NOT block it in Arm D, and the static sphere does NOT rotate it in Arm C — a conductor-specific, non-shieldable, oscillation-dependent torque, as the source claims; requires a second independent replication. FAIL: the brass ring does not rotate in Arm A at all. INCONCLUSIVE: the ring was not free to rotate; the geometry (equatorial plane, distance) was not recorded; the secondary voltage was not confirmed; fewer than three repeats; the rotation was read without a fixed reference. ARTIFACT: the rotation tracks corona/ion wind (Arm B rotates); the ring swings from electrostatic attraction rather than rotating (Arm C rotates); the ring is moved by room air currents (sphere-off null run moves it); the reading tracks the spark rate rather than the field.",
  evidence: "Photo of the built transformer + sphere + suspended ring + the pre-registration sheet (four arms, 60 s interval, repeats, thresholds) + the confirmed secondary voltage + the ring geometry (equatorial plane, distance from sphere) + the angular-displacement table for all four arms across all repeats + the sphere-off null run + the repeat photographs + the void and artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the claim and the apparatus):** G.I. Shipov, *Физический вакуум, торсионные поля, квантовая механика и эксперименты Н. Тесла* (Physical Vacuum, Torsion Fields, Quantum Mechanics and the Experiments of N. Tesla) — https://trinitas.ru/rus/doc/0231/008a/1081-sh.pdf (**full English translation in the library and read this run**: `translations/2026-10-02-fizicheskii-vakuum-torsionnye-polya-tesla-shipov-ru.md`). §4 gives the apparatus in the source's own numbers — a **6-turn 5 mm aluminium primary**, a **1500-turn 0.35 mm copper secondary on a 50 mm polyethylene tube**, driven at **~17.5 V / ~10 MHz by a Brovin generator** to **~5000 V** at the secondary — and reports the result in one sentence: *"an anomalous — from the standpoint of Maxwell–Lorentz electrodynamics — rotation of a brass ring suspended in the plane of the equator of the sphere was discovered."*
- **The primary experiment (cited, not held):** Lobova M., Shipov G., Tawatchai Laosirihongthong, Supakit Chotigo, *Experimental Detection of a Scalar Electromagnetic Field*, 2008 — http://www.shipov.com/science.html. **Not in the Vault.** The card is honest that it is reconstructing a protocol from a secondary description, not reproducing a documented measurement.
- **Scout entry:** `sources/2026-10-02-scout-a-langs-1.md` — **find 4** (the Shipov Tesla paper; scout flag `practical_applicability: false [conceptual]`, note "presents no apparatus"). **This card departs from that flag deliberately and states why** (see below).
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-02-dossier-060-scalar-field-detection.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "scalar field", "monopole radiation", "Shipov", "Tesla non-Hertzian"
- **Aetherforce Reference:** Search "Tesla", "scalar", "monopole", or "radiant" on https://www.aetherforce.energy
- **Related dossiers:** 003 (Tesla Radiant Receiver — the *receiver* end of the same "energy in the field" thesis), 053 (Mini Tesla Coil Wireless Power Transfer — the same apparatus family, a *distance* claim), 030 (Chiappini Planetary Antenna — the same RF/field family), 036 (Sealed-Box Electrostatic Thrust — the queue's other adult-only lethal-voltage card), 041 (Spin-Weight Anomaly — the queue's other card on a claim already contested on physical grounds)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (a Tesla transformer with stated coil dimensions, a Brovin generator, a charged sphere, a suspended brass ring) with a named procedure (four pre-registered arms, 60 s each, three repeats) and a measurable outcome (the ring's angular displacement in degrees per 60 s, per arm). Not pure theory. |
| **Replicable** | YES — Homelab, ~$150–400: magnet wire, a plastic tube, aluminium wire, a Brovin-generator board, a metal sphere, two rings, thread, mesh, a multimeter, and a phone camera. **High-voltage and RF — adult-only, gated** (the same gate as cards 036 and 053). |
| **Relevant** | YES — Energy domain: the scalar / monopole field is the foundational claim of the Tesla/Aetherforce lineage, and every other energy card quietly assumes it. Fills the **Power** mirror (the Electricity complement). |
| **Honest** | YES — The claim is framed as a claim; the card names **ion wind as the central confound and the expected result**, and its discriminator is a material-swap control (brass vs matched insulating ring) plus a grounded-mesh arm and a static-sphere arm. Clean refutation path and a clean anomaly path. |
| **Linked** | YES — One primary source read this run (with the apparatus in numbers), one scout entry, a pre-registered replication dossier, a Vault search pointer, and cross-links to five related cards. |

**Mirror choice, stated:** the card's **domain is energy** (the rotation's next field) and its **guild complement is Power** — the Electricity mirror, whose theme is *Radiant / Tesla / LMD*, the exact lineage of this claim. **Oddball** ("cross-field bridges / suppressed-science re-try candidates", currently one card) was the closest alternative and was considered seriously, because a scalar field is a suppressed-science claim; it was not chosen because the card's subject is an **electrical** phenomenon — a field Tesla said his electrical instruments radiated — and the Electricity mirror is where the queue's other Tesla cards (003, 018, 053) already sit. The family label is `Aetherforce — Power`, the label every energy-domain card in this queue carries.

**Departure from the scout flag, stated:** the scout's 2026-10-02 flag on this paper reads `practical_applicability: false — fields [conceptual]; note: … presents no apparatus`. **The note is wrong about the full translation**, which gives the coil dimensions, the driver, the frequency, the secondary voltage, the sphere and the suspended ring. The scout appears to have read the trinitas HTML abstract (its `source_url` is the `.htm`; the translation is of the `.pdf`). The card departs from the flag on the apparatus point and says so here rather than hiding it. The scout's *spirit* — that the paper is theory-first — is correct, and the card is honest that the primary experiment is not in the Vault.

---

## The honest framing (the spine of the card)

**The claim is a claim.** The source asserts that a charged sphere whose charge oscillates radiates a **scalar (monopole) field** that Maxwell–Lorentz electrodynamics says cannot exist, and that this field was detected as an anomalous rotation of a suspended brass ring. **This card tests that claim; it does not endorse it.**

**The easy signatures are not the claim.** The source also offers two other signatures — a fluorescent lamp glowing in the field, and an oscilloscope probe with its **ends 5 cm apart** showing a voltage. **Both are textbook near-field coupling to a Tesla coil**, and a card built on either would prove nothing. The card is about the **ring rotation**, which is the only signature the source itself calls anomalous.

**The design that makes it a measurement.** Three things do the work:

1. **The material-swap control is the discriminator.** A brass ring rotating proves nothing — a 5 kV sphere makes **corona**, and corona makes **ion wind**, and ion wind pushes any light object. Hanging a **matched insulating ring** (same size, same mass) is what separates "an electromagnetic effect on a conductor" from "the wind moved it."
2. **The grounded mesh is the shield test.** If the rotation is conventional EM or ion wind, a grounded fine mesh between the sphere and the ring stops it. If it survives the mesh, it is not conventional.
3. **The static-sphere arm is the electrostatic test.** A charged sphere attracts a nearby conductor; if the ring swings rather than rotates, Arm C shows it.

**The likely result is ion wind, and that is a complete result.** If the brass ring rotates and the matched plastic ring rotates too, the honest verdict is *"the anomalous rotation is a mechanical corona-wind effect, not a scalar field"* — which retires the claim while leaving the apparatus standing, and is exactly the answer a family needs before spending on a "scalar energy" build.

**The central limitation, stated up front: the source's own result is one unreplicated sentence.** The 2008 paper is not in the Vault, gives no numbers, and reports no control. **The card is testing the phenomenon, not reproducing a documented measurement**, and a single session is a sample of one — repeat on a second day before concluding anything.

**Safety and honesty:** this is a **high-voltage, RF bench experiment — adult-only, and gated.** The secondary reaches **~5000 V at ~10 MHz**: a shock hazard, an RF-burn hazard, and an ozone/EMI source. **Never touch the secondary, the sphere, or the ring while powered. Discharge the sphere after every run. Keep it away from pacemakers, medical devices, radios, and children. Run it on an insulated bench with a marked kill switch.** It is a test, **not** a power source.

---

## Relationship to the rest of the queue

This card is the **foundation the queue's other Tesla cards assume**. Card 003 tests a *receiver* that draws power from the environment; card 053 tests whether a *transmitter's* field carries power across distance; card 018 tests a *turbine's* static-electricity conversion. **All of them presuppose that there is a field to receive from.** This card tests whether the field the source names — the scalar / monopole field, Tesla's "not Hertzian" radiation — exists at all, and it does so with the cheapest discriminator available: **a second ring, made of the wrong material.**

It is also the queue's **first card whose discriminator is a material-swap control** — and the **first card on the scalar / monopole field** of any kind.
