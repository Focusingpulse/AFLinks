---
name: Quest Card — Searl Weight-Change Load-Cell Test
description: "Aetherforce-branded quest card testing the claim that a rotating permanent-magnet ring-and-roller assembly (John R. R. Searl's 'Searl Effect Generator') loses WEIGHT at a critical speed. A magnet rotor and a MATCHED-MASS NON-MAGNETIC rotor, spun at the same speeds on the same rigid load cell — so the only thing that differs between the two runs is whether the rotating mass is magnetic. Energy domain (a rotating magnet assembly's weight — the antigravity half of the free-energy claim); Rocket complement. Implements the archive's own retry_now prescription."
---

# ⚡ Aetherforce — Power

**Guild:** Aetherforce — Power
**Quest Line:** ⚡ Aetherforce · Rocket complement
**Tier:** straw
**Domain:** energy (a rotating magnet assembly's weight — the antigravity half of the free-energy claim)
**Status:** proposed
**Created:** 2026-10-12

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-12-searl-weight-load-cell` · authored_at `2026-10-12` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Power",
  desc: "In 1952, John Searl said, his generator rose off the ground, climbed fifty feet and flew away. His 'Searl Effect Generator' — a ring of magnets with rollers orbiting it — is one of the most famous free-energy claims ever made, and the antigravity half of it is the part nobody has ever properly measured. Here is the claim in its one modern measured form: in 2000, two Russian researchers reported a 35% WEIGHT REDUCTION on a 225 kg magnet converter running at 6-7 kilowatts. And here is why that number never settled anything: they floated the whole platform on springs and shock absorbers and read 'weight' off a displacement sensor, so the vibration of the machine and the pull of the magnets on the sensor were never separated from the weight itself. You can do the measurement they could not. Build a small rotor carrying magnets, mount it RIGIDLY on a scale, and spin it. Then swap in a rotor of exactly the same mass carrying NON-MAGNETIC weights, and spin it at exactly the same speeds. Same mass, same shape, same speed, same air, same mount — the only thing that changed is whether the spinning mass is magnetic. If the magnet rotor gets lighter and the plain one does not, you have found something enormous. If they weigh the same, you have done the measurement that the famous claim has never survived — and you will know exactly why the springs mattered. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Searl Weight-Change Load-Cell Test",
    "FIRST pre-register everything before anyone runs: the rotor mass, the magnet mass, the speed points (target 0, 500, 1000, 2000, 3000 rpm), the run count (at least 5 per condition), the matched-mass non-magnetic control, the enclosure, the scale and its resolution, the threshold, and the analysis - photograph the sheet. Build a rigid rotor carrying permanent magnets (ferrite or neodymium), balanced, on a small motor with speed control. Mount the motor and rotor RIGIDLY on a frame that rests on the scale - NO springs, NO shock absorbers, NO rubber feet - and enclose the rotor so its own airflow does not press on the scale. Weigh the rotor. STATIC CONTROL: motor off, magnets in place, record the scale reading for 60 s (does the static field affect the scale at all?). MAGNET RUN: spin to each speed point in ascending order, hold 30 s at each, and record the scale reading in grams (averaged over the hold) plus the motor input power in watts; return to zero between points; repeat the sweep at least 5 times. CONTROL RUN: swap in a rotor of the SAME MASS carrying NON-MAGNETIC weights (matched within 2%), and repeat the identical sweep, identical run count, identical order. Repeat both runs in a SECOND SET on a different day, with a blind swap if a second person is available. Compute the weight difference between the magnet run and the control run at each matched speed, with the spread. Measurable outcome: the weight difference in grams between the magnet rotor and the matched-mass non-magnetic rotor at each matched speed, and whether it scales with speed. Target: a repeatable difference of 5 g or more that appears ONLY in the magnet run, scales with speed, vanishes when the magnets are replaced, and replicates in a second set = the weight claim is detectable at home scale. A difference below the noise floor at every speed in both sets = a rotating magnet assembly does not change weight at home scale (the expected, complete result).",
    ["Science", "Engineering", "Measurement"],
    "🧲"
  ],
  source_doc: "synthesis/claim-status-records/searl-effect-generator-1946-2002.json — the Searl Effect Generator claim-status record (status died; retry_now prescribes the rigid-load-cell rebuild); primary measured claim doc:3872 (Roschin & Godin, Technical Physics Letters 26(12):1105-1107, 2000); reconstruction doc:2753 (Sandberg 1985); the archive's own null doc:5403 (Roschin & Godin small prototype)",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-10-12-dossier-087-searl-weight-load-cell.md",
  pass_fail: "PASS (claim survives - the surprise): a repeatable weight difference of >= 5 g that appears ONLY in the magnet run, scales with speed, vanishes when the magnets are replaced by matched-mass non-magnetic weights, and replicates in a second set - the weight claim is detectable at home scale and needs the taller follow-up (demagnetised-magnet arm, force plate, blind operator) | PASS (claim refuted - the expected, complete result): the difference is below the noise floor at every speed in both sets - a rotating magnet assembly does not change weight at home scale (Skeptic's Star) | FAIL (void, not a null): the two rotors do not match in mass (within 2%), or the mount is not rigid (springs, rubber feet, a wobbly frame), or the rotor is not enclosed and its airflow reaches the scale, or the motor's vibration/torque is not separated, or the scale is saturated, or the speed was not measured | INCONCLUSIVE: fewer than 5 runs per condition; one set only; no non-magnetic control; scale resolution coarser than 1 g; the enclosure was opened mid-run; or the operator knew which rotor was which | ARTIFACT: the reading tracks the motor's own vibration or torque (it appears in BOTH runs); the reading tracks scale thermal drift (it appears with the motor off); the reading tracks enclosure airflow; or the reading reverses when the rotor is turned over - a magnetic-force-on-the-scale artifact, not a weight change",
  evidence: "Photo of the rotor mounted rigidly on the scale inside the enclosure + the pre-registration sheet (rotor mass, magnet mass, speed points, run count, control, enclosure, scale resolution, threshold, analysis) photographed before anything runs + the static-control record (motor off, magnets in place, 60 s) + the per-speed log for BOTH runs (speed, scale reading in grams, motor input power in watts) + the matched-mass confirmation for the two rotors (weighed, within 2%) + the second-set repeat + the optional field-at-distance readings (0.1, 1, 3, 5, 10, 15 m) with the ambient background + the void/artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the claim and the retry):** `synthesis/claim-status-records/searl-effect-generator-1946-2002.json` — the Searl Effect Generator claim-status record, status **`died`** (grounds: replication-failure, mechanism-superseded, dismissal). Its `retry_now` block is the design brief for this card, verbatim: *"THE WEIGHT-CHANGE CLAIM IS MEASURABLE, and the 2000 apparatus shows exactly how it was not: Roschin & Godin mounted the 350 kg platform on springs and shock absorbers and read 'weight' from an inductive displacement transducer (doc:3872), so vibration and magnetic forces on the transducer are not separated from thrust. A 2026 rebuild should rigidly mount the assembly on a calibrated load cell / force plate, run a power analyser that captures the reactive power the drive draws (integrated V x I x power factor over the full waveform) against a known output load, and repeat with the magnets demagnetised as the control."*
- **The one modern measured claim:** `doc:3872` — V. V. Roschin & S. M. Godin, *An Experimental Investigation of the Physical Effects in a Dynamic Magnetic System*, **Technical Physics Letters 26(12):1105–1107, 2000** — a 110 kg stator / 115 kg rotor rare-earth-magnet converter; **35 % weight reduction at 6–7 kW**, "magnetic walls" of 0.05 T out to 15 m, a 6–8 °C temperature drop, corona discharge and ozone; the paper states the result "cannot be explained" by conventional theory.
- **The archive's own null:** `doc:5403` — Roschin & Godin's own small-prototype test (ceramic magnets, 12 rollers) found **no self-acceleration and no magnetic or thermal walls**: *"we couldn't find any anomalies in the temperature distribution and distribution of magnetic field around the converter."*
- **The reconstruction (geometry + manufacturing):** `translations/2026-10-12-searl-effect-sandberg-ru.md` — S. Gunnar Sandberg, *The Searl Effect* (Academy of Trinitarianism, publ. 13264, 02.05.2006; ru→EN, 3 chunks, complete) — the 1952 flight account, the magnetization procedure (RF AC ~100 mA at ~10 MHz added during magnetization; ≥ 180 ampere-turns; all magnets magnetized simultaneously; ferrite or magnetic ceramic), and the stated 180 kW/tonne. Companion: `doc:2753` (Sandberg 1985, *Design & Manufacturing Procedure* — *"the source of energy is at present unknown"*), `doc:2752` (Sandberg 1987 — the 1983 fire; the radial-voltage seed observation).
- **The blank measurement record:** `doc:2392774` — the INE device-database entry for the "Searl Generator (England)": **every measurement field blank** — Watts Generated, % O/U Measured, % Weight Loss, Date Witnessed, Witnesses Name, Date Tested, Tester Name.
- **The corpus's own modern reading:** `doc:1513540` — *"The SEG works very much as the N-Machine or homopolar faraday generators."* And `doc:5452` — US Patent 6,822,361, *Orbiting Multi-Rotor Homopolar System* (Roschin & Godin, 2004) — a patent, not a confirmation.
- **Companion cards (weight / rotation / thrust, different endpoints):** `synthesis/quest-queue/2026-09-25-spin-weight-anomaly.md` (dossier 041) — a spinning **gyroscope rotor's** weight (Kozyrev; Hayasaka & Takeuchi), control = **spin direction**; `synthesis/quest-queue/2026-09-23-sealed-box-electrostatic-thrust.md` (036) — electrostatic thrust, control = **sealed enclosure**; `synthesis/quest-queue/2026-10-05-adams-motor-load-anomaly.md` (055) — a pulsed magnet motor's **electrical** output, control = **matched load**. **None of them separates MAGNETISM from ROTATION.**
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-12-dossier-087-searl-weight-load-cell.md`
- **Aetherforce Reference:** search "Searl" / "free energy" / "magnet motor" on https://www.aetherforce.energy
- **Vault link:** https://focusingpulse.github.io/AFLinks

---

## Rubric Justification

- **Practical:** a named apparatus (a magnet rotor, a matched-mass non-magnetic rotor, a rigid mount, a scale or load cell, a tachometer, a power meter, an enclosure) with a named procedure (build → pre-register → static control → magnet sweep → control sweep → second set → compute Δ) and a measurable outcome (**the weight difference in grams between the magnet rotor and the matched-mass non-magnetic rotor at each matched speed, and whether it scales with speed**). Not pure theory.
- **Replicable:** home/homelab (**~$150–300** — a small motor, magnets, a frame, a digital scale or a 5 kg load cell + HX711, a phone tachometer). No lab, no chemicals, no mains wiring beyond a low-voltage motor supply. One build, two sessions.
- **Relevant:** maps to the Village **energy** survival domain (a rotating magnet system — the free-energy device class) and complements the **Rocket** guild (free energy / implosion).
- **Honest:** framed as a TEST, not an endorsement. The claim is **recorded as `died`** in the archive's own claim-status record, and the card says so on its face; the expected outcome is a null and the card presents a positive as the surprise. The card carries the archive's own **methodological diagnosis** of why the one modern measurement was uninterpretable, and it states plainly the one limitation it cannot remove — **a home rotor is not the SEG**.
- **Linked:** source doc (the claim-status record + the Sandberg translation + the `doc:` ids), companion cards, a dossier created with protocol + pass/fail, and an evidence protocol defined.

---

## What makes it the queue's first of its kind

- **The first card whose control is the MAGNETS THEMSELVES.** Every prior weight or thrust card controls something adjacent: card 041 (spin-weight anomaly) controls **spin direction** and corrects for friction and temperature; card 036 (sealed-box thrust) controls the **enclosure**; card 055 (Adams motor) controls the **electrical load**. This card runs a **matched-mass non-magnetic rotor at the same speeds on the same mount**, so the only variable left is whether the rotating mass is magnetic. That is the discriminator that separates **magnetism** from **rotation** — and no card in the queue has it.
- **The first card on the Searl Effect Generator lineage** — the most famous free-energy device claim in the archive, and one the queue has never touched. Its claim-status record carries a 35-document corpus and an explicit `retry_now`.
- **The first card whose design is derived from a PRIOR MEASUREMENT'S ERROR.** The archive's own record names the exact confound that made the 2000 result uninterpretable — a 350 kg platform on springs and shock absorbers, with "weight" read from a displacement transducer — and prescribes the fix. The card is that prescription, built at home scale. The transferable lesson is the one every measurement needs: **if your instrument cannot separate the effect from the machine that produces it, you have not measured the effect.**
- **The first card whose endpoint is a weight change on a MAGNETIC assembly** — distinct from 041's gyroscope (no magnets) and from the electrical-output cards (055, 047).

---

## Honest Framing

This is a test, not an endorsement. The Searl Effect Generator is **recorded as `died`** in the archive's own claim-status record, on three grounds — replication-failure, mechanism-superseded, dismissal — and the card says so up front. The record's counterweight is severe and the card keeps it in front of the family: the authors of the one modern measurement **could not reproduce their own effect** at smaller scale (`doc:5403`); the movement's own device database has **every measurement field blank** (`doc:2392774`); the documentation **burned in 1983**; the modern unit is a **mockup**; and the 1991 Heerfordt investigation could verify nothing. The mechanism was never fixed and has no successor — the only real physics in the lineage is the ordinary homopolar effect in a spinning conductor.

**The limitation the card cannot remove, stated plainly:** a home rotor is **not** the Searl Effect Generator. The SEG's own geometry — concentric magnetised rings with rollers orbiting them — is specified in `doc:2753`, but no working device survives. So a null here **bounds the claim at home scale**; it does not disprove an effect in a large device. Two things make the test worth running anyway: the claimed effect is **35 % of a 225 kg assembly** — enormous, and a mechanism that produces it at 225 kg should produce *something* at 1 kg; and the archive's **own** small-prototype test found nothing at a **larger** scale than this card's, so the card replicates the archive's own null rather than inventing a new one.

The card is a method test of a cited claim. It makes **no health claim**, and it involves a spinning rotor — **eye protection, a secured enclosure, and no loose clothing or hair near the rotor.**

---

## Aetherforce Mirror Coverage

This card complements **Guild 8: Rocket** (free energy / implosion) — its **4th** card, after the Vortex Jet Turbine Energy Test (2026-09-10), the Sealed-Box Electrostatic Thrust Test (2026-09-23) and the Spin-Weight Anomaly Test (2026-09-25). Rocket is one of the emptier mirrors, and the Searl claim — a free-energy device that is also claimed to lift — is squarely its subject.

**Mirrors filled: 25/26** (unchanged — no new guild filled; Textiles remains the only empty mirror, with no buildable fiber-resonance source in the archive).

---

## Dossier

- `living-library/synthesis/replication/2026-10-12-dossier-087-searl-weight-load-cell.md` — full protocol, apparatus, pass/fail, confounds and verdict rules.
