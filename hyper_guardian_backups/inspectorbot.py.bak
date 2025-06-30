# === FILE: inspectorbot.py ===

# 🕵️ InspectorBot – Phase 9 upgrade: full system coordinator for audit, reflex, sweep, and AI rebuild

import time
import json
from smart_file_auditor import run_audit
from ghostforge_core import build_missing_files
from reflex_engine import update_mood
from sweep_handler import sweep_system
from ghostforge_repair_watcher import process_repair_requests
from ghostforge_autobuilder import autobuild
from utils.logger import log_event

STATUS_FILE = "logs/inspectorbot_status.json"
HEARTBEAT_FILE = "logs/inspectorbot_heartbeat.json"

def log_status(state, details=None):
    status = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        "state": state,
        "details": details or {}
    }
    with open(STATUS_FILE, "w") as f:
        json.dump(status, f, indent=2)
    log_event("InspectorBot", {"status": state, "details": details})

def write_heartbeat():
    with open(HEARTBEAT_FILE, "w") as f:
        json.dump({"timestamp": time.time()}, f)

def phase9_protocol():
    print("[InspectorBot] 🔍 Starting PHASE 9 sweep...")
    write_heartbeat()

    # === Sweep files and quarantine anything bad
    sweep_system()

    # === Audit system and log issues
    audit = run_audit()

    # === Rebuild missing or outdated files
    build_missing_files()

    # === React emotionally
    update_mood()

    # === Process pending repairs + queue rebuilds
    process_repair_requests()

    # === Rebuild final queue files
    autobuild()

    write_heartbeat()
    log_status("phase9_complete", {"issues_found": audit["missing"] + audit["corrupted"] + audit["outdated"]})
    print("[InspectorBot] ✅ Full PHASE 9 scan complete.")

if __name__ == "__main__":
    phase9_protocol()