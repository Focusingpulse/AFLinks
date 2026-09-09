#!/usr/bin/env python3
"""build_labs.py — Peer-Lab build-time validator.

Validates labs/labs.json and enforces the 3x2 rule by build, not by hand:

  (a) Every equipment/variable id referenced by a protocol exists in its
      registry (cross-references must resolve).
  (b) Enforces the 3x2 rule: a protocol's status displays replication_verified
      ONLY when its replication log holds >=3 entries with verdict
      == "replicated" AND the number of distinct "hand" values among those
      entries is >=2. Otherwise it is "in progress (N/3 replications, M hands)".
  (c) Prints a summary of protocols / equipment / variables / replication log
      and each protocol's computed badge state.

Exit code 0 on pass, 1 on any validation failure (see --fail-fast).

Usage:
    python3 build_labs.py [path/to/labs.json]
"""

import json
import os
import sys

VERDICTS = {"replicated", "partial", "failed", "inconclusive"}


def load(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def badge_state(protocol, log):
    """Compute the 3x2 badge state for one protocol.

    Returns (verified: bool, replicated_count: int, hands_count: int).
    """
    repls = [
        r for r in log
        if r.get("protocol_id") == protocol.get("id") and r.get("verdict") == "replicated"
    ]
    hands = {r.get("hand") for r in repls if r.get("hand")}
    replicated = len(repls)
    verified = replicated >= 3 and len(hands) >= 2
    return verified, replicated, len(hands)


def validate(data, path):
    errors = []
    warnings = []

    schema = data.get("schema")
    if schema != "peer-lab-v1":
        warnings.append(f"schema is {schema!r} (expected 'peer-lab-v1')")

    protocols = data.get("protocols", [])
    equipment = data.get("equipment", [])
    variables = data.get("variables", [])
    log = data.get("replication_log", [])

    equipment_ids = {e.get("id") for e in equipment}
    variable_ids = {v.get("id") for v in variables}
    protocol_ids = {p.get("id") for p in protocols}
    log_ids = {r.get("id") for r in log}

    # Uniqueness
    if len(equipment_ids) != len(equipment):
        errors.append("duplicate equipment id(s)")
    if len(variable_ids) != len(variables):
        errors.append("duplicate variable id(s)")
    if len(protocol_ids) != len(protocols):
        errors.append("duplicate protocol id(s)")
    if len(log_ids) != len(log):
        errors.append("duplicate replication_log id(s)")

    # (a) Every equipment/variable reference resolves; every protocol exists
    for p in protocols:
        pid = p.get("id")
        for eid in p.get("equipment", []):
            if eid not in equipment_ids:
                errors.append(f"protocol {pid} references unknown equipment {eid}")
        for vid in p.get("variables", []):
            if vid not in variable_ids:
                errors.append(f"protocol {pid} references unknown variable {vid}")
        for rid in p.get("replications", []):
            if rid not in log_ids:
                errors.append(f"protocol {pid} references unknown replication {rid}")
        if not p.get("steps"):
            warnings.append(f"protocol {pid} has no steps")

    # Every replication log entry references a known protocol; data_file present
    for r in log:
        if r.get("protocol_id") not in protocol_ids:
            errors.append(f"replication {r.get('id')} references unknown protocol {r.get('protocol_id')}")
        verdict = r.get("verdict")
        if verdict not in VERDICTS:
            errors.append(f"replication {r.get('id')} has invalid verdict {verdict!r} (must be one of {sorted(VERDICTS)})")
        if not r.get("hand"):
            warnings.append(f"replication {r.get('id')} has no hand recorded")
        if not r.get("data_file"):
            warnings.append(f"replication {r.get('id')} has no data_file")

    # Also check equipment/variables substitutes/other refs that should resolve
    for e in equipment:
        for sub in e.get("substitutes", []):
            if "(" in sub:  # free-text substitute note like "equipment://x (control only)"
                sub_id = sub.split("(")[0].strip()
            else:
                sub_id = sub
            if sub_id.startswith("equipment://") and sub_id not in equipment_ids:
                errors.append(f"equipment {e.get('id')} substitute references unknown {sub_id}")

    # (b) Enforce & report the 3x2 rule
    states = {}
    for p in protocols:
        states[p.get("id")] = badge_state(p, log)

    print(f"\nValidating {path}")
    print(f"  schema        : {schema}")
    print(f"  protocols     : {len(protocols)}")
    print(f"  equipment     : {len(equipment)}")
    print(f"  variables     : {len(variables)}")
    print(f"  replication   : {len(log)} log entries")

    print("\n  3x2 badge states (>=3 'replicated' AND >=2 distinct hands):")
    for p in protocols:
        verified, rep, hands = states[p.get("id")]
        if verified:
            mark = "REPLICATION_VERIFIED ✅"
        else:
            mark = f"in progress ({rep}/3 replications, {hands} hands)"
        print(f"    {p.get('id'):40s} -> {mark}")

    if warnings:
        print("\n  warnings:")
        for w in warnings:
            print(f"    - {w}")
    if errors:
        print("\n  ERRORS:")
        for e in errors:
            print(f"    - {e}")

    return errors, warnings, states


def self_test():
    """Prove the 3x2 rule logic works, independent of the seed file."""
    log = [
        {"id": "a", "protocol_id": "p", "hand": "hand1", "verdict": "replicated"},
        {"id": "b", "protocol_id": "p", "hand": "hand2", "verdict": "replicated"},
        {"id": "c", "protocol_id": "p", "hand": "hand1", "verdict": "replicated"},
    ]
    proto = {"id": "p"}
    verified, rep, hands = badge_state(proto, log)
    assert verified is True and rep == 3 and hands == 2, "expected 3x2 pass"
    print("    self-test 1 PASS: 3 replications by 2 hands -> replication_verified")

    # only 1 distinct hand -> must NOT verify
    log2 = [
        {"id": "a", "protocol_id": "p", "hand": "hand1", "verdict": "replicated"},
        {"id": "b", "protocol_id": "p", "hand": "hand1", "verdict": "replicated"},
        {"id": "c", "protocol_id": "p", "hand": "hand1", "verdict": "replicated"},
    ]
    verified, rep, hands = badge_state(proto, log2)
    assert verified is False and rep == 3 and hands == 1, "expected 3x2 fail (1 hand)"
    print("    self-test 2 PASS: 3 replications by 1 hand -> NOT verified")

    # only 2 replications, 2 hands -> must NOT verify
    log3 = log[:2]
    verified, rep, hands = badge_state(proto, log3)
    assert verified is False and rep == 2 and hands == 2, "expected 3x2 fail (2 repls)"
    print("    self-test 3 PASS: 2 replications by 2 hands -> NOT verified")

    # non-replicated verdicts never count
    log4 = [
        {"id": "a", "protocol_id": "p", "hand": "h1", "verdict": "partial"},
        {"id": "b", "protocol_id": "p", "hand": "h2", "verdict": "inconclusive"},
        {"id": "c", "protocol_id": "p", "hand": "h3", "verdict": "failed"},
    ]
    verified, rep, hands = badge_state(proto, log4)
    assert verified is False and rep == 0 and hands == 0, "expected 0 replicated"
    print("    self-test 4 PASS: partial/inconclusive/failed never count")


def main(argv):
    path = argv[0] if argv else os.path.join("labs", "labs.json")
    if not os.path.exists(path):
        print(f"cannot find {path} — run from the AFLinks repo root", file=sys.stderr)
        return 1

    data = load(path)
    errors, warnings, _states = validate(data, path)

    print("\n  running 3x2 rule self-test...")
    self_test()

    if errors:
        print(f"\n  FAIL: {len(errors)} validation error(s) present. Fix before shipping.")
        return 1
    print("\n  PASS: labs.json is internally consistent; 3x2 rule enforced at build.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
