---
name: Cold Machine Vortex-Cooling Test
description: "Run the same water through a coiled vortex tube and a straight tube of equal length, each ending in the same 1 mm orifice, at matched flow — and measure whether the vortex arm runs colder. Food-domain card (cold storage without grid power or fuel); ~$40-120; Food Prep mirror. The queue's first card that isolates the vortex's contribution to cooling against a matched straight-arm control, and its first whose source debunks its own headline claim."
---

# ⚡ Aetherforce — Food

**Guild:** Aetherforce — Food
**Quest Line:** ⚡ Aetherforce · Food Prep complement
**Tier:** straw
**Domain:** food (cold storage — preserving food without grid power or fuel)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-26-cold-machine-vortex-cooling` · authored_at `2026-09-26` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Food",
  desc: "Can a bucket of water keep food cold with no fuel and no grid? The 'cold machine' (冷机) is a century-old Schauberger idea: force water into an inward-spiral vortex through curved tubes, jet it through tiny 1 mm orifices, and the flash evaporation plus the vortex itself is supposed to create a cold source. Here is the honest split: the evaporation part is ordinary physics and will work; the vortex part is the extraordinary claim and has never been isolated. So run the SAME water through two tubes of equal length and diameter — one coiled (vortex), one straight — each ending in the SAME 1 mm orifice, at the SAME flow rate. Evaporation is present in both arms and cancels. Whatever difference is left is the vortex. Then see whether the cold chamber holds a jar below room temperature. The source article itself calls the machine's over-unity claim 'perpetual-motion fantasy' — we are testing only the cooling, and the cooling is the part it says is reproducible. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Cold Machine Vortex-Cooling Test",
    "Build two tube arms of the same inner diameter and the same developed length (8-10 mm ID x 60-80 cm): Arm A coiled around a cylinder (vortex), Arm B straight. Fit BOTH with the same 1 mm orifice and wrap BOTH in the same insulation (the coil has more surface area - that is a confound, not the effect). Mount a head tank 1.0-1.5 m above the orifice and let the water sit to ambient first. Run one arm at a time, alternating A,B,A,B, matching the flow rate between arms within 10% (target about 1.0 L/min, measured with a bucket and stopwatch at the start and end of every run). Each run is 30 minutes; log inlet water temp, chamber air temp, a sealed 500 mL jar's temp, ambient, and flow at t=0, 5, 10, 20 and 30 min. Four alternating sessions per arm. Optional Arm C: the same coil with NO orifice, to isolate the vortex with no evaporation at all. Measurable outcome: the chamber temperature at t=30 min, Arm A versus Arm B at matched flow, plus the absolute cooling below ambient. PASS: A is at least 0.5 C colder than B at t=30 min, same sign in 3 of 4 sessions, with both arms insulated and ambient stable. FAIL: A and B within 0.3 C in 3 of 4 sessions - the vortex adds no cooling beyond evaporation, and the cold machine's cooling is ordinary evaporative cooling. VOID: flow cannot be matched within 10%, or ambient swings more than 2 C during a session. Photograph both spray patterns - a finer mist on Arm A is a real alternate mechanism (atomization), not the claimed one.",
    ["Science", "Engineering", "Measurement"],
    "❄️"
  ],
  source_doc: "translations/2026-09-26-water-based-cold-machine-zh.md (full EN translation of the Chinese article 'The Century-Old Mysterious Water-Based Cold Machine', tech-works.cn, source material by E Yusong) + sources/2026-08-26-scout-a-fr-es-zh.md find 4 (the scout entry that flagged it buildable) + the Schauberger vortex claim record synthesis/claim-status-records/schauberger-vortex-repulsine-1951.json",
  source_url: "https://www.tech-works.cn/-nd-585.html",
  dossier: "living-library/synthesis/replication/2026-09-26-dossier-043-cold-machine-vortex-cooling.md",
  pass_fail: "PASS: at matched flow (+/-10%), the vortex arm A is >=0.5 C colder than the straight arm B in the chamber at t=30 min, same sign in >=3 of 4 sessions, with both arms insulated identically and ambient logged and stable. PASS (strong form, if Arm C is run): Arm C (vortex, no orifice) cools measurably below ambient with no evaporation present. FAIL: A and B within +/-0.3 C at t=30 min in >=3 of 4 sessions - the vortex shape contributes no cooling beyond the orifice's evaporation; the cold machine's cooling is ordinary evaporative cooling (Skeptic's Star; a complete and valuable result). VOID: flow cannot be matched within +/-10%, or ambient swings more than 2 C during a session, or the chamber leaks so freely that both arms track ambient - report the resolution achieved and the control required, NOT a verdict. ARTIFACT: the A-B difference tracks the coil's larger surface area (re-run with both arms insulated identically), or disappears when both arms' water is brought to the same temperature before the orifice, or is fully explained by a finer spray from the swirl (photograph the sprays).",
  evidence: "Photo of the whole rig (tank, both tube arms, insulation, orifice caps, cooler box, thermometers) + the pre-registration sheet (arm order, sessions, flow target, thresholds, scoring rule) + a photo of each spray pattern + the flow measurement (bucket volume and time) at the start and end of every run + inlet water, chamber air, jar and ambient temperatures at t=0/5/10/20/30 for every session + the four alternating sessions per arm dated + Arm A vs Arm B chamber temperature at t=30 min with the session-to-session scatter + the absolute cooling below ambient (the practical cold-storage result) + Arm C's series if run + the void check (flow match and ambient stability) reported whether or not it voids the run + a note on whether the spray on Arm A was visibly finer than on Arm B"
}
```

