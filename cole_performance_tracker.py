# === FILE: cole_performance_tracker.py ===
# Tracks Cole’s decision results AND activates REPL AI to inspect all autonomy files

import json
import os
from datetime import datetime

PERFORMANCE_LOG_PATH = "data/cole_performance_log.json"

# 🔐 Master Autonomy Status File
AUTONOMY_STATUS_REPORT = "data/autonomy_repl_check.json"

def log_performance(event_type, outcome, notes=""):
    """
    Logs Cole’s decisions, then triggers a full REPL AI check of all system files.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "outcome": outcome,
        "notes": notes
    }

    if not os.path.exists(PERFORMANCE_LOG_PATH):
        with open(PERFORMANCE_LOG_PATH, "w") as f:
            json.dump([entry], f, indent=2)
    else:
        with open(PERFORMANCE_LOG_PATH, "r+") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=2)

    print(f"[Performance Tracker] 📝 Logged: {event_type} → {outcome}")

    # 🔍 NEW: Trigger full audit of files via REPL AI
    initiate_repl_file_integrity_audit()

def initiate_repl_file_integrity_audit():
    """
    Sends REPL AI instructions to review all core autonomy files.
    Checks for:
    - Syntax errors
    - Logic breaks
    - Unfinished or partial files
    - Missing modules
    - Autonomy status across the system
    """
    print("[REPL AI Watchdog] ⚠️ Verifying all autonomy files...")

    audit_report = {
        "timestamp": datetime.utcnow().isoformat(),
        "status": "pending",
        "checks": [
            "Syntax validation",
            "Dependency linkage",
            "Loop integrity",
            "Partial file scan",
            "Autonomy readiness"
        ],
        "ai_orders": [
            "✅ Check all code written by lead dev",
            "✅ Audit all autonomy-related logic",
            "✅ Detect and flag bad imports, broken calls, or unfinished logic",
            "✅ Determine if system can self-govern without user input",
            "✅ Report if autonomy is possible: TRUE or FALSE"
        ]
    }

    with open(AUTONOMY_STATUS_REPORT, "w") as f:
        json.dump(audit_report, f, indent=2)

    print("[REPL AI Watchdog] 🧠 Orders delivered to REPL AI. Awaiting report...")

def get_recent_results(limit=10):
    """
    Retrieves Cole’s last actions for performance grading.
    """
    if not os.path.exists(PERFORMANCE_LOG_PATH):
        return []

    with open(PERFORMANCE_LOG_PATH, "r") as f:
        data = json.load(f)
        return data[-limit:]