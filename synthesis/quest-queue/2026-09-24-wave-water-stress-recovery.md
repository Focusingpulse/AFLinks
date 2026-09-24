---
name: Quest Card — Wave-Water Stress-Recovery Test
description: Aetherforce-branded quest card testing the wave-water claim — that water carrying a transferred "vibrational-wave" imprint speeds recovery from mental stress, measured as the EEG alpha/beta ratio after a 15-minute arithmetic stressor. Blinded three-arm crossover (imprinted / plain / nothing), with the discriminating prediction set against PLAIN water, not against nothing. Natural Medicine complement, health domain. Homelab tier, adult-only.
---

# ⚡ Aetherforce — Natural Medicine

**Guild:** Aetherforce — Natural Medicine
**Quest Line:** ⚡ Aetherforce · Natural Medicine complement
**Tier:** wood
**Domain:** health (human physiology — stress recovery; drinking water as the intervention)
**Status:** proposed
**Created:** 2026-09-24

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-24-wave-water-stress-recovery` · authored_at `2026-09-24` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Natural Medicine",
  desc: "A Japanese university team asked a sharp question: does water that has had a 'vibrational-wave' imprint transferred into it speed your recovery from mental stress? They put seven students through a 15-minute arithmetic stressor and measured the brain's alpha/beta ratio before and after. Three arms: no drink, plain water, imprinted water. The imprinted-water group recovered further than the no-drink group — and then the number that matters: PLAIN WATER landed almost as far, and was statistically indistinguishable from both. So the published result never separated the imprint from the water. This quest runs the control the study's own numbers imply and the paper never ran: imprinted water versus plain water, handled identically, blinded, on your own bench. If the imprint does something, imprinted water beats plain water. If it doesn't, you have retired the claim at home scale — which is worth just as much. Adult-only self-experiment; no treatment claim of any kind. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "wood",
  quest: [
    "Wave-Water Stress-Recovery Test",
    "You need a consumer EEG headset that reports alpha (8-13 Hz) and beta (13-30 Hz) band power (~$100-400 — this is the queue's first card that needs a purchased instrument), a printed sheet of one-digit addition problems, a timer, a coil of magnet wire around a 2 L glass jar driven at 7.8 Hz from a BATTERY-powered source (never mains), two identical opaque bottles, and a third person as coder. PRE-REGISTER at least 6 sessions per arm (18 total, one per day) before you start. Each session: 5 min seated rest, 60 s eyes-closed EEG, 15 min of timed one-digit addition, then 2 min drinking 150 mL within the 2 minutes (or sitting quietly for the no-drink arm), then 60 s eyes-closed EEG; analyse the 10-40 s window exactly as the source did. Three arms, randomized from a schedule drawn before session one, blinded so neither subject nor analyst knows the code: IMPRINTED (coil energized 30 min at 7.8 Hz), PLAIN (same jar, same 30-min wait, coil NOT energized), NOTHING (empty coded bottle). First check the assay itself: the alpha/beta ratio must FALL across the stressor in the no-drink arm — if it doesn't, the run is void, not a refutation. Measurable outcome: per-session RECOVERY RATIO = post-stress alpha/beta divided by baseline alpha/beta; compare the imprinted arm against the PLAIN arm within each subject (Wilcoxon signed-rank, pre-registered N, alpha 0.05), with the direction repeating in a second block. Target: imprinted > plain water significantly AND the no-drink arm shows the expected stress drop AND the direction repeats — or imprinted about equal to plain water, which retires the claim honestly and earns the Skeptic's Star. The coil substitutes the archive's own reproducible imprinting method for the source's proprietary device: this tests the class, not the device.",
    ["Science", "Measurement", "Health"],
    "🧠"
  ],
  source_doc: "sources/2026-09-16-scout-a-de-fr-ja.md (find #10) — primary: 江川陽介 (Egawa Yōsuke), 「振動波エネルギーを転写した水（波動水）は精神的ストレス負荷からの回復に影響をあたえるか」, Kokushikan University graduate-school research bulletin, JSPS Kakenhi 16K01669, https://www.kokushikan.ac.jp/gs/department/hs/docs/01_102.pdf",
  source_url: "https://www.aetherforce.energy",
  dossier: "living-library/synthesis/replication/2026-09-24-dossier-039-wave-water-stress-recovery.md",
  pass_fail: "PASS: imprinted-arm mean recovery ratio significantly greater than the PLAIN-water arm (within-subject Wilcoxon signed-rank, pre-registered N, alpha 0.05) AND the no-drink arm shows the expected stress-induced alpha/beta drop (assay valid) AND the direction repeats in a second block of sessions | FAIL: imprinted about equal to plain water (the effect, if any, is the water, not the imprint) — honest negative, Skeptic's Star | INCONCLUSIVE: no alpha/beta drop in the no-drink arm (assay invalid — the run is void, not a refutation), fewer than the pre-registered sessions completed, electrode artefact or headset noise dominated the band powers, the subject could taste or guess the arm, or a session was disturbed (log sleep, caffeine, time of day, illness and exclude by a rule written down in advance)",
  evidence: "Photo of the bench (headset, coil, jar, coded bottles, printed addition sheets) so others can rebuild it; the pre-registration sheet (sessions per arm, session time, caffeine and sleep rules, exclusion rule) photographed before session one; the sealed code key photographed sealed, then opened only after all numbers are written; the raw per-session table (baseline and post-stress alpha/beta, band powers, recovery ratio, arm) as a spreadsheet; the randomized schedule; the no-drink-arm stress drop shown as the assay check; the verdict stated plainly either way"
}
```

