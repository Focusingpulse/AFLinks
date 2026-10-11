---
name: Quest Card — Adams Motor Load-Anomaly Test
description: "Aetherforce-branded quest card testing the one counterintuitive claim in a Brazilian builder's Adams-motor replication notes: that loading (or shorting) a pulsed motor's generator coils does not slow the rotor — and shorting them makes it accelerate. The author's own numbers show a LOSS (~50% utilisation), so the card does not chase over-unity; it isolates the falsifiable anomaly — the rotor's RPM response to generator loading. Energy domain (pulsed magnetic motor — radiant-energy recovery); homelab, ~$50–150; Power mirror (Electricity complement)."
---

# ⚡ Aetherforce — Power

**Guild:** Aetherforce — Power (complements Electricity)
**Quest Line:** ⚡ Aetherforce · Electricity complement
**Tier:** straw
**Domain:** energy (a pulsed magnetic motor — radiant-energy recovery; the rotor's response to generator loading)
**Status:** proposed
**Created:** 2026-10-05

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-05-adams-motor-load-anomaly` · authored_at `2026-10-05` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Power",
  desc: "A conventional generator slows down when you draw power from it — that is Lenz's law, and every motor you have ever met obeys it. In 2025 a Brazilian builder published his replication notes on the Adams motor — the pulsed magnetic motor that inspired the Bedini and Newman motors — and reported the opposite: short the generator coils and the motor speeds up instead of stalling. He also published his numbers, and they show a loss, not free energy. So this quest does not chase over-unity. It chases the one thing in his notes that is actually surprising: does loading the generator coils slow the rotor, or not? You build the motor (drive coils, separate generator coils, a rotor with magnets, an optical or Hall switch), run it at a steady RPM, then load the generator coils three ways — open, shorted, and through a resistor — and watch the tachometer and the input meter together. If the rotor holds speed or speeds up while the coils deliver real power and the input does not rise to pay for it, you have reproduced the anomaly and it needs a second family to confirm it. If the rotor slows as the load rises, you have measured ordinary Lenz drag and the claim is refuted — the expected result, and a complete one. Either way you will have built the circuit behind half the free-energy claims you will ever meet, and you will know exactly how to test the next one. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Adams Motor Load-Anomaly Test",
    "FIRST pre-register before the first run: write down the motor's construction (coil turns, core, rotor magnets, sensor, generator-coil position), the three arms, the 60 s run length, the repeats (>=3, randomised order), and the criteria - photograph the sheet. Then build the Adams motor - a rotor with permanent magnets, drive coils and separate generator coils wound Bedini-style on soldering-rod cores, and an optical or Hall sensor switching the drive coils at the rotor's timing - and run it on a 12 V supply until it holds a steady RPM. Then run three arms, >=3 repeats each, randomised: (A) generator coils OPEN; (B) generator coils SHORTED; (C) generator coils LOADED through a resistor matched to the coil resistance. For each arm measure the steady RPM, the input volts and amps (-> input power), and the generator-coil output volts and amps under load (-> output power). Measurable outcome: the change in steady RPM and the change in input power between Arm A and Arms B/C, together with the generator output power. If the rotor holds speed or speeds up under load while the coils deliver real power and the input does not rise proportionally, you have the source's anomaly - a surprising result needing a second independent replication. If the rotor slows as the load rises, you have measured ordinary Lenz drag and the claim is refuted - the expected result, and a complete one. Check the artifacts: does the drive-coil current waveform's timing shift between arms, and does the effect vanish when the generator coils are moved away from the drive-coil timing zone?",
    ["Science", "Engineering", "Measurement"],
    "🔄"
  ],
  source_doc: "translations/2026-10-05-minha-primeira-replica-motor-adams-magalhaes-pt.md — Kadu Magalhães, 'Minha Primeira Réplica do Motor Adams: O Projeto Original Que Inspirou o Motor Bedini' (pt->EN, 2025)",
  source_url: "https://kadumagalhaes.com/minha-primeira-replica-do-motor-adams-o-projeto-original-que-inspirou-o-motor-bedini/",
  dossier: "living-library/synthesis/replication/2026-10-05-dossier-066-adams-motor-load-anomaly.md",
  pass_fail: "PASS (anomaly — the source's claim): loading/shorting the generator coils does NOT slow the rotor (steady RPM holds or rises) while the coils deliver measurable power, and the input power does not rise proportionally to the generator output — requires a second independent replication | PASS (refutation — the expected, complete result): the rotor slows as the generator load rises, scaling with the load, as a conventional generator does (Skeptic's Star) | FAIL (void, not a null): the motor does not hold a stable RPM, or the generator coils produce no measurable output — the run says nothing about the claim | ARTIFACT: the rotor speeds up because the shorted generator coil acts as a second drive coil (detected by a proportional rise in input power, or the effect appearing only at one generator-coil position); or the RPM change tracks a drive-switching timing shift (the drive-coil current waveform moves between arms)",
  evidence: "Photo of the pre-registration sheet (construction, arms, run length, repeats, criteria) taken before the first run + the built motor (rotor, drive coils, generator coils, sensor) + the tachometer readings and input V/A for each arm across all repeats + the generator-coil output V/A under load in Arm C + the drive-coil current waveform (or timing note) for each arm + the moved-generator-coil repeat + the void and artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the claim and the build):** `translations/2026-10-05-minha-primeira-replica-motor-adams-magalhaes-pt.md` — Kadu Magalhães, *Minha Primeira Réplica do Motor Adams: O Projeto Original Que Inspirou o Motor Bedini* (pt→EN), kadumagalhaes.com, 2025. The author gives the topology (drive coils + separate generator coils, Bedini-style windings on soldering-rod cores, optical/Hall switching), his measurements (**~100 mA / 1.2 W input; ~20–25 mA generator output; "~20% direct return"; "~50% total utilisation"**), and the anomaly verbatim: *"when shorting the generator coils, the motor accelerates instead of stalling — something that does not happen in conventional motors."*
- **Source URL:** https://kadumagalhaes.com/minha-primeira-replica-do-motor-adams-o-projeto-original-que-inspirou-o-motor-bedini/
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-05-dossier-066-adams-motor-load-anomaly.md`
- **Aetherforce Reference:** search "radiant energy" / "Bedini" / "Adams motor" / "magnetic motor" on https://www.aetherforce.energy
- **Vault link:** https://focusingpulse.github.io/AFLinks

---

## Rubric Justification

- **Practical:** a named apparatus (the Adams motor — drive coils + separate generator coils, Bedini-style windings on soldering-rod cores, optical/Hall switching) with a named procedure (pre-register → build → run three load arms → measure RPM and power) and a measurable outcome (**the change in steady RPM and input power between the open, shorted and loaded generator-coil arms**). Not pure theory.
- **Replicable:** homelab-scale (**~$50–150** — PVC, enamelled wire, soldering-rod cores, a rotor with magnets, a sensor, a 12 V supply, a multimeter, a tachometer). 12 V DC only, no mains; the cautions are a guarded spinning rotor, coil heating under short, and a heatsinked drive transistor.
- **Relevant:** maps to the Village **energy** survival domain (a pulsed magnetic motor — radiant-energy recovery) and complements the **Electricity** guild (Radiant / Tesla / LMD).
- **Honest:** framed as a TEST, not an endorsement. The card takes the author's own numbers at face value — **they show a loss (~50% utilisation), so the card does not test over-unity** — and isolates the one falsifiable sub-claim (the rotor's response to generator loading). It names the mundane explanation it must rule out (the shorted coil acting as a second drive coil), keeps **RPM** and **input power** as two separate measurements, and treats a refutation as the expected, complete result.
- **Linked:** source doc (the translation), dossier created with protocol + pass/fail, evidence protocol defined.

