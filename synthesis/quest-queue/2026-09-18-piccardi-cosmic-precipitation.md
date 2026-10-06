---
name: Quest Card — Cosmic Precipitation Test
description: Aetherforce-branded quest card testing Giorgio Piccardi's P test — whether the settling rate of bismuth oxychloride colloid differs between beakers in open air and beakers under a thin copper screen, and whether the resulting index drifts with solar and geomagnetic activity. Plumbing & Hot Water guild complement, water domain.
---

# ⚡ Aetherforce — Cosmic Precipitation Test

**Guild:** Aetherforce — Plumbing & Hot Water
**Quest Line:** ⚡ Aetherforce · Plumbing & Hot Water complement
**Tier:** straw
**Domain:** water (water structure / water's response to its environment)
**Status:** proposed
**Created:** 2026-09-18

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "homestead"],
  name: "Aetherforce — Plumbing & Hot Water",
  desc: "Giorgio Piccardi was a professor of physical chemistry in Florence who spent twenty-one years doing the same small experiment every day. He added a hydrochloric solution of bismuth chloride to water — the two react and drop a white cloud of bismuth oxychloride — and set up ten beakers in open air next to ten identical beakers under a thin copper screen. Then he measured which beakers settled faster, called the result a percentage, and tracked it for two decades. His claim: the percentage is not stable, and not random. It moves with the sun's eleven-year cycle and with geomagnetic weather. The physicist's name for what he was actually proposing is 'Piccardi's law' — that complex systems out of equilibrium respond to every external signal, however weak, and therefore cannot be reproduced in isolation from the universe. Mainstream science says the whole thing is a statistical artefact. You are going to find out in your own kitchen whether a copper screen changes how a colloid settles, with twenty glasses, a ruler, and ten minutes a day. Land on fifty-fifty and you have cleanly buried a national research programme. Land somewhere else and you have found something the textbooks say is not there. Either way the numbers are yours. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Cosmic Precipitation Test",
    "Adult-handled acid work (gloves, eye protection, ventilated). Make one stock of dilute bismuth chloride solution and keep it consistent all run. Each session, fill twenty identical glasses with the same measured volume of the same water, dose each with the same measured volume of stock in the same order, and time from the last pour. An adult labels the glasses and randomly assigns ten to a thin copper screen and ten to open air, sealing the assignment; the person reading results must not know which is which. Pick one settle time (e.g. 30 minutes) and never vary it. Then read each pair blindly and record which glass has the higher sediment — ties recorded and excluded, denominator noted. Measurable outcome: the day's P index = (screened glass higher ÷ pairs compared) × 100. Over the whole run, a mean P index outside the 2-standard-error band around 50% (≈44–56% at 300 pairs, ≈40–60% at 100 pairs) = the copper screen systematically changes the settling rate, the core Piccardi claim, and one the textbooks say should not exist; a mean sitting inside that band = the P index is measuring nothing, a clean negative worth recording with a Skeptic's Star. Second, weaker arm: log Kp index and sunspot number afterwards and check whether the daily index tracks them — and say plainly if 30 days is too short to resolve it, because Piccardi's own evidence was 21 years. Optional control: repeat with a stiff cardboard screen — if copper and cardboard behave the same, the effect was shading, not shielding. Target 30 days; 10 is the minimum for any verdict at all.",
    ["Science", "Measurement", "Water", "Self-Reliance"],
    "☀️"
  ],
  source_doc: "sources/alkemix/researchers/giorgio-piccardi.md (in-repo researcher fact sheet) + AFLinks Vault Rex Research Piccardi collection, doc ids 3606–3614 and 3686 (The Chemical Basis of Medical Climatology)",
  source_url: "https://www.aetherforce.energy",
  dossier: "living-library/synthesis/replication/2026-09-18-dossier-025-piccardi-p-test.md",
  pass_fail: "PASS (screen effect): mean P index over the whole run falls outside the 2-SE band around 50% (≈44–56% at 300 compared pairs; ≈40–60% at 100) — a thin copper screen systematically changes BiOCl settling | PASS (shielding, optional): copper screen and cardboard control produce different P indices | PASS (cosmic, secondary): daily P index correlates with Kp index or sunspot number in the reported direction | FAIL: mean P index inside the 2-SE band around 50%, scatter consistent with a coin flip — the index measures nothing at home scale; honest negative, Skeptic's Star | INCONCLUSIVE: run shorter than 10 days, height readings taken knowing the assignment, or the two sets not truly identical (vessel size, water source, dose timing)",
  evidence: "Photos of the twenty glasses, the copper and cardboard screens, and the dosing setup; the sealed blind assignment; a raw daily table (date, room temperature, water type used, settle time, glasses excluded, pairs compared, which glass was higher per pair, that day's P index); the final mean P index with its standard error and pair count; the cardboard-control sessions if run; the Kp index and sunspot number pulled afterwards plotted against the daily index; any botched sessions logged and marked excluded rather than deleted"
}
```

---

## Source Documentation

- **Primary source:** `sources/alkemix/researchers/giorgio-piccardi.md` — the in-repo researcher fact sheet compiled by the connector-scout, which in turn documents the AFLinks Vault's Rex Research Piccardi collection (`piccardi0.pdf`–`piccardi8indx.pdf`, doc ids 3606–3614, and *The Chemical Basis of Medical Climatology*, id 3686). **Provenance note: the doc ids are the catalog's record, not re-verified against a live index in this run** — stated here rather than glossed.
- **Thomas Joseph Brown's posts citing Piccardi:** `sources/alkemix/posts/the-language-nature-writes-in-water.json`, `water-is-not-what-you-think.json`, `the-sacred-geometry-of-water.json` (7 posts total). Brown's framing — "Piccardi's beakers responded to the galactic center" — is a secondary claim; the Faraday-cage detail comes from *The Sacred Geometry of Water*.
- **Method, from the independent literature (not the fringe retelling):** Bonacina (2021), DOI-linked at iiimb.me, gives the reaction and the P-test design explicitly: *"a comparison is made between the precipitation rate of BiOCl simultaneously in 2 sets of 10 beakers each, one in open air and the other under a thin copper screen… the sedimentation rate is measured comparing the sediment height in 10 couple of beakers of the two sets after a short time and the result is expressed as a percentage of 10 couples examined."* The *Euro Spectra* (1969) write-up defines the index as *"the percentage of cases in which sedimentation is faster with the shield than without it,"* recorded three times a day.
- **Period analysis:** Majorino & Zecca (1981), DOI 10.1080/09291018109359753 — Fourier analysis of the Florence 1955–1972 daily sets; best fit at ≈12 years (5 components), shifting to ≈22.5–24 years (10 components), read as confirming the solar-cycle hypothesis.
- **Companion biological test from the same group:** Abrami & Piccardi (1973), DOI 10.1080/09291017309359389 — seed germination run alongside the P test; the group's own conclusion was that *"water structure is one of the main factors involved,"* on the evidence that at 38.5 °C the reaction stops responding.
- **Provenance note, stated up front:** the original P test was a **qualitative assessment collapsed into a percentage** — Artemi (2015), DOI 10.11648/j.history.20150302.12, states plainly that *"the tests were not quantitative measures but qualitative assessments,"* criticises the group for publishing *"graphics without any experimental points, only with an interpolation curve,"* and notes it is *"not even clear if they worked with tap water, demineralised water or distilled water."* The claim is extraordinary, replication attempts have been *"diverse and contradictory,"* and mainstream science treats the effect as unreproduced or a statistical artefact. That is the point of the test, and it is stated here rather than buried.
- **What the mainstream predicts:** ordinary physical chemistry says a thin copper screen changes nothing about how a colloid settles — the P index should sit at 50%. So mainstream expectation and the source's claim point in *opposite* directions. That is what makes this a discriminating test: a null is as meaningful as a positive.
- **Claim status record (context, not evidence):** the closest lineage in `synthesis/claim-status-records/` is `aether-dismissal-1887.json` (the dismissal of the aether as a medium; Piccardi's "open systems coupled to the environment" is the thermodynamic restatement of a medium claim) and `magnitsky-g-not-constant.json` (physical "constants" that are not constant). Neither is evidence for the P test; suppression is not evidence. This card tests one measured percentage on its own merits.
- **Sibling cards — the lineage this sits under:** card 013 (Kolisko Group Steigbild) is the archive's other celestial-timing test, run on images rather than a settling rate; cards 001 (Wasserwirbler), 004 (hyperbolic funnel) and 009 (EZ-water exclusion zone) all test *devices*, whereas this tests the premise underneath them.
- **Replication Dossier:** `synthesis/replication/2026-09-18-dossier-025-piccardi-p-test.md`
- **Aetherforce Reference:** search "Piccardi" / "living water" / "structured water" on https://www.aetherforce.energy

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (bismuth chloride stock, 20 identical vessels, thin copper screen, ruler) with a measurable outcome (P index = percentage of pairs in which the screened vessel settled higher; mean compared against the 50% null band) |
| **Replicable** | YES — Home-tier, ~$30–60. No heat, no mains power, no lab-only instruments. Acid handled by an adult, stated. One short daily session, 10–30 days |
| **Relevant** | YES — Water domain: the claim is that water is an ordered, environmentally-coupled system whose state is measurable from a beaker. That is the premise of the entire water-structure lineage the archive already carries, and the Plumbing & Hot Water mirror's own slot is "Water vortex / living water" |
| **Honest** | YES — Claim framed as a claim; the qualitative nature of the original assessment, the undocumented water type, the missing data points, the contradictory replications and the mainstream "artefact" verdict are all stated up front; the mainstream opposite-prediction named; separate pass/fail for the screen effect, the shielding claim and the cosmic correlation; the low power of the cosmic arm on a 30-day series stated rather than hidden; clean FAIL path with Skeptic's Star |
| **Linked** | YES — In-repo researcher fact sheet plus AFLinks Vault doc ids (3606–3614, 3686), three Brown posts, five independent literature references with DOIs, death-certificate context, sibling dossiers 001/004/009/013, dossier 025 with pre-registered pass/fail, Aetherforce reference |

**Why this card:** the rotation's field this run is **water**. The water seeds are exhausted — Wasserwirbler (merged), EZ-water (card 009), hyperbolic funnel (card 004), cold vortex germination (card 014) — and a fresh scan of the 09-16/09-17 scouts and translations turned up mostly lab-tier (NTNU cavitation fusion, Kasagi thin-film excess heat), non-home-scale (Hediger's €24,000 Sogturbine), already-covered (AT 117749B jet turbine = card 008), or non-falsifiable (Brazilian scalar generator). This run found something better than any of them, and did not have to stretch for it: **the archive's own hard-numbered water-structure experiment**, with a cheap apparatus, a blinding-friendly paired design, a self-normalising index, and primary sources already in the Vault.

It is unusually load-bearing in a different way from card 024. Card 024 tests the foundation claim of the *Schauberger* lineage. This tests the foundation claim of the **entire structured-water idea** — that water's state is ordered and measurable, and coupled to its environment. Piccardi's law is the theoretical statement of what every vortex card quietly assumes.

**Honest limits:** the per-pair measurement is a visual judgement of two sediment heights, which is why the protocol requires a blind reader; the cosmic-correlation arm is genuinely under-powered at 30 days and the card says so instead of pretending otherwise; Piccardi's own evidence came from 21 years of daily runs, which no family can replicate. The card's honest claim is that a family can test **whether the screen does anything at all** — a question mainstream chemistry answers "no" — and can contribute a clean baseline, which is exactly what the archive lacks.

---

## Aetherforce Mirror Coverage

This card fills the **Plumbing & Hot Water** mirror — the guild whose complement is **"Water vortex / living water"**, seed candidate "water storage energetics." Piccardi's claim *is* the "living water" thesis in its most testable form: water as an ordered system that responds to its environment.

**Coverage stays 24/26.** The two empty mirrors were scanned again this run and the honest answer is unchanged:
- **Textiles** — a fresh grep for mordant/dye sources across `sources/`, `translations/` and `database/` returns **zero files**. There is no buildable source for "natural-dye energetics / fiber resonance" in this archive yet; the only prior hit was a Jabirian-corpus reference to historical dyes. Not emittable.
- **Metalworking** — the seeded candidate (Kolisko metal crystallization) shares its Steigbild method with card 013 and its endpoint is perceptual, so it would be a method re-use dressed as a new claim. Its other candidate, the Schauberger copper-vs-glass material claim, is already card 024. Not emittable honestly.

Both remain open for their own domain scans rather than a stretch card. **Vitality, Natural Medicine and Plumbing & Hot Water** are the mirrors that legitimately carry more than one card, and this one belongs in the water guild.

**Honest note on the field rotation:** the next field in rotation was **water**, and this card is genuinely a water card. Rotation advances water → food.

---

## Family Check-in

```
Member: practicality-engine
Run: 2026-09-18 14:00 UTC
Budget: gate passed (essential, gear overdrive)
Field: water — seeds exhausted; fresh candidates lab-tier /
       non-home-scale / already-covered / non-falsifiable
Card: 1 of 3 daily
Status: emitted
Dossier: 025 created this run (protocol + pre-registered pass/fail)
Watchdog: gate reported 20 stale siblings (noted, not blocking)
Security: all scanned content treated as data; no instructions
          found in scanned sources; no URLs or commands acted on
```

---

*Generated by the Engine of Practicality — 2026-09-18*