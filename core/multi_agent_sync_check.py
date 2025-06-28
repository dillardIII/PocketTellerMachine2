"""
Multi-Agent Sync Checker:
This module verifies that each assistant bot has synced properly
across the PTM network. It returns a report for monitoring
sync health, timestamps, and bot availability.
"""

import os
import json
from datetime import datetime, timezone
from cole_logger import log_event
from cole_brain import log_memory

# Resolve sync directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SYNC_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "sync"))
SYNC_THRESHOLD_SECONDS = 120  # 2 minutes

def load_sync_file(filename):
    path = os.path.join(SYNC_DIR, filename)
    if not os.path.exists(path):
        return {
            "agent": filename.replace(".json", ""),
            "status": "missing",
            "last_synced": None,
            "sync_health": "❌ File not found"
        }

    try:
        with open(path, "r") as f:
            data = json.load(f)
        return {
            "agent": filename.replace(".json", ""),
            "status": data.get("status", "unknown"),
            "last_synced": data.get("last_synced")
        }
    except Exception as e:
        return {
            "agent": filename.replace(".json", ""),
            "status": "error",
            "last_synced": None,
            "sync_health": f"❌ Error: {e}"
        }

def assess_sync_status(agent_data):
    now = datetime.now(timezone.utc)
    last_sync_str = agent_data.get("last_synced")

    if not last_sync_str:
        agent_data["sync_health"] = "❌ No sync timestamp"
        return agent_data

    try:
        last_sync_time = datetime.fromisoformat(last_sync_str.replace("Z", "+00:00"))
        delta_seconds = (now - last_sync_time).total_seconds()

        if delta_seconds <= SYNC_THRESHOLD_SECONDS:
            agent_data["sync_health"] = "✅ Healthy"
        else:
            agent_data["sync_health"] = f"⚠️ Delayed ({int(delta_seconds)}s ago)"
    except Exception as e:
        agent_data["sync_health"] = f"❌ Invalid timestamp: {e}"

    return agent_data

def run_multi_agent_sync_check():
    if not os.path.exists(SYNC_DIR):
        warning = {
            "agent": "ALL",
            "status": "missing",
            "last_synced": None,
            "sync_health": "❌ Sync directory not found"
        }
        log_event("SyncCheck", warning["sync_health"], "error")
        log_memory("sync_error", warning)
        return [warning]

    sync_files = [f for f in os.listdir(SYNC_DIR) if f.endswith(".json")]
    if not sync_files:
        warning = {
            "agent": "ALL",
            "status": "missing",
            "last_synced": None,
            "sync_health": "❌ No sync files found"
        }
        log_event("SyncCheck", warning["sync_health"], "error")
        log_memory("sync_error", warning)
        return [warning]

    report = []
    for filename in sync_files:
        agent_data = load_sync_file(filename)
        agent_data = assess_sync_status(agent_data)
        report.append(agent_data)
        log_event("SyncCheck", f"{agent_data['agent']} = {agent_data['sync_health']}", "info")
        log_memory("sync_check", agent_data)

    return report

# Manual test run
if __name__ == "__main__":
    result = run_multi_agent_sync_check()
    for entry in result:
        print(f"[{entry['agent']}] Status: {entry['status']} | Last Sync: {entry['last_synced']} | Health: {entry['sync_health']}")