---
name: Quest Card — Morning Light Timing Test
description: "Aetherforce-branded quest card testing the claim that bright light in the eyes within an hour of waking improves sleep timing. A four-week within-person A/B/A/B crossover — free, no apparatus — with sleep-onset latency and wake-time variance as the endpoints and morning light minutes as the intervention check. Health domain (sleep timing); Natural Medicine mirror."
---

# ⚡ Aetherforce — Natural Medicine

**Guild:** Aetherforce — Natural Medicine
**Quest Line:** ⚡ Aetherforce · Natural Medicine complement
**Tier:** sand
**Domain:** health (sleep timing — the light environment of the day)
**Status:** proposed
**Created:** 2026-10-03

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-03-morning-light-timing` · authored_at `2026-10-03` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Natural Medicine",
  desc: "Your body keeps time by light — and the light it evolved to read is not the light most of us get. Outdoors on an ordinary day is a hundred times brighter than the brightest room you own, and the signal that sets your clock is bright light in the eyes, early. The claim, made by the quantum-biology lineage and supported by ordinary circadian science, is simple: get bright light into your eyes within an hour of waking and you fall asleep faster and wake at a steadier time. That is a claim you can test on yourself in four weeks, for free, with a notebook. Run two weeks your normal way and two weeks with a ten-minute bright-morning block, in the order normal-bright-normal-bright so the seasons cannot fool you, and log one row a night: when you turned the light off, how long until you slept, how many times you woke, when you got up, how rested you felt, and how many minutes of daylight your eyes actually got. The last column is the one that keeps you honest — if your morning light did not rise, you did not run the experiment. If your sleep moved, you have found a lever you can pull every day for nothing. If it did not, you have learned that this particular lever does not move your sleep, which is a real result and not a wasted month. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Morning Light Timing Test",
    "FIRST pre-register everything before anyone runs: the two conditions, the order (A-B-A-B), the one-week block length, the endpoint definitions, the thresholds, and the exact log fields - photograph the sheet. Condition A (Usual): your normal morning, indoors, ordinary indoor light, no deliberate outdoor light in the first hour. Condition B (Bright): within 60 minutes of waking, get at least 10 minutes of outdoor daylight (or at least 10,000 lux), without sunglasses, ideally without window glass between you and the sky - then continue the day as usual. Run FOUR weeks in the order A, B, A, B (one week per block) - the repeat is what controls for the season and for any change in routine. Log every night and morning: lights-out time, estimated sleep-onset latency in minutes, number of night wakings, wake time, morning alertness 1-10, and morning light minutes (or lux) actually achieved. Change nothing else - bedtime, caffeine, screens, exercise - and mark any night that was disrupted (illness, travel, a late night) so it can be excluded. Measurable outcome: the mean sleep-onset latency and the wake-time variance in the B weeks versus the A weeks, with the morning-light-minutes column as the intervention check. Target: sleep-onset latency at least 10 minutes shorter in BOTH B weeks with morning light up at least 15 min/day = the light-timing lever is real for this family; no difference within 5 minutes across both blocks even though morning light rose = the lever is not detectable in this family's sleep at home scale (the expected, complete result).",
    ["Science", "Measurement", "Health"],
    "☀️"
  ],
  source_doc: "sources/video/2026-10-02-cowan-danny-jones-quantum-circadian.md — 'Dr. Alexis Cowan — Quantum & Circadian Biology, Mitochondrial Medicine' (Danny Jones Podcast, harvested 2026-10-02)",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-10-03-dossier-064-morning-light-timing.md",
  pass_fail: "PASS (claim survives - the effect is real for this family): mean sleep-onset latency in B weeks is >= 10 minutes shorter than in A weeks in BOTH B weeks AND morning light minutes rose >= 15 min/day in the B weeks AND wake-time variance is lower in the B weeks | PASS (refuted - a complete, useful result): sleep-onset latency shows no difference (within +/- 5 min) between A and B weeks across both blocks even though morning light minutes rose - the light-timing lever is not detectable in this family's sleep at home scale (Skeptic's Star) | FAIL (void, not a null): morning light minutes did NOT rise in the B weeks - the intervention was never delivered, so the run says nothing about the claim | INCONCLUSIVE: fewer than four complete weeks; fewer than 20 usable nights; a confound on more than a quarter of nights (illness, travel, alcohol, a bedtime change); or the family changed another variable mid-run | ARTIFACT: the effect tracks the ORDER (the second half always looks better) rather than the condition; or the improvement appears only in the week the family was trying hardest and vanishes in the repeat",
  evidence: "Photo of the pre-registration sheet (conditions, order, block length, endpoints, thresholds, log fields) taken before anything runs + the nightly log (lights-out, sleep-onset latency, wakings, wake time, alertness 1-10, morning light minutes/lux) for all four weeks + the per-block means for sleep-onset latency and the wake-time standard deviation + the morning-light-minutes comparison that proves the intervention was actually delivered + the confound/exclusion notes reported whether or not they change the verdict"
}
```

---

## Source Documentation

