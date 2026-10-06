---
name: Repulsine Sodium Anomaly Test
description: "Test whether 10 minutes of vortex-swirling ordinary drinking water changes what is dissolved in it — the Schauberger Repulsine claim that sodium rose from 7.5 to 47.5 mg/L while calcium and magnesium stayed flat, and that a paraffin jacket around the device suppressed it. Four arms (untreated / still / vortex / vortex+jacket), a TDS screen, and a blinded lab panel. Water card; home, ~$125–200; Self-Reliance mirror (Homesteading complement). The queue's first card on a change in the water's ELEMENTAL COMPOSITION, and its first whose discriminator is the PATTERN across ions — selective vs proportional."
---

# ⚡ Aetherforce — Self-Reliance

**Guild:** Aetherforce — Self-Reliance
**Quest Line:** ⚡ Aetherforce · Homesteading complement
**Tier:** straw
**Domain:** water (drinking-water composition — does vortex treatment change what is dissolved in the water?)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-29-repulsine-sodium-anomaly` · authored_at `2026-09-29` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Self-Reliance",
  desc: "Every water device on the market claims to change your water. Almost none of them tell you how to check. This card checks the loudest claim in the Schauberger archive: that ten minutes of vortex-swirling ordinary drinking water raised its dissolved sodium from 7.5 to 47.5 mg/L while calcium and magnesium sat still - and that wrapping the device in a paraffin jacket stopped it. One batch of water, four arms: untreated, held still in the same vessel, swirled, and swirled with the jacket. Screen every arm with a $15 TDS meter, then send blinded, coded samples to a lab. The whole test turns on one idea you can use on any product you ever buy: a rise in ONE mineral while the others hold is a signal; a rise in ALL of them together is just water leaving the sample. Build it, run it, and find out what your water is actually made of. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Repulsine Sodium Anomaly Test",
    "Build a sealed vortex vessel - a 1-2 L jar with a lid, an inlet aimed tangentially at the wall and a central outlet back to a small pump - and confirm it forms a visible vortex without drawing air. Draw ONE batch of water from one source and split it four ways. Arm A: untreated, bottled at once. Arm B: held still in the same vessel for 10 minutes with the pump OFF (this is the control that separates the vortex from the vessel). Arm C: swirled 10 minutes. Arm D: swirled 10 minutes with the vessel wrapped in a paraffin jacket. Record the TDS of every arm immediately at a recorded temperature, and weigh each vessel before and after if you have a scale. Then have a second person relabel the samples 1-4, seal the key, and send all four to ONE lab in ONE batch for a sodium/calcium/magnesium panel. Repeat the whole run three times on separate days. Measurable outcome: the sodium change in arm C against arms A and B, AND the pattern across all three ions - a rise in sodium ALONE of +10 mg/L or more, with calcium and magnesium within 15% of baseline and arm D flat, reproduces the source's anomaly and needs independent replication; a rise in all three ions together is concentration (evaporation), not composition, and is an artifact; no change in any arm means the anomaly does not reproduce at home, which is the expected result.",
    ["Science", "Chemistry", "Measurement"],
    "🧪"
  ],
  source_doc: "translations/2026-09-29-schauberger-wasser-subtile-energie-strukturen-harthun-de.md (Norbert Harthun, 'Viktor Schauberger — Wasser — Subtile Energie-Strukturen', de, 2010, §5.3 + Table 1) + archives/2026-09-29-harthun-schauberger-wasser-subtile-energien-de.pdf + sources/2026-09-29-scout-a-langs-2.md#find-9",
  source_url: "https://www.geobiologie-sachsen.de/pdf/V_Schauberger_Wasser_u_subt_Energ.pdf",
  dossier: "living-library/synthesis/replication/2026-09-29-dossier-054-repulsine-sodium-anomaly.md",
  pass_fail: "PASS (anomaly reproduced - surprising, requires independent replication): sodium in the vortex arm rises >= +10 mg/L above BOTH the untreated and still arms, while calcium and magnesium stay within +/-15% of baseline (the change is SELECTIVE), and the paraffin-jacket arm stays flat. Report as a surprising result needing a second independent replication - and re-test with the source's own device geometry before it means anything about that device. PASS (anomaly refuted - the expected, complete result): sodium in the vortex arm sits within the lab's stated uncertainty of the untreated and still arms, with no selective rise in any ion. FAIL: the vortex arm differs from baseline but the STILL control differs by the same amount - the change is vessel or pump contact, not the vortex. INCONCLUSIVE: TDS screen only with no lab panel; samples not blinded or coded; fewer than three repeats; the four arms not drawn from one batch; or a lab detection limit coarser than the effect. ARTIFACT: a PROPORTIONAL rise in sodium, calcium and magnesium together (concentration - evaporation or aeration, quantified by the before/after vessel weight); sodium rising in the untreated arm after standing (handling); or a lab batch effect (samples not run together).",
  evidence: "Photo of the built rig + the pre-registration sheet (arms, duration, pump setting, TDS thresholds, lab panel, repeats, criteria) + the water source and whether it is softened + the coded sample labels and the sealed key + the TDS reading for every arm at a recorded temperature + the vessel weights before and after (if taken) + the lab report for all four samples + the sodium/calcium/magnesium table for every repeat + the three repeats + the void and artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the claim and the table):** Norbert Harthun, *Viktor Schauberger — Wasser — Subtile Energie-Strukturen* (Water — Subtle Energy Structures), de, 31 pp, 2010 — https://www.geobiologie-sachsen.de/pdf/V_Schauberger_Wasser_u_subt_Energ.pdf (**full English translation in the library and read this run**: `translations/2026-09-29-schauberger-wasser-subtile-energie-strukturen-harthun-de.md`; archived PDF: `archives/2026-09-29-harthun-schauberger-wasser-subtile-energien-de.pdf`). §5.3 carries the claim in the source's own words: *"ordinary drinking water was swirled in the Repulsine for 10 minutes … the analysis values of the Baier laboratory in Stuttgart were so puzzling with regard to the sodium content that the experiment was repeated — with the same result! The clear increase in the sodium content from 7.5 mg to 47.5 mg cannot be explained conventionally."* Table 1 gives sodium 7.5 → **47.5** (no jacket) → 7.2 (jacket), calcium 14.4 → 13.8 → 13.0, magnesium 3.8 → 5.5 → 3.7.
- **The same document's own honesty (context for the card's posture):** §5.11 reports the Repulsator growth trials sent to ~20 growers in Sweden and Finland — **13 reports, 7 positive, "the differences within the 7 were large"**, effective radius 3.5 m or less, and *"No success can be guaranteed."* §5.6 gives the author's own buildable composite-vortex rig (a preserving jar, a windscreen-washer pump, hoses, a central suction tube). The card's apparatus is in that lineage.
- **Scout entries:** `sources/2026-09-29-scout-a-langs-2.md` (**find 9** — the Harthun document; `buildable, reproducible`; the scout's own note: *"Experiment outcomes are reported as largely inconclusive by the source itself — recorded honestly as such"*; host flagged **fragile** — a single PDF on a regional geobiology site, no mirror); `sources/2026-09-26-scout-a-langs-1.md` (the same compiler's 1980 Schauberger flow-guidance patent analysis — the provenance thread).
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-29-dossier-054-repulsine-sodium-anomaly.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "Schauberger", "Repulsine", "water structure", "vortex water"
- **Aetherforce Reference:** Search "Schauberger", "Repulsine", or "vortex water" on https://www.aetherforce.energy
- **Related dossiers:** 052 (Shared Well Iron & Manganese Vortex — the exact opposite question: a device that claims to take metals **out**; this card asks whether a device puts sodium **in**), 042 (Water Memory Persistence — the queue's other card on a water *state* rather than a water *device*), 048 (Pendulum Water-Quality Discrimination — the queue's other drinking-water-quality card, and the other one whose comparator is a lab-equivalent assay), 001 (Wasserwirbler) and 004 (Hyperbolic Funnel) — the same vortex lineage, a *physical* claim rather than a chemical one

---

## Claim-status context (the lineage this card retries)

`synthesis/claim-status-records/schauberger-vortex-repulsine-1951.json` — **status `died`**, grounds: suppression, contractual gag, political involvement, prototype failure. The record's own `superseded_mechanism` field reads: *"None identified — the mechanism (centripetal vortex motion) remains theoretically untested with modern instrumentation. The patent's molecular build-up claims have never been independently verified or falsified."*

**That is the gap this card fills.** The record's `retry_now` names dossiers 001 (Wasserwirbler) and 004 (hyperbolic funnel) — both of which test the lineage's *physical* claims (temperature differential, dissolved-oxygen transfer). **Neither tests the molecular build-up claim**, which is the one the 1951 Luxembourg patent is actually about and the one the sodium anomaly is a concrete instance of. This card is therefore a **new retry candidate for the same lineage**, at a different point in it: not "does the vortex form," but "does the vortex change what is dissolved."

**The record's `late_confirmation` is also worth carrying:** *"No mainstream physics program has tested Schauberger's vortex claims with calibrated instrumentation. Water revitalization devices based on his designs are sold commercially but lack independent verification of claimed effects."* The card's four-arm, blinded, lab-assayed design is the cheapest available answer to that sentence — and its **still control** is the part the commercial devices never run.

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (a sealed vortex vessel, a small pump, a paraffin jacket, a TDS meter, four lab samples) with a named procedure (one batch, four arms, 10 minutes each, blind and code, one lab batch) and a measurable outcome (the sodium change in the vortex arm **and** the pattern across Na / Ca / Mg). Not pure theory. |
| **Replicable** | YES — Home, ~$125–200: a jar, a small pump, tubing, paraffin, a $15 TDS meter, and four mail-in lab analyses. No mains work required (a 12 V pump avoids it entirely). One afternoon to build and run; a week or two for the lab. |
| **Relevant** | YES — Water domain: what is actually dissolved in the drinking water a household treats and drinks. Fills the **Self-Reliance** mirror (the Homesteading complement), the queue's water-independence lane. |
| **Honest** | YES — The claim is framed as a claim and the card states up front that the conventional explanation (contamination, evaporation, handling) is more probable than the source's. The source's own compilation reports its other experiments as largely inconclusive, so the card's posture is the source's posture. Clean refutation path and a clean "the vessel did it, not the vortex" path. |
| **Linked** | YES — One primary source read this run (translation + archived PDF), two scout entries, a pre-registered replication dossier, the lineage's claim-status record, a Vault search pointer, and cross-links to five related cards. |

**Mirror choice, stated:** the card's **domain is water** (the rotation's next field) and its **guild complement is Self-Reliance** — the Homesteading mirror, whose theme is off-grid water independence. **Plumbing & Hot Water** (the water-vortex/living-water mirror) was the alternative and is where the queue's other Schauberger *device* cards sit (001, 004, 025, 031); **Self-Reliance** was chosen because this card's question is not "does the device work" but **"what is actually in the water I drink, and how would I know?"** — the same reason the queue's other drinking-water-quality card (048, the pendulum discrimination test) sits here. It is the mirror's 4th card.

---

## The honest framing (the spine of the card)

**The claim is a claim.** The source says ten minutes of vortex-swirling raised dissolved sodium more than six-fold, that a Stuttgart laboratory measured it, and that the experiment was repeated with the same result. **This card tests that claim; it does not endorse it.**

**The conventional explanation is the more probable one, and the card says so first.** Sodium is the most easily contaminated ion in any water test — it is in glass, in plasticisers, in pump seals, in detergent residue, and in softened water outright. Ten minutes of swirling also aerates and evaporates, which concentrates everything dissolved. **A card that only measured sodium would be measuring its own contamination.** The design exists to separate those.

**The design that makes it a measurement.** Three things do the work:

1. **The still control (arm B) is the whole test.** Same vessel, same water, same ten minutes — pump off. If the still arm rises as much as the vortex arm, the vessel is responsible and the vortex is exonerated. **Without arm B, a positive result means nothing.**
2. **The panel is three ions, not one.** This is the discriminator. **Evaporation raises sodium, calcium and magnesium together.** A *selective* rise in sodium while the other two hold is the anomaly the source reports — and the source's own numbers are selective (Na +533%, Ca −4%, Mg +45%). **A proportional rise is concentration, not composition.** That single rule is the transferable lesson, and it applies to every water product a family might buy.
3. **The jacket arm is the source's own control, carried forward.** The source reports that a paraffin jacket around the device *suppressed* the rise. The card runs that arm because it is the source's own internal check — and states plainly that a jacket is a thermal/energetic intervention, not a chemical one, so it can show whether the suppression reproduces but cannot explain it.

**The likely result is "nothing changed," and that is a complete result.** If the vortex arm's sodium sits within the lab's uncertainty of the untreated and still arms, the honest verdict is *"the 1980s sodium anomaly does not reproduce at home; a vortex device does not change what is dissolved in your water."* That retires a claim that has sat in the archive untested, and it is exactly what a family needs to know before spending on any water-treatment device. A selective rise would be genuinely surprising and would need independent replication — and a re-test with the source's own device geometry, since **that geometry is not in our copy of the document**.

**The central limitation, stated up front: one vessel, one water, one lab.** The source's Repulsine construction is a figure we do not have; the card specifies a generic sealed vortex vessel and says so. A result here speaks for *this* vessel and *this* water, and the card requires three repeats on separate days before any conclusion.

**Safety and honesty:** this is a bench experiment with a small pump and a jar — **low hazard**, but use any mains-powered pump away from standing water on a GFCI outlet (a 12 V pump avoids the question). **Do not drink the samples** — the entire point is that you do not know what is in them.

---

## Relationship to the rest of the queue

This card is the **composition counterpart to card 052** (Shared Well Iron & Manganese Vortex). 052 tests a device that claims to **take metals out** of a shared well; this card tests a device that allegedly **puts sodium in**. Same domain, opposite direction — and the overlap is stated here rather than hidden.

It is the **first card in the queue about a change in the water's elemental composition**, and the **first whose discriminator is a pattern across ions** rather than a single number. Every prior water card measures a physical property — vortex formation (001), structure (009), retention time (042), dowsing discrimination (048), metal removal (052) — or a device's output. This one asks whether the *list of what is dissolved* changes, which is a different question with a different instrument.

It is also the **first card whose control is a material jacket around the device**, and the first drawn from this document's *practical realisations* section rather than a Schauberger patent — the queue has his pipes (024), his vortex vessels (001, 004) and his motors (031); this is his water-chemistry claim.
