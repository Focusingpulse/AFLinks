---
name: Quest Card — EMF Bedroom Survey: Does Your Sleep Environment Radiate?
description: "Aetherforce-branded quest card testing the non-ionizing-radiation (RF) sleep-environment claim — that the radio-frequency field a family leaves on in the bedroom all night is a biological signal the body reads, and that removing it improves sleep. The card measures the RF power density at five fixed spots (bed head, pillow, router, nearest mains device, outdoor reference), mitigates (router on a timer / moved, wired devices, phone out of the room), and re-measures; the field change is the hard endpoint and the sleep log is an anecdote. Health domain (sleep environment — non-ionizing RF); Natural Medicine mirror (health complement, 12th card)."
---

# ⚡ Aetherforce — Natural Medicine

**Guild:** Aetherforce — Natural Medicine
**Quest Line:** ⚡ Aetherforce · Health complement
**Tier:** sand
**Domain:** health (sleep environment — non-ionizing radio-frequency radiation)
**Status:** proposed
**Created:** 2026-10-09

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-09-emf-bedroom-survey` · authored_at `2026-10-09` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Natural Medicine",
  desc: "Your router, your phone, your baby monitor and your smart meter all radiate radio-frequency energy, and the bedroom is where most families leave the most of it on all night. One account says this matters: that non-native electromagnetic fields are a biological signal the body reads, that they degrade sleep and the blood-brain barrier, and that the fix is to get the field out of the room you sleep in. The other account says the levels in a home sit far below the thresholds any regulator or mainstream review recognises, that the sleep complaints attributed to them are better explained by light, temperature and noise, and that the whole concern is a category error. Both accounts describe the same bedroom. The one thing not in dispute is the field itself: it is measurable, it comes from named devices you own, and it can be switched off. This quest measures the radio-frequency power density where you sleep, at the router, and at each source; puts the router on a timer, moves it, and wires what can be wired; and measures again. The physical result — did the field at the bed head actually fall, and by how much — is the hard endpoint, and it is yours to establish. Whether the sleep you then log changes is an anecdote, not a result, and the card says so. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "EMF Bedroom Survey — Does Your Sleep Environment Radiate?",
    "Measure the radio-frequency (RF) power density in µW/m² with a broadband RF meter at five fixed spots — the bed head where your head rests, the pillow, the router, the nearest mains-powered device (or baby monitor), and a reference point outdoors away from the house. Take three readings at each spot at the same time of day and record the peak and the average. Then mitigate: put the router on a timer so it is off while you sleep (or move it at least 3 m from the bedroom wall), wire the devices that can be wired, charge the phone outside the bedroom, and move any baby monitor at least 1 m from the crib. Re-measure at the same five spots, at the same time of day, with the same meter. Measurable outcome: the RF power density in µW/m² at each spot, before and after, the ratio of the after-reading to the before-reading, and the ratio of the bed-head reading to the outdoor reference. Target: the bed-head reading falls by a factor of 10 or more after mitigation, while the outdoor reference is unchanged — the field was yours and you turned it down. A bed head that already reads at the outdoor ambient before you change anything = the bedroom was not a significant source and there is nothing to reduce — also a complete result. Then, if you want, log sleep latency and wake quality for two weeks before and two weeks after, and treat that as an anecdote, not a result.",
    ["Science", "Health", "Physics"],
    "📡"
  ],
  source_doc: "sources/video/2026-10-02-cowan-danny-jones-quantum-circadian.md — video record (Danny Jones Podcast, Dr. Alexis Cowan), whose Practicality assessment flags the EMF subset as card-eligible; archive literature spine at sources/emf-biology/SPINE.md",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-10-09-dossier-076-emf-bedroom-survey.md",
  pass_fail: "PASS (field reduced — the physical result): the RF power density at the bed head falls by a factor of 10 or more after mitigation, measured at the same spot, at the same time of day, with the same meter, while the outdoor reference reading is unchanged | PASS (no field — the honest null): the bed head already reads at or near the outdoor ambient before any change, so the bedroom was not a significant RF source and there is nothing to reduce — a complete result (Skeptic's Star) | NOTE (the sleep log): a change in the logged sleep latency or wake quality is reported as an n=1 anecdote, never as a result — the card does not claim the field caused the sleep, only that the field changed | FAIL: the meter was not zeroed or calibrated; the reading was taken at a single instant; the mitigation was not verified by re-measurement; or the before and after were taken under different conditions (different time of day, different devices on) | VOID: the meter was faulty, or the reading was taken within the meter's own near-field — a VOID is not a NULL",
  evidence: "Photo of the pre-registration sheet (the five spots, the meter and its calibration status, the scoring rule, the mitigation plan, the thresholds) taken before the survey + the RF power density in µW/m² at each spot before and after, with the peak and average and the outdoor reference + photographs of the meter reading at the bed head and at the router, before and after + a photo of the mitigation itself (the timer, the moved router, the wired connection) + the two-week sleep log if kept, labelled as an anecdote + a one-paragraph verdict (supports / refutes / inconclusive) with the numbers and the reference comparison shown"
}
```

