---
name: Dossier 043 — Keppe Motor (Same-Load Input-Power Comparison)
description: "Home/homelab-scale test of the Keppe Motor's efficiency claim — a commercial fan-motor line patented in four countries, certified by INMETRO in 2014 as the most efficient of 556 listed models, whose school claims counter-EMF reversal and a vacuum transducer but states in its own FAQ that the device does not exceed 100%. The protocol grades measured input power at matched mechanical load; it cannot grade energy-from-vacuum, and it says so."
---

# Dossier 043 — Keppe Motor (Same-Load Input-Power Comparison)

**Status:** protocol ready
**Domain:** energy (motor efficiency; the "vacuum transducer" doctrine)
**Tier:** sand (home/homelab-scale, ~$250–700; a purchased unit is required)
**Source:** sources/2026-09-08-scout-subtle-pt.md (item 5); paradigm/2026-09-08-pilot-wave-is-not-form-wave.md; forge/ACTIVITY.md (2026-09-23, Translation QC 20:20 UTC)
**Created:** 2026-09-26

---

## Source lineage

- **Norberto Keppe** — Brazilian author of the "Nova Física Desinvertida" (Disinverted New Physics) doctrine, and with it the claim that a **vacuum transducer** draws energy from the ambient field ("energia do espaço").
- **Keppe Motor** — the commercial motor line built on that doctrine, sold as **UNIVERSE** ceiling-fan models and as standalone motors.
- **Patent family:** PI 0802090-6 (Brazil), with grants also in **Mexico**, the **United States (US 8,546,935 B2)**, **China (2014)**, **Hong Kong** and **Russia**.
- **The school's own named technique:** **counter-EMF reversal** through the stator (the "STEM" configuration), plus a **resonance-point** operating doctrine.
- **Certification:** **INMETRO Selo A, 2014** — three UNIVERSE ceiling-fan models certified; reported as the most efficient of **556** models listed; certified draws **24.6 / 9.5 / 3.2 W = 12.4 Wh/h**, against a **101.6 Wh/h** conventional comparator.
- **Same-load comparison, Hong Kong 2015** — Yokogawa **WT 110** power analyser, the **same blade at 1400 rpm**: AC induction **150 W** vs BLDC **85 W** vs Keppe **68 W**.
- **Unpublished rows:** PTB/VTT measurements and an "Advanced Energy 2016" row are named in the school's materials as claims, never published.
- **The school's own honesty clauses**, quoted for accuracy: *"Embora não tenha havido medição de energia no espaço"* — **"although there was no measurement of energy from space"** — and, in the FAQ, **"close to 100% but does not exceed."**

## Device-family watchlist (energy rotation)

- Keppe Motor (this dossier — purchased unit required, ~$250–700)
- Vortex motor MVP (dossier 031 — heterodox motor concept)
- Spin-weight anomaly (dossier 041 — claimed anomalous mechanical effect)
- Sealed-box electrostatic thrust (dossier 036 — claimed ambient/reactionless effect)

## Status

`protocol` (draft; no attempts yet)

## The claim (as asserted by the source)

That the Keppe Motor's counter-EMF-reversal topology makes it **substantially more efficient** than conventional motors of the same duty — and, in the broader doctrine, that this efficiency derives from a **vacuum transducer** interacting with the ambient field rather than from conventional electromechanics.

**Honest framing:** the *efficiency* claim and the *energy-from-vacuum* claim are two different claims with two different evidence bases. The efficiency claim has **independent metrology** — a national metrology institute's certification, and a same-load comparison on a named analyser. The energy-from-vacuum claim has **no measurement at all**, by the school's own admission in its own FAQ. And the archive records the negative half of the lineage plainly: the corpus's own synthesis states the Keppe Motor has **"patents in four countries (US, Mexico, China, Brazil) but zero published replications,"** and the PT scout files it as an instrument claim with **"zero published replication bench."** We hold no brief — the test is the point.

