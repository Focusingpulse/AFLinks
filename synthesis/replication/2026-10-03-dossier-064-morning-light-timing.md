---
name: Dossier 064 — Morning Light Timing Test
description: "Replication dossier for the claim that bright light in the eyes within an hour of waking improves sleep timing — a within-person A/B/A/B crossover over four weeks, free, with sleep-onset latency and wake-time variance as the endpoints and morning light minutes as the intervention check. The health-domain card."
---

# Dossier 064 — The Morning Light Timing Test

**Status:** protocol
**Domain:** health (sleep timing — the light environment of the day) / Natural Medicine mirror
**Tier:** sand (home-scale, ~$0; four weeks to run)
**Created:** 2026-10-03

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-03-dossier-064-morning-light-timing` · authored_at `2026-10-03` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

**Source docs (AFLinks Vault):**

- `sources/video/2026-10-02-cowan-danny-jones-quantum-circadian.md` — the video record (Danny Jones Podcast, guest Dr. Alexis Cowan; harvested 2026-10-02). **This is the card's source.** Its `## Practicality assessment` block names the light/EMF behavior subset as quest-card-eligible and the pharmacology subset as refused, and its pass/fail line names the design this card uses ("sleep-onset latency, wake time variance over 4 weeks"). ⚠ **The transcript is P0 — never publish.** The record holds a segment map with short attributed quotes, a termbase, and the assessment — our own analysis (P2). The card cites the record; it does not reproduce the transcript.
- **Companion (the subject directory):** `synthesis/interviews/alexis-cowan/` — the interview-radar subject directory seeded by this episode.
- **Companion (the modality register):** `synthesis/vitality/MODALITIES.md` — light timing and EMF mitigation are registered there, with the `verify` field mandatory.
- **Companion (the graded claims):** `synthesis/ground-truth/claims.jsonl` — slug prefix `interview:`; the episode's light/EMF claims are graded there.

**Honest note on provenance.** The source is a **podcast conversation**, not a controlled study. The guest is a metabolomics-trained researcher (PhD, Princeton — Rabinowitz lab; postdoc, UPenn 2023) who left academia in 2023 for the quantum-biology lineage of Jack Kruse. She **sells** the material she advocates (a year-long course, a forthcoming protocols course, ebooks, a Patreon) — noted as an interest, not treated as a refutation. The episode states claims; it publishes **no measurements**. **The card supplies the protocol the source never published.**

**Honest note on doc-id verification.** The AFLinks Vault repo is not present in this sandbox, so no `doc:<id>` was verified against the live index this run. Sources are cited by repo path (video-record slug) plus the primary video URL, which the quest-card schema explicitly allows (`source_doc: "doc:<id> or translation slug"`). Stated, not papered over.

---

## The claim (as asserted by the source)

The episode's spine is that **modern indoor life breaks a set of environmental signals the body expects** — "bright light by day, darkness and no RF at night, near-infrared all day, grounding, natural water" — and that a large share of chronic disease sits downstream of that mismatch. The light arm of that claim is the one this card tests, and it is the intervention the episode returns to most often.

Three tiers of evidence travel with it, and the card keeps them separate:

1. **Well-supported (mainstream).** Light is the dominant *zeitgeber* — the signal that sets the circadian clock. Bright light in the eyes early in the day advances and stabilizes circadian timing; the melanopsin-containing retinal ganglion cells that carry this signal are established physiology. The episode's segment on sunglasses (02:14:57) names the **lux gap** — "outdoors 100,000+ lux vs indoors <1,000" — a real, measurable feature of modern life.
2. **Hypothesis, stated as such.** The stronger metabolic framing — that the light signal drives mitochondrial and hormonal cascades with disease-level consequences — is a hypothesis. The episode's own graded claim `interview:nir-stimulates-mitochondrial-melatonin` is `claimed`, and the underlying review is reported as missing direct evidence.
3. **Speculative / framework.** The deuterium-vortex and melanin-photosynthesis claims sit in the same episode and are `speculative`. **The card does not touch them.**

**The claim this card tests (operationalized):** *getting bright light into the eyes within an hour of waking improves how quickly you fall asleep at night and how steady your wake time is.*

**Claimants:** Dr. Alexis Cowan (Danny Jones Podcast, 2026-10-02), in the lineage of Jack Kruse
**Verification status:** the core claim (light entrains circadian timing) is **well-supported**; the *magnitude* of the effect on a given person's sleep-onset latency, and whether it is detectable in a family's own four-week log, is what is **untested here**
**Mainstream position:** light timing is a standard, guideline-level sleep intervention (morning bright light; evening dim light). This card is the queue's **first whose core mechanism is mainstream-supported** in the health domain — and it says so, rather than dressing a known practice as a discovery.

---

## The protocol — a within-person A/B/A/B crossover, four weeks

The testable core: **if bright morning light is the lever the source says it is, then weeks with a bright-morning block should show shorter sleep-onset latency and steadier wake times than weeks without it — and the family's morning light minutes should actually rise.**

### Materials (~$0)

1. **A sleep log** — paper or a notes app (free). One row per night.
2. **A phone timer / alarm** (free).
3. **Optional: a light meter or a phone lux app** (~$0–30) — to record morning light in lux rather than minutes. Without it, log **minutes outdoors in daylight** instead.
4. **Optional: a wearable or a phone sleep app** — for an objective-ish sleep-onset estimate. Without it, log **estimated sleep-onset latency** (minutes from lights-out to sleep) each morning.

### Design — the parts that make it a measurement