---

## What makes it the queue's first of its kind

- **The first card on the pulsed magnetic motor (Bedini/Adams) lineage.** Every prior energy card tests a radiant receiver, a turbine, an antenna, a coil, a scalar field, a motor *efficiency* (Keppe), or a thrust anomaly; none tests the **Lenz-drag response** of a pulsed motor — the exact mechanism the whole "radiant energy" family rests on.
- **The first card whose endpoint is the rotor's RPM response to generator loading** — a mechanical-load response rather than a power ratio or a field signature.
- **The first card that tests a claim the source itself reports as a loss.** The author's honest numbers (~50% utilisation) are below unity; the card takes them at face value and isolates the one sub-claim that is actually surprising, rather than the headline.
- **The design choice that is the whole card: two measurements, RPM and input power.** "Acceleration on short" has a mundane explanation — the shorted coil's induced field can attract the rotor magnets, making the generator coil a *second drive coil*. The discriminator is the input meter: if the rotor speeds up but the electrical input rises to pay for it, the "gain" is a torque redistribution; if the rotor holds speed while the coils deliver real power with no matching input rise, that is the anomaly.

---

## Honest Framing

This is a test, not an endorsement. The source is **a single builder's replication notes**, and its own numbers show a **loss** (~50% utilisation) — the card says so plainly and does **not** chase over-unity. The claim under test is narrow and falsifiable: does loading the generator coils slow the rotor? The expected outcome is a **refutation** — the rotor slows as the load rises (ordinary Lenz drag), and the reported "acceleration on short" is a torque redistribution or a switching-timing artifact. **That is a complete, useful result**, and it earns the Skeptic's Star. A clean reproduction of "no drag under load" would be the surprise and would require a second independent family before it is believed. The card makes **no claim that the motor produces net energy** — it measures whether a specific, counterintuitive mechanical response is real, and it teaches the build-and-measure skill behind every free-energy claim a family will meet.

---

## Aetherforce Mirror Coverage

This card complements **Guild 17: Electricity** (Radiant / Tesla / LMD) — its **7th** card, after the Tesla radiant energy receiver (2026-09-08), Bladeless Tesla Turbine Static Electricity Test (2026-09-14), Chiappini Planetary Antenna (2026-09-21), Keppe Motor Matched-Load Efficiency Test (2026-09-27), Mini Tesla Coil Wireless Power Transfer Test (2026-09-29), and Scalar Electromagnetic Field Detection Test (2026-10-02).

**Mirrors filled: 25/26** (unchanged — no new guild filled; Textiles remains the only empty mirror, with no buildable fiber-resonance source in the archive).

---

## Dossier

- `living-library/synthesis/replication/2026-10-05-dossier-066-adams-motor-load-anomaly.md` — full protocol, apparatus, pass/fail, confounds and verdict rules.