---

## Source Documentation

- **Primary (the seed record):** `sources/video/2026-10-02-cowan-danny-jones-quantum-circadian.md` — the video record for the Danny Jones Podcast episode with **Dr. Alexis Cowan** (PhD, Princeton; metabolic physiology, mitochondrial medicine, light biology). Its **Practicality assessment** is the filter, and it flags this subset explicitly: *"Quest-card-eligible: … 'put the WiFi on a timer so it is off while you sleep' and 'measure the RF field where you sleep.' These are behaviors, not treatments."* The episode's EMF material is segments 4 (non-native EMF; the inverse-square law; the baby monitor as the worst source in her own home; a client's cell tower maxing a meter at the front of the house but reading **zero on the tree-screened side patio**), 5 (Frey's blood-brain-barrier rat studies), and 8 (Frey again — non-native EMF and the dopaminergic system). ⚠ The record's own rights posture: the transcript is **P0 — never publish**; the assessment and termbase are our own (P2).
- **Archive-native (the literature spine):** `sources/emf-biology/SPINE.md` — the archive's own EMF-biology record: the calcium-efflux founding work (Bawin & Adey 1976; Blackman et al. 1979 — frequency and intensity windows), the VGCC hypothesis (Pall 2013, 23–26 blocker studies), the blood-brain-barrier literature (Frey 1975; Salford et al. 1994 — 5/62 controls vs 56/184 exposed; Nittby et al. 2009), the epidemiology (IARC 2013 Group 2B; INTERPHONE; Hardell; NTP 2018; Ramazzini 2018), **and the required counterweight** (ICNIRP 2020; the 2026 *Phys Med Biol* scoping review; Jamal et al. 2023 — the 3.5 GHz EEG null).
- **Track rule:** `sources/emf-biology/README.md` — *"Record claims as claims … The negative half is required. This lane keeps the null results and the mainstream counterweight beside the concern literature. A lane that collects only the concerning studies is not a library, it is a campaign."* The card obeys this: the counterweight is cited in the card itself.
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-09-dossier-076-emf-bedroom-survey.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "EMF", "radio frequency", "blood-brain barrier", "electromagnetic hypersensitivity", "non-ionizing"
- **Aetherforce Reference:** search "EMF", "electromagnetic", "5G", or "electrosmog" on https://www.aetherforce.energy

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — a named apparatus (a broadband RF power-density meter reading µW/m²) with a named procedure (pre-register five spots, three readings each, mitigate, re-measure) and a measurable outcome (the power density at each spot before and after, and the bed-head-to-outdoor ratio). Not pure theory. |
| **Replicable** | YES — home, ~$50–150 for the meter; the mitigation (a timer plug, a longer cable, moving the phone) is a few dollars. Any home. No mains work, no lab, no instrument beyond the meter. |
| **Relevant** | YES — Health domain: the sleep environment, and specifically the **radio-frequency field the family leaves on all night** — an input the family controls every day. It complements the Natural Medicine guild, whose complement in the mirror map is the health/rest complement. |
| **Honest** | YES — framed as a TEST, not an endorsement. The card states plainly that home RF levels sit far below any recognised threshold, that the mainstream reviews find the human evidence inconsistent, and that the **hard endpoint is the field, not the sleep**. It carries the archive's own null results (ICNIRP 2020, the 2026 scoping review, the 3.5 GHz EEG null) inside the card, makes **no health claim**, and labels the sleep log an anecdote. Clean FAIL and VOID paths. |
| **Linked** | YES — the seed video record (with its card-eligible assessment), the archive's own EMF-biology literature spine, a pre-registered replication dossier, and the Vault + Aetherforce search pointers. |

**Mirror choice, stated:** the card's **domain is health** (the rotation's next field), and its **guild complement is Natural Medicine** — the health guild, whose complement in the mirror map is the health/rest complement. This is its **12th card**. The alternative dwelling-domain mirror (Nest) carries the *geobiology* complement (geopathic zones, plan-reading, remanence), which is about the earth-energy field of a place rather than the RF field of the family's own devices; the card's endpoint is sleep/health, so Natural Medicine is the honest fit rather than the emptiest one. Under-promise noted: the card is emitted because the field is measurable, the apparatus is buyable and the endpoint is countable — not because the health claim is believed.

