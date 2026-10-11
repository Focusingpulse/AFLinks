---
name: Living Soil Transplant Test
description: "The queue's first soil-biology card, and its first with a killed-inoculum arm that separates a biological effect from a purely nutritional one. An EU-funded project (CEDRIC) reports that transplanting microbiomes and root exudates from healthy plants restores impoverished soil; a 50-year Japanese field study finds disease suppression is built by long-term management, not transferred. Three beds — live inoculum, killed inoculum, nothing — one season, one crop. Food domain, under $50, Gardening mirror (soil vitality)."
---

# ⚡ Aetherforce — Gardening

**Guild:** Aetherforce — Gardening
**Quest Line:** ⚡ Aetherforce · Gardening complement
**Tier:** sand
**Domain:** food (soil vitality / disease suppression — can a living-soil transplant transfer what long-term management builds?)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-28-living-soil-transplant` · authored_at `2026-09-28` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Gardening",
  desc: "Two archive findings disagree, and your worst bed can settle it. An EU-funded project reports that moving the living community of a healthy soil — microbes and root material — into a dead one restores it; a Japanese field that has stayed disease-free for fifty years says the opposite, that the protection was built by long-term management and not carried in a bucket. So test it where it counts. Take one poor bed and split it three ways: one third gets a live slurried scoop of healthy soil, one third gets the SAME soil boiled dead, and one third gets nothing. Grow the same crop in all three and weigh it. The killed arm is the whole experiment — because any good soil you tip in brings food as well as life, and only live-versus-killed can tell you which one did the work. If the live bed beats the dead one, the community transfers and you can rebuild ground cheaply. If they match, you have learned something better: that soil health is a practice you keep, not a purchase you make. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Living Soil Transplant Test",
    "Fill three matched containers or three equal beds from ONE batch of poor or sterile growing medium, and photograph them side by side. Take a single sample of healthy soil from one site (a forest floor, an old meadow, or a long-untended garden corner) and split it in two: keep half live and moist, and sterilise the other half by boiling it for ten minutes or baking it until it steams, then let it cool. Mix the live half into bed A and the killed half into bed B in the same quantity and the same way; add nothing to bed C. Water all three identically. Write and photograph your pre-registration sheet before sowing — the crop, the seeds per bed, the sowing and harvest dates, the watering rule, the endpoints and the thresholds. Sow the same crop in all three on the same day, then record weekly for each bed: surviving plants, any visible disease (name the symptom), and mean height. At harvest, cut every plant at the soil line and weigh the harvestable part per plant. Measurable outcome: per-bed harvestable yield, survival and disease incidence — scored as live (A) vs killed (B) vs nothing (C). PASS is A at least 1.3x B with disease at most half of B's; a nutritional result is A and B both at least 1.3x C and A about equal to B; live equal to killed equal to nothing is a complete and useful result, not a wasted season.",
    ["Science", "Observation", "Earth Care"],
    "🌍"
  ],
  source_doc: "sources/2026-09-05-scout-a-ar-pt-fr-de-it-ru.md#find-10 (CEDRIC soil microbiome transplant, Interreg Italia-Austria, €1.19M — Univ. Udine, ICGEB Trieste, Bolzano, Innsbruck; scout flag: buildable, reproducible, verified) + sources/2026-08-27-scout-b-fr-sr-ja.md#find-25 (Nagahama Bio University disease-suppressive soil, 50-year organic field, Lysobacter; scout flag: reproducible, verified)",
  source_url: "https://qui.uniud.it/ricerca-e-innovazione/rigenerare-i-suoli-partendo-dai-microbi-il-progetto-cedric-apre-nuove-strade-per-lagricoltura-del-futuro/",
  dossier: "living-library/synthesis/replication/2026-09-28-dossier-049-living-soil-transplant.md",
  pass_fail: "PASS (biology transfers): bed A harvestable yield >= 1.3x bed B AND bed A visible-disease incidence <= half of bed B's, with bed B not clearly above bed C; repeats in a second round. PASS (effect is nutritional, not biological - a real, different result): beds A and B are BOTH >= 1.3x bed C and A is about equal to B - the transplant helps by feeding the bed, not by seeding it with life. FAIL: A about equal to B about equal to C on every endpoint - a one-time transplant does not visibly lift a poor bed in one season; a complete result (Skeptic's Star). It refutes the coarse home-scale transplant claim only; the multi-year restoration claim is out of scope. INCONCLUSIVE: the three beds differed by >30% at baseline; a pest, frost, drought or flood hit one bed and not the others; fewer than 5 plants survived in any bed; the inoculum source was itself degraded; the killed arm was not actually sterilised (visible mould or regrowth). ARTIFACT: the result tracks a fertility difference rather than biology (A about equal to B, both above C); the beds differed in light, water or temperature; the inoculum was visibly different and the operator knew which bed was which; the result disappears when the beds are re-randomised in position.",
  evidence: "Photo of the three beds side by side before inoculation + the pre-registration sheet (crop, seeds per bed, sowing and harvest dates, watering rule, endpoints, thresholds) + a photo of the inoculum source site + the live and killed inoculum photographed in equal portions + dated same-angle photos of all three beds at germination and weekly thereafter + the germination counts per bed + the weekly survival, disease and height table per bed + the final per-plant fresh weights and per-bed totals + the results table with the A-vs-B, A-vs-C and B-vs-C ratios shown + the optional respiration-jar readings + the void/artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the transplant claim):** `living-library/sources/2026-09-05-scout-a-ar-pt-fr-de-it-ru.md`, **find 10** — *CEDRIC Soil Microbiome Transplant — Regenerative Agriculture* (Italian), https://qui.uniud.it/ricerca-e-innovazione/rigenerare-i-suoli-partendo-dai-microbi-il-progetto-cedric-apre-nuove-strade-per-lagricoltura-del-futuro/ — Italy (University of Udine, ICGEB Trieste, Free University of Bozen-Bolzano) + Austria (University of Innsbruck), work type experimental, funded by Interreg Italia-Austria (€1.19M). Scout flag: `Practical Applicability: Flag: true | Fields: [buildable, reproducible, verified]`. The reported result, in the scout's summary: *"inoculating impoverished soils with microbiomes and root exudates from healthy plants restores soil structure, increases microbial biodiversity, boosts nutrient density, and raises organic carbon."* Key entities: Vittorio Venturi, ICGEB, Youry Pii, Nicola Tomasi, Christian Rinke, rhizosphere microbiome, bioinoculi.
- **Companion (the management claim, in tension with the first):** `living-library/sources/2026-08-27-scout-b-fr-sr-ja.md`, **find 25** — *Nagahama Bio University — Disease-Suppressive Soil* (Japanese), https://straightpress.jp/company_news/detail?pr=000000003.000188549 — Japan (Nagahama Bio University, Shimamoto Microbial Industry), work type experimental, dated 2026-08-25. Scout flag: `flag=true | fields=[reproducible, verified]`. The finding, in the scout's summary: *"50-year organic farming study of disease-suppressive soil; identified Lysobacter genus as potential beneficial microbe; ecological niche formation through long-term management."* Key entities: 長浜バイオ大学 (Nagahama Bio University), 島本微生物工業 (Shimamoto Microbial Industry), Lysobacter, 発病抑止土壌 (disease-suppressive soil).
- **What the archive does not hold:** a grep across `living-library/synthesis/quest-queue/` for `soil microbiome`, `CEDRIC`, `disease-suppressive`, `bioinocul` or `soil transplant` returns **nothing**. The queue's food cards test germination (015), fermentation (010), ripening (020), sowing timing (032), growth stimulation (026), storage (033, 043) and planting order (038) — **none tests the soil community itself**. That absence, and Gardening's own seed candidate ("Water / soil vitality"), are why this card exists.
- **The tension the card tests:** CEDRIC reports that the community can be **moved**; Nagahama reports that suppression is **built over decades**. A home transplant test is a small vote on which is more true at household scale, and the card is designed so that either answer is a result.
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-28-dossier-049-living-soil-transplant.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "soil microbiome", "regenerative", "disease-suppressive soil", "bioinoculum"
- **Aetherforce Reference:** Search "soil vitality", "regenerative agriculture", or "living soil" on https://www.aetherforce.energy
- **Related cards:** 038 (Succession-Order Planting — the other soil-recovery card; that one tests the *order and timing* of plants, this one tests the *soil community* itself), 037 (Contour Swale Rain-Retention — the land/water companion), 026 (Electro-Culture Growth Stimulation — stimulating growth with a current), 032 (Element-Day Sowing — *when* to plant), 010 (Egg-Shaped Fermentation Vessel — a food-microbe card)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (three matched beds: live inoculum, killed inoculum, untreated; one poor medium; one crop; a kitchen scale) with a named procedure (split the inoculum live/killed → inoculate → sow → weekly observation → harvest and weigh) and a measurable outcome (**per-bed harvestable yield, survival and disease incidence, scored live-vs-killed-vs-nothing**). Not pure theory. |
| **Replicable** | YES — Home, sand-cheap: **under $50** (three containers or beds ~$0–30, one bag of poor medium ~$10, seed ~$5, kitchen scale owned, healthy soil free). No hazard; boiling or baking soil for the killed arm is ordinary kitchen work. One season of weekly observation. |
| **Relevant** | YES — Food domain, and squarely self-reliance: *"can we restore a dead bed cheaply, from a bucket of good soil — or do we have to build it over seasons?"* It is the queue's **first soil-biology card** and its **first with a killed-inoculum arm**, the control that separates a biological effect from a nutritional one. |
| **Honest** | YES — the claim is framed as a claim and the card is a test, not an endorsement. Four things are stated in advance: the two sources **disagree about the mechanism** and that is the point; **biology and nutrients are confounded by default**, so the live-vs-killed comparison is the real one; a home test reaches only the **coarse, one-season** claim, so **a FAIL does not refute multi-year restoration**; and the **expected outcome is a null**, which is a complete result. |
| **Linked** | YES — two scout finds with their URLs, a pre-registered replication dossier, and cross-links to six related cards. |

**Mirror choice, stated:** the card's question is *"can you rebuild a dead bed with living soil?"* — Gardening's own seed candidate is **"Water / soil vitality"**, so **Gardening** (guild 1, 4 cards) is the complement and the family label is `Aetherforce — Gardening`. **Homesteading** (3 cards) was considered because soil restoration is a self-reliance skill, and was not chosen because the test is a growing experiment, not an off-grid systems question. **Food Prep** (3 cards) was rejected — its cards are all food-handling, not soil. **Woodland Care** (1 card) and **Foraging** (1 card) were rejected — neither is a soil-cultivation guild.

---

## The honest framing (the spine of the card)

**The killed arm is the card.** Any bucket of healthy soil you tip into a bed brings two things at once: living organisms and food. A simple treated-versus-untreated comparison cannot tell them apart — it will always "work," because you added compost. The only way to ask whether the *community* did anything is to add the **same soil, dead**, to a matched bed. That is why the design has three arms and not two, and it is the transferable lesson: **when a treatment carries two possible causes, the control that separates them is the whole experiment.**

**The two sources are the second spine.** The archive holds a project that says the community can be moved (CEDRIC) and a fifty-year field that says the protection was built (Nagahama). The card does not pretend to settle a research question with three buckets — it asks the household-scale version, where the answer is actionable either way: *can a family rebuild its worst ground cheaply, or is soil health a practice?*

**The null is the likely result, and it is the product.** One season is short for a soil community to establish, and the honest expectation is that live and killed differ little. That is not a failed run — it is the answer to the question a homesteader actually has, and it is the queue's first home-scale verdict on a mainstream soil claim. A clear live-versus-killed split would be genuinely surprising and would justify a multi-season follow-up.