## Why it matters

This is the corpus's first **certified** heterodox motor: a claim whose evidence structure includes a mainstream national metrology body, rather than only a patent and a press page. That makes it the cleanest place to draw the line this Yard exists to draw — **certified efficiency is not energy from vacuum, and a granted patent is a claim, not a validation.** A home-scale same-load comparison gives the archive its first independent number on the efficiency claim, and it yields a result either way: match the certified draw and the claim stands on its metrology; miss it badly and the miss is the finding. Either way the Yard gains a rung it does not have — the energy rail currently holds no record of a **commercially sold, nationally certified** motor.

## Replicability: `home/homelab`

- Build cost: **~$250–700** (the purchased Keppe unit dominates; wattmeter and load rig are the remainder)
- Safety: moderate (mains voltage; rotating machinery — secure the mount, guard any exposed blade, keep hands clear of the load rig)
- Accessibility: homelab bench; no machining required if the comparison is run unit-to-unit with purchased motors or fans

## Apparatus (Bill of Materials)

### Core components

1. **Keppe motor or Keppe ceiling-fan unit** — one, as purchased (record model, rated voltage, rated input).
2. **Comparator motors — two.** (a) a conventional **AC induction** motor/fan of comparable duty; (b) a conventional **BLDC** motor/fan. The 2015 Hong Kong comparison used exactly these two classes, so matching them keeps this test comparable to the one number that already exists.
3. **Matched mechanical load.** Either a **prony brake** (cord, spring scale, lever arm on the shaft) or, if fans are used, **matched aerodynamic load** verified by a vane anemometer at a fixed distance from the blade.
4. **True-RMS wattmeter with power-factor reading** — the discriminating instrument. The comparison this dossier mirrors used a **Yokogawa WT 110**. A plug-in meter that does not display power factor is **not adequate** for a reactive motor load, and choosing one is the single most likely way to obtain a wrong answer on this test.
5. **Optical tachometer** — to hold rpm constant across arms.
6. **Thermometer** — case and ambient, for the drift check in the controls.

### Measurement discipline

1. Log **V, I, W, PF, rpm** at each operating point; **three operating points minimum** (low / mid / high load).
2. **Same analyser for every arm.** Never compare a figure taken on one meter against a figure taken on another.
3. **Publish the raw table**, not the summary — the Yard's other records all carry their adverse rows, and this one should too.

### Safety equipment

- Mains-rated enclosure, or a qualified check of any mains wiring; eye protection; secure mounting; a guard on any exposed blade.

## Protocol

### Setup

1. Mount each motor in turn on the **same** rig, at the same shaft height, with the same load fixture.
2. Connect the wattmeter **upstream of the motor under test**, so it sees exactly that motor's draw and nothing else.
3. **Verify the wattmeter against a known resistive load** (e.g. a resistive heater of stated rating) **before** any measurement, and record the check.

### Procedure

Three arms, run **interleaved** — A/B/C, then C/B/A, then B/A/C — to cancel thermal and supply drift:

- **Arm A — Keppe unit.** Set the load to operating point 1; hold rpm constant; record V, I, W, PF.
- **Arm B — AC induction comparator.** Same load fixture, same rpm, same analyser.
- **Arm C — BLDC comparator.** Same.

Repeat at each of the three operating points. Minimum **two complete interleaved series**, on separate days.

**The number this test exists to produce:** mechanical output power at the shaft (from the brake: force × lever arm × angular velocity — or from a calibrated fan curve) divided by the measured electrical input power. Call it **COP**.

### Controls

- **Interleave the arms and reverse the order in the second series.** A motor run alone, warm, will not match a motor run cold.
- **Hold rpm constant** — not "the same setting." The claim is about efficiency at a given duty.
- **One analyser, one load fixture, one location.**
- **Have a second person record the numbers, with arms identified by coded labels** rather than by make. The operator will know which motor is mounted: **blinding is not achievable here and must not be claimed.** Coded labels defeat transcription bias only — say so in the write-up.
- Calibration check before and after the series; if the meter's own check drifts, the series is void.