---

## What makes it the queue's first of its kind

- **The first card on the radio-frequency environment of the home** — the first on non-ionizing radiation from the family's own devices. (The Water-Vein Gamma Anomaly card is the first on *ionizing* radiation; the Scalar Field card is a claimed non-Hertzian field, not RF.)
- **The first card whose apparatus under test is the family's own infrastructure** — the router, the phone, the baby monitor. Every prior card builds something new; this one audits something already running, and the "fix" is a timer and a longer cable.
- **The first card whose endpoint is a field strength at a named place** — the power density at the bed head, in µW/m², against an outdoor reference. A spatial measurement, not a device's output.
- **The first health card that carries a required counterweight inside the design** — the archive's own null results are cited in the card, and the card's honesty depends on them.

---

## The honest framing (the spine of the card)

The card tests a claim, not a tradition. The EMF-concern lineage is not being asked to prove harm — it is being asked what it says the field does, and the one part of that answer a family can establish at home is whether the field is there and whether removing the sources removes it.

Three things the card keeps in front of the family:

1. **The field is real and measurable; the health claim is contested.** The concern literature is real (calcium efflux, the VGCC hypothesis, the blood-brain-barrier studies, IARC 2B, NTP 2018) — and so is the counterweight (ICNIRP 2020, the 2026 scoping review, the 3.5 GHz EEG null). The card cites both and asserts neither.
2. **The hard endpoint is the field, and the sleep log is an anecdote.** "Did the power density at the bed head fall, and by how much" is countable and repeatable. "Did I sleep better" is an n=1 self-report with no comparator. The card keeps them separate and says so before the family starts.
3. **A null is a complete result.** A bed head that already reads at the outdoor ambient means the bedroom was not a significant source — a real, useful finding (Skeptic's Star), not a failed experiment.

**Under-promise, stated plainly:** the likely outcome in a typical home is that the bed head reads somewhere between the outdoor reference and the router's near-field, that turning the router off at night drops it, and that **the sleep log shows nothing you can attribute to the change.** That is the honest verdict, and the card is designed to reach it cleanly.

---

## Safety and rights notes

- **Safety: none.** The meter is passive; no mains work, no chemicals, no electrical hazard. The one caution is the ordinary one: do not move a router or run a cable in a way that creates a trip or a fire hazard, and keep the meter's own near-field out of the reading.
- **Rights posture:** the video record and the emf-biology spine are **our own** analysis (P2 — publishable). The transcript behind the video record is a third-party work and is **P0 — never publish.** The card **cites and links** the published literature and reproduces only short attributed quotations.