---

## Source Documentation

- **Primary source (fetched and read in full this run, 2026-09-24):** 江川陽介 (Egawa Yōsuke), 「振動波エネルギーを転写した水（波動水）は精神的ストレス負荷からの回復に影響をあたえるか」 — *"Does water to which vibrational-wave energy has been transferred (wave water) affect recovery from mental-stress loading?"* — Kokushikan University (国士舘大学) graduate-school research bulletin, funded by JSPS Kakenhi 16K01669 · [`https://www.kokushikan.ac.jp/gs/department/hs/docs/01_102.pdf`](https://www.kokushikan.ac.jp/gs/department/hs/docs/01_102.pdf). n = 7 healthy male students (21.1 ± 0.8 y); randomized three-arm crossover, one arm per week; 15-minute Uchida-Kraepelin arithmetic stressor; 60 s eyes-closed EEG before and after, α 8–13 Hz / β 13–30 Hz, endpoint α/β ratio; double-blind with a third-party check on the experimenter.
- **Scout record:** `sources/2026-09-16-scout-a-de-fr-ja.md` find #10 — `practical_applicability: flag=true, fields [reproducible]`, *"protocol fully specified (frequencies table included) — replicable EEG study design; effect claim weak, n=7."*
- **Named as this card by an existing card:** `synthesis/quest-queue/2026-09-17-qi-water-conductivity.md` (dossier 022) cites this study as *"the natural follow-up card for the physiology side."*
- **Same author's prior work (cited inside the paper, not independent):** Egawa & Ishizuka, *Kokushikan University Education Bulletin* No. 33, pp. 1–14, 2016; Egawa, *Kokushikan Jimbun-gaku* No. 8, pp. 1–9, 2018 (delayed-onset muscle soreness).
- **The imprinting instrument, shared with an existing card:** `synthesis/quest-queue/2026-09-20-water-memory-imprint.md` (dossier 028) — the 7.8 Hz coil, from the Pollack-lab result that 7.8 Hz and 75 Hz alternating fields induce EZ-like reorganization persisting 30+ minutes. **028 asks whether the imprint survives in the water; this card asks whether imprinted water does anything to a person.**
- **Context — suppression is not evidence:** `synthesis/claim-status-records/radionics-abrams-era-1916-1988.json` and `orgone-reich-fda-1957.json` document health-instrument claims that were never demonstrated under blinding. That history is a **warning about method, not evidence either way** about this claim. This card tests the claim on its own merits and inherits no verdict.
- **Replication Dossier:** `synthesis/replication/2026-09-24-dossier-039-wave-water-stress-recovery.md`
- **Aetherforce Reference:** search "water memory" / "structured water" / "wave water" on https://www.aetherforce.energy

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (consumer EEG headset, coil at 7.8 Hz, coded bottles, printed addition sheets) with a named procedure and one hard measurable outcome (the per-session α/β recovery ratio), plus an assay-validity check that can void the run. Not pure theory. |
| **Replicable** | YES — **Homelab: ~$120–440**, dominated by the EEG headset (~$100–400) plus ~$20–40 of coil and signal-source parts. ≥18 sessions at ~25 minutes each. **This is the queue's first card requiring a purchased instrument rather than hardware-store parts**, which is why the tier is **wood** and not sand or straw — a family without a headset should not run it. |
| **Relevant** | YES — Health domain: the human body is the measured object, which no health card in the queue has carried before (006, 012, 017, 022, 028, 034 are all an instrument, a water sample, an animal, or a measurement skill). Complements the Natural Medicine guild and connects directly to the water-memory lineage. |
| **Honest** | YES — and this is the card's spine. The source is a **small single-site study (n=7, all male)** in its own institution's bulletin, by a professor testing a **commercial product with a proprietary, undisclosed production method**, with **no independent replication** and the author's own prior work as its only lineage. Its own numbers show **plain water moved most of the way and was indistinguishable from both arms** — so the card's discriminating prediction is **imprinted vs plain water**, not imprinted vs nothing. The source's own concessions are quoted in the dossier (the water's existence *"is not academically recognized"*; the theory *"has poor scientific grounding"*). The product's far wider claimed scope — including cancer — is **named and explicitly not tested**; the card makes **no treatment claim**. Clean FAIL path. |
| **Linked** | YES — A primary document fetched and read in full, its scout entry, the card that named it as the follow-up (022), the card that shares its instrument (028), two claim-status records as method context, and a pre-registered replication dossier. |