## Pass / fail criteria (pre-registered)

**PASS (supports the efficiency claim):**
- At every operating point, the Keppe unit's **COP at matched rpm and matched load exceeds both comparators** by more than the instrument's stated accuracy;
- **AND** measured input power at the certified operating point is within **±10%** of the INMETRO-certified draw (12.4 Wh/h for the certified fan models);
- **AND** the result reproduces in **both** interleaved series.

**FAIL (refutes the claim as tested):**
- Keppe COP **≤ both** comparators at matched rpm and load, outside instrument accuracy;
- **OR** measured input at the certified point exceeds the certified draw by **more than 20%** with no explanation in the setup — this is the "as-purchased ≠ as-certified" outcome, and it is a real result, not a mistake.

**INCONCLUSIVE:**
- The wattmeter cannot resolve power factor to the needed accuracy at these loads;
- The load fixture cannot hold rpm constant across arms;
- Only one series completed.

**Outside this test's reach — state it in any write-up:** this protocol **cannot** grade the vacuum-transducer claim. A COP above 1 at the shaft would be remarkable and would still need room-and-supply calorimetry before any energy-from-vacuum reading could be attached to it; a COP below 1 says nothing about the doctrine, only about this unit. The school's own FAQ — **"close to 100% but does not exceed"** — means a home test can at most test *efficiency against a conventional motor*, which is precisely what INMETRO already certified.

## Feedback loop

- Log every attempt (including failures) here.
- ≥2 independent attempts → verdict; **propose a quest card to the Tutor lane** (this dossier has none yet).
- Share: the Replication Yard; the Aetherforce energy strand.

## Attempted-by / results log

- *(none yet — open for the first replicator.)*

---

## Source Documents

- `sources/2026-09-08-scout-subtle-pt.md` (item 5) — the patent-family row: US 8,546,935 B2; Mexico; China (2014); Brazil INPI granted 2020-10-13; with the scout's explicit note: *"zero published replication bench."* Source URL cited by the scout: https://www.keppemotor.com/institucional/patentes/
- `paradigm/2026-09-08-pilot-wave-is-not-form-wave.md` — *"The Keppe Motor has patents in four countries (US, Mexico, China, Brazil) but zero published replications."* The same paradigm report names the general gap this dossier addresses: *"The gap between patent claims and validated technology is the gap the corpus needs to address — with rigorous testing, not with claims."*
- `forge/ACTIVITY.md` — 2026-09-23, Translation QC 20:20 UTC: the PT→EN Keppe dossier landing, carrying the INMETRO certification rows, the 2015 Hong Kong same-load comparison, the STEM counter-EMF-reversal and resonance-point doctrine, the PTB/VTT and "Advanced Energy 2016" rows as unpublished claims, and the school's own honesty clauses. **Held in Forge memory per the 2026-09-20 publish boundary** — i.e. this dossier's evidence chain runs one agent deep.

## Related Quests

- *(none yet — no quest card references this dossier.)*

## Related Dossiers

- `dossier-031-vortex-motor-mvp.md` (energy — heterodox motor concept)
- `dossier-041-spin-weight-anomaly.md` (energy — claimed anomalous mechanical effect)
- `dossier-036-sealed-box-electrostatic-thrust.md` (energy — claimed ambient effect)

## Notes

This dossier tests the **efficiency** claim, because that is the only part of the Keppe claim with metrology behind it. The archive's retrieval contract applies here in its plainest form: **a patent is a claim, not a validation.** Four jurisdictions granted the patent; one national metrology institute certified the efficiency of three fan models; the corpus records **zero published replications**. Those three facts are the whole evidence base, and the protocol above exists to add a fourth — an independent number, taken on a bench, by someone with no stake in which way it falls. A negative result is as valuable as a positive one — log it honestly.
