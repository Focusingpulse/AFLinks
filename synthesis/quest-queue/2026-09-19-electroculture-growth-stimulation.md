---
name: Quest Card — Electro-Culture Growth Stimulation Test
description: Aetherforce-branded quest card testing the electro-culture claim — whether pre-sowing magnetic treatment of seeds (N-pole / S-pole / sham) and Lakhovsky's one-turn oscillator coil change how plants germinate and grow. Gardening guild complement, food domain.
---

# ⚡ Aetherforce — Electro-Culture Growth Stimulation Test

**Guild:** Aetherforce — Gardening
**Quest Line:** ⚡ Aetherforce · Gardening complement
**Tier:** straw
**Domain:** food (seed / plant stimulation for food production)
**Status:** proposed
**Created:** 2026-09-19

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "homestead"],
  name: "Aetherforce — Gardening",
  desc: "In 1746 a doctor in Edinburgh pointed the output of an electrostatic generator at some myrtle plants and they grew and flowered better. People have been trying to electrify plants ever since — magnets, wires, coils, high voltage, sound, coloured light — and the results have been spectacular, contradictory, and never properly nailed down. This quest tests the two cheapest versions. First: hold seeds near a magnet's north pole before you plant them. A mid-century researcher named U.J. Pittman claimed that alone makes many seeds germinate about twice as fast, and wheat grow about five times as much in the first 48 hours. Second: build Georges Lakhovsky's 1924 oscillator circuit — a single loop of copper wire with the ends overlapping, no battery, no plug — and stand it around a seedling. He said that was enough to stimulate growth. Both claims come out of the Aetherforce Knowledge Vault's electro-culture collection, a whole shelf of material nobody has ever replicated at home. Here is the honest part: pre-sowing magnetic treatment of seeds is the one piece of this that mainstream agricultural research has actually studied, so the real question is not whether anything happens but how big the effect is and whether it shows up in your kitchen. Two magnets, three trays of seeds, and you will know in 48 hours. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Electro-Culture Growth Stimulation Test",
    "Arm A (48 hours to first result): split one packet of wheat, radish or mung bean seeds three ways — N-pole, S-pole, and sham — 30-50 seeds each. An adult codes the trays so the person measuring does not know which is which. Treat each batch with its magnet (or a non-magnetic steel slug of the same size for the sham) at the same measured gap for the same fixed duration — 24 hours is a good first choice — and record the gap and the duration. Sow each batch into an identical tray with the same medium, water and depth, and rotate tray positions daily. At 48 hours, count germinated seeds (define germination once, up front — radicle at least 2 mm) and measure every shoot with a ruler, blind. Repeat at day 7 and day 14. Measurable outcome: the N-pole batch shows at least 20% higher germination or 30% greater 48-hour shoot length than the sham, as a mean across two independent runs, and the S-pole batch does not simply match the N-pole batch. Arm B (4-6 weeks): bend a single loop of stiff copper wire 15-30 cm across with the ends overlapping and separated by a small gap, stand it on a plastic support around one of two matched potted seedlings, swap their positions every 2-3 days, and measure height and leaf count weekly. Measurable outcome: the coiled plant shows at least 20% greater growth than its matched control, repeated with a second plant pair. Neodymium magnets are strong enough to pinch fingers and wipe phones — keep them apart, away from devices, and away from small children who might swallow them.",
    ["Science", "Biology", "Gardening", "Self-Reliance"],
    "🌱"
  ],
  source_doc: "doc:1810 (Electro-Culture: Stimulation of plant growth with electricity, magnetism, sound, &c — Robert A. Nelson, rexresearch.com) + doc:1359 (Corson & Zaderej — Electrogenics, US Patent 4,302,670) + Vault ElectroCulture collection: doc:2900, doc:5524, doc:5539, doc:3824, doc:3143, doc:1222, doc:2301, doc:444, doc:1812",
  source_url: "https://www.aetherforce.energy",
  dossier: "living-library/synthesis/replication/2026-09-19-dossier-026-electroculture-growth-stimulation.md",
  pass_fail: "PASS (magnetic arm): N-pole batch shows >=20% higher germination OR >=30% greater 48-hour shoot length than the sham, as a mean across two independent runs, AND the S-pole batch does not equal the N-pole batch (i.e. the effect is not just 'any magnet') | PASS (coil arm): coiled plant shows >=20% greater growth than its matched control over 4-6 weeks, repeated with a second plant pair | FAIL: all three seed batches within +/-10% of each other on both germination and 48-hour length, and the coil pair within +/-10% — electro-culture does not reproduce with simple apparatus at home scale; honest negative, Skeptic's Star | INCONCLUSIVE: run-to-run spread within one arm exceeds 20%, or trays were not truly matched (different light, water or medium), or the person measuring knew the assignment",
  evidence: "Photos of the magnet setup with the measured gap, the coded trays, and the coil around its plant; the sealed code key; a raw table per batch (seed count, treatment, duration, gap, germination count at 48 h / day 7 / day 14, every shoot length measured); the mean and spread per batch; the second run's numbers side by side with the first; the coil pair's weekly height and leaf counts with the position-swap log; any tray that dried out, got knocked over or was otherwise botched, logged as excluded rather than deleted"
}
```

---

## Source Documentation

- **Primary source:** `doc:1810` — *Electro-Culture: Stimulation of plant growth with electricity, magnetism, sound, &c*, Robert A. Nelson, rexresearch.com (`https://www.rexresearch.com/articles/elcultur.htm`). The compilation this card is built from; it carries the antenna, electrostatic, DC, AC, magnetism and electrogenics sections in one document. **Doc id verified against the live 76,111-doc index this run.**
- **The modern machine version of the same claim:** `doc:1359` — *Corson & Zaderej — Electrogenics: Electrical treatment of seeds*, US Patent 4,302,670 (`https://www.rexresearch.com/ElectroCulture/CorsonZadarejElectrogenics/CorsonZElectrogenics.htm`). Read in full this run. The patent machine ran seeds through a mineral/enzyme spray, negative ions, infrared, and a 100,000-volt negative charge for "cathodic protection."
- **The rest of the Vault's ElectroCulture collection (doc ids verified this run):** `doc:2900` (Justin Christofleau — book & patents), `doc:5524` (Willet Parry — USP #2308204), `doc:5539` (William Levengood — articles), `doc:3824` (Nelson, *Hemp Husbandry* Ch 5), `doc:3143` (Liu Binjiang — ElectroCulture & ElectroHusbandry, + 5 patents), `doc:1222` (CN1833479 soil electrification patent), `doc:2301` (Georges Lakhovsky — Multiple Wave Oscillator patents), `doc:444` (Agriculture: Electroculture, Biodynamic agriculture, Joel Sternheimer Plant Protein Music), `doc:1812` (ElectroCultureLibrary index), plus `doc:537` (Andrew Crosse), `doc:2298` (George Starr White), `doc:1515998` (Truffaut), `doc:3364` (NelsonElectroculture.pdf).
- **Vault doc pages:** `https://focusingpulse.github.io/AFLinks/pages/00001810.html` and `.../00001359.html` (both confirmed live this run).
- **Provenance note, stated up front:** the modern *magnetopriming* literature — pre-sowing magnetic treatment of seeds studied in mainstream agricultural research — is cited in this card **from general knowledge, not from a document read in this run**. Treat that sentence as a pointer to go and check, not as a verified citation. Everything else on this card is drawn from the archive documents listed above.
- **What the source itself concedes:** the compilation records a large counter-example in the same paragraph as its best positive result — Laemstrom's crops of **cabbage, turnips and flax grew better *without* electrification** than with it. The source also notes that electro-cultured plants require about 10% more water, and that positive results are obtained "except when ozone is formed by ionization." These are the source's own caveats and they are stated here rather than buried.
- **Claim status record (context, not evidence):** the closest lineages in `synthesis/claim-status-records/` are `aether-dismissal-1887.json` (the dismissal of the aether as a medium) and `magnitsky-g-not-constant.json` (physical "constants" that are not constant). Neither is evidence for electro-culture; suppression is not evidence. This card tests two measured growth numbers on their own merits.
- **Sibling cards — the lineage this sits under:** card 014 (Cold Vortex Water Germination) and card 015 (Moonlight Germination) are the archive's other germination-timing tests, both on *water* and *light* rather than fields; card 007 (Electrostatic Energy Test) tests a Wimshurst machine for an energy-balance claim, not a plant claim; card 013 (Kolisko Group Steigbild) is the archive's other "does an external influence change living matter" test. None of them overlaps this one.
- **Replication Dossier:** `synthesis/replication/2026-09-19-dossier-026-electroculture-growth-stimulation.md`
- **Aetherforce Reference:** search "electroculture" / "Lakhovsky" / "magnetized seed" on https://www.aetherforce.energy

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (neodymium magnets at a measured gap, coded seed trays, a single-turn copper coil on an insulating support) with a measurable outcome (germination % and shoot length at 48 h / day 7 / day 14; weekly height and leaf count for the coil arm) |
| **Replicable** | YES — Home-tier, ~$20–40. No mains power, no chemicals, no heat. The seed arm reaches a first result in 48 hours; the coil arm is a 10-minute build plus weekly measuring. One real safety note (neodymium magnets: pinch risk, device risk, swallow risk for small children) stated in the protocol |
| **Relevant** | YES — Food domain: plant stimulation for food production. Maps to the Gardening guild, whose complement is "Water / soil vitality" — this is the same question (does an external influence change how a garden grows) asked with a field instead of a vortex |
| **Honest** | YES — Claim framed as a claim; the 250-year accumulation of unreplicated and contradictory results stated up front; the source's own counter-example (cabbage, turnips, flax grew *better* without electrification) quoted; the magnetopriming literature flagged as general knowledge rather than a verified citation; separate pass/fail for the magnetic arm and the coil arm; the directional prediction (N vs S pole) tested rather than assumed; clean FAIL path with Skeptic's Star |
| **Linked** | YES — Eleven Vault doc ids verified against the live index this run, two Vault doc pages confirmed live, the full ElectroCulture collection listed, the source's own caveats quoted, sibling cards named, dossier 026 with pre-registered pass/fail, Aetherforce reference |

