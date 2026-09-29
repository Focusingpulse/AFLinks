---
name: Pendulum Water-Quality Discrimination Test
description: "The queue's first card that scores dowsing against a CHEMICAL ground truth rather than a hidden physical location, and its first whose comparator is a lab-equivalent assay. A Dutch water-sector trade journal says radiesthesia 'reproducibly' determines water quality and flags pharmaceutical/toxic load; no protocol, no n, no blinding are reported. Eight jars, four with a known substance dissolved in them, four plain — call them blind. Water domain, under $60, Homesteading mirror (Self-Reliance complement)."
---

# ⚡ Aetherforce — Self-Reliance

**Guild:** Aetherforce — Self-Reliance
**Quest Line:** ⚡ Aetherforce · Homesteading complement
**Tier:** sand
**Domain:** water (drinking-water quality — can a person detect what is dissolved in water without an instrument?)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-27-pendulum-water-quality` · authored_at `2026-09-27` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Self-Reliance",
  desc: "The Dutch water sector's own trade magazine carries an article on radiesthesia as an operational technique — dowsing rods to find mains, and a pendulum that 'reproducibly' determines the quality of drinking and waste water and flags pharmaceutical and toxic load after purification. No protocol, no number of tests, and no blinding are reported. That word is the whole claim, and nobody has ever turned it into a number. So do it in your kitchen. One batch of water, eight identical jars: four get a known substance dissolved in them (salt, sugar, vinegar, a few drops of bleach), four get nothing. A referee codes them and seals the key. You call each jar plain or treated, blind, and rank them by how much is dissolved. A TDS meter and chlorine strips confirm the jars really differ — and if they can't, the run is void, because there is nothing to tell apart. Three sessions, twenty-four calls, scored against a 50% coin flip. Either you have found something the water utilities should be told about, or you have learned to reach for the meter instead of the pendulum before you trust your own well. Both are worth the afternoon. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Pendulum Water-Quality Discrimination Test",
    "First, find your own noise floor: have the referee hand you one jar of plain water ten times in a row, blind, and record your rating each time. If your readings vary more within one sample than you expect between samples, the test cannot work and you should say so. Then the referee fills eight identical opaque jars from one batch of water, adds salt to one, sugar to one, vinegar to one and a few drops of unscented bleach to one, leaves four plain, codes them, and seals the key. The referee verifies with a TDS meter, chlorine strips and pH strips that the treated jars really differ from the plain ones, and writes down the true order of dissolved load. You then call each jar PLAIN or TREATED, blind, and rank all eight from lowest to highest dissolved content, writing every call down before the key is opened. Repeat with freshly prepared and freshly coded jars on three separate days. Measurable outcome: pooled blind plain/treated hits out of 24 against a 50% chance baseline, and the rank correlation between your ordering and the TDS meter's. PASS is 18 of 24 or better with a rank correlation of 0.6 or more. Chance-level is a complete result, not a wasted run.",
    ["Science", "Measurement", "Water"],
    "💧"
  ],
  source_doc: "sources/2026-09-27-scout-b-langs-2.md#find-7 (H2O Water Netwerk, 'Water wichelen en radiësthesie', Frank Silvis, 2016 — the Dutch water-sector trade journal carrying radiesthesia as an operational technique; scout flag: conceptual, testable; also mirrored at the Wageningen UR repository, edepot.wur.nl/401827)",
  source_url: "https://www.h2owaternetwerk.nl/vakartikelen/water-wichelen-en-radiesthesie",
  dossier: "living-library/synthesis/replication/2026-09-27-dossier-048-pendulum-water-quality.md",
  pass_fail: "PASS: pooled blind plain/treated hits >= 18 of 24 (binomial p about 0.011 one-tailed, chance 0.5) AND pooled Spearman rank correlation with the TDS-meter order >= 0.6 - the coarse water-quality claim survives a blind test with an objective comparator, and justifies a harder trace-level follow-up. FAIL: pooled hits within chance (9-15 of 24, p > 0.05) and rank correlation near 0 - no detectable ability to distinguish dissolved content at home scale; a complete result (Skeptic's Star). This refutes the COARSE version only and does not refute trace detection. INCONCLUSIVE: you cannot produce a stable reading even on a known positive (distilled versus heavily salted water, key open) - the blind arms are then uninformative, NOT a refutation; fewer than 3 sessions; your within-sample scatter exceeds the between-sample spread; the referee saw your calls before unsealing. VOID: the TDS meter and strips cannot separate the treated jars from the plain ones (the samples do not differ); the key was opened before the calls were written; the jars were visibly or olfactorily different (fill level, condensation, smell); you were told anything about the contents. ARTIFACT: your calls track a smell or a visible cue rather than the pendulum; your calls track jar order (position bias); the result disappears when a second, fresh operator runs it.",
  evidence: "Photo of the bench (jars, pendulum or rods, TDS meter, strips) so others can rebuild it + the pre-registration sheet (trial counts, thresholds, chance model, scoring rule, key-holder) + the sealed key photographed sealed, then photographed opened only after the calls were written + the TDS, chlorine and pH readings for every jar + the true order derived from the TDS readings + your calls and ranks for every jar, every session, timestamped before unblinding + the ten-reading within-sample scatter table + the control operator's results if run, reported separately + the full tally with the binomial calculation shown + the void/artifact checks reported whether or not they void the run + the three sessions dated"
}
```

