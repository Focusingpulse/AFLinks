---
name: Quest Card — Qi-Water Conductivity Test
description: Aetherforce-branded quest card testing the energy-healing claim — that a person can emit "Qi" and change a water sample's electrical conductivity — with a blinded meter protocol at 40±1°C. Natural Medicine guild complement, health domain.
---

# ⚡ Aetherforce — Qi-Water Conductivity Test

**Guild:** Aetherforce — Natural Medicine
**Quest Line:** ⚡ Aetherforce · Natural Medicine complement
**Tier:** sand
**Domain:** health
**Status:** proposed
**Created:** 2026-09-17

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Natural Medicine",
  desc: "The energy-healing traditions say a person can emit a healing influence — Qi, Reiki, 'the gift.' The strongest version of that claim isn't 'it feels nice'; it's 'something changes matter.' In 1993 a Japanese team put it to a meter: 10 Qi senders imposed Qi on water and measured the water's electrical conductivity at 40±1°C. Their own results were mixed — three different conductivity curves from an identical method, and no imprint at all in purified water. Nobody in the archive has repeated it. You will. Code eight cups so the measurer stays blind, have someone attempt Qi on half of them while the other half is handled exactly the same way without any attempt, and measure conductivity before and after at a held 40±1°C. Measurable outcome: a blinded conductivity shift in the attempted cups of at least 2× your meter's own repeat-measurement noise, consistent in 2 of 3 sessions, with no such shift in the handled-only cups. Find it and you have a real anomaly; find nothing and your family has honestly retired the claim on its own bench. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Qi-Water Conductivity Test",
    "Build a blinded water bench: one handheld EC/TDS meter (~$30–40), three water types (distilled, tap, mineral — each split from a single bottle across all cups), eight identical lidded glass cups, a thermometer, and a warm bath held at 40±1°C. First measure the meter's noise floor (10 repeated readings of one sample → standard deviation). Then a non-participating family member codes the cups A–H and seals the key. Measure baseline conductivity of every cup at 40±1°C; a 'sender' attempts Qi on half the cups while the other half is handled identically but with no attempt; re-measure blinded; repeat 3 sessions on different days, re-coding each time. Finally run the ions test — distilled vs tap vs mineral — because the 1993 study found Qi did NOT imprint into purified water. Measurable outcome: attempted-group mean conductivity change ≥2× the measured meter noise, direction consistent in ≥2 of 3 sessions, with no comparable shift in the handled-only controls = the healing claim showed up in an instrument in your kitchen; no difference = a clean, publishable null with the archive's own source cited.",
    ["Science", "Measurement", "Health"],
    "🙌"
  ],
  source_doc: "sources/2026-09-16-scout-a-de-fr-ja.md (find #9) — Sasaki, Sako & Kobayashi, J. Mind-Body Science 2(1), 1993, DOI 10.20788/jmbs.2.1_1",
  source_url: "https://www.aetherforce.energy",
  dossier: "living-library/synthesis/replication/2026-09-17-dossier-022-qi-water-conductivity.md",
  pass_fail: "PASS: blinded attempted-group EC change ≥2× measured meter noise AND direction consistent in ≥2 of 3 sessions AND handled-only controls show no comparable shift | FAIL: no difference between attempted and control groups, or both shift equally (handling/temperature, not Qi) — honest negative, Skeptic's Star | INCONCLUSIVE: effect below the 2× threshold, <3 sessions, or temperature/CO2 drift dominated the readings",
  evidence: "Photo of the bench (meter, cups, bath, thermometer); the sealed code key photographed sealed and opened only after numbers are recorded; noise-floor table (10 readings → SD); raw EC readings per cup per session (baseline and after); the distilled-vs-tap-vs-mineral ions test side by side"
}
```

---

## Source Documentation

- **Primary source (open access, English abstract):** Sasaki Shigemi, Sako Yoichiro & Kobayashi Yasuki, 「気功水の電導率変化から見た気の性質」 ("Properties of Qi as seen from conductivity changes in Qi-water"), *人体科学 / Journal of Mind-Body Science* **2**(1), 1993 — DOI [10.20788/jmbs.2.1_1](https://doi.org/10.20788/jmbs.2.1_1) · [J-STAGE record](https://www.jstage.jst.go.jp/article/jmbs/2/1/2_KJ00005467816/_article/-char/ja/)
- **Scout record:** `sources/2026-09-16-scout-a-de-fr-ja.md` find #9 — rarity: rare (thinly known in the West), host stable (J-STAGE); scout flags `practical_applicability: reproducible` with the note that "ions required for Qi imprinting" is a testable constraint
- **Companion find, same scout run:** `sources/2026-09-16-scout-a-de-fr-ja.md` find #10 — Kokushikan University wave-water stress-recovery double-blind EEG study (n=7, α/β ratio) — the same Japanese "wave water" (波動水) tradition tested on *people* rather than water; the natural follow-up card for the physiology side
- **Related lineage — water as information storage:** `translations/2026-09-15-zenin-water-as-information-storage-ru.md`; EZ-water card `synthesis/quest-queue/2026-09-11-ez-water-exclusion-zone.md` (dossier 009)
- **Context — suppression is not evidence:** `synthesis/claim-status-records/rife-beam-ray-ama-1939.json` documents a health device suppressed by the AMA in 1939. That history is real and worth preserving; it is **not** evidence for the device's claim. This card tests a claim on its own merits — it does not inherit a verdict from a suppression story.
- **Replication Dossier:** `synthesis/replication/2026-09-17-dossier-022-qi-water-conductivity.md`
- **Aetherforce Reference:** search "water memory" / "structured water" / "Qi" on https://www.aetherforce.energy

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (EC meter, lidded cups, 40±1°C bath) with a measurable outcome (blinded conductivity change vs the meter's own noise floor) |
| **Replicable** | YES — Home-tier, ~$30–40 meter + kitchen items; any family, one evening per session |
| **Relevant** | YES — Health domain (energy healing / biofield); complements the original Natural Medicine guild, whose second seed candidate was explicitly "structured water for health" |
| **Honest** | YES — Claim framed as a claim; the 1993 study's *own* mixed findings and its "no imprint in purified water" null stated up front; mainstream no-mechanism position named; clean FAIL path; suppression story explicitly separated from evidence |
| **Linked** | YES — Primary source with DOI, scout record, dossier 022 with pre-registered pass/fail, companion EEG find, related water-memory lineage, Aetherforce reference |

**Why this card:** the archive preserves the energy-healing claim across a dozen traditions, and every one of them rests on a felt experience. This is the rare case where the tradition itself reached for an instrument — and then nobody followed up. The test is cheap, blindable, and the original paper's own inconsistency is the honest baseline. It is also the health-domain twin of the Earth-Energy Grid card: the same move, applied to a different wrong turn — **ask the claim to show up in a number, not a feeling.**

---

## Aetherforce Mirror Coverage

This card fills **Guild 19: Natural Medicine** (subtle energy / biofield) — its second seed candidate, "structured water for health."

**Coverage stays 22/26.** The four mirrors still empty are all craft guilds — **Tool Care, Dim Lumber Woodworking, Textiles, Metalworking** — and none of them has a health-domain candidate with a verifiable buildable source. Rather than force a mirror, this run says so plainly.

---

## Family Check-in

```
Member: practicality-engine
Run: 2026-09-17 14:00 UTC
Budget: gate passed (essential, gear overdrive)
Field: health (rotating from shelter)
Card: 1 of 3 daily
Status: emitted
Watchdog: gate reported 19 stale siblings (noted, not blocking)
```

---

*Generated by the Engine of Practicality — 2026-09-17*
