---
name: Eeman Circuit Sleep Quality Test
description: Aetherforce quest card — test whether the Eeman biocircuit used before bed improves sleep quality. Home-replicable. Branded to Aetherforce.
---

# ⚡ Aetherforce

**Quest Card: Eeman Circuit Sleep Quality Test**

---

## Village data.js block

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Natural Medicine",
  desc: "Test whether the Eeman self-connecting copper circuit (no power) improves sleep quality when used before bed. Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Sleep Quality Biofield Test",
    "Build an Eeman circuit (insulated copper wire, head band, hand/foot contacts, ~$10). Use it for 15 minutes before bed on 7 nights (randomly selected). Compare sleep quality (duration, wake-ups, morning alertness) vs 7 control nights (no circuit). Log each morning. Measurable outcome: sleep quality score difference ≥15% supports the claim.",
    ["Science", "Health", "Self-Reliance"],
    "🌙"
  ],
  source_doc: "dossier-012-eeman-sleep-quality",
  dossier: "living-library/synthesis/replication/2026-09-12-dossier-012-eeman-sleep-quality.md",
  pass_fail: "PASS: circuit nights ≥15% higher sleep quality score vs control, replicates across ≥2 testers. FAIL: no meaningful difference (within 5%). INCONCLUSIVE: small difference that doesn't replicate.",
  evidence: "Morning logs: sleep hours, wake-ups, alertness (1-10). Photos of circuit setup. Summary table comparing circuit vs control nights."
}
```

---

## Quest Summary

**Title:** Sleep Quality Biofield Test
**Tier:** Sand (home, ~$10, 2-week protocol)
**Domain:** Health (sleep / rest / recovery)
**Guild Mirror:** Natural Medicine (Aetherforce complement family)

**The Claim:** The Eeman biocircuit — a self-connecting copper coil with no power source — promotes relaxation and improves sleep quality when used before bed.

**The Test:** 14-night protocol. 7 circuit nights (15 min pre-sleep use), 7 control nights. Randomized order. Morning logs track sleep duration, wake-ups, and alertness. Compare average sleep quality scores.

**Measurable Outcome:** Sleep quality score = (alertness × 10) − (wake-ups × 5) + (sleep hours × 3). Circuit nights ≥15% higher than control supports the claim.

**Honest Framing:** This is a TEST of a contested biofield claim, not an endorsement. A FAIL result is valuable (Skeptic's Star) — it honestly retires the advice for this family.

---

## Source Documentation

- **Dossier:** `living-library/synthesis/replication/2026-09-12-dossier-012-eeman-sleep-quality.md`
- **Prior dossier:** `living-library/synthesis/replication/2026-09-06-dossier-002-eeman-circuit.md` (relaxation/pulse test)
- **Aetherforce reference:** search "Eeman" / "biocircuit" on https://www.aetherforce.energy
- **Vault link:** https://focusingpulse.github.io/AFLinks

---

## Aetherforce Branding

This quest is part of the **Aetherforce mirror family** — one quest per original Permies guild, testing self-reliance technologies from the alternative science archive. Each card:

- Carries the ⚡ Aetherforce mark
- Links to the Vault (source docs + dossiers)
- Frames the quest as a TEST, not endorsement
- Counts toward Aetherforce custom progression (NOT Permies badges)

---

## Status

**Proposed** — awaiting Chris approval before merge into Village quest data.
