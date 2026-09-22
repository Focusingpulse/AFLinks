---
name: Quest Card — MVP Vortex Motor (Open-Source Schauberger Water Vortex Generator)
description: Aetherforce-branded quest card testing the "MVP Vortex Motor" claim — that a water vortex in a resonant cavity can generate enough energy to light an LED (a negentropic / over-unity claim) — via an open-source <50€ home build with an energy-balance endpoint. Plumbing & Hot Water guild complement, water domain.
---

# ⚡ Aetherforce — Water

**Guild:** Aetherforce — Water (complements Plumbing & Hot Water)
**Quest Line:** ⚡ Aetherforce · Plumbing & Hot Water complement
**Tier:** sand
**Domain:** water (water vortex device — with an energy-generation claim)
**Status:** proposed
**Created:** 2026-09-21

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-21-vortex-motor-mvp` · authored_at `2026-09-21` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Water",
  desc: "Viktor Schauberger spent his life arguing that nature builds with implosion — the inward, cooling, ordering vortex — not explosion, and that a vortex of water holds energy we throw away. In November 2025 a Spanish engineer published an open-source build challenge that puts that claim on a workbench: for under 50 euros, using common materials, build a small water vortex in a resonant cavity and use it to light an LED. He published the plans, the materials list, and a step-by-step guide — and he was honest that it is a challenge, not a result. So here is the quest, and it is a good one precisely because the honest test is not 'does the LED light' — a little turbine spun by falling water will do that by ordinary means — but 'does the output beat the input.' You will measure the water's own power going in (flow rate, head) and the electrical power coming out, and you will find out for yourself whether the vortex is doing something thermodynamics says it can't, or whether it is a clever little water wheel. Either answer is worth having, and you will have measured energy in and energy out with your own hands. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "The Vortex Motor Energy Balance",
    "Obtain the open-source build doc (Zenodo DOI 10.5281/zenodo.17635970) and build the MVP Vortex Motor to its specification — cavity, rotor, turbine, circuit — photographing each stage. Then instrument it honestly: measure the energy GOING IN (if gravity-fed, flow rate in litres per minute and usable head in metres, so P_in = ρ·g·Q·h; if pumped, the pump's wall power with a plug-in meter) and the energy COMING OUT (voltage and current at the LED/load). Run at least 3 timed runs of 10+ minutes on different days, record every number, and compare. Measurable outcome: P_out > P_in in every run, by more than measurement uncertainty = a genuine anomaly worth reporting to the world; P_out ≤ P_in in every run = ordinary turbine generation and the over-unity claim is retired honestly. Note in your write-up that 'the LED lights' alone proves nothing — only the balance does.",
    ["Science", "Engineering", "Self-Reliance"],
    "🌀"
  ],
  source_doc: "translations/2026-09-11-vortex-motor-negentropic-propulsion-es.md — 'El Motor de Vórtice: Hacia una Tecnología de Propulsión Negentrópica Basada en la Dinámica de Implosión del Éter,' the companion theoretical paper (Zenodo 10.5281/zenodo.17626722, 2025-11-17, CC BY 4.0). Build doc: Zenodo 10.5281/zenodo.17635970 (external — see Honest Framing).",
  source_url: "https://www.aetherforce.energy",
  dossier: "living-library/synthesis/replication/2026-09-21-dossier-031-vortex-motor-mvp.md",
  pass_fail: "PASS: P_out > P_in in every run (≥ 3 runs, ≥ 10 min each, on different days), margin larger than combined measurement uncertainty — a genuine over-unity anomaly, report raw numbers and seek independent replication | FAIL: P_out ≤ P_in in every run — ordinary turbine generation; the over-unity claim is retired honestly (Skeptic's Star) | INCONCLUSIVE: fewer than 3 runs, input or output not measured, flow/head not recorded, or the device not built to the doc's specification",
  evidence: "Photos of the cavity, rotor, turbine, and circuit at each build stage; the materials list as actually purchased with costs; flow-rate and head measurements (or pump power draw) for each run; voltage and current at the load for each run; the raw run log (date, time, duration, input numbers, output numbers); a build-accuracy note recording how closely the doc's specification was followed"
}
```

---

## Source Documentation

