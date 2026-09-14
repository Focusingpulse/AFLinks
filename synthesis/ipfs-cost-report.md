# IPFS Pinning Pilot — Cost & Scale Report (Phase 4)

**Date:** 2026-09-09
**Scope:** 10 documents pinned to IPFS (CIDv1, raw-leaves), SHA-256 recorded.
**Manifest:** `synthesis/ipfs-manifest.json`

## What was pinned
5 flagship Open Lab docs + 5 death-certificate lineage docs (the ones worth
permanently anchoring — the LENR/wrong-turn corpus and the replicable claims).

## Cost findings
- **Pinning itself is free** — IPFS CIDs are content-addressed; `ipfs add`
  computes them locally at zero monetary cost. The data is ~1.4 KB total for
  the text layers (these are text previews, not the full PDFs).
- **The real cost is persistence, not pinning.** A local node's pins vanish
  when the machine dies. For permanent availability you need a remote pinning
  service:
  - **Pinata** (public IPFS pinning): ~$20/mo for 1,000 pins / 10GB. 10 docs
    would be pennies under a free tier.
  - **Filebase / web3.storage** (now Storacha): free tiers for small archives.
  - **Arweave** (permanent, one-time): ~$1-8 per document depending on size —
    true permanence, no recurring fee, but a real per-doc cost.
- **Sandbox node caveat:** this sandbox's node is ephemeral and offline
  (no swarm). The CIDs are valid and reproducible from the manifest, but the
  data is only "pinned" on a machine that won't outlive the session. The
  badges are honest about this — they certify the hash + CID, which is the
  anti-fragile part; a reader can re-add from the manifest.

## Scale decision (top-100)
- **Recommended:** do NOT pay for the top-100 yet. The value of the pilot is
  the mechanism + honest hashes, which cost nothing. When the Hub computer
  arrives (a persistent machine), run a node there and pin the top-100 for
  free — persistence without a service fee.
- **If Chris wants true permanence now:** Arweave the 10 pilot docs (~$10-80
  one-time) and display the Arweave tx link alongside the IPFS CID.
- **Skip Pinata** at this scale — the free-persistence route (Hub node) beats
  a recurring $20/mo for 100 docs.

## Bottom line
Mechanism built, honest badges live, cost ≈ $0. Persistence is the only real
expense and the Hub computer solves it for free. No service subscription
warranted at 10 or 100 docs.
