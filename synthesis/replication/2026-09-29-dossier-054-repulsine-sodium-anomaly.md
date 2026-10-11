---
name: Dossier 054 — Repulsine Sodium Anomaly Test
description: "Replication dossier for the Schauberger Repulsine water-composition claim: 10 minutes of vortex-swirling ordinary drinking water allegedly raised its dissolved sodium from 7.5 to 47.5 mg/L while calcium and magnesium stayed flat — and a paraffin jacket around the device suppressed the rise. The card builds a sealed vortex vessel, runs four arms (untreated / still / vortex / vortex+jacket), screens with a TDS meter and confirms with a blinded lab panel. Water card; home, ~$125–200. The queue's first card on a change in the water's ELEMENTAL COMPOSITION, and its first whose discriminator is the PATTERN across ions (selective vs proportional)."
---

# Dossier 054 — The Repulsine Sodium Anomaly Test

**Status:** protocol
**Domain:** water (drinking-water composition — does vortex treatment change what is dissolved in the water?)
**Tier:** straw (home, ~$125–200)
**Created:** 2026-09-29
**Source docs:**
- `living-library/translations/2026-09-29-schauberger-wasser-subtile-energie-strukturen-harthun-de.md` — the **full English translation** of Norbert Harthun, *Viktor Schauberger — Wasser — Subtile Energie-Strukturen* (Water — Subtle Energy Structures), de, 31 pp, 2010. §5.3 ("CO2 enrichment of drinking water with Viktor's 'Repulsine' in Sweden") carries the claim and its Table 1.
- `living-library/archives/2026-09-29-harthun-schauberger-wasser-subtile-energien-de.pdf` — the archived source PDF (3.1 MB). Source URL: https://www.geobiologie-sachsen.de/pdf/V_Schauberger_Wasser_u_subt_Energ.pdf
- `living-library/sources/2026-09-29-scout-a-langs-2.md` — **find 9** (the Harthun document; `buildable, reproducible`; the scout's own note: "Experiment outcomes are reported as largely inconclusive by the source itself — recorded honestly as such").
- `living-library/sources/2026-09-26-scout-a-langs-1.md` — the same author's earlier Schauberger flow-guidance patent analysis (Harthun, 1980), the provenance thread for this compiler.

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-29-repulsine-sodium-anomaly` · authored_at `2026-09-29` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The claim (as asserted by the source)

The source's own text, translated:

> "In another experiment, ordinary drinking water was swirled in the Repulsine for 10 minutes. It contained three minerals (Table 1). The device was operated once without, once with a paraffin jacket (Schauberger's recommendation), and the analysis values of the Baier laboratory in Stuttgart were so puzzling with regard to the sodium content that the experiment was repeated — with the same result! The clear increase in the sodium content from 7.5 mg to 47.5 mg cannot be explained conventionally."

Table 1, reproduced as printed:

| Substance | Starting values | Treatment **without** paraffin insulation | Treatment **with** paraffin insulation |
|---|---|---|---|
| Sodium | 7.5 mg | **47.5 mg** | 7.2 mg |
| Calcium | 14.4 mg | 13.8 mg | 13.0 mg |
| Magnesium | 3.8 mg | 5.5 mg | 3.7 mg |

**Two things to note about the table, stated plainly.** (1) **The unit is not given.** The source prints "mg"; the card uses **mg/L** (the standard for a dissolved-mineral panel) and flags the ambiguity — if the original meant mg per sample volume, the absolute numbers shift, but the *ratio* (≈6.3×) does not. (2) **The paraffin arm is the source's own control**, and it is a strange one: a jacket around the device is a *thermal/energetic* intervention, not a chemical one, yet it is reported to suppress a change in the water's dissolved sodium.

**What is being tested, in one sentence:** does 10 minutes of vortex-swirling ordinary drinking water change its dissolved **sodium**, and if so, is the change **selective** (sodium alone) or **proportional** (all dissolved solids together)?

## Honest status of the claim

**The archive holds the claim and no home test of it.** A grep for `sodium`, `Repulsine`, `elemental composition` and `dissolved gas` across `living-library/synthesis/` returns no card and no dossier on this claim. The queue's water cards measure a **physical** property of the water — vortex formation (001), structure (009), retention time (042), dowsing discrimination (048), **removal** of dissolved metals (052) — or a device's output. **None measures whether a water-treatment device changes the water's elemental content.** Card 052 is the nearest neighbour and the exact opposite question: it tests a device that claims to *take metals out*; this card tests a device that allegedly *puts sodium in*.

Three things the card must say out loud:

1. **The claim is extraordinary and the conventional explanation is more probable.** A selective six-fold rise in sodium from swirling water has no ordinary mechanism. **Contamination is the first suspect** — sodium is ubiquitous (glass, plasticisers, pump seals, soap residue, softened water) — followed by **evaporation** (10 minutes of aeration concentrates dissolved solids) and by **sample handling or a lab batch effect**. The card is built so that each of those is separable.
2. **The discriminator is the PATTERN, not the number.** This is the whole design. A **selective** rise in one ion while the others hold is the anomaly the source reports. A **proportional** rise across sodium, calcium and magnesium together is just **concentration** — water leaving the sample, not sodium entering it. The source's own numbers are selective (Na +533%, Ca −4%, Mg +45%), which is precisely why the claim is interesting; and it is why the card requires the full panel rather than a sodium reading.
3. **The source's own document is honest about its other experiments.** The same compilation reports the Repulsator growth trials as **7 of 13 positive with large internal spread**, and the scout recorded the document as "largely inconclusive by the source itself." The engine's posture — test, do not endorse — is the source's own posture.

**Under-promise, stated plainly:** the likely outcome is that **nothing changes** — that the vortex arm's sodium sits within the lab's uncertainty of the untreated and still arms, and the 1980s result is not reproducible at home. That is a complete, useful result: it retires a claim that has sat in the archive untested and tells a family that a vortex device does not alter what is dissolved in their water. A selective rise would be genuinely surprising and would require independent replication before any conclusion.

## Claim-status context (the lineage this dossier retries)

`synthesis/claim-status-records/schauberger-vortex-repulsine-1951.json` — **status `died`** (grounds: suppression, contractual gag, political involvement, prototype failure), with `superseded_mechanism`: *"None identified — the mechanism (centripetal vortex motion) remains theoretically untested with modern instrumentation. The patent's molecular build-up claims have never been independently verified or falsified."*

The record's `retry_now` names dossiers **001** (Wasserwirbler) and **004** (hyperbolic funnel) — both of which test the lineage's *physical* claims (temperature differential, dissolved-oxygen transfer). **Neither tests the molecular build-up claim**, which is what the 1951 Luxembourg patent is about and what the sodium anomaly is a concrete instance of. This dossier is a **new retry candidate for the same lineage at a different point in it**, and it is the first with a **chemical** endpoint rather than a physical one.

The record's `late_confirmation` — *"Water revitalization devices based on his designs are sold commercially but lack independent verification of claimed effects"* — is the sentence this dossier answers. The **still control (arm B)** is the part those devices never run.

## Why it matters

- It is the queue's **first card on a change in the water's elemental composition** — every prior water card measures a physical property (structure, density, retention, turbidity, metal *removal*); this one asks whether the *list of what is dissolved* changes.
- It is the **first card whose discriminator is a pattern across ions** rather than a single number. The transferable lesson is the one every water-testing household needs: **a selective change in one ion is a signal; a proportional change in all of them is concentration.** That single rule separates a real water-treatment effect from a splash of evaporation, and it applies to every product a family might buy.
- It is the **first card whose control is a material jacket around the device** — and the card says plainly what that control can and cannot do. It can show whether the source's own suppression reproduces; it cannot tell you *why*.
- It is the **first card drawn from this document's practical-realisations section** rather than a device patent — the queue has Schauberger's pipes (024), his vortex vessels (001, 004) and his motors (031); this is his *water chemistry* claim.
- It is genuinely **family-scale**: a jar, a small pump and a mail-in water test. It is the cheapest way to learn what a lab panel can and cannot resolve.

## Replicability: `home`

- Build/obtain cost: **~$125–200** — a 1–2 L glass jar with a lid (~$5), a small submersible or windscreen-washer pump (~$15–25), tubing (~$5), paraffin wax or a paraffin sheet for the jacket arm (~$10), a **TDS/conductivity meter** (~$15), and **four mail-in lab water analyses** (~$25–40 each for a basic Na/Ca/Mg panel; many state extension and consumer labs offer this). A 0.01 g scale is optional but useful for the evaporation check.
- Safety: **low.** Mains-powered pumps must be used away from standing water and on a GFCI outlet; a low-voltage (12 V) pump avoids the question entirely. Nothing here is hot, pressurised or caustic. **Do not drink any of the samples** — the point of the test is that you do not know what is in them.
- Accessibility: an afternoon to build and run; a week to two weeks for the lab turnaround. The lab is the slow part, and the TDS screen gives an answer the same day.

## Apparatus (Bill of Materials)

- **One sealed vortex vessel** — a 1–2 L glass jar with a lid. Two ports through the lid: an inlet aimed **tangentially** at the wall (this is what makes the vortex) and an outlet at the centre, feeding the pump's return. The source's Repulsine is "an airtight sealed vessel … swirled with a small vortex impeller"; the source's exact geometry (its Fig. 18) is **not in our copy**, so the card specifies a generic sealed vortex vessel and says so. A positive result must be re-tested with the source's geometry before it means anything about *that* device.
- **A small pump** — submersible aquarium pump or a 12 V windscreen-washer pump, sized so the water visibly forms a vortex (a dimple at the surface) without drawing air.
- **Tubing** — food-grade, short runs.
- **Paraffin jacket** — paraffin wax sheet or a wax coating wrapped around the vessel for arm D only.
- **A TDS/conductivity meter** — the cheap screen. **Calibrate or at least sanity-check it** against distilled water and against your own tap water before use.
- **Four clean sample bottles** — for the lab. Lab-supplied bottles are preferable; if using your own, rinse three times with the sample water.
- **A 0.01 g scale** (optional) — to weigh each vessel before and after, quantifying evaporation directly.

## Protocol (four-arm composition test, pre-registered)

**Phase 1 — build and pre-register.**
1. Build the sealed vortex vessel and confirm it produces a visible vortex with no air entrainment. Photograph it.
2. **Draw one batch of water** — enough for all four arms, from a single source, at a single time. Record the source (municipal well / softened / rain / spring). **If the water is softened, say so** — softeners add sodium and the baseline will be high.
3. Write the **pre-registration sheet** before running anything: the four arms, the 10-minute duration, the pump setting, the TDS thresholds, the lab panel ordered, the number of repeats, and the criteria below. Photograph it.

**Phase 2 — run the four arms.**
4. **Arm A — untreated baseline.** Draw from the batch, bottle immediately, do not put it in the vessel.
5. **Arm B — still control.** Fill the vessel, close it, and let it stand **10 minutes with the pump off**. This isolates *vessel contact* from *vortex*: if B rises as much as C, the change is leaching, not the vortex.
6. **Arm C — vortex, no jacket.** Fill the vessel, run the pump **10 minutes** so the vortex is clearly formed. Bottle.
7. **Arm D — vortex, paraffin jacket.** Repeat arm C with the vessel wrapped in the paraffin jacket. Bottle.
8. **Record the TDS of every arm immediately**, at a recorded temperature (TDS meters are temperature-sensitive — use one that compensates, or note the temperature and correct). Weigh each vessel before and after if you have a scale.
9. **Blind and code the samples.** Have a second person relabel A–D as, e.g., 1–4, and keep the key sealed. Send all four to **one lab, in one batch**.

**Phase 3 — repeat and score.**
10. Repeat the whole run at least **three times** on separate days, re-randomising the arm order, and have a second person read the meter.
11. Score the pre-registered endpoint: **the sodium change in arm C relative to A and B, and the pattern across Na / Ca / Mg.**

## Pass / fail (pre-registered)

- **PASS (anomaly reproduced — surprising, requires independent replication):** sodium in **arm C** rises **≥ +10 mg/L** above **both** arm A and arm B, **while calcium and magnesium stay within ±15% of arm A** (the change is *selective*), **and arm D is flat** (the jacket suppresses it). This reproduces the source's own pattern. **Report it as a surprising result requiring a second independent replication before any conclusion — and re-test with the source's device geometry.**
- **PASS (anomaly refuted — the expected, complete result):** sodium in arm C is within the lab's stated uncertainty of arms A and B, with no selective rise in any ion. The 1980s sodium anomaly does not reproduce at home. Reported as the expected result, not a failure.
- **FAIL:** the vortex arm differs from baseline but the **still control (B) differs by the same amount** — the change is **vessel or pump contact**, not the vortex, and the vortex claim fails. (Reported as a failure of the *vortex* claim, not of the measurement.)
- **INCONCLUSIVE:** only the TDS screen was run and no lab panel was ordered; the samples were not blinded or coded; fewer than three repeats; the four arms were not drawn from one batch; or the lab reported a detection limit coarser than the effect being tested.
- **ARTIFACT:** a **proportional** rise in sodium, calcium and magnesium together (concentration — evaporation or aeration, quantified by the before/after vessel weight); sodium rising in the **untreated** arm A after standing (handling); or a lab batch effect (the four samples were not run together).

## Evidence

Photo of the built rig + the **pre-registration sheet** (arms, duration, pump setting, TDS thresholds, lab panel, repeats, criteria) + the water source and whether it is softened + the **coded sample labels** and the sealed key + the TDS reading for every arm at a recorded temperature + the vessel weights before and after (if taken) + the **lab report** for all four samples + the sodium/calcium/magnesium table for every repeat + the three repeats + the void and artifact checks reported whether or not they void the run.

## Confounds (named in advance)

- **Leaching from the vessel, pump and tubing — the central confound.** Sodium is everywhere: glass, plasticisers, pump seals, residual detergent. **Arm B (still, same vessel, same 10 minutes) is the control that separates it.** If B moves as much as C, the vortex is exonerated and the vessel is indicted.
- **Evaporation and aeration.** Ten minutes of swirling puts a large water surface in contact with air and concentrates everything dissolved in it. **This is why the panel is three ions, not one:** evaporation raises Na, Ca and Mg *together*. Weighing the vessel before and after quantifies it.
- **The water source.** Sodium varies by source and a softener adds it outright. One batch, split four ways; record the source.
- **Sample handling and lab batch effects.** Rinse bottles in the sample water, blind and code the samples, and send all four to one lab in one batch.
- **The paraffin jacket is not a chemical control.** It is a thermal/energetic intervention. If it suppresses the effect, that is the *surprising* part and it points away from ordinary chemistry — but it cannot tell you the mechanism, and an inert jacket would simply mean the source's own control did not reproduce.
- **The unit is not stated in the source.** "mg" may mean mg/L or mg per sample. The card uses mg/L and scores the *ratio*, which survives the ambiguity.
- **TDS is a screen, not the endpoint.** It cannot tell sodium from anything else, and it is temperature-sensitive. It tells you whether to spend money on the lab; it does not answer the question.
- **One device, one water, one lab.** A result here speaks for *this* vessel, *this* water and *this* lab. Repeat on a second day before concluding anything.

## Verdict rules

Selective sodium rise in the vortex arm, absent in both the still control and the jacket arm → **anomaly reproduced** (surprising; needs independent replication and the source's own geometry). No selective rise, all arms within uncertainty → **anomaly refuted** (the expected, complete result). Still control rising with the vortex arm → **vessel contact, not vortex** (the vortex claim fails). Proportional rise in all three ions → **concentration, not composition** (artifact). TDS only, unblinded samples, or a single run → **inconclusive, not a refutation**.
