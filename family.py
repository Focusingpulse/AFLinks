#!/usr/bin/env python3
"""
Aetherforce Living Library — Family Coordination Ledger
=========================================================

The family ledger coordinates work across the agent fleet.
Each agent checks in before starting work (budget gate) and after finishing (delta check-in).

Usage:
    python family.py checkin <agent_name> <role> <task_description>
    python family.py checkout <agent_name> <task_description> <delta_summary>
    python family.py propose_upgrade <agent_name> <target_description> <rationale>
    python family.py status
    python family.py log

Ledger file: family_ledger.json (created automatically next to this script)
"""

import json
import os
import sys
from datetime import datetime, timezone

LEDGER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "family_ledger.json")

AGENTS = {
    "synthesist": {"role": "analysis", "description": "Cross-references, synthesis documents, research briefs"},
    "scout": {"role": "collection", "description": "Hunts and acquires new sources for the library"},
    "forge": {"role": "translation", "description": "Translates sources into English"},
    "curator": {"role": "quality", "description": "Reviews translations, maintains taxonomy, flags errors"},
    "translation-qc": {"role": "quality", "description": "Quality-checks recent translations for accuracy, completeness, and formatting"},
    "village-growth": {"role": "growth", "description": "Grows the Village RPG with new quests, learning resources, and permies SKIP/PEP updates"},
    "village-audit": {"role": "quality", "description": "Audits Village RPG data integrity, translations, and quest structure"},
    "archivist": {"role": "database", "description": "Refreshes person-index, research-index, and library feed from latest archive and translations"},
    # Agents can be added as the fleet grows
}

def load_ledger():
    if os.path.exists(LEDGER_PATH):
        with open(LEDGER_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "version": "0.1.0",
        "created": datetime.now(timezone.utc).isoformat(),
        "members": {},
        "checkins": [],
        "checkouts": [],
        "upgrade_bank": [],
    }

def save_ledger(ledger):
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)

def cmd_checkin(agent_name, role, task):
    """Budget gate — check in before starting work."""
    ledger = load_ledger()
    now = datetime.now(timezone.utc).isoformat()

    # Register member if new
    if agent_name not in ledger["members"]:
        ledger["members"][agent_name] = {
            "role": role,
            "joined": now,
            "total_checkins": 0,
            "total_checkouts": 0,
        }
        print(f"[family] New member registered: {agent_name} ({role})")

    entry = {
        "agent": agent_name,
        "role": role,
        "task": task,
        "timestamp": now,
    }
    ledger["checkins"].append(entry)
    ledger["members"][agent_name]["total_checkins"] += 1
    save_ledger(ledger)
    print(f"[family] Check-in recorded: {agent_name} — {task}")

def cmd_checkout(agent_name, task, delta):
    """Delta check-in — report what was accomplished."""
    ledger = load_ledger()
    now = datetime.now(timezone.utc).isoformat()

    entry = {
        "agent": agent_name,
        "task": task,
        "delta": delta,
        "timestamp": now,
    }
    ledger["checkouts"].append(entry)
    if agent_name in ledger["members"]:
        ledger["members"][agent_name]["total_checkouts"] += 1
    save_ledger(ledger)
    print(f"[family] Check-out recorded: {agent_name} — {delta[:80]}...")

def cmd_propose_upgrade(agent_name, target, rationale):
    """Propose a new hunt target for the Scout fleet."""
    ledger = load_ledger()
    now = datetime.now(timezone.utc).isoformat()

    entry = {
        "id": f"upgrade-{len(ledger['upgrade_bank']) + 1:03d}",
        "proposed_by": agent_name,
        "target": target,
        "rationale": rationale,
        "status": "proposed",
        "timestamp": now,
    }
    ledger["upgrade_bank"].append(entry)
    save_ledger(ledger)
    print(f"[family] Upgrade proposed: {entry['id']} — {target}")

def cmd_status():
    """Show current fleet status."""
    ledger = load_ledger()
    print("=== Aetherforce Living Library — Family Ledger ===")
    print(f"Version: {ledger['version']}")
    print(f"Created: {ledger['created']}")
    print(f"\nMembers ({len(ledger['members'])}):")
    for name, info in ledger["members"].items():
        print(f"  {name} ({info['role']}) — {info['total_checkins']} check-ins, {info['total_checkouts']} check-outs")
    print(f"\nRecent check-ins ({len(ledger['checkins'])}):")
    for c in ledger["checkins"][-5:]:
        print(f"  [{c['timestamp'][:19]}] {c['agent']}: {c['task']}")
    print(f"\nRecent check-outs ({len(ledger['checkouts'])}):")
    for c in ledger["checkouts"][-5:]:
        print(f"  [{c['timestamp'][:19]}] {c['agent']}: {c['delta'][:80]}")
    print(f"\nUpgrade bank ({len(ledger['upgrade_bank'])}):")
    for u in ledger["upgrade_bank"]:
        print(f"  {u['id']} [{u['status']}] {u['target']} — by {u['proposed_by']}")

def cmd_log():
    """Show full log."""
    ledger = load_ledger()
    print(json.dumps(ledger, indent=2, ensure_ascii=False))

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == "checkin":
        if len(sys.argv) < 5:
            print("Usage: python family.py checkin <agent_name> <role> <task_description>")
            return
        cmd_checkin(sys.argv[2], sys.argv[3], sys.argv[4])

    elif cmd == "checkout":
        if len(sys.argv) < 5:
            print("Usage: python family.py checkout <agent_name> <task_description> <delta_summary>")
            return
        cmd_checkout(sys.argv[2], sys.argv[3], sys.argv[4])

    elif cmd == "propose_upgrade":
        if len(sys.argv) < 5:
            print("Usage: python family.py propose_upgrade <agent_name> <target_description> <rationale>")
            return
        cmd_propose_upgrade(sys.argv[2], sys.argv[3], sys.argv[4])

    elif cmd == "status":
        cmd_status()

    elif cmd == "log":
        cmd_log()

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)

if __name__ == "__main__":
    main()
