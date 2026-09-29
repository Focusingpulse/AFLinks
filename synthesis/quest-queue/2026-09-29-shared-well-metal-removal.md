---
name: Shared Well Iron & Manganese Vortex Test
description: "Test whether a vortex agitator removes iron and manganese from a shared well's water MORE than a compressed-air aerator at the same dissolved oxygen — the Malmö IET reported in 2002 that a vortex precipitated manganese 'which traditional treatment (with compressed air) did not accomplish.' Community/shared-infra card; home/homelab, ~$150–300; Community mirror. The queue's first card on dissolved-metal removal, and its first that tests a water device against the ordinary treatment it claims to beat."
---

# ⚡ Aetherforce — Community

**Guild:** Aetherforce — Community
**Quest Line:** ⚡ Aetherforce · Community complement
**Tier:** straw
**Domain:** community (shared-infra knowledge — treating a shared water source)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-29-shared-well-metal-removal` · authored_at `2026-09-29` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Community",
  desc: "Every shared well eventually asks the same question: what do we do about the iron and the manganese? The standard answer is to aerate the water and filter it — and the standard answer is exactly what the claim says a vortex beats. The Malmö Institute for Ecological Technology reported in 2002 that a vortex agitator precipitated manganese 'which traditional treatment (with compressed air) did not accomplish.' Test it the only way that settles it: three arms of the same well water — untreated, air-pumped, and vortexed — with the two treated arms finishing at the same dissolved oxygen, sampled before treatment, after treatment and after the filter. You get a removal fraction for iron and for manganese in each arm, and the one number that matters: whether the vortex beat the air pump at the same oxygen. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Shared Well Iron & Manganese Vortex Test",
    "Draw one 20-40 L batch of your shared well water and split it into three matched vessels. Arm A sits untreated. Arm B is aerated with an air pump and airstone until dissolved oxygen reaches the pre-registered target. Arm C is run through a vortex rig (a conical or hyperbolic vessel with a small impeller or pump driving a swirling flow) until it reaches the same dissolved oxygen - within +/-1 mg/l of arm B, or the run is void. Sample all three for iron, manganese, dissolved oxygen, pH and temperature before treatment, after treatment and after the gravel filter (same filter, same flow, same rest period for every arm). Measurable outcome: the manganese removal fraction of the vortex arm is >= 2x the aeration arm's at matched dissolved oxygen, with the drop appearing after filtering - or the honest result that both treated arms remove metal equally, meaning the vortex is aerating and an air pump is the cheaper tool. Baseline iron and manganese below the test kits' detection limits makes the run inconclusive, not a pass.",
    ["Science", "Measurement", "Community"],
    "🧲"
  ],
  source_doc: "translations/2026-09-27-self-organizing-flow-technology-iet-sv.md (IET Research Report No. 1, ch. 4.3 'Ion precipitation', Table 4.2) + sources/2026-09-28-scout-b-langs-2.md#find-7",
  source_url: "https://www.iet-community.org/publications/reports/IET%20Forskningsrapporter%20Nr%201.pdf",
  dossier: "living-library/synthesis/replication/2026-09-29-dossier-052-shared-well-metal-removal.md",
  pass_fail: "PASS (vortex-specific): the vortex arm's manganese removal fraction is >= 2x the aeration arm's at matched dissolved oxygen (+/-1 mg/l), and the manganese drop appears AFTER filtering (the vortex made it filterable), repeated in a second draw - iron reported separately, never pooled with manganese. PASS (the effect is aeration, not the vortex - a real, different result): both treated arms remove metal, C ~ B at matched DO, and B > A - the vortex's contribution is the oxygen it dissolves. FAIL: no arm removes metal above the untreated control - an honest negative (Skeptic's Star). INCONCLUSIVE: baseline iron and manganese below the kits' detection limits (nothing to remove); the two treated arms finished more than 1 mg/l apart in dissolved oxygen; the filter, flow or rest period differed between arms; or only one draw was run. ARTIFACT: the result tracks temperature or rest time rather than treatment; the arms differed at baseline; or the result disappears when arm positions and order are re-randomised.",
  evidence: "Photo of the three arms side by side before treatment + the pre-registration sheet (treatment times, DO target, rest period, filter procedure, sampling points, endpoints, thresholds) + the well and draw recorded + the baseline Fe/Mn/DO/pH/temperature table for all three arms + the post-treatment pre-filter table + the post-filter table + the dissolved-oxygen trace showing the two treated arms finished matched + the removal-fraction table with the C-vs-B ratio at matched DO shown + the second draw's repeat + the void and artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the claim and its numbers):** Lars Johansson, Morten Ovesen & Curt Hallberg, *Self-organizing flow technology – in Viktor Schauberger's footsteps*, Institute for Ecological Technology (IET), Malmö 2002 (first edition 1997) — https://www.iet-community.org/publications/reports/IET%20Forskningsrapporter%20Nr%201.pdf (**full English translation in the library and read this run**: `translations/2026-09-27-self-organizing-flow-technology-iet-sv.md`; archive copy `archives/2026-09-27-iet-forskningsrapporter-nr1-sjalvorganiserande-stromningsteknik.pdf`). **Chapter 4.3 (Ion precipitation)** reports the Pålträsk waterworks trial (1990): a hyperbolic vessel ~1 m high with an Aquagyro agitator inside a 3 m³ tank; iron precipitates visible in the tank; **"In a subsequent filtering in a gravel filter the manganese ions were to a large extent precipitated, which traditional treatment (with compressed air) did not accomplish."** Table 4.2 gives Mn **0.26 → <0.05 mg/l** and Fe **0.23 → 0.21 mg/l**, with the note *"The iron does not precipitate on compressed-air aeration in the lab."* The source cites **Nordmaling 1987** (Mn and NO₂ reduction) and **Vistbäcken waterworks** (extremely iron-rich water — effective iron precipitation, "more effective than traditional compressed-air aeration, in contrast to the experiments at Pålträsk", plus a manganese reduction).
- **Primary (the control that makes the card possible):** the *same* report, **Chapter 4.2 (Oxygenation of water)** — the IET trough trial (50 cm diameter × 80 cm, a Plan Pump on a 70 W sewing-machine motor) raised dissolved oxygen to ~90 % of saturation in 15–30 minutes, and states plainly that *"If no air funnel was drawn down (e.g. by placing a ball in the center), no oxygenation took place… it is thus only the small air bubbles that play an important role for the oxygenation."* **The vortex aerates — the source says so in the same document that reports the metal claim.**
- **Primary (the source's own request for this card):** the section closes *"It would be interesting to repeat these trials more systematically, with, e.g., the Plan Pump in the trough, and with water with different ion contents."*
- **Scout entries:** `sources/2026-09-28-scout-b-langs-2.md` (find 7 — IET Malmö Schauberger replication program, `buildable, reproducible`; find 8 — IET Report 2, the alternative-water-treatment monograph).
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-29-dossier-052-shared-well-metal-removal.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "Schauberger", "ion precipitation", "water treatment", "IET"
- **Aetherforce Reference:** Search "Schauberger", "water vortex", or "water treatment" on https://www.aetherforce.energy
- **Related dossiers:** 001 (Wasserwirbler — the vortexer itself, tested on temperature and taste), 004 (Hyperbolic Funnel — the same vortex tested on *aeration*; this card is the metal-removal follow-up and shares its apparatus family), 031 (MVP Vortex Motor — the same lineage, an energy claim), 040 (Shared Well Yield Estimate — *sizing* a shared source; this card is about *treating* its water)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (a vortex rig, an air pump, a gravel filter, iron/manganese/dissolved-oxygen test kits) with a named procedure (split one batch, treat two arms to matched oxygen, sample at three points, filter, compute removal fractions) and a measurable outcome (the manganese removal fraction per arm and the C-vs-B ratio at matched dissolved oxygen). Not pure theory. |
| **Replicable** | YES — Home/homelab, ~$150–300: test kits, an aquarium air pump, a small water pump or impeller, a conical vessel, and gravel. No mains work, no chemicals beyond test reagents, no purchased instrument beyond a DO test. One afternoon to build, one day of trials. |
| **Relevant** | YES — Community domain: a shared well's water is shared infrastructure, the decision to treat it is a shared decision, and the pooled test is the evidence a group needs before spending shared money. Fills the **Community** mirror (the community-domain complement). |
| **Honest** | YES — The claim is framed as a claim and the source itself flags its iron result as *"remarkable"* and unexplained, offering two competing explanations without choosing; **the source's own report shows the vortex aerates, and aeration is the classic mechanism for removing these metals** — so the card's default expectation is that the vortex is aerating, and the matched-oxygen air-pump arm is the design that can prove it. Clean FAIL path and a clean "the effect is aeration" path. |
| **Linked** | YES — Two chapters of one primary document read this run (the claim and the control), two scout entries, a pre-registered replication dossier, and cross-links to four related cards. |

**Mirror choice, stated:** the card's **domain is community** (the rotation's next field) and its **guild complement is Community** — the community-domain mirror, whose theme is shared measurement capacity and shared-infrastructure decisions. **Plumbing & Hot Water** was the alternative (the object is a water-treatment device, the same class as cards 001, 009, 025 and 031); it was not chosen because this card's subject is the *community's* decision about a shared source, not the plumbing itself — the same domain/mirror split the queue already uses for card 040 (community domain, Community mirror) and card 035 (community domain, Earthworks mirror).

---

## The honest framing (the spine of the card)

**The claim is a claim.** The IET reports that a vortex agitator precipitated manganese from well water *"which traditional treatment (with compressed air) did not accomplish."* **This card tests that claim; it does not endorse it.**

**The source hands the card its own control — and then hands it the confound.** Two chapters of the same 2002 report do the work:

1. **Ch. 4.3** is the claim: the vortex removed manganese where compressed air did not.
2. **Ch. 4.2** is the confound: the *same vortex* raised dissolved oxygen to ~90 % of saturation, and the authors state that *"it is only the small air bubbles that play an important role for the oxygenation."*

Iron and manganese are removed from well water by **oxidation followed by filtration** — Fe²⁺ oxidises and precipitates quickly, Mn²⁺ oxidises slowly and needs a higher redox potential. **A device that dissolves oxygen into the water is therefore already doing the classic thing, and a card that compares "vortexed vs untreated" would pass on aeration alone.** That is why the design is not two arms but three, and why the two treated arms must finish at the **same dissolved oxygen**.

**The design that makes it a measurement.** Three things do the work:

1. **The matched-oxygen air-pump arm is the experiment, not an extra.** The claim is *relative* — the vortex did what aeration did not. The only way to test a relative claim is to run the comparator at matched conditions. If the two treated arms finish more than 1 mg/l apart, the run is void, and the card says so.
2. **Three sampling points separate precipitation from filtration.** The source's manganese drop appears at the **gravel precipitation** step, not during treatment. A filter removes precipitated metal; the question is whether the vortex makes the metal *filterable* when aeration does not. Measuring before treatment, after treatment and after the filter is what tells the two apart.
3. **Iron and manganese are reported separately, always.** They oxidise at different rates and the source's own iron result is contested and unexplained — it offers two competing explanations (organic binding; a complex bond) and chooses neither. **Do not let a manganese result lend confidence to the iron one.**

**The likely result is that the vortex is aerating, and that is a complete result.** If both treated arms remove metal equally at matched oxygen, the honest verdict is *"the vortex's contribution is the oxygen it dissolves, and an air pump is the cheaper tool."* That is a positive mechanistic finding, not a failure — it retires the device-specific claim while leaving the ordinary method standing, and it is exactly the kind of answer a family sharing a well needs before spending shared money.

**The central limitation, stated up front: one well is one water.** The source's trials were on specific Swedish well waters and the outcome depends on pH, hardness and humus content. A result here speaks for *this* well's water on *these* days, and the card requires a second draw before any conclusion.

**Safety and honesty:** this is a bench test of a treatment claim, **not** advice to drink the treated water or to treat a well without testing. Iron and manganese above the local drinking-water limit are a real problem with a real fix; never substitute a home bench result for a certified water analysis.

---

## Relationship to the rest of the queue

This card is the **metal-removal follow-up to card 004** (Hyperbolic Funnel Vortex Aerator). 004 tests the same apparatus family on **oxygen transfer**; this card tests it on **what the oxygen then removes**. Same lineage, same rig family, a different endpoint — and the overlap is stated here rather than hidden.

It is also the **first card in the queue whose comparator is the ordinary treatment the device claims to beat** rather than an untreated control or a shielded arm — a genuinely different measurement design, and the reason it is worth a card of its own rather than a paragraph appended to 004.

It is the **first card on dissolved-metal removal** of any kind: iron and manganese are the two most common reasons a household well's water stains fixtures, tastes metallic and fails a buyer's inspection, and no prior card in the queue has a contaminant concentration as its endpoint.
