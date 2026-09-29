---
name: Dossier 052 — Shared Well Iron & Manganese Vortex Test
description: "Replication dossier for the IET Malmö ion-precipitation claim: a vortex agitator followed by a gravel filter precipitates iron and manganese from well water 'which traditional treatment (with compressed air) did not accomplish.' The card tests whether the vortex does the work or whether it is simply the aeration the vortex provides — a matched-dissolved-oxygen compressed-air arm is the whole experiment. Community/shared-infra card; home/homelab, ~$150–300."
---

# Dossier 052 — The Shared Well Iron & Manganese Vortex Test

**Status:** protocol
**Domain:** community (shared-infra knowledge — treating a shared water source)
**Tier:** straw (home/homelab, ~$150–300)
**Created:** 2026-09-29
**Source docs:**
- `living-library/translations/2026-09-27-self-organizing-flow-technology-iet-sv.md` — the **full English translation** of *Självorganiserande strömningsteknik – i Viktor Schaubergers fotspår* (Johansson, Ovesen & Hallberg, Institute for Ecological Technology, Malmö 2002; first edition 1997; ISBN 91-975722-0-9). **Chapter 4.3 (Ion precipitation)** carries the claim and its numbers; **Chapter 4.2** carries the control that makes the card possible. Source PDF: https://www.iet-community.org/publications/reports/IET%20Forskningsrapporter%20Nr%201.pdf — archive copy `archives/2026-09-27-iet-forskningsrapporter-nr1-sjalvorganiserande-stromningsteknik.pdf`.
- `living-library/sources/2026-09-28-scout-b-langs-2.md` — **find 7** (IET Malmö Schauberger replication program, `buildable, reproducible`) and **find 8** (IET Report 2, the alternative-water-treatment monograph).

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-29-dossier-052-shared-well-metal-removal` · authored_at `2026-09-29` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The claim (as asserted by the source)

The Institute for Ecological Technology (IET, Malmö) reports that a **vortex agitator** — a hyperbolic vessel with an impeller inside — **precipitates iron and manganese ions out of well water, and does so when traditional treatment does not.** The source's own words:

> "In experiments at the Pålträsk waterworks in 1990, Aquagyro found that their agitator appeared to facilitate the precipitation of iron and manganese ions. A hyperbolic vessel of ca. 1 m height, with an Aquagyro agitator inside, had been placed in a 3 m³ tank. During the treatment, iron precipitates could be observed in the tank. **In a subsequent filtering in a gravel filter the manganese ions were to a large extent precipitated, which traditional treatment (with compressed air) did not accomplish.** The iron content in the treated water was found on analysis to be the same as in the raw water, but **the iron did not precipitate on compressed-air aeration of the sample, which was considered remarkable.**"

The source's own numbers (Table 4.2, Pålträsk waterworks, water temperature 7 °C):

| State | Mn (mg/l) | Fe (mg/l) | Note |
|---|---|---|---|
| Before treatment | 0.26 | 0.23 | — |
| During treatment | 0.29 | 0.24 | — |
| After gravel precipitation | **<0.05** | 0.21 | The iron does not precipitate on compressed-air aeration in the lab. |

Supporting trials the source cites: **Nordmaling 1987** (a reduction of Mn and NO₂ ions was found); **Vistbäcken waterworks** (extremely iron-rich water — "an effective precipitation of iron, more effective than traditional compressed-air aeration, in contrast to the experiments at Pålträsk, and also a reduction of the manganese content").

**What is being tested, in one sentence:** does a vortex agitator remove iron and manganese from a shared well's water **more than a compressed-air aerator does at the same dissolved-oxygen level** — or is the vortex's apparent effect simply the aeration the vortex provides?

## Honest status of the claim

**The archive holds the claim and no home test of it.** A grep for `Pålträsk`, `Aquagyro`, `ion precipitation` and `manganese` across `living-library/synthesis/` returns only this dossier and the card it belongs to — the queue has no card on **dissolved-metal removal** at all. Its water cards test vortex *temperature and taste* (001), *aeration* (004), *exclusion-zone structure* (009), *cosmic precipitation* (025), *water memory* (028, 042), *dowsed quality* (048) and *flow energy* (031). **None tests whether a device removes a dissolved contaminant from drinking water** — the one endpoint that a household can take to a lab and settle.

Four things the card must say out loud, because they are what a family is actually testing:

1. **The source's own control is the tell, and the card must reproduce it.** The claim is *relative*: the vortex did what **compressed-air aeration did not**. That is a claim about a difference between two treatments, not about a device working. A card that only compares "vortexed vs untreated" cannot answer it — it would pass on aeration alone.
2. **The vortex aerates, and the source says so in the same report.** Chapter 4.2 of the same document shows the vortex raising dissolved oxygen to ~90 % of saturation in 15–30 minutes, and states plainly that *"it is only the small air bubbles that play an important role for the oxygenation."* Iron and manganese removal from well water is classically **oxidation followed by filtration**: Fe²⁺ → Fe³⁺ (which precipitates), Mn²⁺ → MnO₂ (slower). **So the default expectation is that a vortex removes metals because it aerates, and the card must hold dissolved oxygen matched between arms or it proves nothing.**
3. **The gravel filter is a second candidate cause.** The source's manganese drop appears at the **gravel precipitation** step, not during treatment. A filter removes precipitated metal; the question is whether the vortex makes the metal *filterable* when aeration does not. The card therefore measures **before treatment, after treatment (pre-filter), and after filter** — three points, not two.
4. **The source itself flags its iron result as unexplained, and asks for exactly this replication.** *"The iron did not precipitate on compressed-air aeration of the sample, which was considered remarkable"* — and the source offers two competing explanations (organic binding; a complex bond) without choosing. It closes the section: *"It would be interesting to repeat these trials more systematically, with, e.g., the Plan Pump in the trough, and with water with different ion contents."* **The card is that replication, at household scale.**

**Under-promise, stated plainly:** the likely outcome is that **both** treated arms remove metals and the vortex arm is not clearly better than the aeration arm at matched dissolved oxygen — i.e. the honest verdict is *"the vortex aerates, and aeration is what removes the metal."* That is a complete, useful result (it tells a family to buy an air pump, not a vortex). A vortex-specific effect would be genuinely surprising and would justify a second round.

## Why it matters

- It is the queue's **first card on dissolved-metal removal** — iron and manganese are the two most common reasons a household well's water stains fixtures, tastes metallic and is refused by a buyer. It is the first water card whose endpoint is a **contaminant concentration**, not a temperature, a taste, a structure or a memory.
- It is the **first card that tests a water device against the ordinary treatment it claims to beat.** Every prior device card compares treated water to untreated water; this one compares it to **the standard method at matched conditions** — the design that separates a device's real contribution from the physics it happens to share.
- It is genuinely **shared-infrastructure**: a well serves several households, and the decision to install treatment is a shared one. The card is the pooled test a group can run before spending shared money.
- It teaches the transferable lesson: **when a device's plausible mechanism is something the device also does incidentally, match the incidental variable or the experiment is void.** Here the incidental variable is dissolved oxygen.

## Replicability: `home` / `homelab`

- Build/obtain cost: **~$150–300** — an iron test kit and a manganese test kit (~$15–40 each), a dissolved-oxygen test (a titration kit ~$40–80, or a meter ~$80–150), a small air pump + airstone (~$20–40), a small water pump or drill-mounted impeller (~$20–60), a conical/hyperbolic vessel and a bucket (~$0–40), and gravel for a filter (~$10).
- Safety: **no hazard.** All voltages are low-voltage aquarium/pond pumps. Do not drink the treated test water; it is a bench sample. Dispose of test reagents per their label.
- Accessibility: one afternoon to build, one day of trials. The measurement is the slow part — a manganese kit is a colour-match or a lab send-out.

## Apparatus (Bill of Materials)

- **One source of shared well water** — a single 20–40 L batch drawn at one time from the well the group actually uses. Record the well, the date, the depth and the draw method. **Split this one batch across all three arms** so every arm starts identical.
- **Three matched vessels** — same size, same material. Arms: **A (untreated)**, **B (compressed-air aeration)**, **C (vortex)**.
- **An air pump + airstone** — arm B's treatment. This is the standard method the claim is measured against.
- **A vortex rig** — arm C's treatment. A conical or hyperbolic vessel with a small impeller or a pump arranged to drive a swirling flow (the source's own home-scale version was an egg-shaped vessel with a small agitator; its trough was 50 cm diameter × 80 cm high with a 70 W motor). Record the vessel shape, the impeller and the drive.
- **A gravel filter** — the same filter, same gravel, same flow rate, applied to every arm after treatment.
- **Test kits** — iron, manganese, and dissolved oxygen; plus pH and a thermometer.
- **A log sheet** — pre-registered columns: arm, time, temperature, pH, DO, Fe, Mn — at each of the three sampling points.

## Protocol (three-arm, matched-oxygen metal-removal test, pre-registered)

**Phase 1 — build and pre-register.**
1. Draw **one** batch of the shared well water and split it into the three matched vessels, equal volume. Photograph them side by side.
2. Sample every arm **before treatment** for Fe, Mn, DO, pH and temperature. **If baseline iron and manganese are below the test kits' detection limits, stop — there is nothing to remove and the run is inconclusive, not a pass.**
3. Write the **pre-registration sheet** before treating: the treatment time for each arm, the target dissolved-oxygen level for the matched comparison, the rest period, the filter procedure, the sampling points, the endpoints and the thresholds. Photograph it.

**Phase 2 — treat, matched.**
4. **Arm A:** no treatment — rest for the same period as the others.
5. **Arm B:** aerate with the air pump until dissolved oxygen reaches the pre-registered target (aim for the level arm C reaches; if C overshoots, aerate B longer to match — **the two treated arms must finish at the same DO within ±1 mg/l, or the run is void**).
6. **Arm C:** run the vortex for the pre-registered time; measure DO as it rises. Record the time to reach the target.
7. Sample every arm **after treatment, before filtering** for Fe, Mn, DO, pH, temperature. This is the point that separates *precipitation* from *filtration*.
8. Rest every arm for the same pre-registered period (the source used a rest before filtering), then pass every arm through the **same gravel filter** at the same flow.
9. Sample every arm **after filtering** for Fe and Mn.

**Phase 3 — score.**
10. Compute, per arm, the **removal fraction** for iron and for manganese at each sampling point: (baseline − final) / baseline.
11. Score the pre-registered endpoints: **C vs B at matched DO** (the vortex-specific claim), **B vs A** (does aeration alone remove metal), and **C vs A**.

## Pass / fail (pre-registered)

- **PASS (vortex-specific):** the vortex arm removes **≥ 2× the manganese** of the aeration arm **at matched dissolved oxygen (±1 mg/l)**, and the manganese drop appears **after filtering** (i.e. the vortex made it filterable), repeated in a second draw. Iron reported separately — the source's own iron result is contested and is not the primary endpoint.
- **PASS (the effect is aeration, not the vortex — a real, different result):** both treated arms remove metal, **C ≈ B at matched DO**, and **B > A** — the vortex's contribution is the oxygen it dissolves. Recorded as a positive mechanistic finding: *an air pump is the cheaper way to get this result.*
- **FAIL:** no arm removes metal above the untreated control — the claim does not reproduce at home scale. **A complete result** (Skeptic's Star).
- **INCONCLUSIVE:** baseline iron and manganese below the kits' detection limits (nothing to remove); the two treated arms finished at dissolved-oxygen levels more than 1 mg/l apart; the filter differed between arms; the rest period differed; the source water changed between draws; fewer than two independent draws were run.
- **ARTIFACT:** the result tracks **temperature** or **rest time** rather than treatment; the arms differed at baseline; the operator knew which arm was which and the reading is a colour-match; the result disappears when the arms are re-randomised in position and order.

## Evidence

Photo of the three arms side by side before treatment + the **pre-registration sheet** (treatment times, DO target, rest period, filter procedure, sampling points, endpoints, thresholds) + the well and draw recorded + the baseline Fe/Mn/DO/pH/temperature table for all three arms + the post-treatment pre-filter table + the post-filter table + the dissolved-oxygen trace for the two treated arms showing they finished matched + the removal-fraction table with the C-vs-B ratio at matched DO shown + the second draw's repeat + the void/artifact checks reported whether or not they void the run.

## Confounds (named in advance)

- **Aeration — the central confound.** The vortex oxygenates; aeration is the classic metal-removal mechanism. **The matched-DO aeration arm is the only thing that separates them; without it the card cannot answer its own question.**
- **The filter does work of its own.** A gravel filter removes precipitated metal regardless of what precipitated it. The three sampling points (before / after treatment / after filter) are what separate the two.
- **Iron and manganese behave differently.** Manganese oxidises slowly and needs a higher redox potential; iron oxidises fast. A result on one is not a result on the other — report them separately, always.
- **The source's own iron result is contested and unexplained.** It offers two competing explanations (organic binding; a complex bond) and does not choose. Do not let the manganese result lend confidence to the iron one.
- **Water chemistry varies by source.** The source's trials were on specific Swedish well waters; humus content, pH and hardness all change the outcome. Record the source water's own parameters.
- **Colour-match kits are operator-read.** Where a kit is a colour match rather than a titration, have a second person read it, and keep the arm labels keyed by someone other than the reader.
- **One batch is a sample of one.** Draw twice on different days before concluding anything.

## Verdict rules

C ≥ 2× B on manganese at matched DO, drop appearing after filtering, repeated → **vortex-specific effect** (supports the claim). C ≈ B at matched DO with B > A → **the effect is aeration, not the vortex** (a positive mechanistic result; the air pump is the cheaper tool). A ≈ B ≈ C → **refutes the coarse home-scale claim**. Baseline below detection, DO unmatched, or a single draw → **inconclusive, not a refutation**.
