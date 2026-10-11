---
name: Dossier 060 — Scalar Electromagnetic Field Detection Test
description: "Replication dossier for the scalar (monopole) electromagnetic field claim: an oscillating charged sphere radiates a scalar field S that Maxwell–Lorentz electrodynamics says it cannot, detectable as an anomalous rotation of a suspended brass ring in the sphere's equatorial plane. The card builds the source's own apparatus (a Tesla transformer driven by a Brovin generator, a charged sphere, a suspended brass ring) and tests whether the rotation is anomalous or explained by ion wind, static electrostatics, or eddy-current induction. Energy card; homelab, ~$150–400; Power mirror (Electricity complement)."
---

# Dossier 060 — The Scalar Electromagnetic Field Detection Test

**Status:** protocol
**Domain:** energy (a claimed monopole / scalar electromagnetic field — Tesla's "non-Hertzian" radiation)
**Tier:** straw (homelab, ~$150–400)
**Created:** 2026-10-02
**Source docs:**
- `living-library/translations/2026-10-02-fizicheskii-vakuum-torsionnye-polya-tesla-shipov-ru.md` — the **full English translation** of G.I. Shipov, *Физический вакуум, торсионные поля, квантовая механика и эксперименты Н. Тесла* (Physical Vacuum, Torsion Fields, Quantum Mechanics and the Experiments of N. Tesla). Source page: https://trinitas.ru/rus/doc/0231/008a/1081-sh.pdf — §4 ("Connection of the scalar electromagnetic field with Tesla's experiments") gives the apparatus and the claimed result.
- `living-library/sources/2026-10-02-scout-a-langs-1.md` — **find 4** (the Shipov Tesla paper; scout flag `practical_applicability: false [conceptual]`, note: "presents no apparatus"). **This card departs from that flag deliberately and states why below** — the scout's note is factually wrong about the full translation, which carries the apparatus with numbers.
- **The primary experiment (cited by the source, not held in the archive):** Lobova M., Shipov G., Tawatchai Laosirihongthong, Supakit Chotigo, *Experimental Detection of a Scalar Electromagnetic Field*, 2008 — http://www.shipov.com/science.html. The translation reports its result in one sentence; the paper itself is not in the Vault.

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-02-scalar-field-detection` · authored_at `2026-10-02` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The claim (as asserted by the source)

The source's own framing, translated:

> "Equations (21) and (22) do not follow from the equations of Maxwell–Lorentz electrodynamics, since in the latter the law of conservation of charge is satisfied and **monopole radiation is absent**. Therefore, for an experimental investigation of equations (21) and (22), it is necessary to create physical conditions in which the continuity equation (1) is not satisfied, i.e. monopole radiation of charge exists. In the macroworld this can be done not for a single charge but for a system of charges. Indeed, suppose we have a charged sphere … and let the charge of the sphere be +Q. If the switch k is closed, the charge of the sphere will change and, as a result … a **scalar electromagnetic field S = (1/rc)·∂Q(t)/∂t** will appear outside the sphere."

> "Preliminary experiments on the detection of the scalar electromagnetic field were carried out in the work [7]. As a result of the experiments, **an anomalous — from the standpoint of Maxwell–Lorentz electrodynamics — rotation of a brass ring suspended in the plane of the equator of the sphere was discovered.**"

The apparatus, in the source's own numbers:

> "a Tesla transformer consisting of a primary coil of thick (d = 5 mm) aluminium wire (6 turns) and a secondary coil formed by **1500 turns of copper wire (d = 0.35 mm) wound on a polyethylene tube (d = 50 mm)**. Pulses with an amplitude **V = 17.5 volts at a frequency of the order of 10 MHz from a Brovin generator** were fed to the primary winding … In the secondary winding (owing to the resonant properties of the system) we obtained a **sinusoidal voltage with an amplitude of 5000 volts**."

The source offers three signatures of the claimed field: (a) a fluorescent lamp glows in the field; (b) an oscilloscope probe with its **ends separated by 5 cm** shows a voltage (current in an open circuit); (c) **the brass ring rotates**. **Only (c) is anomalous** — (a) and (b) are textbook near-field capacitive/inductive coupling to a Tesla coil, which the source itself concedes is "impossible to explain … by the ordinary displacement current" only by assertion, not by measurement.

**What is being tested, in one sentence:** does a suspended brass ring in the equatorial plane of an oscillating charged sphere rotate, and if it does, is the rotation explained by **ion wind**, **static electrostatics**, or **eddy-current induction** — or does it survive the controls and stand as an anomaly?

## Honest status of the claim

**The archive holds the claim and no home test of it.** A grep for `scalar electromagnetic`, `monopole radiation`, `Brovin`, and `kacher` across `living-library/synthesis/` returns no card and no dossier. The queue's nearest energy cards test a **radiant-energy receiver** (003), **wireless power transfer** (053), a **planetary RF antenna** (030), and a **motor's matched-load efficiency** (047) — **none tests whether a scalar/monopole field exists at all.** The claim is the *foundation* of the whole Tesla/Aetherforce lineage (Tesla's own answer to "what field do your instruments radiate?" was that they are "not Hertzian electromagnetic waves"), and it has never been tested at home scale in this queue.

Three things the card must say out loud, because they are what a family is actually testing:

1. **The expected result is a refutation, and that is a complete result.** A 5 kV sphere at 10 MHz produces **corona**, and corona produces **ion wind** — a real, well-documented mechanical force that will push a light suspended object. The most likely outcome is that the brass ring rotates *because of ion wind*, and that the matched insulating ring rotates too. The card is designed so that this outcome is scored as a clean refutation of the scalar-field reading, not as a failure.
2. **The discriminator is the control arms, not the rotation.** A ring that rotates proves nothing on its own. What separates "anomalous scalar field" from "ion wind" is whether a **matched insulating ring** rotates as much (mechanical), whether a **static charged sphere** rotates it (static electrostatics), and whether a **grounded mesh** between sphere and ring blocks it (conventional EM / ion wind).
3. **The source's own concession.** The paper offers no chance baseline, no shielding control, no ion-wind control, and reports the ring result in a single sentence with no numbers. **The card supplies the controls the source lacked** — which is the whole point of a replication dossier.

**Under-promise, stated plainly:** the likely outcome is that the rotation is ion wind, and the honest verdict is *"the anomalous rotation is a mechanical corona-wind effect, not a scalar field."* A rotation that survives the grounded mesh **and** is absent on the matched insulating ring would be genuinely anomalous and would require independent replication before any conclusion.

## Why it matters

- It is the queue's **first card on the scalar / monopole electromagnetic field** — the foundational claim of the Tesla/Aetherforce lineage, and the one claim every other energy card quietly assumes.
- It is the queue's **first card whose discriminator is a material-swap control** (brass ring vs matched insulating ring) — the cheapest way to separate an electromagnetic effect from a mechanical one.
- It teaches the transferable lesson: **a claimed field that "cannot be shielded" is tested by shielding it; a claimed force on a conductor is tested by removing the conductor.**
- It is genuinely **homelab-scale**: a wound Tesla transformer, a Brovin generator, a metal sphere, a thread, and a ring — the same bench the queue's Tesla cards (003, 018, 053) already assume.

## Departure from the scout flag (stated)

The scout's 2026-10-02 flag on this paper reads `practical_applicability: false — fields [conceptual]; note: … presents no apparatus`. **The note is wrong about the full translation.** §4 of `translations/2026-10-02-fizicheskii-vakuum-torsionnye-polya-tesla-shipov-ru.md` gives the primary/secondary coil dimensions, the driver, the frequency, the secondary voltage, the sphere, and the suspended brass ring — enough to reconstruct a protocol. The scout appears to have read the trinitas HTML abstract (its `source_url` is the `.htm`, while the translation is of the `.pdf`). **The card departs from the flag on the apparatus point and states the departure here rather than hiding it.** The scout's *spirit* — that the paper is theory-first — is correct, and the card is honest that the primary experiment is not in the Vault.

## Replicability: `homelab`

- Build/obtain cost: **~$150–400** — magnet wire for the 1500-turn secondary (~$10–20), a 50 mm polyethylene tube former (~$0–5), aluminium wire for the primary (~$5), a Brovin-generator board or parts (~$30–80), a metal sphere 10–20 cm (~$20–50), a brass ring + a matched insulating ring (~$10–30), fine nylon thread, a grounded fine mesh, a multimeter, and a phone camera or a small mirror + laser for reading rotation.
- Safety: **HIGH-VOLTAGE AND RF — adult-only, gated.** The secondary reaches **~5000 V at ~10 MHz**. This is a shock hazard, an RF-burn hazard, and an ozone/EMI source. **Never touch the secondary, the sphere, or the ring while powered. Discharge the sphere after every run. Keep it away from medical devices (pacemakers), radios, and children.** Run it on an insulated bench, one hand behind the back, with a clearly marked kill switch. This card carries the same gate as card 036 (lethal-voltage) and card 053 (Tesla coil).
- Accessibility: a weekend to wind and assemble, one session to measure. The winding and the Brovin generator are the slow parts.

## Apparatus (Bill of Materials)

- **A Brovin generator** (a self-oscillating high-voltage driver; also known as a "kacher") — the source's driver, ~17.5 V input.
- **A Tesla transformer** — primary: **6 turns of 5 mm aluminium wire**; secondary: **1500 turns of 0.35 mm copper wire on a 50 mm polyethylene tube**. Tuned to resonate at ~10 MHz, giving ~5000 V at the secondary.
- **A metal sphere** (10–20 cm) on an **insulating stand**, connected to the secondary's high end — the charge source.
- **A brass ring** (thin, ~10 cm diameter) **suspended by a fine nylon thread** so it hangs **in the equatorial plane of the sphere** and is free to rotate about the vertical axis.
- **A matched insulating ring** — same outer diameter, same mass, non-conductive (e.g. acrylic or a 3D-printed ring with a brass ring's mass) — the material-swap control.
- **A grounded fine metal mesh** — placed between the sphere and the ring for the shielding arm.
- **A rotation readout** — a small mirror glued to the ring plus a laser pointer and a wall scale, or a phone camera with a fixed reference mark. **A protractor and a fixed interval (60 s) are the measurement.**
- **A multimeter** and a **log sheet** — pre-registered arms, intervals, and thresholds.

## Protocol (four-arm, pre-registered)

**Phase 1 — build and pre-register.**
1. Build the Tesla transformer and the Brovin generator per the source's dimensions. Photograph them.
2. Mount the sphere on its insulating stand and connect it to the secondary's high end. Confirm the secondary reaches ~5000 V (a spark-gap or a HV probe — **do not touch**).
3. Suspend the brass ring by its thread in the sphere's equatorial plane, free to rotate. Photograph the geometry. **Record the ring's resting position.**
4. Write the **pre-registration sheet** before measuring: the four arms, the 60 s interval, the number of repeats (≥3), the order randomisation, and the angular displacements that would count as "rotates" vs "does not rotate". Photograph it.

**Phase 2 — measure.**
5. **Arm A (claim):** power the sphere. Record the brass ring's angular displacement over 60 s. Power down, discharge the sphere, reset the ring.
6. **Arm B (material control):** repeat with the **matched insulating ring**. If B rotates as much as A, the effect is mechanical (ion wind), not electromagnetic.
7. **Arm C (static control):** charge the sphere **statically** (no oscillation) and record the brass ring's displacement. If C rotates, the effect is static electrostatics.
8. **Arm D (shield control):** repeat Arm A with the **grounded mesh** between the sphere and the ring. If D blocks A's rotation, conventional EM / ion wind explains it.
9. Repeat the whole four-arm series **≥3 times**, re-randomising the order. Have a second person read the rotation where it is judged by eye.

**Phase 3 — score.**
10. Tabulate the angular displacement (degrees / 60 s) for each arm across repeats.
11. Score the pre-registered endpoint: **does Arm A rotate, and does it survive the controls?**

## Pass / fail (pre-registered)

- **PASS (refutation — the expected result):** the brass ring rotates in Arm A **and** the matched insulating ring rotates comparably in Arm B **and/or** the grounded mesh blocks it in Arm D — the rotation is **ion wind / conventional EM**, not a scalar field. Reported as the expected, complete result.
- **PASS (anomaly — a surprising result):** the brass ring rotates in Arm A, the **matched insulating ring does not** in Arm B, the **grounded mesh does not block** it in Arm D, and the **static sphere does not** rotate it in Arm C — a conductor-specific, non-shieldable, oscillation-dependent torque, which is what the source claims. **Requires a second independent replication before any conclusion.**
- **FAIL:** the brass ring does not rotate in Arm A at all — no effect to explain.
- **INCONCLUSIVE:** the ring was not free to rotate; the geometry (equatorial plane, distance) was not recorded; the secondary voltage was not confirmed; fewer than three repeats; the rotation was read without a fixed reference.
- **ARTIFACT:** the rotation tracks the corona/ion wind (Arm B rotates); the ring swings from electrostatic attraction to the sphere rather than rotating (Arm C rotates); the ring is moved by air currents in the room (repeat with the sphere off — a null run); the reading tracks the spark rate rather than the field.

## Evidence

Photo of the built transformer + sphere + suspended ring + the **pre-registration sheet** (four arms, interval, repeats, thresholds) + the confirmed secondary voltage + the ring geometry (equatorial plane, distance from sphere) + the **angular-displacement table for all four arms across all repeats** + the null run with the sphere off + the repeat photographs + the void/artifact checks reported whether or not they void the run.

## Confounds (named in advance)

- **Ion wind — the central confound.** A 5 kV sphere at 10 MHz coronas; corona drives an ion wind that pushes light objects. **This is the most likely cause of any rotation.** Arm B (matched insulating ring) and Arm D (grounded mesh) exist to catch it.
- **Static electrostatic attraction.** A charged sphere attracts a nearby conductor; if the ring is not perfectly symmetric, the attraction can produce a torque. Arm C (static sphere) exists to catch it.
- **Eddy-current induction.** A conducting ring in a time-varying field can carry induced currents. Arm B (non-conductive ring) separates this from a mechanical effect.
- **Air currents.** Room air moves a light suspended ring. The sphere-off null run catches it.
- **The reading is operator-judged.** Use a mirror + laser or a fixed camera reference, and a second reader.
- **One session is a sample of one.** Repeat on a second day before concluding anything.
- **The source's own result is a single unreplicated sentence.** The card is testing the *phenomenon*, not reproducing a documented measurement.

## Verdict rules

Arm A rotates and Arm B rotates comparably (and/or Arm D blocks) → **ion wind / conventional EM** (the expected, complete result; the scalar-field reading is refuted). Arm A rotates, Arm B does not, Arm D does not block, Arm C does not rotate → **anomaly** (surprising; needs independent replication). Arm A does not rotate → **refutes the coarse claim**. Ring not free, geometry unrecorded, voltage unconfirmed, or a single session → **inconclusive, not a refutation**.