---

## Source Documentation

- **Primary (the archive find):** `living-library/sources/2026-09-27-scout-b-langs-2.md`, **find 7** — *H2O Water Netwerk, "Water wichelen en radiësthesie"* (Frank Silvis, 2016), https://www.h2owaternetwerk.nl/vakartikelen/water-wichelen-en-radiesthesie — Dutch, Netherlands (Dutch water sector), work type review/trade-technical. Scout flag: `Practical Applicability: flag — fields: conceptual, testable; note: the water-quality-by-pendulum claim is testable against standard assays — a genuine T2 candidate with a defined professional context`. Scout's rarity note: *"A water-utilities trade journal publishing radiesthesia as an operational technique"* — locating mains with dowsing rods, *"reproducibly"* determining the energetic quality of drinking and waste water, and indicating pharmaceutical/toxic load after purification steps. Verification: full article retrieved, plus the Wageningen UR depot mirror (edepot.wur.nl/401827).
- **The claim in the source's own terms:** radiesthesia is presented as an **operational** method used in the Dutch water sector — dowsing rods for locating mains, and a pendulum for judging water quality and flagging contamination after purification. The word *"reproducibly"* is the source's assertion; **no protocol, no sample size, no blinding and no statistics are reported**.
- **What the archive does not hold:** a grep across `living-library/synthesis/quest-queue/` for water-quality-by-dowsing returns nothing. Every dowsing card in the queue tests a **spatial location** — 005 (blind geopathic zone mapping), 029 (psi-track dowsing), 035 (blind water-line location), 044 (plan-reading location). **None tests a property of the water itself, and none has a chemical comparator.** That absence is why this card exists.
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-27-dossier-048-pendulum-water-quality.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "radiesthesia", "dowsing", "water quality", "pendulum"
- **Aetherforce Reference:** Search "radiesthesia", "dowsing", or "water quality" on https://www.aetherforce.energy
- **Related cards:** 035 (Blind Water-Line Location Test — the queue's other blind water-dowsing card; that one asks *where*, this one asks *what*), 029 (Psi-Track Dowsing — dowsing against a hidden track), 044 (Plan-Reading Location Test — dowsing from a representation), 009 (EZ Water Exclusion Zone — a water *structure* measurement), 022 (Qi-Water Conductivity — a water property against a claimed influence)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (eight identical coded jars, a pendulum or rods, a TDS meter, chlorine and pH strips) with a named procedure (session-0 noise floor → referee prepares and codes → blind plain/treated calls plus a full ranking → three independent sessions) and a measurable outcome (**pooled blind hits out of 24 against a 50 % chance baseline, and the Spearman rank correlation against the TDS-meter order**). Not pure theory. |
| **Replicable** | YES — Home, sand: **under $60** (pendulum ~$0–15, eight jars ~$10, TDS meter ~$15, strips ~$15, kitchen additions). No hazard beyond a few drops of bleach in a labelled jar that is never drunk. One afternoon to prepare, three short sessions. |
| **Relevant** | YES — Water domain, squarely, and the most directly self-reliance-relevant question in the field: **can we know our drinking water is safe without a lab?** It is also the queue's **first card that scores dowsing against a chemical ground truth** rather than a hidden physical location, and its **first whose comparator is a lab-equivalent assay**. |
| **Honest** | YES — the claim is framed as a claim and the card is a test, not an endorsement. Four things are stated in advance: the source is a **trade journal, not a study**, and *"reproducibly"* is the claim and not a finding; a home test reaches only the **coarse** version, so **a FAIL refutes the coarse claim and not trace detection, and a PASS on the coarse version does not validate trace detection either**; if the reference instrument cannot separate the jars the run is **VOID** because there is nothing to discriminate; and the **expected outcome is FAIL**, which is a complete result. |
| **Linked** | YES — a scout find, the article URL, the Wageningen UR mirror, a pre-registered replication dossier, and cross-links to five related cards. |

**Mirror choice, stated:** the card's question is *"can a homestead know its own water is safe?"* — a self-reliance question, so **Homesteading** ("Self-reliance / off-grid", 2 cards) is the complement, and the family label is `Aetherforce — Self-Reliance`. **Plumbing & Hot Water** (4 cards) was the closest alternative and was considered seriously, because drinking water is literally that guild's subject; it was not chosen because its four cards (Wasserwirbler, EZ water, Piccardi P, MVP Vortex Motor) are all water **treatment** cards, and the spec's rule is to fill the emptier mirror. **Community** (4 cards) was rejected — the claim's professional context is a utility sector, but the test is a household one. **Natural Medicine** (7 cards) was rejected as full.

---

## The honest framing (the spine of the card)

**A claim that names no protocol and no n is a claim about a word, not a phenomenon.** The Dutch article says radiesthesia determines water quality *"reproducibly"*. Reproducibly by whom, how many times, scored how, blinded against what? None of it is reported — because it is a trade-press article, not a study, and it is not obliged to report it. The card's whole product is the conversion of that word into a number a family can check.

**This is the first dowsing card in the queue whose ground truth is chemistry.** Every dowsing card the library already holds asks *"where is it?"* — a buried line, a geopathic zone, a track, a room on a plan — and scores against a hidden physical layout. This one asks *"what is in it?"* and scores against a **known concentration**, with a second, independent instrument (the TDS meter) confirming that the samples really differ. That is a stronger comparator than any previous dowsing card has had, and it is the reason the claim earns a card at all.

**The home test reaches only the coarse version, and the card says so in both directions.** The source's strongest form is *trace* detection — pharmaceuticals and toxins at microgram or nanogram per litre after purification. A kitchen cannot make or verify that. So: **a FAIL retires the coarse claim only and leaves trace detection untouched; a PASS on the coarse version does not validate trace detection either.** A card that let either sentence stand alone would be dishonest in the direction that flatters whoever is reading.

**The reference instrument is the gate, not the scoreboard.** If the TDS meter and strips cannot separate the treated jars from the plain ones, the run is **VOID** — a discrimination test on samples that do not differ measures nothing, and reporting it as a null would be a manufactured false negative. *Instrument the denominator, not just the outcome.*

**The expected outcome is FAIL, and that is the point.** A chance-level score is a complete result (Skeptic's Star). It would be the first blind test of a claim the archive holds only as a trade-press assertion, and it would tell a family plainly: for water quality, reach for the meter, not the pendulum. A PASS would be genuinely surprising — surprising enough to justify a harder, trace-level follow-up — and the card says so.

**One-sidedness, written down before the run:** this test is informative on a PASS and only *partially* informative on a FAIL. A FAIL cannot distinguish "the pendulum does not work" from "this operator is not sensitive" — which is why session 0 exists and why a failure to produce a stable reading even on a known positive is **INCONCLUSIVE, not a refutation**.

**Under-promise:** a weak card is worse than none. This card's claim is modest by design — grams per litre, in a kitchen, three sessions — and its most likely verdict is that the word *"reproducibly"* does not survive contact with a coin flip.
