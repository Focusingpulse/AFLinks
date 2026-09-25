---
name: Water Memory Persistence Test
description: "Give one batch of water two different thermal histories — slow-cooled (equilibrium) and rapidly warmed from 4 C (activated) — and measure the density difference with a pycnometer at a controlled 20.0 C, then follow it for 14 days. Water-domain card; ~$60-150; Homesteading mirror. The water field's first card whose endpoint is a TIME CONSTANT, and its first built on a calculated prediction (Vysotskii & Kornilova, Vestnik MGU, 2004)."
---

# ⚡ Aetherforce — Self-Reliance

**Guild:** Aetherforce — Self-Reliance
**Quest Line:** ⚡ Aetherforce · Homesteading complement
**Tier:** straw
**Domain:** water (the time dimension of water's state — how long a thermal-history memory persists)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-25-water-memory-persistence` · authored_at `2026-09-25` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Self-Reliance",
  desc: "Does water remember how you heated it? One batch, boiled once, split two ways: one part cooled slowly to room temperature (the equilibrium state), the other chilled to 4 C and then warmed rapidly back to 20 C (the activated state). The source - a 2004 Moscow University physics paper - calculates for the first time how long such a state should last: about 10 days at 20 C, and it predicts the activated water should be LESS dense and LESS viscous. Weigh a fixed volume of each in a pycnometer at a controlled 20.0 C and follow the difference for two weeks. The whole test is one thermal history against another, on the same water - and the paper's own signature is that the two directions decay at wildly different speeds, days versus minutes. Build it, run it, and find out whether a kitchen can see it. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Water Memory Persistence Test",
    "Boil one batch of water 10 minutes to drive out dissolved gas, then split it. Arm A: cool slowly, insulated, to 20 C and hold - this is the equilibrium state. Arm B: chill to 4 C for at least 2 hours, then warm the whole volume rapidly to 20 C in a bath and measure at once - this is the activated state. Optionally Arm C: hold water at 50 C, cool it rapidly in an ice bath, and measure within 60 seconds. Weigh a 25 mL pycnometer filled to the mark at 20.0 C on a 0.001 g scale, arms interleaved, 3-5 repeats each, every sample equilibrated in the bath 10 minutes first. Pre-register the arm order, repeats, timepoints and thresholds. Measurable outcome: delta-rho = density(Arm A) minus density(Arm B) at t=0, against the pooled repeat scatter, then the same at 1, 2, 4, 7, 10 and 14 days to fit the relaxation time constant. PASS is delta-rho >= 3x the repeat scatter, same sign in 4 of 5 runs, decaying with a time constant of 5-20 days (the paper predicts about 10 days at 20 C), and - if Arm C is run - the excess vanishing within minutes. Arm A must stay flat across the 14 days or the run is VOID, not a refutation.",
    ["Science", "Chemistry", "Measurement"],
    "💧"
  ],
  source_doc: "sources/2026-09-25-scout-a-langs-2.md (find 7, the scout entry flagging it conceptual-to-buildable) + the primary paper: V.I. Vysotskii & A.A. Kornilova, 'Physical foundations of long-term memory of water', Vestnik Moskovskogo Universiteta, Ser. 3, Fizika. Astronomiya, 2004 - the clathrate-cavity model, the first calculated storage duration (about 10 days at 20 C for the deficit state, about 4 minutes for the excess state), the occupancy-vs-temperature table (18% at 4 C, 38% at 36.6 C, about 50% at 55 C), and the predicted lower density and viscosity of rapidly-heated water",
  source_url: "https://cyberleninka.ru/article/n/fizicheskie-osnovy-dolgovremennoy-pamyati-vody",
  dossier: "living-library/synthesis/replication/2026-09-25-dossier-042-water-memory-persistence.md",
  pass_fail: "PASS: delta-rho at t=0 >= 3x the pooled repeat scatter, same sign in >=4 of 5 independent runs, converging to Arm A with a time constant within about 2x of the paper's 10 days at 20 C (i.e. 5-20 days); and, if Arm C is run, Arm C's excess vanishes within minutes (the predicted asymmetry - days versus minutes cannot be produced by a temperature artifact). FAIL: delta-rho at t=0 within the pooled repeat scatter in >=4 of 5 runs - no measurable thermal-history memory in water at home scale; a complete result, Skeptic's Star. VOID: Arm A drifts as much as Arm B across the 14 days, or the bath cannot hold 20.0 +/- 0.1 C, or the pycnometer repeat scatter exceeds the predicted effect size (about 0.5-0.6% in density) - report the resolution achieved and the control required, NOT a verdict. ARTIFACT: delta-rho tracks the sample temperature difference between arms rather than the thermal history, or disappears when both arms are brought to exactly the same temperature before weighing.",
  evidence: "Photo of the setup (scale, pycnometer, bath, thermometer, the two sealed jars) + the pre-registration sheet (arm order, repeats, timepoints, thresholds, scoring rule) + the empty and filled pycnometer masses for every measurement + the bath temperature logged at every weighing + the daily storage temperature + Arm A's full 14-day series (the control) + Arm B's full 14-day series + the fitted relaxation time constant with its uncertainty + the t=0 difference and its repeat scatter + the five independent runs dated + Arm C's minute-scale series if run + the void check (predicted effect size vs measured resolution) reported whether or not it voids the run"
}
```

---

## Source Documentation

- **Primary:** В.И. Высоцкий, А.А. Корнилова, *«Физические основы долговременной памяти воды»* (Physical foundations of long-term memory of water), **Вестник Московского университета, Серия 3, Физика. Астрономия, 2004** — https://cyberleninka.ru/article/n/fizicheskie-osnovy-dolgovremennoy-pamyati-vody — **fetched and read in full this run.** Held in the Vault as `sources/2026-09-25-scout-a-langs-2.md` find 7 (the scout entry). The paper carries the whole claim: the Pauling clathrate model (dodecahedral framework, ~2.6 Å cavities, ~2.5 Å windows narrower than a water molecule), the occupancy-vs-temperature table, the two relaxation times with their full temperature tables, and the predicted property changes.
- **The headline number:** *«Впервые вычислена длительность хранения информации»* — **"for the first time, the storage duration of the information is calculated."** τ1w ≈ **10 days at 20 °C** (deficit state, from rapid heating); τ2w ≈ **4 minutes at 20 °C** (excess state, from rapid cooling).
- **The predicted property change:** rapidly-heated water → *«избыток как аморфной воды, так и количества незаполненных микропустот»* → **lower bulk density** and **lower viscosity**. Rapidly-cooled water → higher density and viscosity.
- **The authors' own limits, quoted in the card's framing:** the key energies are *«определены нами исходя из модельных расчетов»* (from model calculations) and the times *«могут существенно изменяться»* (may change substantially); the work concerns *«чистой воды»* (pure water) and excludes dissolved impurities; the medical aspect is *«изучен крайне слабо»* (extremely weakly studied).
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-25-dossier-042-water-memory-persistence.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "water memory", "clathrate", "structured water"
- **Aetherforce Reference:** Search "water memory", "structured water", or "clathrate" on https://www.aetherforce.energy
- **Related dossiers:** 028 (Water Memory Imprint — the imprinting claim; this is the persistence claim), 009 (EZ Water Exclusion Zone — structure, not time), 025 (Piccardi Cosmic Precipitation — a water property against an external variable), 037 (Contour Swale Rain-Retention — water's quantity and path)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (a pycnometer, a 0.001 g scale, a temperature-controlled bath) with a named procedure (one boiled batch, two thermal histories, arms interleaved, 14 daily weighings) and a measurable outcome (Δρ in g/mL at t = 0, and the relaxation time constant fitted across 14 days). Not pure theory. |
| **Replicable** | YES — Home, straw: ~$60–150 for a 1 mg scale, a pycnometer, a 0.1 °C thermometer, a thermostatted bath and sealed jars. No mains work, no chemicals, no purchased preparation. The one demanding requirement is temperature control to ±0.1 °C, which is why density (not viscosity) is the primary endpoint. |
| **Relevant** | YES — Water domain, and it fills a real gap: every other water card tests water's *structure*, *vitality*, or *quantity/path*; **none tests water's time dimension**, and none has a time constant as its endpoint. Fills the **Homesteading** mirror (self-reliance / off-grid — water independence), 2nd card. |
| **Honest** | YES — and this is the card's spine: the source is a **model calculation, not a measurement**; its parameters are the authors' own estimates and they say the times may change substantially; it is about pure water and excludes dissolved impurities; its medical aspect is the authors' own admitted weak point and **the card makes no health claim**. The claim is framed as a claim; the card is a test, not an endorsement. Clean FAIL and VOID paths. |
| **Linked** | YES — A scout source doc and the primary paper (read in full this run), a pre-registered replication dossier, and cross-links to four related cards. |

**Mirror choice, stated:** the card's **domain is water**, and among the mirrors still carrying only one card, **Homesteading** (self-reliance / off-grid — *water independence*) is the honest fit: a homestead stores water — cisterns, rain catchment, hot-water tanks — and this card asks whether *how you heat and store it* changes a measurable property of that water and for how long. **Plumbing & Hot Water** ("water storage energetics") is the closest thematic alternative and was not chosen because it already carries four cards (001, 009, 025, 031) and the mirror map's own instruction is to fill the emptiest. **Oddball** (suppressed-science re-try candidates) was the second alternative; it was not chosen because this claim is a minority *mainstream* model published in a university physics journal, not a suppressed lineage.

---

## The honest framing (the spine of the card)

**The claim is a claim — and its source is unusually candid about being a model.** Most water-memory writing asserts an effect and stops. This paper does the opposite: it builds a clathrate model, computes how long a non-equilibrium state should last, and states plainly that its own parameters are estimates that *may change substantially* if refined. That candour is exactly what makes it testable — a number can be checked, an assertion cannot.

**What the card tests.** Not "water memory" in general — that field is contested (Benveniste, Montagnier, Emoto) and this card claims nothing about it. The card tests **one quantified prediction**: that a rapid thermal transition leaves water in a state that changes its density, and that the state decays with a stated time constant and a stated temperature dependence.

**The design that makes it a measurement.** Four things do the work:

1. **All arms come from one boiled batch.** Boiling drives out dissolved gas, and degassing itself changes density. So every arm is boiled identically and the only variable is the *thermal history after boiling* — which is precisely the paper's own definition of "ordinary water" (long boiling and slow cooling).
2. **The comparison is thermal-history versus thermal-history, not "special water" versus tap water.** Same source, same boil, same measurement. Only the post-boil path differs.
3. **Density is primary because it is ~100× less temperature-sensitive than viscosity.** Water's density near 20 °C moves ~0.02 %/°C; its viscosity moves ~2.5 %/°C. A 0.5 °C arm-to-arm error would swamp a viscosity reading but barely touch a density reading. The card picks the endpoint that survives its own worst confound.
4. **Arm A's flatness is the assay's validity check.** If the control drifts as much as the activated arm, the rig has not measured anything — and the card calls that VOID, not a refutation.

**The asymmetry is the discriminating prediction.** The paper says the deficit state lives ~10 days at 20 °C and the excess state ~4 minutes. A temperature artifact, a dissolved-gas difference, or a container effect cannot produce a 3,600× asymmetry between two arms of the same water. A family that watches B persist and C vanish has watched the model's signature — and a family that sees both behave identically has watched it fail.

**The central limitation, stated up front: the source is a calculation, and a home pycnometer is not a laboratory.** The predicted density change is roughly 0.5–0.6 %, which a 1 mg scale on a 25 mL sample can resolve — but a home pycnometer cannot separate a 0.5 % bulk-density change from a 0.5 % volume or fill error. That is why the **VOID** condition is a first-class outcome and why the card requires the achieved resolution to be reported either way. A rig that cannot see the effect has not tested it.

**Safety:** boiling water and glassware — use heat-safe containers, vent lids during the boil, and handle the bath with care. Nothing here is hazardous; the only real risk is a scald.

---

## Relationship to the rest of the queue

This is the **first water card whose endpoint is a time constant**, and the first water card built on a *calculated* prediction rather than a device claim. 001, 004, 009, 019 and 031 test whether a device does something; 025 and 028 test whether water responds to an external influence; 037 tests where water goes. **None asks how long a state of water lasts** — and that is the question this paper answers with a number.

Its nearest neighbours are **028** (Water Memory Imprint) and **025** (Piccardi Cosmic Precipitation). 028 asks whether a field writes information into water; this asks how long any such state survives. 025 tests a water property against an external variable (cosmic); this tests it against an internal one (thermal history). Together the three make the water field's memory axis legible for the first time.
