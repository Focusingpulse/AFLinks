---
name: Dossier 007 — Electrostatic Energy Test
description: "Home-scale test of the claim that electrostatic machines can extract energy from the physical vacuum, as demonstrated by the Methernita community's Testatika system (750 kW since 1980)."
---

# Dossier 007 — Electrostatic Energy Test

**Status:** protocol ready
**Domain:** community (energy)
**Tier:** sand (home-scale, $50-100)
**Source:** translations/2026-09-04-shipov-torsion-fields-ru-en.md
**Created:** 2026-09-10

---

## The Claim

The Methernita religious community in Linden, Switzerland, has operated the **Testatika** — an electrostatic energy machine — since 1980. According to G.I. Shipov's documentation:

- Multiple installations: 100 W to 30 kW each
- Total output: 750 kW
- Hotels in Linden heated and illuminated solely by this energy
- Disks rotate constantly after manual start; load permanently connected
- Claim: "drawing energy from the Physical Vacuum"

The community conceals manufacturing details, believing the principles could be used for harm.

**The testable core:** If electrostatic machines can extract vacuum energy, a simple Wimshurst machine should output MORE energy than input from manual cranking.

---

## Protocol

### Materials (home-scale, ~$50-100)

1. Wimshurst machine (kit or DIY from acrylic sheets, aluminum foil, PVC pipe)
2. Capacitor bank: 2-4 × 10µF 400V electrolytic capacitors ($10)
3. Rectifier bridge (HV diodes) ($5)
4. LED array (white, 3V, 20mA) or small motor ($5)
5. Multimeter with capacitance/voltage measurement ($15)
6. Stopwatch ($2)
7. Camera (phone) for evidence

### Setup

1. Build or buy Wimshurst machine (standard design, two counter-rotating disks, brushes, Leyden jar capacitors)
2. Connect output to external capacitor bank via rectifier
3. Connect LED array to capacitor bank with switch

### Procedure

**Phase 1: Energy Input Measurement**
1. Crank machine at steady rate for 60 seconds
2. Measure capacitor voltage at end of cranking
3. Calculate stored energy: E = ½CV²
4. Record cranking duration and perceived effort

**Phase 2: Energy Output Measurement**
1. Close switch to LED array
2. Time how long LED stays visibly lit (above ~50% brightness)
3. Calculate delivered energy: E = V × I × t (or use energy meter if available)

**Phase 3: Comparison**
1. Compare input energy (cranking work) to output energy (LED illumination)
2. Standard physics: Output should be LESS than input due to losses
3. Claim: Output EXCEEDS input if vacuum energy is extracted

### Controls

- **Sham run:** Crank with output disconnected, measure effort
- **Temperature check:** Measure machine heating (should not overheat)
- **Capacitor check:** Verify capacitor rating (no over-voltage)

---

## Pass/Fail Criteria

**PASS (supports claim):**
- LED illumination time > 66 seconds (10% above 60s cranking)
- AND calculated output energy > calculated input work by >10%
- AND no external power source connected

**FAIL (refutes claim):**
- LED illumination time ≤ 66 seconds
- OR output energy matches or is less than input
- OR significant losses visible (heating, sparks)

**INCONCLUSIVE:**
- Machine fails to charge capacitors
- Measurements unreliable
- Requires more precise instrumentation

---

## Evidence to Collect

1. Photo of apparatus
2. Video of full 60s cranking + LED illumination
3. Capacitor voltage readings (start, end of cranking, end of LED)
4. Stopwatch times
5. Ambient temperature and machine temperature

---

## Honest Framing

This is a test of the CLAIM, not an endorsement. The Testatika is not independently replicated; the Methernita community keeps details secret. A home-scale Wimshurst machine tests whether electrostatic generators can produce excess energy, which is the core claim. If it fails, the claim is weakened. If it passes, it warrants further investigation — not automatic acceptance.

---

## Source Documents

- translations/2026-09-04-shipov-torsion-fields-ru-en.md (Shipov's description of Testatika)
- translations/2026-09-10-shipov-torsion-fields-and-torsion-technologies-ru.md (same passage)
- living-library/sources/2026-08-27-scout-a-it-pt-ar.md (Arabic source mentioning Testatika schematics)

---

## Related Quests

- dossier-002-eeman-circuit.md (biofield energy, different mechanism)
- dossier-003-tesla-radiant-receiver.md (Tesla's radiant energy, related claim)

---

## Notes

The Testatika is based on Wimshurst machine principles but with claimed modifications. This protocol tests the simplest version. If positive, more sophisticated builds could be attempted. The community's secrecy makes exact replication impossible, but the core claim (electrostatic = vacuum energy) is testable.
