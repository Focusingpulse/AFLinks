---
name: Dossier 066 — Adams Motor Load-Anomaly Test
description: "Replication dossier for the Adams-motor claim that loading a pulsed motor's generator coils does not slow the rotor (and shorting them makes it accelerate) — the counterintuitive sub-claim in a Brazilian builder's Adams-motor replication notes (Kadu Magalhães, 2025). The author's own numbers show a LOSS (~50% utilisation), so the dossier does not test over-unity; it isolates the one falsifiable anomaly: the rotor's RPM response to generator loading. Energy card (pulsed magnetic motor — radiant-energy recovery); homelab, ~$50–150; Power mirror (Electricity complement)."
---

# Dossier 066 — The Adams Motor Load-Anomaly Test

**Status:** protocol
**Domain:** energy (a pulsed magnetic motor — radiant-energy recovery; the rotor's response to generator loading)
**Tier:** straw (homelab, ~$50–150)
**Created:** 2026-10-05
**Source doc:** `living-library/translations/2026-10-05-minha-primeira-replica-motor-adams-magalhaes-pt.md` — Kadu Magalhães, *Minha Primeira Réplica do Motor Adams: O Projeto Original Que Inspirou o Motor Bedini* (pt→EN). Source: https://kadumagalhaes.com/minha-primeira-replica-do-motor-adams-o-projeto-original-que-inspirou-o-motor-bedini/

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-05-adams-motor-load-anomaly` · authored_at `2026-10-05` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The claim (as asserted by the source)

The source is a builder's own replication notes on the **Adams motor** — a pulsed electromagnetic motor (Robert Adams) that the author describes as the ancestor of the Bedini and Newman motors. Its topology: **drive coils** propel the rotor; separate **generator coils** collect the "return energy pulses" (the "radiant pulses"). Coils are wound Bedini-style on soldering-rod (transformer-iron) cores; switching is by an optical sensor (or a Hall sensor). The author reports two things:

1. **Numbers (a loss).** Consumption ≈ **100 mA (1.2 W)**; generator-coil output ≈ **20–25 mA**; "estimated yield: around **20% direct return**"; "total utilisation can reach about **50% of the energy applied**." On the author's own figures this is **below unity** — the device does not produce more energy than it consumes.
2. **The anomaly (the counterintuitive claim).** "When shorting the generator coils, the motor **accelerates instead of stalling** — something that does not happen in conventional motors." And: "Little drag at 3000 RPM … when we extract energy from the generator coils the motor **barely feels the weight any more**."

**What is being tested, in one sentence:** when a family loads (or shorts) the generator coils of an Adams motor running at steady RPM, does the rotor slow as a conventional generator would (Lenz drag), or does it hold speed or accelerate as the source claims?

## Honest status of the claim

The archive holds **one builder's replication notes and no independent test.** A grep for `adams`/`bedini` across `living-library/synthesis/quest-queue/` and `living-library/synthesis/replication/` returns **no card and no dossier**. The claim-status records mention "Bedini" only in passing, inside other motors' records — there is no Adams/Bedini record.

Three things the card must say out loud:

1. **The source's own headline is a loss, and the card says so.** The author's numbers (~50% utilisation) are **below unity**. The card therefore does **not** test for over-unity — it isolates the one genuinely counterintuitive, falsifiable sub-claim: the rotor's RPM response to loading the generator coils.
2. **"Acceleration on short" has a mundane explanation the card must rule out.** Shorting a generator coil makes current flow, which makes a magnetic field, which interacts with the rotor magnets. If the coil is positioned so its induced field attracts the approaching rotor magnet, shorting it adds torque — the generator coil acting as a **second drive coil**. That is a torque redistribution, not a violation. The discriminator is **input power**: if the rotor speeds up but the electrical input rises proportionally, the "gain" is paid for; if the rotor holds speed while the coils deliver real power with no matching input rise, that is the anomaly.
3. **A refutation is the expected, complete result.** The likely outcome is that the rotor slows as the generator load increases (ordinary Lenz drag) and the "acceleration" is a positioning artifact. That is a real result and earns the Skeptic's Star.

**Under-promise, stated plainly:** the expected result is a refutation — the rotor slows under load, and the source's anomaly is a torque redistribution or a switching-timing artifact. A clean reproduction of "no drag under load" would be the surprise and would require a second independent replication.

## Why it matters

- It is the queue's **first card on the pulsed magnetic motor (Bedini/Adams) lineage** — every prior energy card tests a radiant receiver, a turbine, an antenna, a coil, a scalar field, a motor *efficiency* (Keppe), or a thrust anomaly; none tests the **Lenz-drag response** of a pulsed motor.
- It is the queue's **first card whose endpoint is the rotor's RPM response to generator loading** — a mechanical-load response rather than a power ratio or a field signature.
- It is the queue's **first card that tests a claim the source itself reports as a loss** — the card takes the author's honest numbers at face value and isolates the one sub-claim that is actually surprising.
- It is a **buildable electronics education**: winding coils, timing a switch to a rotor, and measuring input vs output power is the core skill behind every "free energy" claim a family will ever meet — and this card teaches it against a claim that is likely false.

## Replicability: `home`

- Build cost: **~$50–150** — PVC pipe, enamelled copper wire, soldering-rod (transformer-iron) cores, a rotor with magnets, an optical or Hall sensor, a small 12 V supply, a multimeter, and a tachometer (or a phone RPM app / an optical tach).
- Safety: **low-to-moderate.** 12 V DC only — no mains. The cautions are (a) a spinning rotor with magnets can pinch or fly — guard it; (b) shorting coils can heat them — keep runs short and watch the wire temperature; (c) the drive transistor can get hot — heatsink it.
- Accessibility: an evening or two to build, an afternoon to test.

## Apparatus (Bill of Materials)

- **Rotor** with permanent magnets on a shaft, on low-friction bearings.
- **Drive coils + generator coils** — Bedini-style windings on soldering-rod / transformer-iron cores (the source's own construction).
- **Switching** — an optical sensor (the source used one from a printer) or a Hall sensor, positioned to switch the drive coils at the rotor's timing.
- **A 12 V DC supply** (current-limited) and a **multimeter** (input V and A).
- **A tachometer** — optical tach, or a phone RPM app, or a slotted-disc + sensor.
- **A load** for the generator coils — a short (0 Ω) and a resistor matched to the coil's DC resistance.
- **Optional:** an oscilloscope to watch the drive-coil current waveform (the artifact check).
- **A camera/phone** — to photograph the pre-registration sheet and the build.

## Protocol (pre-registered home test)

**Phase 1 — pre-register, before the first run.**
1. Write down the motor's construction (coil turns, core, rotor magnets, sensor type, generator-coil position relative to the drive coils).
2. Write the three arms (below), the run length (60 s), the number of repeats (≥3, randomised order), the RPM and power thresholds, and the criteria. **Photograph the sheet before running.**

**Phase 2 — build and establish a steady baseline.**
3. Run the motor with the **generator coils open** until it holds a **steady RPM** (record the RPM and the input V/A). A motor that will not hold a stable RPM is a **void** run.

**Phase 3 — the three arms (randomised order, ≥3 repeats each, 60 s).**
- **Arm A — generator coils OPEN** (baseline). Record steady RPM, input V, input A, generator-coil output (should be ~0 under no load).
- **Arm B — generator coils SHORTED.** Record steady RPM, input V, input A, short-circuit current.
- **Arm C — generator coils LOADED** with a resistor matched to the coil resistance. Record steady RPM, input V, input A, output V and A (→ output power).

**Phase 4 — verify and check the artifacts.**
6. Repeat the arms in randomised order ≥3 times; report the spread.
7. **Artifact check (timing):** with an oscilloscope (or by ear/optical if unavailable), check whether the **drive-coil current waveform's timing shifts** between arms — a shorted generator coil's back-EMF can move the drive transistor's switching point.
8. **Artifact check (position):** repeat Arm B with the generator coils moved **away** from the drive-coil timing zone. If the acceleration only appears at one position, it is a torque redistribution, not a general effect.

## Measurable outcome

The **change in steady RPM (ΔRPM)** and the **change in input power (ΔP_in)** between Arm A (open) and Arms B/C (shorted/loaded), together with the **generator-coil output power (P_out)** in Arm C.

## Pass / fail (pre-registered)

- **PASS (anomaly — the source's claim):** loading/shorting the generator coils does **not** slow the rotor (**ΔRPM ≥ 0** — RPM holds or rises) **while the coils deliver measurable power (P_out > 0)**, and the input power does **not** rise proportionally to the generator output (the extra mechanical output is not paid for electrically). Requires a second independent replication.
- **PASS (refutation — the expected, complete result):** the rotor **slows** as the generator load increases (**ΔRPM < 0**, scaling with the load), as a conventional generator does — the source's anomaly is not reproduced. (Skeptic's Star)
- **FAIL (void, not a null):** the motor does not run at a stable RPM, or the generator coils produce no measurable output — the run says nothing about the claim.
- **ARTIFACT:** the rotor speeds up because the shorted generator coil acts as a **second drive coil** — detected by a **proportional rise in input power** (the "gain" is paid for electrically) or by the effect appearing only at one generator-coil position; **or** the RPM change tracks a **drive-switching timing shift** (the drive-coil current waveform moves between arms).

## Confounds and controls

- **RPM must be measured, not estimated** — a phone tach or optical tach, at a fixed sample interval.
- **Input power must be measured at the supply**, not inferred — V × A at the DC input, averaged over the run.
- **Generator-coil output must be measured under load**, not open-circuit voltage (open-circuit volts overstate the recoverable power).
- **The generator-coil position must be recorded** — the source itself notes the position affects output; a position-dependent effect is a torque redistribution.
- **Temperature drift** — coils and the transistor heat over a run; keep runs short and randomised so drift does not track the arm.

## Verdict rules

- Two independent family attempts agreeing → the dossier verdict updates (replicated / refuted) and the archive cross-links.
- One attempt → **inconclusive**, filed as a single data point.
- A refutation is a **result**, not a failure of the run — it earns the Skeptic's Star and closes the claim honestly.