1. **Pre-register everything before anyone runs:** the two conditions, the order (A-B-A-B), the block length (one week each), the endpoint definitions, the thresholds, and the exact log fields — **photograph the sheet.**
2. **Condition A (Usual):** your normal morning — indoors, ordinary indoor light, no deliberate outdoor light in the first hour.
3. **Condition B (Bright):** within **60 minutes of waking**, get **≥10 minutes of outdoor daylight** (or ≥10,000 lux of bright light), **without sunglasses**, ideally without window glass between you and the sky. Then continue the day as usual.
4. **Run four weeks: A, B, A, B** — one week per block. The repeat (A-B-A-B) is what controls for drift: a change in the season, or in the family's routine, shows up in *both* A weeks or *both* B weeks, not in one.
5. **Log every night/morning:** lights-out time; estimated sleep-onset latency (min); number of night wakings; wake time; morning alertness (1–10); and **morning light minutes** (or lux) actually achieved.
6. **Do not change anything else** — bedtime, caffeine, screens, exercise — for the four weeks. If something changes (illness, travel, a late night), **mark that night** so it can be excluded.

### Endpoints

- **Primary — sleep-onset latency:** mean minutes from lights-out to sleep, B weeks vs A weeks.
- **Secondary — wake-time variance:** the standard deviation of wake time, B weeks vs A weeks.
- **Secondary — morning alertness:** mean 1–10 rating, B weeks vs A weeks.
- **Intervention check — morning light minutes:** did the B weeks actually deliver more light than the A weeks? **Without this, the experiment has no denominator.**

### Pre-registered pass/fail

- **PASS (claim survives — the effect is real for this family):** mean sleep-onset latency in B weeks is **≥10 minutes shorter** than in A weeks, **in BOTH B weeks**, **AND** morning light minutes rose by **≥15 min/day** in the B weeks, **AND** wake-time variance is lower in the B weeks.
- **PASS (refuted — a complete, useful result):** sleep-onset latency shows **no difference** (within ±5 min) between A and B weeks across both blocks, even though morning light minutes rose — the light-timing lever is not detectable in this family's sleep at home scale (Skeptic's Star).
- **FAIL (void, not a null):** morning light minutes did **not** rise in the B weeks — the intervention was never delivered; the run says nothing about the claim.
- **INCONCLUSIVE:** fewer than four complete weeks; fewer than 20 usable nights; a confound on more than a quarter of nights (illness, travel, alcohol, a bedtime change); or the family changed another variable mid-run.

### Confounds to name (the card says these out loud)

- **Unblinded.** You know which week you are in. Expectation can move a subjective endpoint; sleep-onset latency is partly self-reported, so treat a small effect with suspicion.
- **The intervention is bundled.** Getting morning light also means going outside — movement, fresh air, cooler temperature, a change of scene. A change in sleep could come from any of those, not from the light.
- **n = 1.** A single family's four weeks is a personal experiment, not a study. The result is *yours*, and it is real for you — it is not a general finding.
- **Season drift.** Four weeks spans a change in daylight length. The A-B-A-B repeat is the control for it; a one-block (A-B) design would not be.
- **The endpoint is soft.** Sleep-onset latency estimated from memory is noisy. A wearable improves it; a self-report does not.

---

## Why it matters

This is the queue's **first card on the light environment** — the timing of light exposure rather than a device, a field, or a material. Every prior health card tests an apparatus (Eeman circuit, orgone accumulator, pendulum, wheel) or a water treatment; **none tests the light a person's eyes actually receive in the first hour of the day.** It is also the queue's **first purely behavioral health card** — no apparatus, no purchase, no build.

And it is the queue's **first card whose core mechanism is mainstream-supported**. That is stated as a finding, not hidden: the value here is not that the claim is doubtful, it is that the **numbers are yours** — how quickly you actually fall asleep on a bright-morning week versus an ordinary one. The contested part of the source (the metabolic cascade) is explicitly out of scope.

## Replicability: `home`

- Build cost: **~$0** (a log; optionally a lux app or meter, ~$0–30).
- Safety: **none** — daylight and a notebook. Do not stare at the sun; ordinary outdoor light is the intervention. Anyone with a sleep disorder, or on sleep medication, should treat this as a log, not a treatment, and keep their clinician in the loop.
- Accessibility: four weeks, one row a night. Runs in any season, in any climate (a bright overcast day is still far brighter than indoors).

## Apparatus (Bill of Materials)

- A sleep log (paper or app); a pen.
- A phone timer/alarm.
- Optional: a lux meter or phone lux app; a wearable or sleep app.
- A pre-registration sheet.

## What a result means (and what it does not)

- A **pass** means: for your family, over four weeks, bright morning light shortened the time to fall asleep and steadied the wake time. That is a real, local, measured result — and a habit worth keeping.
- It does **not** mean the source's metabolic framework is correct, that light prevents disease, or that the effect would hold for anyone else. Those are out of scope.
- A **fail** means the light-timing lever did not move your sleep measurably. That is a complete result and earns the Skeptic's Star.
- The confounds to name in the report: unblinded; the intervention is bundled with going outside; n = 1; season drift; and a soft, partly self-reported endpoint.

## Cross-links

- **Dossier 012** (Eeman Sleep Quality) — the other sleep-endpoint card; that one tests an apparatus, this one tests a behavior.
- **Dossier 039** (Wave-Water Stress-Recovery) — the other card whose endpoint is a human physiological state.
- **Dossier 028** (Water Memory Imprint) / **058** (Form-Field Water-Structure) — the other health cards whose intervention is a *treatment applied to a person*.
- **Claim status record:** none — the light-entrainment claim is not a closed claim; it is live, mainstream physiology. The card tests a family's own response to it, not the claim's existence.