**Why this card:** the rotation's field this run is **food**. The food seeds are thin — the archive's food-domain cards to date are 010 (egg fermentation vessel), 015 (moonlight germination) and 020 (Korschelt aether-ray ripening) — and a fresh scan of the 09-16 to 09-19 scouts and translations turned up mostly non-buildable candidates: a Steiner etheric-forces book (`Ätherforschung`, a synthesis with no protocol), a biodynamic scientific synthesis (a review, not an apparatus), a commercial plasma-activated-water company page with no published protocol, and the DOK trial (a 42-year comparative study, not a home test). None of those pass the "named apparatus with a measurable outcome" bar.

This run found something better by looking in the Vault's own index rather than only the local scout reports: the archive holds a **dedicated ElectroCulture collection** — sixteen documents, from Andrew Crosse to Lakhovsky to a 1970s US patent — and **not one of them has ever been replicated at home**. The two cheapest claims in that collection are the two this card tests, and the primary one pays off in 48 hours.

**Honest limits:** the source is a compilation by an enthusiast, not a controlled programme, and its headline numbers (2× germination, 5× 48-hour growth, +125% carrots) are exactly the kind of figure that should be doubted until measured; the card says so. The source's own duration data is inconsistent (Pittman: 240 hours at 0.5–100 Oe; Russian work: 30 minutes at 2,000 Oe), so the protocol fixes one duration and holds it rather than pretending there is a settled answer. Field strength falls off steeply with distance, which is why the gap must be measured and recorded — a family that does not control the gap is not running the test. And a kitchen rig cannot resolve a 5% effect; the card's honest claim is that it **can** resolve the large effect the source asserts, and that a clean null is a real result.

