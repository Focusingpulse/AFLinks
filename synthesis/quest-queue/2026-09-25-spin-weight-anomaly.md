---
name: Spin-Weight Anomaly Test
description: "Weigh a rotor spinning clockwise and counterclockwise about a vertical axis and measure the direction-difference, in milligrams, against the balance's own repeatability. Energy/spin-axis card; ~$100–180; Rocket mirror. The queue's first card whose source claim has already been REFUTED in the peer-reviewed literature — and it says so."
---

# ⚡ Aetherforce — Power

**Guild:** Aetherforce — Power
**Quest Line:** ⚡ Aetherforce · Rocket complement
**Tier:** straw
**Domain:** energy (a rotating body's weight — the spin / gyroscopic-force axis)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-25-spin-weight-anomaly` · authored_at `2026-09-25` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Power",
  desc: "The torsion lineage's founding experiment: does a spinning rotor weigh less when it turns one way than the other? Weigh a rotor at the same speed clockwise and counterclockwise, on a balance that can see a milligram, with the vibration the source says the effect requires running identically in both arms. The comparison is CW vs CCW, not spinning vs still — that cancels vibration, air, heat and drift in one move. Four independent labs tested this claim in 1990-91 and found nothing, and one of them showed exactly how the original false positive was made. Build it, run it, and find out for yourself what a null looks like. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Spin-Weight Anomaly Test",
    "Mount a 90-180 g metal rotor on a motor with a vertical axis, on a rigid platform, on a 0.001 g scale, inside a clear box that stops air currents, with a slack power loop so the leads don't load the pan. Clamp a small unbalanced motor to the platform as the vibration source - the source says the effect needs it. Pre-register your speeds (about 3,000 and 8,000 rpm), arm order, reading count and thresholds. Then run five arms, interleaved, five times on different days: motor off with vibrator on (the noise floor), CW and CCW at each speed with the vibrator on, and CW and CCW with the vibrator OFF. Hold the speed steady - do not weigh it as it spins down - let the temperature stabilise, and log the rotor temperature every arm. Measurable outcome: the direction-difference delta = mean(CW) - mean(CCW) in milligrams, at each speed, against the off-arm repeatability; PASS is |delta| >= 3x the repeatability, same sign in 4 of 5 sessions, growing with speed, and absent with the vibrator off. If |delta| stays inside the noise, that is the published result and a complete one.",
    ["Science", "Engineering", "Measurement"],
    "🌀"
  ],
  source_doc: "translations/2026-09-15-lether-fluide-et-tourbillonnaire-des-champs-de-torsion-fr (Alain Boudet, 'L'ether fluide et tourbillonnaire des champs de torsion' - Kozyrev's 8 mg/90 g/25 m-per-s figures, the CCW-only condition, the vibration condition, Kozyrev's own balance design, DePalma's balls and gyroscope) + translations/2026-09-25-torsion-field-and-qi-li-si-chen-zh (Li Si-Chen, NTU, 2006 - the same claim in a credentialed voice)",
  source_url: "https://spirit-science.fr/doc-pdf/torsion.pdf",
  dossier: "living-library/synthesis/replication/2026-09-25-dossier-041-spin-weight-anomaly.md",
  pass_fail: "PASS: direction-difference |delta| >= 3x the off-arm repeatability, same sign in >=4 of 5 sessions, growing with speed, and absent (approximately 0) with the vibrator off - either rotation sense counts, since Kozyrev reports counterclockwise and Hayasaka reports clockwise. FAIL: |delta| <= the off-arm repeatability in >=4 of 5 sessions - no direction-dependent weight anomaly at home scale. THIS IS THE EXPECTED RESULT and matches the four published nulls (Faller et al. NIST PRL 64,825 1990; Nitschke & Wilmarth LBNL PRL 64,2115 1990; Quinn & Picard Nature 343,732 1990; Imanishi et al. JPSJ 60,1150 1991); an honest negative, Skeptic's Star. VOID: the off-arm repeatability exceeds the predicted effect size (about 8 mg x rotorMass/90 g x peripheralSpeed/25 m-per-s) - the rig cannot resolve the claim; report the noise floor and the resolution required, NOT a verdict. ARTIFACT: delta tracks the rotor temperature difference between arms, or appears with the vibrator off, or vanishes when speed is held steady instead of run down - record the known artifact (Quinn & Picard traced theirs to the friction couple and temperature).",
  evidence: "Photo of the rig (rotor, motor, platform, vibrator, enclosure, scale) + the pre-registration sheet (speeds, arm order, reading count, thresholds, scoring rule) + the reference-mass check between arms + every arm's raw readings with the rotor temperature logged + the off-arm repeatability calculation shown + the CW-CCW difference at each speed with its session-to-session spread + the vibrator-off arms reported separately + the five sessions dated + the void check (predicted effect size vs measured noise floor) reported whether or not it voids the run"
}
```

---

## Source Documentation

- **Primary:** Alain Boudet, *"L'éther fluide et tourbillonnaire des champs de torsion"* (Dr. in Physical Sciences) — https://spirit-science.fr/doc-pdf/torsion.pdf — held in the Vault as `translations/2026-09-15-lether-fluide-et-tourbillonnaire-des-champs-de-torsion-fr.md`. It carries the whole claim in one place: the abstract (*"the experiments of DePalma and Kozyrev show that the weight of a rotating object is modified under certain conditions"*), **Kozyrev's numbers** (*"8 mg for a gyroscope of 90 g and 4.6 cm in diameter spinning at 25 m/s at its periphery … proportional to the gyroscope's weight and to its peripheral rotation speed"*), **the direction condition** (*"true only when the axis of rotation is vertical and the gyroscope spins counterclockwise. The reduction is zero if the gyroscope spins clockwise"*), **the vibration condition** (*"observed only if they are subjected to an additional movement, for example a vibration"*), **Kozyrev's own balance design** (a light rod on a nylon thread, no pans, asymmetrical for sensitivity), and the related **DePalma** ball and gyroscope free-fall experiments.
- **Second source:** 李嗣涔 (Si-Chen Lee), *"Torsion Field and Qi"*, 《生命學報》Journal of Life Sciences, 2006 — `translations/2026-09-25-torsion-field-and-qi-li-si-chen-zh.md`. The same claim from a former university president: *"a rotating gyroscope in a special mode of oscillation shows a slight change in weight depending on the speed and direction of rotation"*, with Veinik (1970s) as confirmation and Hayasaka–Takeuchi (1989) as the free-fall version. **It also dismisses the null results** — *"it was pointed out that those gyroscopes whose weight did not change were not being moved"* — an uncited assertion about the null experimenters' apparatus, and the reason this card exists in the form it does.
- **The refutations (verified this run):** Faller, Hollander, Nelson & McHugh (NIST), *Phys. Rev. Lett.* **64**, 825 (1990) — *"no anomalous weight changes of the magnitude reported that depend on rotor speed and/or rotational sense."* Nitschke & Wilmarth (LBNL), *Phys. Rev. Lett.* **64**, 2115 (1990) — null, limit **−0.025 ± 0.07 mg**, two orders of magnitude below the claimed effect. Quinn & Picard, *Nature* **343**, 732 (1990) — apparent changes ~5% of the claimed size, **gone after correcting for the friction couple and temperature**. Imanishi, Maruyama, Midorikawa & Morimoto, *J. Phys. Soc. Jpn.* **60**, 1150 (1991) — null, (−0.20 ± 0.35) mg left and (−0.02 ± 0.33) mg right.
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-25-dossier-041-spin-weight-anomaly.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "torsion field", "Kozyrev", "gyroscope"
- **Aetherforce Reference:** Search "torsion field", "Kozyrev", or "ether physics" on https://www.aetherforce.energy
- **Related dossiers:** 036 (Sealed-Box Electrostatic Thrust — the other force-anomaly card), 024 (Spiral-Pipe Friction — the other foundation-result test), 018 (Bladeless Tesla Turbine — rotation as conversion, not force)
- **Claim status record:** `synthesis/claim-status-records/soviet-torsion-psychotronics-1960s.json` (status `suppressed`)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (a rotor on a motor, a 0.001 g balance, a vibration source, an enclosure) with a named procedure (five arms, interleaved, five sessions) and a measurable outcome (the clockwise−counterclockwise weight difference in milligrams against the balance's own repeatability). Not pure theory. |
| **Replicable** | YES — Home, straw: ~$100–180 for a 1 mg scale, a motor and rotor, a vibrator, and an enclosure. No mains work, no chemicals. The source's own cheaper instrument (a light rod on a nylon thread, read with a laser pointer) is offered as an alternative. |
| **Relevant** | YES — Energy domain, and it fills a real gap: every other energy card is about *harvesting* or *converting* energy; **none touches rotation as a force.** Fills the **Rocket** mirror (free energy / implosion — the rotation-and-force complement), 3rd card. |
| **Honest** | YES — and this is the card's distinguishing feature: **the source claim is already refuted, and the card says so in its own text**, naming all four null studies and the mechanism of the original false positive (Quinn & Picard's friction couple and temperature drift). The claim is framed as a claim; the card is a test, not an endorsement; and the expected outcome is stated up front. Clean FAIL path. |
| **Linked** | YES — Two source docs (one translation carrying the full quantitative claim, one carrying it in a credentialed voice), a pre-registered replication dossier, the claim-status record, and cross-links to three related cards. |

**Mirror choice, stated:** the card's **domain is energy** (the rotation's next field) and its **guild complement is Rocket** — whose complement theme is *free energy / implosion*, i.e. rotation-based force and energy claims, and whose seed candidate is the Repulsine, itself a rotation device. **Oddball** (cross-field bridges / suppressed-science re-try candidates) was the alternative and is a fair thematic fit for a refuted suppressed-science claim; it was not chosen because the object here is a *rotating body's weight* — a force claim of exactly the class the Rocket complement exists for — and because Oddball already carries a card (017, orgone accumulator).

---

## The honest framing (the spine of the card)

**The claim is a claim — and this one has already been tested and closed.** The torsion lineage's founding experiment asserts that a spinning rotor's weight depends on the direction of its rotation about a vertical axis. Kozyrev reported 8 mg on a 90 g gyroscope at 25 m/s peripheral speed, counterclockwise only. Hayasaka and Takeuchi published a version in *Physical Review Letters* in 1989 — **clockwise only**, the opposite sense — and it was repeated within two years by four independent groups, **all of which found nothing**. The NIST and LBNL limits sit two orders of magnitude below the claimed effect.

**Why the card exists anyway.** Because **the archive still carries the claim as live.** The Boudet document presents it as established and does not mention the nulls. The Li Si-Chen paper mentions them and waves them away with an uncited assertion about the null experimenters' apparatus. **A family reading only the vault would not know the claim was closed.** The archive preserves claims; the engine tests them and reports the verdict — and here the verdict is already in the literature, so the card's job is to hand it over honestly rather than pretend the question is open.

**The design that makes it a measurement.** Three things do the work:

1. **The comparison is clockwise versus counterclockwise, not spinning versus still.** Vibration, air movement, motor heating, the motor's magnetic field and the scale's drift are all identical in the two arms; only the sense of rotation differs. A spinning-versus-still comparison would be swamped by every one of them at once — and that is precisely the comparison that produced the original false positive.
2. **The vibration-off arm tests the source's own condition.** The source says the effect appears *only* with an additional movement. So the card runs CW and CCW with the vibrator off too. If a direction-difference shows up there, the source's stated condition is wrong — a discriminating prediction, not a decoration.
3. **Temperature is logged, not ignored.** Quinn & Picard's apparent effect **disappeared once temperature and the friction couple were corrected for.** That is the card's most valuable lesson: if the direction-difference tracks the rotor temperature, the family has just reproduced a known artifact with their own hands and watched it die.

**The central limitation, stated up front: a home rig cannot match the published limits.** The nulls were run on precision balances at 0.07 mg and better. A $50 scale resolves 1 mg. So a **home null is weaker evidence than the published nulls** — it says "not visible at 1 mg on this bench," not "the effect does not exist." That is why the **VOID** condition is a first-class outcome: a rig whose noise floor exceeds the predicted effect has not tested the claim, and the card requires the noise floor to be reported either way.

**A null is the expected outcome, and it is a complete result.** The family gets a measured null, the four published nulls cited beside it, the artifact mechanism in their own hands, and the Skeptic's Star. That is the archive's epistemics taught at the bench.

**Safety:** the rotor is a spinning mass — guard it, keep fingers and hair clear, secure the platform so it cannot walk off the scale, and use a low-voltage motor supply. Nothing here is mains-voltage work.

---

## Relationship to the rest of the queue

This is the **queue's first card whose source claim has already been refuted in the peer-reviewed literature**, and it is the first card that asks a family to reproduce a *null* rather than to test an open question. Every other card here tests a claim that is open or contested, where a null is a new datum; here the null is known, and reproducing it — with the confounds named in advance — is the exercise.

It is also the **first energy card about rotation as a force** rather than rotation as a converter. 008, 018, 024 and 031 all turn motion into something else; this one asks whether the motion changes the object's weight at all.

Its nearest neighbour is **card 036** (Sealed-Box Electrostatic Thrust) — the queue's other force-anomaly card, and its precedent for emitting a card where a null is the likely outcome. The difference is worth stating plainly: **036's claim is unreplicated; this one is refuted.** The card carries that distinction in its own text.
