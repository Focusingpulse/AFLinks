---
name: Quest Card — Hammer-Charged Blade Test
description: Aetherforce-branded quest card testing Schauberger's tool claim — that a hammer-peened blade carries a "charge" that improves cutting and feeds plant regrowth, and that sunlight "flattens" it — with a blinded cutting bench and a sward-regrowth arm. Tool Care guild complement, community domain (shared tool care).
---

# ⚡ Aetherforce — Hammer-Charged Blade Test

**Guild:** Aetherforce — Tool Care
**Quest Line:** ⚡ Aetherforce · Tool Care complement
**Tier:** sand
**Domain:** community (shared tool care / shared-infra knowledge)
**Status:** proposed
**Created:** 2026-09-17

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "homestead"],
  name: "Aetherforce — Tool Care",
  desc: "Viktor Schauberger claimed something strange about a scythe. Hammer the edge against a hardwood block — not an iron anvil — and the blade takes on a 'charge'; that charge is released at harvest and feeds the grass you cut; and if you leave the blade in the sun, the charge drains out and the edge goes 'flat.' He also said a hammered edge beats a ground one. Here is the part that makes it worth your bench: the sun claim has no other explanation. Same blade, same steel, same edge — an hour of sunlight is the only difference. If the charge is real, the sun blade cuts worse. If it isn't, the two blades are identical, and no story about edge geometry can save the difference. You will blind the blades, count strokes, mow three matched plots, and weigh what grows back. Find a difference and you have an anomaly 90 years old and never benched; find nothing and your family has honestly retired a claim — and learned to peen an edge while you were at it. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Hammer-Charged Blade Test",
    "Get three sickles or machetes of the same type (~$10–30 each). Peen two edges with a hammer on a hardwood block; file the third ('the normal way'). Leave one peened blade in full sun for an hour, the other in the dark. A family member who will not score codes all three and seals the key. Then the blinded bench: 10 uniform grass bundles per blade in randomized order, scorer counts strokes to sever each bundle; keep going until strokes double, and record strokes-to-failure. Finally mow three matched 1 m² plots, one per blade, and weigh regrowth at 2 and 4 weeks. Measurable outcome: blade B (sun) needs ≥15% more strokes than blade A (dark) in ≥2 of 3 sessions AND plot A out-grows plot B by ≥15% at 4 weeks = the charge claim shows up in your own yard; A and B within ±5% = the claim is retired honestly, and the A-vs-C result tells you what peening actually does to an edge. Run it as a neighborhood blade bench — two or more households contributing blades and pooling trials — so the numbers mean something.",
    ["Science", "Measurement", "Craft"],
    "🔨"
  ],
  source_doc: "translations/2026-09-11-acqua-viva-viktor-schauberger-it.md (lines 3262–3271) — Olof Alexandersson, *Living Water: Viktor Schauberger and the Secrets of Natural Energy* (English ed. 1982; Italian ed. *Acqua Viva*), ch. 'Biological Techniques in Agriculture'",
  source_url: "https://www.aetherforce.energy",
  dossier: "living-library/synthesis/replication/2026-09-17-dossier-023-hammer-charged-blade.md",
  pass_fail: "PASS: sun blade B needs ≥15% more strokes per bundle than dark blade A (blinded, mean) AND direction consistent in ≥2 of 3 sessions AND plot A regrows ≥15% more biomass than plot B at 4 weeks | FAIL: A and B within ±5% (or B cuts better) — honest negative, Skeptic's Star | INCONCLUSIVE: difference below threshold, blade geometry not equalized well enough to trust A vs B, or <3 sessions",
  evidence: "Close-up photos of all three edges showing bevel geometry; photo of the bench (hammer, hardwood support, blades, bundles); the sealed key photographed sealed and opened only after numbers are recorded; raw strokes-per-bundle table (10 bundles × 3 blades × 3 sessions); strokes-to-failure per blade; the three plots before mowing and at 2 and 4 weeks with clipped biomass on a scale"
}
```

---

## Source Documentation

- **Primary source:** Olof Alexandersson, *Living Water: Viktor Schauberger and the Secrets of Natural Energy* — English edition 1982, Italian edition *Acqua Viva*. Full translation in the Vault: `translations/2026-09-11-acqua-viva-viktor-schauberger-it.md` (passage at lines 3262–3271). The claim is quoted verbatim in the dossier.
- **Provenance note:** the source asserts the advantage without naming a trial, a date, or an instrument — "it was shown to be particularly advantageous." It is an assertion inside a biography, not a report. That is stated up front, not hidden.
- **Companion claim, same chapter:** the iron-plow vs copper-plow field comparison immediately following (Schauberger reported harvest increases on copper-plowed sections). Bigger claim, needs a season and a plow — a natural follow-up card for Gardening.
- **Death certificate (context, not evidence):** `synthesis/death-certificates/schauberger-vortex-repulsine-1951.json` — Schauberger's vortex/implosion lineage, status *died* (suppression, contractual gag, prototype failure). The certificate documents that his *machines* were never independently tested. **Suppression is not evidence.** This card tests one small tool claim on its own merits and inherits no verdict from that history.
- **Sibling dossiers:** dossier 001 (Wasserwirbler) and dossier 004 (hyperbolic funnel vortex) — the water-side retries of the same lineage.
- **Related tool-material material:** Korschelt's 1892 *Nutzbarmachung* discusses magnetized water and "biologically magnetic" materials; Schauberger's iron-vs-copper agricultural material is the same intuition applied to farm tools.
- **Replication Dossier:** `synthesis/replication/2026-09-17-dossier-023-hammer-charged-blade.md`
- **Aetherforce Reference:** search "Schauberger" / "implosion" / "living water" on https://www.aetherforce.energy

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (hammer, hardwood support, three blades, grass bundles, matched plots) with measurable outcomes (blinded strokes-per-bundle, strokes-to-failure, regrowth biomass) |
| **Replicable** | YES — Home-tier, ~$30–90 for three blades; the peening itself is free and teachable |
| **Relevant** | YES — Tool Care is a survival-relevant craft, and the field is community: the card is designed as a **shared blade bench** across ≥2 households (shared-infra knowledge), which is the community field's own seed candidate |
| **Honest** | YES — Claim framed as a claim; the source's missing citation stated plainly; the geometry confound named and used to *isolate* the discriminating A-vs-B comparison; mainstream explanation for arm 1 given; clean FAIL path with Skeptic's Star; suppression story explicitly separated from evidence |
| **Linked** | YES — Full in-repo translation with line reference, death certificate for lineage context, sibling dossiers, dossier 023 with pre-registered pass/fail, Aetherforce reference |

**Why this card:** the archive's tool-care material is thin — the Tool Care mirror has sat empty since the mirror map was drawn, and the reason was always the same: no verifiable buildable source. This is one. It is a **primary-source claim from the Vault's own Schauberger corpus**, it has a **falsifiable core that no ordinary explanation can absorb** (identical blade, one hour of sun), and it teaches a real skill — peening an edge — that a household actually needs. It is the first card in the queue whose *discriminating test* is this clean: everything else is controlled, and one variable is left standing.

---

## Aetherforce Mirror Coverage

This card fills **Guild 5: Tool Care** — its seed candidate was explicitly "subtle energies on tools | magnetized/energized tool effects (engine-verify)." Schauberger's charge-in-the-blade claim is exactly that class of claim, and it is verifiable.

**Coverage advances 22/26 → 23/26.**

Three mirrors remain empty — **Dim Lumber Woodworking, Textiles, Metalworking**. All three are craft guilds whose seed candidates (Schauberger spiral shaping; natural-dye energetics; Kolisko metal crystallization / alloy tuning) still lack a source with a buildable home protocol. The engine is not forcing them.

**Honest note on the field rotation:** the next field in rotation was **community**, and this run found **no qualifying community-domain candidate with a verifiable buildable source** — the archive's community-adjacent material (Soviet group-field research, radionics corpora) is either flagged `practical_applicability: false` by the scouts or already covered by the blind geopathic mapping card. Rather than force a weak card, this run filled the **emptiest verifiable mirror** instead, and the community dimension is carried honestly: the card is built to be run as a shared blade bench across households. Rotation advances community → energy.

---

## Family Check-in

```
Member: practicality-engine
Run: 2026-09-17 22:00 UTC
Budget: gate passed (essential, gear overdrive)
Field: community (rotating from health) — no qualifying candidate; filled emptiest verifiable mirror (Tool Care) instead
Card: 1 of 3 daily
Status: emitted
Watchdog: gate reported 20 stale siblings (noted, not blocking)
```

---

*Generated by the Engine of Practicality — 2026-09-17*
