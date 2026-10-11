---
name: Quest Card — Wood Acoustic Resonance Test
description: Aetherforce-branded quest card for testing whether wood grain density correlates with acoustic resonance — Round Wood guild complement.
---

# ⚡ Aetherforce — Wood Acoustic Resonance Test

**Tier:** sand
**Domain:** shelter (building materials)
**Guild complement:** Round Wood (material resonance)
**Created:** 2026-09-13

---

## Quest

Test Schauberger's claim that "resonance wood" — slow-grown wood with tight annual rings — has superior acoustic properties. Compare wood samples of varying grain density using a simple tap test and sound analysis.

**Title:** Wood Acoustic Resonance Test
**Description:** Collect wood samples from different trees or species. Count annual rings per inch (grain density). Tap each sample and measure how long the note sustains. Test whether tighter grain correlates with longer resonance.
**Subjects:** Science, Woodworking, Observation
**Emoji:** 🪵

---

## Village data.js Schema Block

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Round Wood",
  desc: "Test whether wood grain density affects acoustic resonance. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Wood Acoustic Resonance Test",
    "Collect 3-5 wood samples from different trees or species. Count annual rings per inch. Tap each sample with consistent force and record the sound. Use a free sound analyzer app to measure sustain time (how long the note rings). Compare: Does tighter grain correlate with longer sustain?",
    ["Science", "Woodworking", "Observation"],
    "🪵"
  ],
  source_doc: "translations/2026-09-09-schauberger-water-blood-of-earth-de.md",
  dossier: "living-library/synthesis/replication/2026-09-13-dossier-016-wood-resonance.md",
  pass_fail: "PASS: Sample with tightest grain shows ≥20% longer sustain than sample with widest grain. FAIL: No consistent correlation between grain density and sustain time.",
  evidence: "Photos of wood grain (showing annual rings), audio recordings of tap tests, sustain time measurements from sound analyzer app, data table comparing grain density vs. sustain time."
}
```

---

## Source Documentation

- **Source document:** `translations/2026-09-09-schauberger-water-blood-of-earth-de.md` (Schauberger, "Water - The Blood of the Earth", German text translated)
- **Key passage:** "It is known that with the onset of forest management... the qualitatively most valuable wood... the so-called resonance wood, disappeared at a single stroke... This slowly growing wood exhibits... annual rings that are almost invisible to the naked eye... Resonance wood... is used primarily in instrument making. The wonderful tone color of the instruments made from this wood... points not only to the healthiest, because most natural, form of development; this wood also has an almost unlimited durability."
- **Replication dossier:** `living-library/synthesis/replication/2026-09-13-dossier-016-wood-resonance.md`
- **Aetherforce site:** search "Schauberger" / "resonance wood" on https://www.aetherforce.energy

---

## Rubric Justification

- **Practical:** Named apparatus (wood samples + smartphone app) with measurable outcome (sustain time in seconds)
- **Replicable:** Home-scale (<$50), requires only wood samples and free sound analyzer app
- **Relevant:** Maps to shelter domain (building materials) and Round Wood guild complement (material resonance)
- **Honest:** Framed as test of contested claim; correlation ≠ causation, but measurable relationship
- **Linked:** Source doc, dossier, and Aetherforce reference all provided

---

## Status

**Status:** proposed
**Next step:** Chris approval → merge to Village data.js
