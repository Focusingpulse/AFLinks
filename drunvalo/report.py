#!/usr/bin/env python3
"""
Report script for AetherForce translation QC cron runs.
Generates a summary of the QC pass and pushes to the AFLinks repo.
"""

import argparse
import json
import os
import subprocess
from datetime import datetime, timezone

def main():
    parser = argparse.ArgumentParser(description="Report translation QC results")
    parser.add_argument("--summary", required=True, help="Summary of the QC pass")
    parser.add_argument("--status", required=True, choices=["ok", "warning", "error"], help="Status of the QC pass")
    parser.add_argument("--files", required=True, help="Comma-separated list of files checked")
    parser.add_argument("--issues", default="", help="Issues found and fixed")
    args = parser.parse_args()

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent": "Drunvalo",
        "cron": "aetherforce-translation-qc",
        "summary": args.summary,
        "status": args.status,
        "files_checked": args.files.split(",") if args.files else [],
        "issues_found_fixed": args.issues.split("|") if args.issues else [],
    }

    # Write report to stdout
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
