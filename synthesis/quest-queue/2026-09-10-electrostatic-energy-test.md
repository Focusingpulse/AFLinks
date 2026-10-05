---
name: Electrostatic Energy Test — Community Power Claim
description: "Home-scale test of the Methernita/Testatika claim: can electrostatic machines extract vacuum energy? A community-scale energy system running since 1980 demands honest verification."
---

# ⚡ Aetherforce — Electrostatic Energy Test

**Guild:** Aetherforce — Community (complements Community Living)
**Tier:** sand (home-scale, $50-100)
**Domain:** community (energy)
**Status:** proposed
**Created:** 2026-09-10

---

## The Claim

The Methernita religious community in Linden, Switzerland, has operated the **Testatika** — an electrostatic energy machine — since 1980. According to G.I. Shipov's documentation:

- Multiple installations: 100 W to 30 kW each
- Total output: **750 kW**
- Hotels heated and illuminated solely by this energy
- Disks rotate constantly after manual start; load permanently connected
- **Claim:** "drawing energy from the Physical Vacuum"

The community conceals manufacturing details, believing the principles could be weaponized.

**Testable core:** If electrostatic machines extract vacuum energy, a simple Wimshurst machine should output MORE energy than the manual cranking input.

---

## The Quest

**Build and test a Wimshurst electrostatic generator to measure energy balance.**

**Quest line:** ⚡ Aetherforce · Community complement

**Description:**
Crank a Wimshurst machine for 60 seconds, charging a capacitor bank. Measure how long an LED array stays lit. Compare output energy to cranking input. If output exceeds input by >10%, the vacuum energy claim has support. If output matches or is less than input, the claim is weakened.

**Aetherforce custom:** Does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.

---

## Village Data.js Schema

```js
{
  type: "AETHER",
  biomes: ["suburb","rural"],
  name: "Aetherforce — Community",
  desc: "Test whether electrostatic machines can extract vacuum energy, as claimed by the Methernita community's 750 kW Testatika system running since 1980.",
  tier: "sand",
  quest: [
    "Electrostatic Energy Balance Test",
    "Build or buy a Wimshurst machine ($50-100). Crank for 60 seconds to charge a capacitor bank (20-40µF, 400V). Close switch to LED array. Time how long LED stays lit (>50% brightness). Calculate energy: E = ½CV². Compare output to cranking input work. Measurable outcome: LED illumination time > 66 seconds (10% above cranking duration) AND calculated output > input by >10% = supports claim; LED time ≤ 60s or output ≤ input = refutes claim.",
    ["Science","Engineering","Energy"],
    "⚡"
  ],
  source_doc: "translations/2026-09-04-shipov-torsion-fields-ru-en.md",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-09-10-dossier-007-electrostatic-energy-test.md",
  pass_fail: "LED illumination >66s AND calculated output > input by >10% = PASS; LED ≤60s or output ≤ input = FAIL; machine fails to charge = INCONCLUSIVE",
  evidence: "Photo of apparatus, video of full cranking + LED illumination, capacitor voltage readings (start, end of cranking, end of LED), stopwatch times, ambient and machine temperature"
}
```

---

## Rubric Justification

- **Practical:** Named apparatus (Wimshurst machine), measurable outcome (energy balance), specific protocol
- **Replicable:** Home-scale ($50-100), standard parts, no lab equipment required
- **Relevant:** Maps to Village community domain (shared infrastructure knowledge), complements Community Living guild
- **Honest:** Framed as test of claim, not endorsement; pass/fail criteria pre-registered
- **Linked:** Source document (Shipov translation), dossier created, evidence protocol defined

---

## Source

- **Document:** translations/2026-09-04-shipov-torsion-fields-ru-en.md
- **Passage:** "P. Bauman is the founder of the religious community Methernita, which built several such installations with power from 100 W to 30 kW. The total power of all installations is 750 kW... the community built in Linden, Switzerland, a number of hotels that, since 1980, have been heated and illuminated solely by the energy of the Physical Vacuum."
- **Vault URL:** https://focusingpulse.github.io/AFLinks

---

## Dossier

- living-library/synthesis/replication/2026-09-10-dossier-007-electrostatic-energy-test.md

---

## Pass/Fail

- **PASS:** LED illumination >66 seconds AND calculated output > input by >10%
- **FAIL:** LED illumination ≤60 seconds OR output ≤ input
- **INCONCLUSIVE:** Machine fails to charge capacitors or measurements unreliable

---

## Evidence to Post

1. Photo of Wimshurst apparatus
2. Video of full 60s cranking + LED illumination phase
3. Capacitor voltage readings: start, end of cranking, end of LED
4. Stopwatch times
5. Ambient and machine temperature readings

---

## Notes

The Testatika's exact design is secret, but the core claim (electrostatic = vacuum energy) is testable. This is the simplest home-scale test. If positive, more sophisticated builds could follow. If negative, the claim is weakened for home-scale applications.

This quest complements the **Community Living** guild — shared infrastructure knowledge for family and neighborhood self-reliance.