- **Primary build source (external):** Zenodo DOI `10.5281/zenodo.17635970` — *"El Motor de Vórtice (MVP v1.0): Un Generador Negentrópico de Código Abierto para Encender un LED"* by Juan Miguel Rivero y Hornos Tverjanovich (Laboratorio de Sinergia Humano-IA), 2025-11-17, CC BY 4.0. Verified live 2026-09-21 via the DOI resolver (abstract retrieved). The abstract confirms: materials list < 50 €, step-by-step construction for cavity / rotor / turbine / circuit, a testing protocol with Basic / Intermediate / Advanced success levels, and a troubleshooting guide.
- **Archive source (theory companion):** `translations/2026-09-11-vortex-motor-negentropic-propulsion-es.md` — full ES→EN translation of the companion paper (Zenodo `10.5281/zenodo.17626722`). Describes the resonant-cavity architecture (ovoid / logarithmic-spiral geometry, centripetal vortex, applied EM resonance).
- **Scout finds:** `sources/2026-08-29-scout-b-es-fr-zh.md` §1 — flagged `practical_applicability: true, fields [buildable, reproducible]`, "Open-source engineering manifesto with step-by-step build instructions, materials list (<50€), validation metrics. Designed for community replication. Not a results report — a build challenge." · `sources/2026-09-07-scout-a-ja-zh-ar-es-ru-it.md` §8 — "complete plans … materials list, step-by-step construction for cavity/rotor/turbine/circuit, testing protocol (Basic/Intermediate/Advanced success levels), and troubleshooting guide."
- **Companion card (water vortex, merged):** `synthesis/quest-queue/2026-09-06-wasserwirbler.md` (Dossier 001) — the water-*quality* vortex claim; this card tests the water-*energy* claim from the same lineage.
- **Companion card (vortex energy, proposed):** `synthesis/quest-queue/2026-09-10-vortex-jet-turbine.md` (Dossier 008, Rocket complement).
- **Replication Dossier:** `synthesis/replication/2026-09-21-dossier-031-vortex-motor-mvp.md`
- **Aetherforce Reference:** search "Schauberger" / "vortex" / "implosion" / "water" on https://www.aetherforce.energy
- **Vault link:** https://focusingpulse.github.io/AFLinks

---

## Rubric Justification

- **Practical:** a named apparatus (a water vortex in a resonant cavity, driving a turbine and a small circuit) with a measurable outcome (an energy balance: `P_out` vs `P_in`).
- **Replicable:** home-scale — the author estimates **< 50 €** in common materials. No lab equipment; the instruments are a flow meter / measuring jug, a tape measure, a multimeter, and (if pumped) a plug-in power meter.
- **Relevant:** maps to the Village **water** survival domain and complements the **Plumbing & Hot Water** guild (the water-vortex home — Wasserwirbler, EZ water, Piccardi P).
- **Honest:** framed as a TEST of a self-published, unrefereed, over-unity claim, not an endorsement. The turbine confound is named up front; the author's own "it's a challenge, not a result" framing is quoted; a null is presented as the likely and equally valuable outcome.
- **Linked:** source doc (archive theory translation) + verified live build-doc DOI + dossier with protocol and pre-registered pass/fail + evidence protocol.

---

## Honest Framing

This is a test, not an endorsement. The MVP Vortex Motor is a **self-published Zenodo
deposit** by an author affiliated with a "Human-AI Synergy Laboratory." It is not
peer-reviewed, it has no independent replication, and its claim — a water vortex
producing net energy — is an **over-unity claim that contradicts the second law of
thermodynamics as ordinarily stated.** Treat it accordingly.

Two limitations are stated plainly rather than hidden:

1. **The build doc is not in the archive, and the engine could not read it.** Zenodo
   returns HTTP 403 to the sandbox, so the engine verified the record exists and read
   the author's abstract, but did not read the construction steps. This card therefore
   points the builder at the doc; it does not reproduce steps the engine has not read.
   The archive holds the companion *theoretical* paper, which describes the architecture
   but contains no build specs.
2. **The build includes a turbine, which is the central confound.** An LED lighting up
   can be ordinary mechanical generation. The card's endpoint is deliberately an
   **energy balance**, not "the LED lights," because only the balance can discriminate
   the claim from a clever water wheel.

The value of the card is that a family can build it cheaply, measure energy in and
energy out, and get their own honest answer — including the null. **If the LED lights
but `P_out ≤ P_in`, the correct sentence is "the vortex device generated electricity
by ordinary means," not "the vortex device works."**

---

## Status

**Proposed** — awaiting Chris approval before merge into Village quest data.