---

## Source Documentation

- **Primary:** *百年神秘「水基冷机」：人类差点错过拯救全球变暖的终极解药* (The Century-Old Mysterious "Water-Based Cold Machine": the ultimate cure for global warming humanity almost missed), **tech-works.cn** (先进制造网 / Advanced Manufacturing Network), source material by **E Yusong (鄂雨松)** — https://www.tech-works.cn/-nd-585.html — held in the Vault as `translations/2026-09-26-water-based-cold-machine-zh.md` (full English translation, translated 2026-09-26). The article carries the six-step working principle, the vortex-tube + micro-orifice construction, and — unusually — its own list of the claim's fatal flaws.
- **The claim in the source's own words:** *"a natural power device that uses water as its circulating medium, creates low temperature through vortex spiraling plus micro-orifice phase change, harvests the atmosphere's greenhouse waste heat and converts it into power and electricity, simultaneously cools the atmosphere, and runs in a sealed perpetual loop."*
- **The source's own refutation of the headline, quoted in the card's framing:** the over-unity framing *"crosses the red line of conservation of energy… violates classical physics, is perpetual-motion fantasy, and cannot stand at present"*; the core concepts *"lack formal scientific support… no mathematical models and no repeatable experiments."* Its own summary of what survives: *"the fluid effects, the cooling structures, and the water-cycle logic of the cold machine can be partially reproduced; but complete high-power output, crewed flight, and self-sustaining energy circulation have never received formal scientific verification or engineering realization."*
- **Lineage:** `synthesis/claim-status-records/schauberger-vortex-repulsine-1951.json` — the Schauberger vortex/implosion claim record. Its `late_confirmation` field states the gap this card fills: *"No mainstream physics program has tested Schauberger's vortex claims with calibrated instrumentation."* Its `retry_now` field points at dossiers 001 and 004; this card adds the cooling-specific comparison neither of them makes.
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-26-dossier-043-cold-machine-vortex-cooling.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "cold machine", "Schauberger", "vortex", "implosion"
- **Aetherforce Reference:** Search "Schauberger", "vortex", or "implosion" on https://www.aetherforce.energy
- **Related dossiers:** 001 (Wasserwirbler — a temperature differential across a funnel, but no orifice and no straight-arm control), 004 (Hyperbolic Funnel Vortex — dissolved-oxygen endpoint), 024 (Spiral-Pipe Friction — flow/head endpoint; temperature only a side-claim), 010 (Egg-Shaped Fermentation Vessel — the other Food Prep preservation card), 033 (Pyramid Storage Desiccation — the desiccation half of food preservation)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (two tube arms of equal ID and developed length, one coiled and one straight, each with the same 1 mm orifice; a head tank; an insulated spray chamber holding a sealed jar) with a named procedure (alternating arms, matched flow, 30-minute runs, five timepoints, four sessions per arm) and a measurable outcome (chamber temperature at t = 30 min, arm A vs arm B at matched flow, plus absolute cooling below ambient). Not pure theory. |
| **Replicable** | YES — Home, straw: ~$40–120 for a tote, copper tube and coil, fittings, two orifice caps, a small cooler box, three 0.1 °C thermometers, a bucket and a stopwatch. No mains work, no chemicals, no combustion, no heat. The one demanding requirement is matching flow between arms to ±10 %, which is why the VOID path is first-class. |
| **Relevant** | YES — Food domain, and it fills a real gap: the food field's cards cover fermentation *vessel geometry* (010), germination timing (015), ripening (020), growth stimulation (026), sowing timing (032) and succession order (038) — **none covers preservation by temperature**, and none is a cold-storage card. Fills the **Food Prep** mirror (living food / food preparation and preservation), 3rd card. |
| **Honest** | YES — and this is the card's spine: the source **debunks its own headline** (over-unity = *"perpetual-motion fantasy"*), so the card tests only the cooling, and only the half of the cooling that is extraordinary. The claim is framed as a claim; the card is a test, not an endorsement. Clean FAIL, VOID and ARTIFACT paths, and the alternate mechanism (swirl atomization) is named in advance. |
| **Linked** | YES — A Vault translation, the scout entry that flagged it, the Schauberger claim record, a pre-registered replication dossier, and cross-links to five related cards. |