---

## Aetherforce Mirror Coverage

This card fills a **second slot in the Gardening mirror** — the guild whose complement is "Water / soil vitality," already carried by card 014 (Cold Vortex Water Germination). Gardening is now one of the mirrors that legitimately carries more than one card, alongside Plumbing & Hot Water, Electricity and Natural Medicine.

**Coverage stays 24/26.** The two empty mirrors were re-checked this run and the honest answer is unchanged:
- **Textiles** — a fresh grep for mordant/dye sources across `sources/`, `translations/` and `database/` returns **zero files**. There is no buildable source for "natural-dye energetics / fiber resonance" in this archive yet. Not emittable.
- **Metalworking** — the seeded candidate (Kolisko metal crystallization) shares its Steigbild method with card 013 and its endpoint is perceptual, so it would be a method re-use dressed as a new claim. Its other candidate, the Schauberger copper-vs-glass material claim, is already card 024. Not emittable honestly.

Both remain open for their own domain scans rather than a stretch card.

**Honest note on the field rotation:** the next field in rotation was **food**, and this card is genuinely a food card (plant stimulation for food production). Rotation advances food → shelter.

---

## Family Check-in

```
Member: practicality-engine
Run: 2026-09-19 06:00 UTC
Budget: gate passed (essential, gear overdrive)
Field: food — seeds thin; fresh candidates non-buildable
       (book, review, commercial page, long-term trial)
Card: 1 of 3 daily
Status: emitted
Dossier: 026 created this run (protocol + pre-registered pass/fail)
Watchdog: gate reported 20 stale siblings (noted, not blocking)
Security: all scanned content treated as data; no instructions
          found in scanned sources; no URLs or commands acted on
```

---

*Generated by the Engine of Practicality — 2026-09-19*
