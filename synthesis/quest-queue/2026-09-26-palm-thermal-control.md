---
name: Palm Thermal Control Test
description: "Can a person drive their own palm hotter on one instruction and colder than ambient on another, with no feedback and no physical means? A skin-mode IR thermometer at a fixed 15 cm standoff, a within-subject WARM/COOL/REST crossover, and the direction of change as the discriminator. Health-domain card (voluntary thermal control); ~$25; Natural Medicine mirror. The queue's first card whose object is the practitioner's own body."
---

# ⚡ Aetherforce — Natural Medicine

**Guild:** Aetherforce — Natural Medicine
**Quest Line:** ⚡ Aetherforce · Natural Medicine complement
**Tier:** sand
**Domain:** health (human physiology — voluntary thermal control / autonomic self-regulation)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-26-palm-thermal-control` · authored_at `2026-09-26` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Natural Medicine",
  desc: "Prof. Lee Si-Chen of National Taiwan University pointed a cooled infrared detector at a qigong master's palm from 15 cm away and found two modes in the same man: 'regulating qi' made the palm run HOT (blood flowing in — vasodilation), and 'strong qi', the rare one, made it run COLDER THAN THE ROOM (blood shut out — vasoconstriction). His own explanation is ordinary autonomic physiology, which is exactly why you can test it with a $25 thermometer. Here is the honest version: you are not testing whether qi is a field. You are testing whether a person told WARM warms and told COOL cools, on command, with no feedback and no rubbing. Three conditions — WARM, COOL, REST — in randomized order, the measurer blind, the palm temperature read every 30 seconds. The number that matters is not how much the palm moved; it is W − C, the difference between the two instructions. A palm that warms in both conditions has learned to relax, not to control. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Palm Thermal Control Test",
    "Get a non-contact IR thermometer with a skin mode and 0.1 °C steps (~$25). Fix a standoff so the gun sits at the same 15 cm and the same angle for every reading — hand-held readings at varying distance are the whole noise floor. FIRST run the positive control: sit 5 min, measure the palm, rub your hands briskly 30 s, measure again. The palm must rise at least 0.5 °C or the setup cannot resolve the effect — fix it before going on. Then three roles: a practitioner, a measurer who reads the numbers but is BLIND to the condition, and a referee who shuffles three sealed cards (WARM / COOL / REST) and fills in the condition column afterward. Baseline 5 min (reading every 30 s), then draw one card — shown to the practitioner only — and attempt it for 5 min, then rest 5 min off the stand. Repeat all three conditions in random order. Do the whole set on three separate days. Measurable outcome: W − C, the palm's temperature change under WARM minus under COOL, in °C. PASS: W − C >= 1.0 °C in at least 2 of 3 sessions — direction-specific voluntary control. STRONG PASS: the palm also falls >= 1.0 °C below its own baseline AND below ambient during COOL — the 'ice palm' prediction. FAIL: W − C <= 0.3 °C in at least 2 of 3 sessions — the palm follows rest and arousal, not instruction (Skeptic's Star; a complete result). VOID: the rub-hands control did not register, ambient moved more than 1.5 °C, the hand left the stand, or the measurer knew the condition. Report the numbers whether they change or not.",
    ["Science", "Health", "Observation"],
    "🖐️"
  ],
  source_doc: "translations/2026-09-26-qigong-infrared-spectrum-lee-si-chen-zh.md (full EN translation of Prof. Lee Si-Chen 李嗣涔, 'The Infrared Spectrum of Qigong States and Emitted External Qi', Dept. of Electrical Engineering, National Taiwan University — §III(2) and the Discussion; hosted by the Taipei Qigong Culture Society, original site dead, Wayback capture 2020-08-03) + translations/2026-09-26-tsinghua-qigong-research-1987-zh.md (the sibling external-qi-on-water claim, Guangming Daily 1987-01-24)",
  source_url: "https://web.archive.org/web/20200803204038/http://www.chikung.org.tw/txt/paper/p02.htm",
  dossier: "living-library/synthesis/replication/2026-09-26-dossier-045-palm-thermal-control.md",
  pass_fail: "PASS: W − C >= 1.0 °C in >= 2 of 3 sessions (the palm moves in opposite directions on opposite instructions). STRONG PASS: additionally the palm falls >= 1.0 °C below its own baseline AND below ambient during COOL in >= 2 of 3 sessions — Lee's 'ice palm' prediction confirmed. FAIL: W − C <= 0.3 °C in >= 2 of 3 sessions — no direction-specific control; palm temperature follows rest and arousal only (Skeptic's Star; a complete and valuable result). INCONCLUSIVE: between the two, or fewer than 3 sessions. VOID: the rub-hands positive control did not register >= 0.5 °C; or ambient moved > 1.5 °C during a session; or the hand left the stand mid-condition; or the measurer knew the condition — report the resolution achieved and the control required, NOT a verdict. ARTIFACT: the result tracks ambient drift (re-run at the same time of day); or the instrument cannot resolve 0.3 °C (the positive control is the check); or the practitioner is trained in qigong or thermal biofeedback (record practice history — a PASS in a trained person and a FAIL in an untrained one are both informative).",
  evidence: "Photo of the fixed standoff and the thermometer model + the pre-registration sheet (thresholds, scoring rule, condition order, who is blind to what) + the three sealed cards + the rub-hands positive-control reading (before and after) + the recording sheet for each session (time, temperature, condition column filled by the referee) + ambient temperature logged per session + the three sessions dated + each participant's practice history + the void check reported whether or not it voids the run"
}
```

