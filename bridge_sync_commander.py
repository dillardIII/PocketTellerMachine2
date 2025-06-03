# === FILE: bridge_sync_commander.py ===
# Logs sync events and routes bridge status signals to assigned handlers

import json
import os
from datetime import datetime
from bridge_status_scanner import read_bridge_status
from repair_team_commander import trigger_repair_ops

# === File Paths ===
BRIDGE_LOG_FILE = "logs/bridge_sync_log.json"
SYNC_CACHE = "bridge_sync_cache.json"
os.makedirs("logs", exist_ok=True)

# === Logging System ===
def log_bridge_event(event_type, detail):
    """
    Records a timestamped sync event to the bridge log.
    """
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event_type,
        "detail": detail
    }

    # Load existing log
    if os.path.exists(BRIDGE_LOG_FILE):
        with open(BRIDGE_LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    else:
        logs = []

    logs.append(log_entry)
    logs = logs[-200:]  # Keep last 200 entries only

    with open(BRIDGE_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    print(f"[BridgeSync] 📘 Logged {event_type}: {detail}")

# === Sync Snapshot System ===
def get_cached_sync():
    if os.path.exists(SYNC_CACHE):
        try:
            with open(SYNC_CACHE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def update_cached_sync(sync_data):
    with open(SYNC_CACHE, "w") as f:
        json.dump(sync_data, f, indent=2)

# === Core Watchdog Dispatcher ===
def check_bridge_and_dispatch():
    """
    Compares latest bridge sync stats to previous snapshot.
    If failure count rises, trigger repair bots.
    """
    current_sync = read_bridge_status()
    last_sync = get_cached_sync()

    if current_sync.get("status") != "ok":
        print("[SyncCommander] ⚠️ Sync file unreadable.")
        return

    if current_sync.get("fail_count", 0) > last_sync.get("fail_count", 0):
        print("[SyncCommander] 🚨 Sync error spike detected.")
        trigger_repair_ops(reason="bridge_sync_failures")
        log_bridge_event("sync_error_spike", "Repair triggered due to sync error increase")

    update_cached_sync(current_sync)
    print(f"[SyncCommander] ✅ Bridge sync check completed at {datetime.utcnow().isoformat()}")
    log_bridge_event("sync_check", "Bridge sync reviewed")

# === Manual Entry ===
if __name__ == "__main__":
    check_bridge_and_dispatch()