**Mirror choice, stated:** the card's **domain is food**, and **Food Prep** is the honest fit — it already carries the two other preservation cards (010 fermentation vessel, 033 storage desiccation), and a cold store completes the preservation triad: **fermentation · desiccation · refrigeration**. **Homesteading** ("self-reliance / off-grid") was the closest thematic alternative and was not chosen because it already carries two cards and the mirror map's own instruction is to fill the emptiest; **Plumbing & Hot Water** ("water vortex / living water") was the second alternative and was not chosen because it already carries four cards (001, 009, 025, 031) and because the card's *outcome* is preserved food, not supplied water.

---

## The honest framing (the spine of the card)

**The claim is a claim — and its source is unusually candid about being wrong.** Most over-unity writing asserts an effect and stops. This article builds the machine in loving detail, then devotes a section to why it cannot work: it *"crosses the red line of conservation of energy,"* it is *"perpetual-motion fantasy,"* its core concepts have *"no mathematical models and no repeatable experiments."* That candour is exactly what makes the source usable — it hands us the part it still believes (the cooling) and the part it has given up on (the energy). **The card tests the first and ignores the second.**

**What the card tests.** Not "free energy," and not "water memory." One comparison: **does water come out of a vortex-shaped tube colder than out of a straight tube of the same length, through the same orifice, at the same flow?**

**The design that makes it a measurement.** Three things do the work:

1. **The same orifice on both arms.** Flash evaporation at a 1 mm jet cools water regardless of the tube's shape. Put the identical orifice on both arms and that cooling is present in both and cancels — leaving only the vortex term. A card that asked "does it get cold?" would measure evaporation and prove nothing.
2. **The comparison is vortex versus straight at matched flow, not device versus nothing.** Same water, same head, same orifice, same insulation. Only the tube's shape differs. Mainstream fluid mechanics predicts the vortex arm should be *slightly warmer* (Dean vortices add dissipation), which makes the sign of the result itself discriminating: the claim says colder, the textbook says warmer-or-equal.
3. **Arm C is the clean signal.** The coil with **no orifice** has no evaporation at all. If arm C cools, the vortex alone is doing something. If arm C is flat while A and B both cool, the cooling is evaporation and nothing else — and that is a complete answer.

**The confound named in advance.** A coiled tube has **more surface area** than a straight tube of the same developed length, so an uninsulated coil exchanges more heat with the room — which can look exactly like a vortex effect. The card requires **both arms insulated identically** and ambient logged and stable, and it makes "the difference tracks surface area" an explicit ARTIFACT test rather than a footnote. A second alternate mechanism is named too: a swirl at the orifice can **atomize the spray more finely**, increasing evaporation. That is a real effect — but it is not "spontaneous vortex cooling," and the card asks for photographs of both sprays so the two can be told apart.

**The central limitation, stated up front: a home rig is a screen, not a calorimeter.** The claim is old, unreplicated with modern instrumentation, and the effect (if any) may be far below what a bucket and a kitchen thermometer can resolve. That is why **VOID is a first-class outcome** and why the card requires the achieved resolution and the control that would be needed to be reported either way. **A rig that cannot hold its controls has not tested anything.**

**Two outcomes, reported separately.** The **practical** outcome — does the chamber hold a jar below ambient, and by how much — is a homesteading capability, and it will almost certainly be positive, because evaporation works. The **claim** outcome — is the vortex arm colder than the straight arm — is the science, and it is the one that can fail. Conflating them is exactly how a device that merely evaporates gets sold as a vortex engine.

**Safety:** gravity-fed water only — no mains, no chemicals, no combustion, no heat. Vent the spray chamber's lid so pressure cannot build, lift the tank safely, and keep the outlet clear.

---

## Relationship to the rest of the queue

This is the **first card in the queue that isolates a vortex's contribution to cooling against a matched straight-arm control**, and the **first whose source debunks its own headline claim**. Dossier 001 measures a temperature differential across a hyperbolic funnel — but with no orifice and no straight-arm control, so its endpoint cannot separate vortex from geometry from ambient. Dossier 024 measures flow and head in a spiral pipe, with temperature only a noted side-claim. This card asks the one question neither can: **is the vortex term real, once evaporation is subtracted?**

Its nearest neighbours are **024** (Spiral-Pipe Friction — the *flow* half of the same 1952 lineage; this is the *temperature* half) and **001** (Wasserwirbler — the temperature differential without the control). Together the three make the vortex lineage's two measurable claims — resistance and cooling — legible for the first time, both against proper controls. And on the food side it sits beside **010** (fermentation) and **033** (desiccation) to complete the preservation triad.