- **Primary (the claim):** `sources/video/2026-10-02-cowan-danny-jones-quantum-circadian.md` — the video record for the Danny Jones Podcast episode with **Dr. Alexis Cowan** (harvested 2026-10-02). Its `## Practicality assessment` block names the light/EMF behavior subset as quest-card-eligible ("Get bright light in your eyes within an hour of waking, every day for two weeks, and log it — free, safe, self-measurable, and it is the one intervention the episode returns to repeatedly") and names the design this card uses ("a light-timing protocol has a pre-registerable criterion (e.g., sleep-onset latency, wake time variance over 4 weeks)"). Source video: https://youtu.be/WNXknj4EL1w. ⚠ **The transcript is P0 — never publish**; the record holds a segment map with short attributed quotes, a termbase, and the assessment (our own analysis, P2).
- **Companion (the subject directory):** `synthesis/interviews/alexis-cowan/` — the interview-radar subject directory seeded by this episode, with Jack Kruse as the anchor figure.
- **Companion (the modality register):** `synthesis/vitality/MODALITIES.md` — light timing and EMF mitigation are registered there, with the `verify` field mandatory (claim shape: "this is what the source says and here's how you'd test it," never "this works").
- **Companion (the graded claims):** `synthesis/ground-truth/claims.jsonl` — slug prefix `interview:`; the episode's light/EMF claims are graded there, and the card keeps the well-supported tier separate from the speculative one.
- **Companion card (the other sleep endpoint):** `synthesis/quest-queue/2026-09-12-eeman-sleep-quality.md` (dossier 012) — the same endpoint (sleep quality), a different kind of intervention (an apparatus).
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-03-dossier-064-morning-light-timing.md`
- **Aetherforce Reference:** search "circadian" / "light" / "melanopsin" / "EMF" on https://www.aetherforce.energy
- **Vault link:** https://focusingpulse.github.io/AFLinks

---

## Rubric Justification

- **Practical:** a named action (a bright-morning block: ≥10 min of outdoor daylight within an hour of waking) with a named procedure (pre-register → A-B-A-B → log nightly → compare blocks) and a measurable outcome (**mean sleep-onset latency and wake-time variance, B weeks vs A weeks, with morning light minutes as the intervention check**). Not pure theory.
- **Replicable:** home-scale (**~$0** — a notebook and a phone; optionally a lux app or meter, ~$0–30), no lab, no chemicals, family-safe, any season.
- **Relevant:** maps to the Village **health** survival domain (sleep timing) and complements the **Natural Medicine** guild.
- **Honest:** framed as a TEST, not an endorsement. The card separates the **well-supported** tier (light entrains circadian timing — mainstream physiology) from the **hypothesis** tier (the metabolic cascade) and the **speculative** tier (deuterium vortices, melanin photosynthesis), and tests only the first. It names its confounds out loud — unblinded, the intervention is bundled with going outside, n = 1, season drift, a soft endpoint — and pre-registers the thresholds before anyone runs. The expected outcome is a null, and a positive is presented as the surprise.
- **Linked:** source doc (video record + primary URL), companion subject directory and modality register, dossier created with protocol + pass/fail, evidence protocol defined.

---

## What makes it the queue's first of its kind

- **The first card on the light environment** — the timing of light a person's eyes actually receive, rather than a device, a field, or a material. Every prior health card tests an apparatus (Eeman circuit, orgone accumulator, pendulum, Egely wheel) or a water treatment; **none tests the light of the day.**
- **The first purely behavioral health card** — no apparatus, no purchase, no build. The whole experiment is a habit and a notebook.
- **The first health card whose core mechanism is mainstream-supported** — and the card says so plainly rather than dressing a known practice as a discovery. The value is not that the claim is doubtful; it is that the **numbers are yours**.
- **The design that makes it a measurement: the A-B-A-B repeat.** A one-block (A-B) design cannot tell a light effect from the season turning or the family trying harder. Repeating the condition twice, in order, is what makes the comparison interpretable — and the card's first ARTIFACT condition is exactly the case where the effect tracks the order rather than the light.

---

## Honest Framing

This is a test, not an endorsement. The source is a **podcast conversation**, and the guest — a credentialed metabolomics researcher who left academia for the quantum-biology lineage — **sells** the material she advocates. The episode states claims and publishes **no measurements**. The card supplies the protocol the source never published. Three honesty notes the card keeps in front of the family: (1) the core mechanism — **light entrains the circadian clock** — is **mainstream-supported**, not fringe; the card is the queue's first to say so, and it does not pretend a known practice is a discovery; (2) the episode's stronger metabolic framing (near-infrared, mitochondrial melatonin) is a **hypothesis**, and its deuterium-vortex and melanin-photosynthesis claims are **speculative** — the card tests none of them; and (3) the endpoint is **soft and partly self-reported**, the intervention is **bundled** with going outside, and the run is **n = 1**, so the likely outcome is a null, and a null is a **complete and useful result** (Skeptic's Star), not a failure. A clear, repeating effect (≥10 min shorter in both B weeks, with morning light actually up) would be a genuinely useful personal finding. The card is a method test of a cited claim; it makes **no health claim** and issues **no treatment instruction**.

---

## Aetherforce Mirror Coverage

This card complements **Guild 1: Natural Medicine** (health) — its **10th** card, after the Eeman Biofield Test (2026-09-06), Eeman Sleep Quality (2026-09-12), Qi-Water Conductivity (2026-09-17), Water Memory Imprint (2026-09-20), Neutral Pendulum Discrimination (2026-09-22), Wave-Water Stress-Recovery (2026-09-24), Palm Thermal Control (2026-09-26), Egely Wheel Vital-Force (2026-09-28), and Form-Field Water-Structure (2026-09-30).

**Mirrors filled: 25/26** (unchanged — no new guild filled; Textiles remains the only empty mirror, with no buildable fiber-resonance source in the archive).

---

## Dossier

- `living-library/synthesis/replication/2026-10-03-dossier-064-morning-light-timing.md` — full protocol, apparatus, pass/fail, confounds and verdict rules.
