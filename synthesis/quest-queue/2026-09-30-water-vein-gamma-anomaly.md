---
name: Quest Card — Water-Vein Gamma Anomaly Test
description: "Aetherforce-branded quest card for the queue's first ionising-radiation card: a Hungarian practitioner manual cites a French team who put a Geiger-Müller counter over the 'stimulus bands' of water-vein and fault-line earth radiations and found the gamma strengthened. Nobody has re-run it in a house. This card runs it — dowsed lines vs a known physical water feature vs control points, blind, with a mandatory instrument check on a known source. The physics points the other way (water shields gamma), so a null is the expected result. Earthworks mirror (Earth energy / geobiology), shelter domain."
---

# ⚡ Aetherforce — Earthworks

**Guild:** Aetherforce — Earthworks
**Quest Line:** ⚡ Aetherforce · Earthworks complement
**Tier:** sand
**Domain:** shelter (dwelling geobiology — does a water-vein band under a dwelling read differently on a gamma counter?)
**Status:** proposed
**Created:** 2026-09-30

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-30-water-vein-gamma-anomaly` · authored_at `2026-09-30` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Earthworks",
  desc: "The geopathic-survey tradition says a water vein under your home does more than feel odd — it changes what an instrument reads. A Hungarian practitioner manual carries the claim from a French team: they put a Geiger-Müller counter over the 'stimulus bands' of water-vein and fault-line earth radiations and found the gamma radiation strengthened. It has never been re-run in a house. So run it. Get a Geiger counter, prove it responds over a bag of salt, then measure gamma over three dowsed water-vein lines, over a water feature you can actually point at — a buried pipe, a stream, a pond edge — and over three control spots on the same ground, blind. Here is the twist the source does not mention: water shields gamma, so the physics predicts a LOWER reading over a wet vein, not a higher one. A null is the expected result — and a complete one. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Water-Vein Gamma Anomaly Test",
    "Get a Geiger-Müller counter (or a gamma dosimeter) and write down its model and its stated sensitivity. Prove it works first: take 10 one-minute readings 1 m above the ground indoors for your background (record the mean and the standard deviation), then 5 one-minute readings over a bag of potassium chloride (water-softener salt or a salt substitute) or a granite offcut — if the source reading does not rise clearly above background (target: at least 2× the background SD), the counter is not sensitive enough and the run is void, not a null. Then mark three arms on the same ground: A, three dowsed water-vein lines (three points on each, 1 m apart); B, a water feature you can actually point at (a buried water pipe, a stream, or a pond edge); C, three control points with no water feature. Have someone else code the points so you measure blind, randomise the order, and measure every point at a fixed height (5 cm) for a fixed time (3 min), logging the time, temperature, humidity and whether it rained in the last 48 hours. Repeat the whole set on 3 separate days, at the same time of day. Measurable outcome: background-subtracted counts per minute for each arm, and whether A or B exceeds C repeatably by at least 2× the background SD in >= 2 of 3 sessions. PASS: A or B beats C repeatably — surprising, and it needs a radon test and a second site before any conclusion. FAIL: A, B and C are indistinguishable — a null, the expected result, and a complete one (Skeptic's Star).",
    ["Science", "Measurement", "Earth"],
    "☢️"
  ],
  source_doc: "translations/2026-09-30-radiesztezia-meres-foldugarzas-brunda-hu.md (Brunda Károly & Jávorszky György, 'Radiesztézia — a radiesztéziai mérés fogalma, módszere és a földsugárzások elleni védekezés', hu->EN 8/8 chunks; the cited claim is in the 'Direction of radiesthesia's scientific research' section)",
  source_url: "https://www.radiesztezia.net/radiesztezia.html",
  dossier: "living-library/synthesis/replication/2026-09-30-dossier-057-water-vein-gamma-anomaly.md",
  pass_fail: "PASS: arm A (dowsed lines) or arm B (known water feature) shows a repeatable background-subtracted elevation above arm C (control) of >= 2x the background SD, in >= 2 of 3 sessions, with the instrument check (arm D - a known gamma source) confirming the counter responds - the cited claim survives, and it needs a radon measurement and a second site before any conclusion. FAIL: arms A, B and C are within the scatter of each other once background is subtracted - a null, the expected result, and a complete result (Skeptic's Star). INCONCLUSIVE: the instrument check did not rise above background; fewer than 3 sessions; the arms were not measured in the same session; the counter height or integration time changed between points; or the dowsed lines were re-marked between sessions. ARTIFACT: the reading tracks the counter's own warm-up; the reading follows the time of day or recent rain rather than the arm; the reading follows the counter's position rather than the marked line; or a 'control' point sits over an unmarked pipe or drain.",
  evidence: "Photo of the counter with its model and stated sensitivity + the pre-registration sheet (arms, points, height, integration time, sessions, criteria) photographed before the first reading + the background log (10 readings -> mean and SD) + the instrument-check log over the known source + the marked arms photographed with a tape measure showing the height and spacing + the randomised measurement order + the raw cpm per point per session with the time, temperature, humidity and recent-rain column + the background-subtracted results table with the arm A-vs-C and B-vs-C ratios + the optional indoor baseline against the source's stated threshold + the void/artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the archive find):** `living-library/translations/2026-09-30-radiesztezia-meres-foldugarzas-brunda-hu.md` — Brunda Károly & Jávorszky György, *Radiesztézia — a radiesztéziai mérés fogalma, módszere és a földsugárzások elleni védekezés* (hu→EN, 8/8 chunks), source https://www.radiesztezia.net/radiesztezia.html. Copyright © Brunda Károly 2003–2021, Bio BPM Kft. Translated and archived 2026-09-30 (commit `0e1af89a`).
- **Scout record:** `living-library/sources/2026-09-30-scout-b-langs-1.md` § Hungarian, find 1 — *"Brunda Károly — Hungarian radiesthesia / geopathic-stress measurement system"*, `practical_applicability: flag — buildable, reproducible`. The scout records the ordered protocol (I. ionising radiation by instrument → II. electrosmog LF/HF by instrument → III. radiesthetic mapping of earth radiations → IV. neutral-zone designation) and the source's stated dwelling threshold: **background should not exceed 0.21 µSv/h, ideal 0.07–0.14 µSv/h.**
- **The claim, in the source's own words** (the section *"The direction of radiesthesia's scientific research"*):
  > *"The Swiss researcher Dr. Joseph A. Kopp states that in the stimulus bands of water veins, anomalies measurable with a magnetometer can be experienced, but changes in the conductivity of the soil and the air can also be demonstrated. He further experienced that the frequencies of the UHF band and the intensity of electromagnetic waves in the infrared range rise in earth radiation (especially above water veins). **French researchers used an oscilloscope and a Geiger-Müller counter to experimentally confirm that in the stimulus bands of certain water-vein and fault-line earth radiations the radioactive gamma radiation is also strengthened.**"*
- **The source's own candid limit** (carried into the card, not smoothed over):
  > *"**There is no instrumental earth-radiation measurement.** The measurement of earth radiations is possible exclusively by radiesthetic methods…"*
  > *"Despite all these attempts, however, the nature of the water-vein, hartmann, curry, ley, Szent György net … etc. earth radiations, and of the vortices (and the rest), **has just as undefinable as it was.** There is no correspondence with the concepts occupied by physics, such as electricity and magnetism."*
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-30-dossier-057-water-vein-gamma-anomaly.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "water vein", "geopathic", "radiesthesia", "dowsing", "Geiger"
- **Aetherforce Reference:** search "geopathic" / "water vein" / "earth radiation" on https://www.aetherforce.energy
- **Related cards:** 005 (Blind Geopathic Mapping — locating zones by dowsing; this card asks whether an *instrument* agrees), 021 (Earth-Energy Grid Instrument Scan — a **magnetometer** scan of the Hartmann grid; this card uses a **gamma counter** on water veins), 044 (Plan-Reading Location — locating zones from a plan), 048 (Pendulum Water-Quality Discrimination — dowsing scored against a chemical ground truth; this is dowsing scored against a *physical* ground truth)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — a named apparatus (a Geiger–Müller counter, a known source for the instrument check, marked arms) with a measurable outcome (**background-subtracted cpm per arm, and whether the dowsed or known-water arm exceeds the control arm repeatably by ≥ 2× the background SD**). Not pure theory. |
| **Replicable** | YES — Home, sand: **~$60–150** for a Geiger–Müller counter or gamma dosimeter, ~$5 for a bag of potassium chloride (or a free granite offcut), plus markers and a notebook. No chemicals, no heat, no mains wiring touched. The demanding requirement is **discipline** (the instrument check, the blinding, the same-session/same-time-of-day repeat). |
| **Relevant** | YES — Shelter domain, squarely: the ground under a dwelling and what an instrument reads over a claimed geopathic band. It is also the queue's **first card on ionising radiation** — every prior geobiology card measures magnetism or a dowsing response. |
| **Honest** | YES — the claim is framed as a claim and the card is a test, not an endorsement. Four things are stated in advance: the claim is **second-hand** (a French team, cited by a Hungarian manual); the source that carries it **says the thing it is about cannot be measured instrumentally**; **water shields gamma**, so the naive physics predicts the *opposite* direction and a null is the expected result; and a null is a **complete** result (Skeptic's Star). The one mechanism that could produce the claimed rise — **radon** — is named in advance. |
| **Linked** | YES — a scout find, the primary translated source, a pre-registered replication dossier, the source's checkable threshold, and cross-links to four related cards. |

**Mirror choice, stated:** the claim's object is a **water-vein / fault-line band in the ground** — an earth-energy phenomenon — so **Earthworks** ("Earth energy / geobiology") is the honest complement, and the family label is `Aetherforce — Earthworks`. This is the mirror's **third** card, and the pairing is deliberate: **021 asks whether a magnetometer can find the Hartmann grid; 057 asks whether a gamma counter can find a water vein.** **Nest** ("Home harmony / geobiology / EMF structure") was the closest alternative and was not chosen because the object here is the *ground's* bands, not a dwelling's internal zones, and because Nest already carries the two dowsing-location cards (005, 044). The emptier mirrors (Animal Care, Community Living, Foraging, Round Wood, Oddball, Woodland Care, Commerce, Tool Care, Dim Lumber Woodworking, Metalworking — one card each) were checked and none carries a source that fits an ionising-radiation claim on the ground; forcing this card into one of them would mislabel it.

---

## The honest framing (the spine of the card)

**The claim is second-hand, and the source that carries it says the thing it is about cannot be measured.** The Hungarian manual's own position is explicit — *"there is no instrumental earth-radiation measurement"* — and yet, three paragraphs later, it cites a French team that used a Geiger–Müller counter to measure a correlate of exactly those radiations. The source is candid that the nature of the earth radiations *"has remained just as undefinable as it was."* **The card's posture is the source's posture: test the cited claim, do not endorse it, and do not pretend the source claims more than it does.** The card is the first home execution of a 20th-century measurement the archive has held untested.

**Water shields gamma — which is why the test is worth running.** A wet vein is extra shielding between the soil's natural potassium/uranium/thorium and the counter, so the naive physical prediction is a **lower** reading over a wet vein, not a higher one. The claim asserts the opposite direction. **A null is therefore the expected result, and the card says so before the run** — so a null cannot later be re-read as a surprise, and a rise cannot be read as confirmation without a mechanism. The one mechanism that could produce the claimed rise is **radon**: groundwater can carry radon, and radon daughters deposit on the ground surface, adding a local gamma signal. The card names that in advance and makes a radon test the natural follow-up.

**A dowsed line is a claim, not a fact — so the card separates "water" from "dowsing".** If the family measured only over a dowsed line and found nothing, they would not know whether the vein was mis-located or the effect absent. **Arm B (a known physical water feature)** is the discriminator: if gamma rises over a buried pipe or a stream but not over the dowsed lines, the effect (if any) tracks physical water, not the radiesthetic method; if it rises over the dowsed lines but not over the known water, the opposite. **Neither arm alone can answer the question** — this is the card's design contribution, and it is the same error class the fleet keeps finding: *the instrument answers the question it was built around, and that was a different question.*

**A Geiger counter that has not been shown to respond is not a measurement.** A cheap counter may be insensitive, may be reading its own background, or may have a long warm-up. **The instrument check (arm D — a known source) is mandatory:** if the counter does not rise over a bag of potassium chloride or a granite offcut, the run is **void, not a null** — a distinction the card makes explicitly, because "no difference" and "the instrument could not have seen a difference" are different results and get filed identically if the check is skipped.

**Under-promise:** the most likely outcome is that the dowsed lines, the known water feature and the control points are indistinguishable once background is subtracted. That is a complete result — it files the first home test of a cited claim, and it tells a family that the gamma half of the geopathic-survey tradition does not reproduce at home. A repeatable elevation would be genuinely surprising and would need a radon measurement and a second site before any conclusion.
