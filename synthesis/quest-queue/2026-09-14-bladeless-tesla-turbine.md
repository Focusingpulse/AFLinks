---
name: Bladeless Tesla Turbine Static Electricity Test
description: "Home/homelab-scale test of the 2026 bladeless Tesla turbine claim: compressed air + electrostatic charges generate usable electrical output. Electricity guild Aetherforce mirror."
---

# ⚡ Aetherforce — Bladeless Tesla Turbine Static Electricity Test

**Guild:** Aetherforce — Power (complements Electricity)
**Quest line:** ⚡ Aetherforce · Electricity complement
**Tier:** straw (home/homelab, ~$150-250)
**Domain:** energy (static-to-electrical conversion)
**Status:** proposed
**Created:** 2026-09-14

---

## The Claim

A 2026 multi-university study (Chung-Ang University, Kumoh National Tech, MIT, National Taiwan University) reports that a modern bladeless Tesla turbine — fed with compressed air and electrostatic charges — generates usable electrical output: **800V, 2.5A, 325Hz** at **8,472 RPM** with **300 m/s airflow**. Secondary claims: neutralizes ambient static and improves air quality. Published in Nanowerk, Jan 2026.

**Testable core:** Does combining compressed air flow with electrostatic injection into a bladeless Tesla turbine produce measurable electrical output beyond either condition alone?

---

## The Quest

**Build a three-condition test: air only, electrostatic only, combined — and measure electrical output.**

**Description:**
Assemble a bladeless Tesla turbine (smooth disks, 5-10 cm diameter, 1-2 mm spacing) on a shaft with low-friction bearings. Connect a compressed air source (2-4 bar) with a tangential nozzle aimed at disk edges. Add an electrostatic generator (Van de Graaff or Wimshurst, 10-50 kV) with an electrode injecting charges into the airflow. Wire an electrical pickup (brushes or induction coil) to a multimeter and oscilloscope. Run three configurations, 5 runs each, alternating order: (A) compressed air only, (B) electrostatic only, (C) combined. Each run: log voltage, current, RPM, airflow, ambient static before/after. Measurable outcome: C produces measurable output (V > 10V, I > 0.1A) while A and B produce negligible output; RPM/airflow in reported range (±20%) = supports the electrostatic conversion claim; C ≈ A or B = the combined effect does not replicate at home scale.

**Aetherforce custom:** Does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.

---

## Village Data.js Schema

```js
{
  type: "AETHER",
  biomes: ["suburb","rural"],
  name: "Aetherforce — Power",
  desc: "Test the 2026 bladeless Tesla turbine claim: compressed air + electrostatic injection generates usable electrical output beyond either alone. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Bladeless Tesla Turbine Static Electricity Test",
    "Build a bladeless Tesla turbine (5-10 smooth disks, 1-2 mm spacing) on low-friction bearings. Connect compressed air (2-4 bar) via tangential nozzle at disk edges. Add electrostatic generator (10-50 kV) with electrode injecting charges into airflow upstream of turbine. Wire electrical pickup (brushes or induction coil) to multimeter and oscilloscope. Run three configs, 5 runs each, alternating order: (A) air only, (B) electrostatic only, (C) combined. Each run: log voltage, current, RPM (tachometer), airflow (anemometer), ambient static before/after. Measurable outcome: C produces V > 10V and I > 0.1A while A and B produce negligible output, with RPM 6,800-10,100 and airflow 240-360 m/s = supports electrostatic conversion claim; C within noise of A or B = combined effect does not replicate at home scale; RPM/airflow significantly below range = inconclusive (mechanical issues).",
    ["Science","Engineering","Energy"],
    "⚡"
  ],
  source_doc: "sources/2026-08-29-scout-b-es-fr-zh.md",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-09-14-dossier-018-bladeless-tesla-turbine.md",
  pass_fail: "C produces V > 10V and I > 0.1A while A and B produce negligible output, with RPM 6,800-10,100 and airflow 240-360 m/s = PASS; C within noise of A or B = FAIL (no combined effect); RPM/airflow below range = INCONCLUSIVE",
  evidence: "Photo of turbine assembly and three configurations, video of one run per config (disks + multimeter visible), voltage/current table per run, RPM and airflow measurements, ambient static readings before/after each run"
}
```

---

## Rubric Justification

- **Practical:** named apparatus (bladeless Tesla turbine + electrostatic injection), measurable outcome (voltage, current, RPM, airflow), pre-registered thresholds
- **Replicable:** home/homelab scale (~$150-250), requires compressed air source, basic machining or 3D printing, multimeter; oscilloscope recommended for 325Hz verification
- **Relevant:** energy domain (rotation slot); Electricity guild mirror — complements Tesla radiant receiver with a different mechanism (static-to-electrical vs. atmospheric reception)
- **Honest:** framed as a test of the 2026 claim, not an endorsement; the air-only and electrostatic-only conditions are controls that separate "combined effect" from trivial mechanisms
- **Linked:** real source doc (scout find from Jan 2026), dossier 018 with protocol + pass/fail, related Tesla radiant receiver context

---

## Source

- **Document:** sources/2026-08-29-scout-b-es-fr-zh.md (item 3: Turbina Tesla Sin Aspas)
- **Original article:** https://computerhoday.20minutos.es/ciencia/energia-inalambrica-una-turbina-tesla-sin-aspas-es-capaz-convertir-electricidad-estatica-energia-util_6920492_0.html
- **Nanowerk reference:** Jan 2026, multi-university collaboration
- **Vault URL:** https://focusingpulse.github.io/AFLinks
- **On Aetherforce:** search "Tesla turbine" / "bladeless" / "static electricity" on https://www.aetherforce.energy

---

## Dossier

- living-library/synthesis/replication/2026-09-14-dossier-018-bladeless-tesla-turbine.md (protocol ready, pass/fail pre-registered)

---

## Pass/Fail

- **PASS:** C produces measurable output (V > 10V, I > 0.1A) while A and B produce negligible output, with RPM and airflow in reported range (±20%)
- **FAIL:** C output within noise of A or B (no combined effect beyond trivial mechanisms)
- **INCONCLUSIVE:** Turbine fails to reach target RPM, electrostatic injection fails, or measurement gear insufficient

---

## Evidence to Post

1. Photo of bladeless Tesla turbine assembly
2. Photo of three configurations (air only, electrostatic only, combined)
3. Video of one run per config (turbine + multimeter visible)
4. Voltage/current readings per run (table)
5. RPM measurements per config
6. Airflow velocity measurements per config
7. Ambient static readings before/after each run

---

## Notes

This quest complements the **Electricity** guild (Tesla radiant receiver already merged) with a different mechanism: static-to-electrical conversion via turbine rather than atmospheric reception. The 2026 study is new and unreplicated — the card tests the mechanism's direction at home scale. A negative result is as valuable as a positive one.

This fills **mirror 19/26** (Electricity guild already has Tesla radiant receiver; this adds a second Aetherforce quest to the same guild, complementing rather than duplicating).
