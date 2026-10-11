---
name: Vortex Jet Turbine Energy Test
description: "Home-scale test of the Schauberger/Herbrand claim: vortex-induced jet flow extracts more power from water than a straight pipe at the same head. Rocket guild Aetherforce mirror."
---

# ⚡ Aetherforce — Vortex Jet Turbine Energy Test

**Guild:** Aetherforce — Power (complements Rocket)
**Quest line:** ⚡ Aetherforce · Rocket complement
**Tier:** straw (home/homelab, ~$120-200)
**Domain:** energy (water-power)
**Status:** proposed
**Created:** 2026-09-10

---

## The Claim

Schauberger's 1930 **Jet Turbine** patent (No. 117,749) claims that a jet tube with screw-shaped ribs — inducing a longitudinal vortex — "increases the velocity of the water jet and the efficiency of the machine." The same translation documents Herbrand's Rheinfelden observation: a low-head, low-flow generator reportedly matching one with 5× the flow and 12× the head, attributed to the dynamic energy of fast-flowing water. Supporting line: the 1952 Stuttgart Pöpel experiments, where spiral pipes showed friction *decreasing* with velocity.

**Testable core:** at fixed head and flow, does a jet restriction + spiral vortex induction deliver more electrical power to a small turbine than a straight pipe — and more than the jet effect alone?

---

## The Quest

**Build a three-configuration micro-hydro test: straight pipe vs jet vs jet + spiral vortex.**

**Description:**
Set up a small water turbine (5-12V DC generator wheel) at a fixed 1 m head. Run three intakes: (A) straight pipe control, (B) jet-restriction only, (C) jet + spiral ribs/vanes inducing a vortex. 5 runs each, alternating order. Measure voltage and current into a fixed resistor load, plus timed bucket flow-rate and inlet/outlet water temperature. Compute power P = V·I per run. Measurable outcome: config C beats control A by >15% AND beats jet-only B by >10% beyond run noise = supports the vortex-efficiency claim; C ≈ B = the spiral ribs add nothing at home scale.

**Aetherforce custom:** Does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.

---

## Village Data.js Schema

```js
{
  type: "AETHER",
  biomes: ["suburb","rural"],
  name: "Aetherforce — Power",
  desc: "Test Schauberger's 1930 jet-turbine claim: spiral vortex induction makes flowing water deliver more power than a straight pipe at the same head. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Vortex Jet Turbine Energy Test",
    "Mount a small DC water turbine generator ($20-40) at a fixed 1 m head. Run three intake configs, 5 runs each, alternating order: (A) straight 3-4cm pipe control, (B) same pipe with a jet restriction reducing to 1-1.5cm, (C) jet + spiral ribs or angled vanes inducing a vortex. Each run: record voltage and current into a fixed 10-50 ohm resistor load for 60s, time a bucket fill for flow rate (L/s), measure inlet vs outlet water temperature. Compute P = V·I per run. Measurable outcome: C beats A by >15% AND beats B by >10% beyond run-to-run spread, with flow not dropping enough to explain the gain = supports the vortex-efficiency claim; C within noise of B = spiral ribs add nothing at home scale; flow varying >10% between runs = inconclusive.",
    ["Science","Engineering","Energy"],
    "🌀"
  ],
  source_doc: "translations/2026-09-09-schauberger-dynamic-hydroelectric-energy-es.md",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-09-10-dossier-008-vortex-jet-turbine.md",
  pass_fail: "C > A by >15% AND C > B (jet-only control) by >10% beyond noise = PASS; C ≈ B = FAIL (ribs add nothing); flow variance >10% or output <0.5 W = INCONCLUSIVE",
  evidence: "Photo of all three intake configs, video of one run per config (wheel + multimeter visible), voltage/current table per run, timed flow-rate measurements, inlet/outlet water temperatures, head measurement photo"
}
```

---

## Rubric Justification

- **Practical:** named apparatus (jet tube + spiral ribs + micro turbine), measurable outcome (electrical power vs. controls), pre-registered thresholds
- **Replicable:** home/homelab scale (~$120-200), standard parts, no lab equipment beyond a multimeter
- **Relevant:** energy domain (rotation slot); Rocket guild mirror (free energy / implosion) — the Repulsine itself is lab-tier, this is the home-testable member of the same family
- **Honest:** framed as a test of the patent claim, not an endorsement; the jet-only condition B is the control that separates "vortex effect" from plain Venturi speed-up; a FAIL is defined and valuable
- **Linked:** real source doc (full Sep 9 translation of patent 117,749 + Herbrand account), dossier 008 with protocol + pass/fail, related Schauberger death-cert context

---

## Source

- **Document:** translations/2026-09-09-schauberger-dynamic-hydroelectric-energy-es.md (full translation from giurfa.com/schauberger.pdf)
- **Passage:** "Inside the jet tube (2) there are screw-shaped ribs (5) that promote a rotation which, according to actual observations, increases the velocity of the water jet and the efficiency of the machine." — Schauberger patent 117,749 (1930), as translated
- **Vault URL:** https://focusingpulse.github.io/AFLinks
- **On Aetherforce:** search "Schauberger" / "vortex" / "implosion" on https://www.aetherforce.energy

---

## Dossier

- living-library/synthesis/replication/2026-09-10-dossier-008-vortex-jet-turbine.md (protocol ready, pass/fail pre-registered)

---

## Pass/Fail

- **PASS:** C beats A by >15% AND beats jet-only B by >10%, beyond run noise, without flow dropping enough to explain it
- **FAIL:** C ≈ B within noise (spiral ribs add nothing at home scale) OR total power in B/C lower than A
- **INCONCLUSIVE:** flow varies >10% between runs, head not constant, or output <0.5 W

---

## Evidence to Post

1. Photo of all three intake configurations
2. Video of one run per config (turbine wheel + multimeter in frame)
3. Voltage/current readings per run (table)
4. Timed bucket-fill flow rates per config
5. Inlet/outlet water temperatures (tests the vortex-cooling side-claim)
6. Head measurement photo

---

## Notes

The Herbrand/Rheinfelden story (50 m³/s at 1 m head matching 250 m³/s at 12 m) is second-hand and unverified — the card does not promise it. What it tests is the *mechanism's direction* at home scale. The jet-only control is what makes this card honest: most "vortex power" demos skip it.

This quest complements the **Rocket** guild (free energy / implosion) as its Aetherforce mirror — filling mirror 8/26.
