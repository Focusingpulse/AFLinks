---
name: Korschelt Aether-Ray Ripening Test
description: Aetherforce quest card — food-domain blind triangle test of Oskar Korschelt's 1892 claim that a galvanic-element "aether ray" apparatus ripens wine/spirits and promotes plant growth. Home-replicable (~$30-60). Branded to Aetherforce.
---

# ⚡ Aetherforce

**Quest Card: Korschelt Aether-Ray Ripening Test**

---

## Village data.js block

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Commerce",
  desc: "Test Oskar Korschelt's 1892 claim that a galvanic-element 'aether ray' apparatus ripens sealed wine and spirits — improving their taste — and promotes plant growth. Run a blind triangle test to see whether the taste change survives when the taster doesn't know which bottle was treated. Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Korschelt Aether-Ray Ripening Test",
    "Build a simplified Korschelt ray apparatus: a sheet-metal tube with two discs ~4 cm apart connected to a low-voltage DC source, plus a wire spiral along the tube. Split 6 matched bottles of a young wine or spirit into treated (3, inside the tube, energized 2-7 days) and control (3, same room, unpowered). Then run a blind triangle test: 9 trials, each with 3 cups (two from one bottle, one from the other), taster identifies the odd cup and states a preference. Measurable outcome: taster correctly identifies the odd cup in at least 6 of 9 trials (p<0.05). Optional plant arm: run the Fig. 10 star-disc apparatus under one of two matched potted plants for 14 days and compare new shoot growth.",
    ["Science", "Commerce", "Food", "Self-Reliance"],
    "🍷"
  ],
  source_doc: "korschelt-1892-aether-ray-ripening",
  dossier: "living-library/synthesis/replication/2026-09-16-dossier-020-korschelt-aether-ray-ripening.md",
  pass_fail: "PASS: Taster identifies the odd cup in >=6 of 9 blind triangle trials (p<0.05) AND prefers the treated sample in a majority of trials; plant arm shows >20% greater new shoot growth than control, repeated in a second run. FAIL: <=3 of 9 correct (chance) — taste effect not detectable blind. INCONCLUSIVE: 4-5 of 9 correct, or effect in one beverage type only, or plant difference within measurement noise.",
  evidence: "Photos of apparatus (tube, discs, wiring, power source, bottles in place). Settings: voltage, polarity, disc spacing, tube length, run duration. Answer key recorded before tasting + randomization method. Full 9-trial triangle sheet (correct/incorrect + preference). Negative control and sham (power-off) control results. Plant arm day-0/day-14 photos + shoot measurements if run. Observer notes (warmth, smell, sediment)."
}
```

---

## Quest Summary

**Title:** Korschelt Aether-Ray Ripening Test
**Tier:** Sand (home-scale, ~$30-60, 2-7 day irradiation + one tasting session)
**Domain:** Food (beverage ripening / preservation)
**Guild Mirror:** Commerce (value of a preserved product — the empty mirror)

**The Claim:** Oskar Korschelt (1892) reported that sealed bottles of wine and spirits placed inside his "aether ray apparatus" — a galvanic element driving metal plates and wire spirals — improved substantially in taste after 2-7 days, judged by a retired wine merchant and a circle of connoisseurs. He also reported that potted plants grew only while the apparatus ran and withered when it was switched off. He framed the wine result explicitly as commercial value.

**The Test:** Rebuild a simplified version of the apparatus, treat sealed bottles, and run a **blind triangle test** — the design upgrade the original 1892 trials lacked.

**Measurable Outcome:** The taster correctly picks the odd cup in ≥6 of 9 blind triangle trials (p<0.05) and prefers the treated sample in a majority of trials.

**Honest Framing:** The original trials were **unblinded** and the outcome was **subjective taste** — the two classic ways a real effect is manufactured out of nothing. Korschelt himself distrusted his own palate and worried about evaporation. Under a blind protocol the expected result for a skeptic is **no detectable effect**. A PASS would be genuinely anomalous; a FAIL honestly retires the claim for family purposes. Either outcome is a real result.

---

## Source Documentation

- **Dossier:** `living-library/synthesis/replication/2026-09-16-dossier-020-korschelt-aether-ray-ripening.md`
- **Translation:** `living-library/translations/2026-09-15-korschelt-1892-nutzbarmachung-lebendigen-kraft-aethers-de.md` — pp. 197-206 (wine/spirit ripening), pp. 74-76 (ray-apparatus construction), pp. 108-110 (long-wave generator), pp. 240-242 (plant-growth apparatus, Figs. 10-11)
- **Original scan:** https://www.naturschule-oberlausitz.de/wp-content/uploads/2022/08/DieNutzbarmachungderlebendigenkraftdesaethers1892-korschelt.pdf
- **Scout find:** `living-library/sources/2026-09-16-scout-a-de-fr-ja.md`
- **Author:** Oskar Korschelt (1892)
- **Aetherforce reference:** search "Korschelt" / "aether ray" / "long waves" on https://www.aetherforce.energy
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

*Merge note: `name` uses the guild label "Aetherforce — Commerce" per the mirror map (AETHERFORCE-QUESTS.md #18). village-maintain should confirm the exact guild name against data.js at merge time.*