---

## The honest framing (the spine of the card)

**This is not a re-run of the study. It is the control the study's own numbers imply and the paper never ran.**

The published result: α/β fell after the stressor in all three arms (the stressor worked); the imprinted-water arm ended higher than the no-drink arm; and **plain water ended in between and differed from neither.** The paper's own words are that the plain-water relaxation *"does not exceed the placebo effect."* So the study's significant comparison is imprinted water against **drinking nothing** — which tests whether drinking water calms you down, not whether the imprint does anything. **The card's discriminating prediction is imprinted versus plain water, handled identically.** That single design choice is the whole card.

**What the card cannot do, stated up front.** The source's imprinting apparatus — a Reyonex "Reyometer Digital" and the 大光明清水 concentrate — is proprietary, and the paper states the production method *"has not been published."* **This card cannot make the source's water.** It substitutes the archive's own reproducible imprinting method (a 7.8 Hz coil, the Pollack-lab result already used in dossier 028), so it tests the **class** — "water imprinted by a declared procedure" — and not the device. A null therefore does **not** prove the source's product is inert.

**The assay's own control is mandatory.** The α/β ratio must fall across the stressor in the no-drink arm. If it does not, the instrument did not register the effect the source measured, and the run is **void — not a refutation.** A test whose instrument failed has produced no information, and filing it as a negative would be a manufactured false negative.

**Adult-only, and no treatment claim.** This is a self-experiment on healthy adults measuring a relaxation index. It is not a therapy and carries no medical claim. Do not run it with children; skip it if you have a heart condition, are pregnant, take cardiac or psychiatric medication, or find timed arithmetic distressing. The coil is low-voltage and low-frequency and must be driven from a battery-powered source — **never from mains.** The EEG headset is a passive sensor and a consumer headset is not a medical device.

**The confounds to name.** The α/β ratio is sensitive to arousal, alertness, caffeine, time of day, sleep debt and electrode placement — pre-register the session time, hold caffeine fixed, and log sleep. Expectation is not fully controlled even with a blinded subject, because the coder knows and the subject may guess. And **≥18 sessions is the real cost of this card**; with fewer, a null is uninformative rather than a refutation.

---

## Why this is the health card, and why it is tier wood

The health field has six cards and none of them measures a person. 006 (Eeman animal calm) and 012 (Eeman sleep quality) put a passive circuit on an animal or a sleeper; 017 (orgone To-T) measures a box; 022 (Qi-water conductivity) measures water; 028 (water memory imprint) measures water; 034 (neutral pendulum) measures an operator's discrimination. **This card's measured object is the human body** — the axis the health field had never carried, and the one the queue's own 022 named as the follow-up.

The tier is **wood** because the apparatus is an instrument. Every prior card in the queue was buildable from hardware-store parts; this one is not, and pretending otherwise would be the kind of optimism the engine's refusal rule exists to prevent. **A family without an EEG headset should not run this card.** A heart-rate-recovery variant of the same three arms is possible and is noted in the dossier — but it is a **different endpoint**, it does **not** replicate the source, and it must never be reported as one.