---

## Source Documentation

- **Primary:** **Prof. Lee Si-Chen (李嗣涔), "The Infrared Spectrum of Qigong States and Emitted External Qi"** — held in the Vault as `translations/2026-09-26-qigong-infrared-spectrum-lee-si-chen-zh.md` (full English translation, translated 2026-09-26). Lee was a professor in NTU's Department of Electrical Engineering and later became president of National Taiwan University. The paper's original host (chikung.org.tw, Taipei Qigong Culture Society) is **dead** — the only copy is a Wayback capture of 2020-08-03, which makes this a preservation candidate as well as a source.
- **The claim in the source's own words:** on the warming mode — *"about 10 seconds after emission began, the infrared radiation increased greatly, indicating the palm began to warm; after stopping, the infrared did not decrease, indicating the palm maintained the same temperature."* On the cooling mode — *"The AC signal measured by the detector was actually negative, indicating the master's palm temperature dropped colder than the environment — the palm was absorbing heat from the environment… This state persisted until the master withdrew the qi, at which point the palm instantly became hot."* Lee names the mode **"ice palm" (寒冰掌)** and concludes: *"this Daoist master had mastered two different practice methods: one controlling the parasympathetic nervous system, the other controlling the sympathetic nervous system, used alternately to achieve control over the body."*
- **The baseline the source itself supplies:** *"when an ordinary person sits quietly with eyes closed, the peak alpha-wave power changes little within 6 minutes — within about 10%."* The equivalent for temperature is what the REST condition measures.
- **The method, for fidelity:** cooled InSb detector, **3–5.6 µm band**, **15 cm standoff** at the Laogong point (palm centre), chopper + lock-in amplifier. Because a body near 300 K radiates as a blackbody, measuring that band **is** measuring the palm's temperature — which is why a skin-mode IR thermometer is a legitimate home substitute for the *temperature* claim (it is not a substitute for the *spectral* claim, which this card does not test).
- **Lineage:** `sources/2026-09-25-scout-a-langs-1.md` finds 4–5 — Lee's torsion-field/qi bridge paper (*Journal of Life Sciences*, 2006) and the scalarwave.cc China↔Germany torsion collaboration. The scout's own flag on the infrared paper is `practical_applicability: false [conceptual]`; **this card departs from that flag deliberately and states why** (see "Departure from the scout flag" below).
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-26-dossier-045-palm-thermal-control.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "qigong", "Lee Si-Chen", "external qi", "infrared"
- **Aetherforce Reference:** Search "qigong", "qi", or "biofield" on https://www.aetherforce.energy
- **Related cards:** 039 (Wave-Water Stress-Recovery — the other human-physiology card, instrument tier), 022 (Qi-Water Conductivity — the same tradition on an *external* object), 028 (Water Memory Imprint), 034 (Neutral Pendulum Discrimination)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (skin-mode IR thermometer, fixed 15 cm standoff, palm rest, three sealed condition cards, recording sheet) with a named procedure (positive control → baseline → randomized WARM/COOL/REST → three sessions) and a measurable outcome (**W − C**, the palm's temperature change under WARM minus under COOL, in °C, plus the below-ambient check). Not pure theory. |
| **Replicable** | YES — Home, sand: **~$25**. No mains, no chemicals, no heat source, no sharp tools. The only demanding requirement is sitting still and keeping the standoff fixed. |
| **Relevant** | YES — Health domain (human physiology — voluntary thermal control / autonomic self-regulation). Fills the **Natural Medicine** mirror, 7th card. |
| **Honest** | YES — the claim is framed as a claim and the card is a test, not an endorsement. The source's own mundane mechanism (autonomic vasodilation/vasoconstriction) is stated up front; the **direction of change within one person is the discriminator**, not the magnitude; the REST condition exists to measure the arousal/relaxation confound; the instrument's resolution limit is named and the positive control is the gate; and the blinding limit (the practitioner cannot be blind to their own instruction) is stated rather than faked. Clean FAIL / INCONCLUSIVE / VOID paths. |
| **Linked** | YES — A Vault translation, the sibling primary document, the lineage scout file, a pre-registered replication dossier, and cross-links to four related cards. |

**Mirror choice, stated:** the card's domain is **health**, and **Natural Medicine** is the honest fit — it is the health guild and already carries the tradition's other cards (006 Eeman animal calm, 012 Eeman sleep quality, 022 qi-water conductivity, 028 water memory imprint, 034 neutral pendulum discrimination, 039 wave-water stress-recovery). No other mirror competes: the card's object is a human body, and the only other body-facing mirror (Animal Care, card 006) is for animals.

---

## The honest framing (the spine of the card)

**The object is new, and that is the point.** Every prior health card in the queue tests an *external* object: water's conductivity (022), water's memory (028), a pendulum's discrimination (034), a recipient's EEG (039). **None asks whether a person can voluntarily move one of their own physiological variables, on command, in a specified direction.** That is the claim the qigong tradition actually makes about the practitioner, and it is the one nobody in the queue has tested.

**The design choice that is the whole card is the direction of change.** A palm that warms when you attend to it has demonstrated relaxation — a real thing, and not the claim. The claim is *two opposite modes in the same body*. So the discriminating quantity is **W − C**, the difference between the two instructions in the same person on the same day. That single number separates voluntary control from sitting still, and it is why the REST condition and the opposite instruction are not extras but the test itself.

**The positive control is the card's validity gate.** A cheap IR gun at a varying distance can produce a 1 °C difference from noise alone. The rub-hands test — 30 seconds of friction, which must move the palm ≥ 0.5 °C — proves the setup can resolve the effect *before* any result is claimed. If it does not register, the session is void, and that is stated as a first-class outcome rather than a footnote.

**A PASS would not show that qi is a field.** It would show that a person can drive their own peripheral temperature up on one instruction and down on another, without feedback — which the mainstream literature already accepts is trainable (thermal biofeedback) and which the source's own mechanism predicts. The card's value is the number: how fast, how large, and whether the cooling mode can go **below ambient**, which is Lee's sharpest and most falsifiable prediction.

**A FAIL is a complete and valuable result.** It establishes what ordinary voluntary thermal control looks like in this family's hands — the baseline the tradition's claim rests on — and it is the archive's most useful kind of negative.

---

## Departure from the scout flag (stated, not hidden)

The scout file that surfaced this document carries `practical_applicability: false [conceptual]` (`sources/2026-09-25-scout-a-langs-1.md`). **This card departs from that flag, deliberately, and here is the reason.** The scout's flag is a judgment about the *document* — it is a 1980s instrumented report whose headline claims (a fifth force, an information field, exceptional function) are conceptual and unreplicated. The engine's rubric is a judgment about whether a *card* can be built with a named apparatus and a measurable outcome. Lee's paper contains one claim that is neither conceptual nor unreplicated-by-construction: **a palm temperature that moves in two directions on instruction.** That is measurable with a $25 instrument, and the source supplies its own mundane mechanism. The card tests that claim and **only** that claim — it does not touch the torsion field, the information field, or the EEG resonance state (the last is explicitly deferred to the instrument tier, card 039's apparatus).

**This is a departure, not an override.** The scout's flag stands for the document as a whole; the card is narrower than the document, and the narrowing is written down here so a later reader can see exactly what was carved out and why.