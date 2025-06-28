# === FILE: bots/inspector_bot.py ===

# 🕵️ InspectorBot – The PTM watchdog that audits files, reports threats, and kicks GhostForge if needed.

import os
import json
import time
from smart_file_auditor import run_audit
from ghostforge_repair_watcher import process_repair_requests

INSPECTOR_STATUS_FILE = "logs/inspectorbot_status.json"
INSPECTOR_HEARTBEAT_FILE = "logs/inspectorbot_heartbeat.json"

def log_status(status, details=None):
    """Log current status of InspectorBot."""
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        "status": status,
        "details": details or {}
    }

    os.makedirs(os.path.dirname(INSPECTOR_STATUS_FILE), exist_ok=True)

    try:
        with open(INSPECTOR_STATUS_FILE, "w") as f:
            json.dump(entry, f, indent=2)
        print(f"[InspectorBot] 🗂️ Status updated: {status}")
    except Exception as e:
        print(f"[InspectorBot] ❌ Failed to log status: {e}")

def write_heartbeat():
    """Track that InspectorBot is alive and ticking."""
    beat = {
        "timestamp": time.time()
    }

    os.makedirs(os.path.dirname(INSPECTOR_HEARTBEAT_FILE), exist_ok=True)

    try:
        with open(INSPECTOR_HEARTBEAT_FILE, "w") as f:
            json.dump(beat, f)
        print("[InspectorBot] ❤️ Heartbeat sent.")
    except Exception as e:
        print(f"[InspectorBot] ❌ Heartbeat failed: {e}")

def full_system_inspect():
    """Trigger a full audit and repair sweep."""
    log_status("audit_start")
    write_heartbeat()

    results = run_audit()

    issues = results["missing"] + results["corrupted"] + results["outdated"]
    if issues:
        log_status("issues_found", {"problem_files": issues})
        process_repair_requests()
    else:
        log_status("all_clear")

    write_heartbeat()

# === CLI Runner ===
if __name__ == "__main__":
    print("[InspectorBot] 🧠 Scanning PTM system...")
    full_system_inspect()
    print("[InspectorBot] ✅ Done.")