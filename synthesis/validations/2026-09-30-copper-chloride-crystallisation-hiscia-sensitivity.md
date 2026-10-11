---
name: Goethean Method — Copper Chloride Crystallisation Tested for Sensitivity at the Hiscia Institute (Scientific Reports, 2026)
description: A peer-reviewed pilot in Scientific Reports takes the Steigbild / Kolisko picture-forming method into the phytopharmaceutical quality question and asks a narrower question than the tradition does — can the copper-chloride fingerprints see differences that are independently known to be there? The answer grades cleanly: 7 of 7 image variables separate two mistletoe subspecies, 4 separate apple- from oak-grown mistletoe, and only 2 separate hand- from machine-blended extract, against 6 systematic control experiments that hold flat. The one test that is not merely re-detecting known chemistry is the third, and the authors themselves call its systems-level reading speculative.
---

# Validation — Copper Chloride Crystallisation as a Systems-Level Characterisation Method

**Domain:** anthroposophical / Goethean experimental method (picture-forming analysis — Pfeiffer's copper chloride crystallisation, the Kolisko lineage)
**Recorded:** 2026-09-30 (Replication Watch)

## What was claimed

The picture-forming methods were proposed inside anthroposophical research as a way of reading a substance's *whole* state rather than any single constituent. Lili Kolisko put plant sap on filter paper and studied the rising shapes (capillary dynamolysis, "Steigbild"); **Ehrenfried Pfeiffer**, on Steiner's suggestion, mixed plant substance or blood with metal salts — above all **copper(II) chloride dihydrate** — and let the solution crystallise in a shallow dish. The claim attached to the resulting dendritic picture is that it is a **fingerprint of the sample as a system**: sensitive not only to chemistry but to growing conditions, preparation, and (in the strongest version of the claim) non-material or formative factors.

The claim under test here is the *usable* part of that: that a CuCl₂ crystallisation fingerprint carries systems-level information a normal analytical assay would miss — specifically that it can distinguish samples that differ only subtly, including a manufacturing step whose difference other metabolomic methods could not detect.

The method itself is real chemistry and has been used since the 1930s for food-quality work; a 2024 handbook and roughly 40 peer-reviewed papers exist. What has been contested is whether the patterns carry anything beyond the sample's ordinary chemistry, and whether any of it replicates.

## Who replicated it, when

**Greta Guglielmetti, Paul Doesburg, Claudia Scherr, David Martin, Stephan Baumgartner and Alexander L. Tournier** — the **Hiscia Research Institute (Society for Cancer Research), Arlesheim, Switzerland**, with the Institute of Integrative Medicine at the **University of Witten/Herdecke** (Germany) and the Institute of Complementary and Integrative Medicine at the **University of Bern** (Switzerland).

**Experiments run January–March 2023. Published 24 February 2026** in *Scientific Reports* **16**, article 7506, open access.

Two things make this the strongest entry on this rail so far. It is a **mainstream, peer-reviewed venue** publishing an institutional version of the method, and it is **not run by the claimants' opponents or by its promoters alone** — it is the method's own community subjecting it to blinded, pre-designed sensitivity tests and reporting the weak parts as weak.

## Method

**Samples.** *Viscum album* L. (mistletoe) extracts, three of them: subsp. *album* grown on **apple**, subsp. *album* grown on **oak**, and subsp. *austriacum* grown on **pine**. All supplied by **Iscador AG, Arlesheim**. Two production batches were used (**2109**, made September 2021; **2204**, made April 2022), so the "batch" factor is real and biological, not a lab artefact. Three extracts × two blending procedures × two batches = **12 stock solutions per experimental day**, each prepared fresh from 20 vials.

**The three progressively finer differences — the design is the point.** The study asks one question three times, in order of difficulty:

1. **Subspecies** (*album* vs *austriacum*) — already distinguishable by standard HPLC, so this is the easy test that the instrument *must* pass.
2. **Host tree** (apple vs oak, same subspecies) — a modest chemical difference.
3. **Blending procedure** (hand vs machine) — the subtlest. The machine is one **specifically developed for this purpose at Hiscia** for anthroposophical pharmacy, which claims it modifies *systemic* properties of the remedy. A **recent metabolomics study could not detect any chemical difference** between the two processes. This is the test that matters.

**Rig.** Two crystallisation chambers at the Hiscia laboratory, built to the Andersen design, held at **29 °C, 49% initial relative humidity, 4 cm s⁻¹ air velocity**. Crystallisation solution = sample + CuCl₂·2H₂O + deionised water, pipetted into Petri dishes arranged in **two concentric rings, 43 allocations per run**, on cleaned float glass with acrylic rings. **150 mg sample and 150 mg CuCl₂ per plate**; four plates per sample (technical replicates). Evaporation photographed at 10-minute intervals from the chamber ceiling.

**Analysis.** Fingerprints scanned in transmission after ≥24 h at 26 °C / 44% rH, colour-calibrated against an IT8.7 target, then analysed by the group's **ACIA** software using **seven variables** describing *texture* (kappa, cluster_shade, entropy, diagonal_moment) and *structure* (lend, l220, l250).

**Blinding and controls.** Samples block-randomised and decoded only at the statistical-analysis stage. **Six systematic control (SC) experiments** ran first, to establish that the setup itself does not manufacture differences; then **12 Verum experiments**. Analysis by ANOVA with four factors: experimental day, batch, process, and the parameter under test.

## Result

**The design behaved as designed — SC experiments were flat.**

- In the control experiments, **no significant main effect** was found for the parameter in question in **any of the seven variables** — not for subspecies, not for host tree, not for blending. The only significant SC effect was experimental day, on four variables (kappa, entropy, lend, l250). Three variables (diagonal_moment, cluster_shade, l220) were stable across all three SC experiments with no main effect even for day or batch.
- The SC runs also showed **no significant batch effect**, which the authors read as evidence the two crystallisation chambers are equivalent.

**The Verum tests graded cleanly:**

| Sensitivity test | Variables passing (p < 0.01) | Best variable | Effect size |
|---|---|---|---|
| 1. Subspecies (*album* vs *austriacum*) | **7 of 7** | l250, no interactions | Cohen's *d* **1.75** (range 1.75 → 0.22) |
| 2. Host tree (apple vs oak) | **4 of 7** (mostly texture) | l220, p < 0.0001 | *d* **0.57** (range 0.56 → 0.26) |
| 3. Blending (hand vs machine) | **2 of 7** (both structure) | lend *d* 0.28 (interacts with day); l250 *d* 0.20, no interactions | *d* **0.20–0.28** |

**288 fingerprints** were used for tests 1 and 3; **192** (subsp. *album* only) for test 2. The authors' own summary of the pattern: the number of variables reaching significance tracked the difficulty of the test, and effect sizes fell as the difference got subtler — which is what an honest instrument looks like.

**Interactions are heavy and the authors say so.** In test 1, five of seven variables interacted with experimental day, and kappa worked only in batch 2204. In test 2, **all four significant variables detected the host-tree difference in only one batch (2204)**. In test 3, lend worked only on apple-grown mistletoe. Their conclusion: "the detection of such effects, while valid for our specific experimental setup, cannot yet be generalised."

**The third test is the interesting one, and it is stated as a question, not a result.** The machine-vs-hand difference is the one thing here that is *not* just re-detecting documented chemistry. The authors lay out three possible readings — a chemical difference in a range the metabolomics study did not scan; a **physical/structural** difference, given the machine's high rotational speed; or a property "not strictly confined either to the chemical or physical level." Then they write: "the hypothesis that CCC could have caught a system-level property, given the current state of the research, **remains speculative**."

## Confidence: medium — for the method's sensitivity; low — for anything beyond chemistry

**It is the best-designed test of this rail in the archive, and it says only what it measured.**

*For:* peer-reviewed in *Scientific Reports*; institutional labs; **pre-designed sensitivity ladder** where the hardest test could have failed and the easy one functioned as an instrument check; **six systematic control experiments** that came back flat, including a chamber-equivalence result; blinded sample allocation; 288 fingerprints; two real production batches with biological meaning; and a written refusal to over-read the third test.

*Against treating it as validation of the tradition's claim:* the study tests **discrimination**, not mechanism. Everything it detects is compatible with ordinary chemistry and physics. The strongest single finding — that CCC separated hand- from machine-blended extract where metabolomics could not — has a mundane candidate in the same paragraph as the exotic one: **high-shear mechanical blending changes physical structure**, and the authors name that possibility themselves. Nothing here tests the claim that the pattern responds to *timing*, *place*, cosmic configuration, or the "formative" forces that the Kolisko/Pfeiffer lineage was built to detect. The authors' own stated limitation is that the analysis was **computer-vision only** — the human trained-panel evaluation that the tradition considers the actual instrument was not used. And the pervasive interaction with batch and day means the detection, while internally valid, "cannot yet be generalised."

## Source

- `https://doi.org/10.1038/s41598-026-41081-6` — Guglielmetti, G., Doesburg, P., Scherr, C., Martin, D., Baumgartner, S. and Tournier, A. L., *Evaluation of copper chloride crystallisation as a method for systems-level characterisation of phytopharmaceuticals — a pilot investigation*, **Scientific Reports 16:7506 (2026)**, published 24 February 2026, open access (CC BY 4.0). DOI and metadata confirmed against Crossref; article read in full.
- Cited within it, not read from this checkout: the metabolomics null on the two blending procedures (ref. 40); the in-vitro efficacy difference between hand- and machine-blended extracts (ref. 41); the CCC handbook and the ~40-paper literature; Andersen et al. for the chamber design (refs. 15, 44).
- The lineage: Lili Kolisko, *Working With the Stars in Earthly Substance* — filed in this Yard's own `synthesis/replication/2026-09-12-dossier-013-kolisko-group-steigbild.md`.

## Related Yard artifacts

- `synthesis/replication/2026-09-12-dossier-013-kolisko-group-steigbild.md` — the community protocol for the *timing* version of the claim (do pictures made the same evening in different homes cluster together?). That is the claim this paper does **not** test, and the dossier remains the honest way to test it.
- `synthesis/validations/2026-09-28-biodynamic-preparations-18yr-field-trial-geisenheim.md` and `synthesis/validations/2026-09-23-biodynamic-preparations-spring-wheat-nitrogen.md` — the anthroposophical method rail. Both are field nulls on the preparations; this record is the method-instrument question rather than the field question.
- `synthesis/validations/2026-09-17-pendulum-chevreul-1854-ideomotor.md` and the radiesthesia rail — the other place where an unblinded human reading instrument met a blinded protocol.

## Honest framing

We hold no brief — the test is the point.
