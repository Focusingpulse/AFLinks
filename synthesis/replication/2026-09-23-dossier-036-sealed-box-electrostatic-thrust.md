---
name: Dossier 036 — Sealed-Box Electrostatic Thrust Test
description: "Replication dossier for the claim that an asymmetric electrostatic-pressure device produces a net thrust that is NOT ion wind — tested by whether the thrust survives inside a sealed enclosure. Home/homelab, ~$120–180, with a balsa lifter as the enclosure's own control. The energy/propulsion card."
---

# Dossier 036 — The Sealed-Box Electrostatic Thrust Test

**Status:** protocol
**Domain:** energy (electrostatic propulsion — propellantless thrust) / Rocket mirror
**Tier:** straw (home/homelab, ~$120–180; one weekend to build, three sessions to run)
**Created:** 2026-09-23

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-23-dossier-036-sealed-box-electrostatic-thrust` · authored_at `2026-09-23` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

**Source docs (AFLinks Vault):**

- `sources/2026-09-14-deep-dive-morning-a.md` — find 2: the Exodus Propulsion "New Force" status report (Buhler / Aurigema, ~2,000 vacuum-chamber tests, 5–10 mN, no independent replication as of 2026-08).
- `translations/2026-09-22-shipov-institute-vacuum-physics-experiments-ru.md` — the Institute of Vacuum Physics *Experiments* page (RU→EN, translated 2026-09-22): Brown's asymmetric capacitor with **construction numbers** — one plate of foil 3–4 cm wide, the other a wire 0.2–0.4 mm thick, 35–50 kV applied, "the whole construction takes off, overcoming the force of its own weight."
- `sources/2026-09-17-patent-watch.md` — find 1: **US 12,715,620**, granted 2026-08-25, which claims thrust "via Biefeld-Brown electrogravitic effect." Evidence that the claim is live in the 2026 patent record — and a granted patent is not evidence the effect works.
- **Primary (the device class):** WO2020159603A2, *"System and method for generating forces using asymmetrical electrostatic pressure"*, inventors **Andrew Neil Aurigema** and **Charles Raymond Buhler**, priority 2018-11-19, published 2020-08-06, status **Ceased** — https://patents.google.com/patent/WO2020159603A2/en (**fetched and read 2026-09-23**).
- **Primary (the 2026 claim and the demonstration):** Brian Wang, *"Exodus Propulsion and the Exodus Force aka Electrostatic Pressure Force"*, NextBigFuture, 2026-03-31 — https://www.nextbigfuture.com/2026/03/exodus-propulsion-and-the-electrostatic-pressure-force.html (**fetched and read 2026-09-23**).

**Honest note on doc-id verification:** the AFLinks Vault repo is not present in this sandbox, so no `doc:<id>` was verified against the live index this run. Sources are cited by repo path (scout/translation slugs) plus the primary URLs, a form the quest-card schema explicitly allows (`source_doc: "doc:<id> or translation slug"`). Stated, not papered over.

**Honest note on provenance.** Two of the three archive sources are **proponent documents**: the Shipov page is the Institute of Vacuum Physics' own experiments page (a torsion-physics advocacy site that lists Brown's device among "other engines" it endorses), and the NextBigFuture piece is a technology-enthusiast outlet relaying an interview. The **patent is a primary document** — but a patent describes a claimed invention, not a demonstrated result, and this one has **Ceased**. The one genuinely independent voice in the record is critical: the Army Research Lab's Bahder & Fazi (2002), cited *inside the patent itself*, concluded *"At present, the physical basis for the Biefeld-Brown effect is not understood."* **The card supplies the protocol the sources describe but never publish in full.**

---

## The claim (as asserted by the sources)

The claim under test is not "a lifter can lift." It is the **stronger** claim that the force from an asymmetric electrostatic-pressure device is **not ion wind** — that it survives conditions in which ion wind cannot produce net thrust.

In the claimants' own words and numbers:

1. **The device.** The patent (Aurigema & Buhler) describes an "Electrostatic Pressure Force (EPF)" apparatus: electrically conductive surfaces arranged so that the **vector sum of electrostatic pressures** on the object's surfaces is non-zero. The worked geometry is a **blade configuration** — a first electrode carrying a *proximal* conductive surface (close to the opposing electrode) and a *distal* conductive surface (further away), joined by a conductive web, opposing a flat plate, held apart by a **non-conductive** structure. The patent states plainly: *"the present invention does not require the use of an ion wind to generate the force."*

2. **The magnitude.** The patent derives the EPF from electrostatic pressure (½ε₀E²) and notes that in air, with breakdown at ~10⁶ V/m, the pressure is on the order of **1 pascal** — and that the EPF is *"about five orders of magnitude less"* than the Coulomb attraction between the electrodes. The 2026 report puts the demonstrated force at **5–10 mN** on devices of roughly **30–40 g**.

3. **The discriminating predictions.** The 2026 report states the force is **perpendicular to the expected ion-wind direction**, **reverses cleanly when the device is flipped**, **remains present inside a sealed enclosure where no ionized air can escape**, and **persists after the power is switched off**. The patent says the same about the enclosure: *"the invention may be encapsulated in an enclosure to remove ion wind effects. The proof of concept and reduction to practice tests mentioned herein were generally performed within an enclosed box to nullify ion wind effects."*

4. **The claimed control, and the crux.** The 2026 report describes Buhler's own public demonstration of the *contrast*: *"a balsa lifter placed inside a sealed plastic box on a scale, powered up, lifts internally while the scale reads flat. That is conservation of momentum. That is what ion wind looks like."* In other words, the claimants themselves put the **balsa lifter in a sealed box on a scale** as the picture of the ion-wind result — and claim their own geometry does not read flat in the same rig.

**That contrast is the whole card.** A sealed box closes the momentum budget: if the thrust comes from the device pushing air out of the system, then inside a closed box the air's momentum stays inside, the device's pull on the box cancels the air's push on the box, and **the scale does not move**. If the scale *does* move, the device has produced a net external force on a closed system — which is the anomaly. The test does not require anyone to accept or reject a mechanism. It requires only that the box be closed.

**Honest status of the claim — stated up front:**

- **The Biefeld-Brown effect is conventionally attributed to ion wind.** The mainstream reading of Townsend Brown's asymmetric-capacitor thrust is that it is corona-driven ion drift — a real force, but one that requires an ionizable medium and an open path. The claimants dispute exactly this, which is why the enclosure is the test.
- **There is no independent replication.** The 2026 report says so: ~2,000 vacuum-chamber tests by two inventors, *"NO independent replication published"* as of mid-2026. One of the two is the lead of NASA's electrostatics laboratory and incoming president of the Electrostatic Society of America — **credential is a reason to take the claim seriously, not evidence that it is true.**
- **There is no peer review.** The claimant deliberately routed the work through patents rather than journals and describes the patent examiner's witness affidavits as *"equivalent to scientific peer review."* It is not; an affidavit that someone saw an effect is not a controlled measurement.
- **The patent has Ceased**, and a patent is a claim, not a result.
- **The nearest precedent failed.** The report itself places the work in the EmDrive lineage, and the EmDrive did not survive independent testing.
- **The claimed force is small and the device is loud.** 5–10 mN is 0.5–1 g-force on a 30–40 g article, and the patent says the EPF is five orders of magnitude below the Coulomb forces inside the same device. That is why this card's endpoint is a **scale reading in grams, repeated, with a control** — not a single observation.
- **A null is the likely outcome and is a complete result.** If the blade device reads flat in the box while the lifter reads thrust in the open, the card has produced the first home-scale, pre-registered, independently-run data point on the question — and the honest negative earns the Skeptic's Star.

**Claimants:** Charles Raymond Buhler (NASA KSC Electrostatics & Surface Physics Laboratory; incoming president, Electrostatic Society of America) and Andrew Neil Aurigema (Townsend Brown electrogravitics lineage), Exodus Propulsion Technologies, Florida — with the patent's priority date 2018-11-19
**Verification status:** **unverified** — no independent replication known to the archive as of 2026-09; no peer-reviewed publication; patent WO2020159603A2 status *Ceased*
**Mainstream position:** the asymmetric-capacitor thrust is attributed to ion wind / corona discharge; the ARL study cited in the patent itself found the physical basis "not understood"; the EmDrive precedent failed independent test

---

## The protocol — two devices, one box, one scale

The testable core: **if the thrust is not ion wind, then a device inside a sealed enclosure should still push on the scale. If it is ion wind, it should not.** One device is the control that proves the box is doing its job.

### Materials (~$120–180)

1. **High-voltage supply, current-limited, enclosed** (~$50–90). A commercial "lifter power supply" or a neon-sign transformer (10–15 kV) with a **current-limiting resistor** and a **bleeder/discharge wand**. **This is the hazard in this card — see the safety gate below.**
2. **Device A — the enclosure control: a balsa lifter** (~$15). Balsa or foam frame, aluminium-foil skirt, and a thin corona wire. The archive's own construction numbers (Shipov page): foil plate **3–4 cm** wide, wire **0.2–0.4 mm** thick.
3. **Device B — the test article: the patent's blade geometry** (~$20). Two conductive surfaces on one electrode — a *proximal* face close to the opposing plate and a *distal* face further away, joined by a conductive web — opposing a **flat plate**, the two held apart by a **non-conductive** brace. Copper foil or sheet metal; the brace from acrylic, wood, or 3D-printed plastic. The patent's figures 4–8 and 16 show the class; build one stage, not a stack.
4. **A digital scale, 0.01 g resolution** (~$20). 0.01 g = 0.098 mN, so the claimed 5–10 mN is 50–100 counts — resolvable.
5. **A clear plastic storage box with a lid** (~$10), large enough for the device plus its stand. **The box is the experiment and the safety enclosure at the same time.**
6. **A rigid non-conductive stand** (~$5) that carries the device and rests on the box floor, plus a tether so the device cannot fly.
7. **A dummy** of the same mass as Device B, with the same lead (~$0) — the lead-artifact control.
8. **A pre-registration sheet and a pen.**

### Design — the parts that make it a measurement

1. **Establish the open-air baseline first.** With the box open (or the device out of it), power the device and record the scale reading, powered off vs powered on, **10 cycles each**, alternating. Δm_open = the thrust in air. Both devices get this arm. This is where a lifter is expected to show a clear reading.
2. **Then seal it.** Place the device and its stand inside the box, close the lid, put the **box** on the scale. Power the device through a **slack, flexible** high-voltage lead entering through a small hole, with a service loop inside so the lead cannot push or pull on the device. Record powered-off vs powered-on, **10 cycles each**, alternating. Δm_sealed.
3. **Run the lifter as the enclosure's control, not as a warm-up.** Device A (the lifter) must read **flat** in the sealed box. If it does not, the box is leaking momentum or the lead is transmitting force and **the whole test is invalid** — that is the enclosure's own calibration. The source predicts this result; the card requires it.
4. **Run the dummy as the lead's control.** Same lead, same geometry, a mass instead of a device. Any reading here is an artifact of the lead or of thermal drift, and must be subtracted.
5. **Flip and reverse.** Repeat with the device flipped 180° and with polarity reversed. The claim predicts the thrust **reverses cleanly on flip**; ion wind does not reverse on flip. This is the second discriminator and it costs nothing.
6. **Pre-register everything.** Cycle counts, thresholds, the scoring rule, and who holds the key are written down **before** the first powered cycle.
7. **Repeat in three sessions on different days**, to separate a real effect from a thermal or electrostatic one-off.

### Optional deeper arm — the pressure arm

If the family has a **vacuum pump and a sealed vessel** (~$100–300; a hand pump reaches only ~0.3–0.5 atm, which is *not* enough to remove ion wind), repeat the sealed-box arm at reduced pressure. Ion wind scales with the available gas; a genuine electrostatic-pressure force should not. **This arm is optional and its absence does not change the card's pass/fail** — the sealed-box arm already tests momentum closure, which is the stronger question.

### Endpoints

- **Primary — the sealed-box reading:** Δm_sealed for Device B (the blade geometry), in grams, against the dummy's Δm and against Device A's Δm_sealed.
- **Secondary — the open-air reading:** Δm_open for both devices, which establishes that the rig can see a thrust at all.
- **Control 1 — the enclosure:** Δm_sealed for the lifter (must be flat).
- **Control 2 — the lead:** Δm for the dummy (must be flat).
- **Control 3 — flip and polarity:** sign of the reading on flip and on reversal.

### Pre-registered pass/fail

- **PASS (claim supported):** Device B shows **Δm_sealed ≥ 0.5 g (≥5 mN)** in the sealed box, at least **10× the dummy's reading**, with the **lifter control flat (|Δm_sealed| ≤ 0.1 g)**, and the reading **reverses on device flip** — repeated in **three separate sessions**.
- **FAIL (honest negative):** Device B reads **flat in the sealed box** (within 2× the dummy's noise) while the lifter shows a clear thrust in the **open** arm — the force is momentum exchange with the external air, and the claim does not survive at home scale. Skeptic's Star.
- **INCONCLUSIVE:** the **lifter control does not read flat in the sealed box** (the enclosure is invalid — a leak, a stiff lead, a draught); the scale cannot resolve the claimed force; the device arcs at the working voltage; the dummy shows a reading comparable to the device's; the key was opened before the tally; or N was not pre-registered.

---

## Why it matters

This is the **propulsion card** in the queue, and it is the queue's first card aimed at a claim that is **live, credentialed, and genuinely unreplicated in 2026**. Every other card tests a claim whose verdict is old or whose stakes are local. This one tests a claim two engineers are actively making to the public, that a NASA laboratory lead is putting his name behind, and for which the *only* missing ingredient is an independent measurement.

It is also the queue's **first card whose control is another card's device.** The balsa lifter — the thing cards 008 and 018 build for their own claims — appears here as the instrument that calibrates the enclosure. That is the design element that makes the result interpretable either way.

And it is the queue's **first card with a lethal-voltage hazard**, which is stated in the card and gated below rather than softened.

## Replicability: `homelab` (with an adult-only gate)

- Build cost: **~$120–180** (HV supply, two devices, scale, box, stand). The optional vacuum arm adds ~$100–300.
- **Safety — this is the hard gate, and it is not boilerplate.** The supply runs at **10–50 kV**. It can kill. Preconditions, all of them: **adults only; no children in the room; never work alone; one hand in the pocket; insulated probe and discharge wand; power off and discharge before any touch; keep the whole apparatus inside the closed box while energised; switch on from a distance; keep the supply's current-limiting resistor in circuit; and no pacemakers, no heart conditions, no water on the floor.** If any precondition cannot be met, **do not run this card** — the refusal is the correct outcome.
- Accessibility: one weekend to build, three short sessions to run.

## Apparatus (Bill of Materials)

- Current-limited, enclosed high-voltage supply (10–50 kV) + insulated probe + discharge wand.
- Device A: balsa lifter (foil 3–4 cm, wire 0.2–0.4 mm).
- Device B: single-stage blade-geometry electrostatic-pressure article (proximal + distal conductive faces, flat opposing plate, non-conductive brace).
- Digital scale, 0.01 g resolution.
- Clear plastic box with lid; rigid non-conductive stand; slack flexible HV lead.
- Mass-matched dummy with the same lead.
- Pre-registration sheet, a pen, and a person to hold the key.

## What a result means (and what it does not)

- A **pass** means: on this bench, in this box, a blade-geometry electrostatic article produced a net external force on a closed system — the anomaly the claimants describe — three times, against a control that behaved as predicted. It does **not** mean the mechanism is understood, that it scales, that it works in space, or that the claimants' theory is right.
- A **fail** means: at home scale, the force did not survive enclosure, while the lifter behaved exactly as ion wind predicts. That is a complete and publishable result, and it is the result the mainstream account predicts.
- Either way, three confounds must be named in the report: **the high-voltage lead is a mechanical path into the box** (hence the dummy control); **thermal and electrostatic drift** on a 0.01 g scale over minutes (hence alternating cycles and three sessions); and **the enclosure must actually be closed to air** (hence the lifter control, which is the only thing that proves it is).
- **This card cannot reproduce Buhler's own device.** The patent describes a *class* of geometries; the specific test articles are not fully dimensioned in any source we hold. The card tests the **discriminating prediction** on the closest home-buildable member of the same class. That limitation is the card's, and it is stated here rather than hidden.

## Cross-links

- **Dossier 018** (Bladeless Tesla Turbine) — the other card in the queue whose claim is about converting one form of energy to thrust or current with an anomalous mechanism.
- **Dossier 008** (Vortex Jet Turbine) — the other Rocket-mirror card; a heat-engine claim rather than a field claim.
- **Dossier 002** (Tesla Radiant Receiver, merged) — the archive's other "receiving energy from an ambient field" card.
- **Claim status record:** none covers this lineage — the Biefeld-Brown effect has no death certificate in the corpus. This is a **live claim, not a closed one**, which is precisely why it is worth a card.
