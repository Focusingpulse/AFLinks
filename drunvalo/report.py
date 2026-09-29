#!/usr/bin/env python3
"""Drunvalo agent report script for AetherForce Links."""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

def main():
    parser = argparse.ArgumentParser(description="Report Drunvalo agent activity")
    parser.add_argument("--summary", required=True, help="Summary of the report")
    parser.add_argument("--status", required=True, choices=["ok", "error", "warning"], help="Status of the operation")
    parser.add_argument("--files", nargs="*", default=[], help="Files modified")
    parser.add_argument("--details", default="", help="Additional details")
    args = parser.parse_args()
    
    report = {
        "agent": "drunvalo",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "summary": args.summary,
        "status": args.status,
        "files_modified": args.files,
        "details": args.details
    }
    
    # Write report
    report_file = f"drunvalo/report-{datetime.now(timezone.utc).strftime('%Y-%m-%d-%H%M%S')}.json"
    os.makedirs("drunvalo", exist_ok=True)
    with open(report_file, "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"Report written to {report_file}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
