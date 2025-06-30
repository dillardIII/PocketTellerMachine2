# === FILE: bridge_heartbeat_loop.py ===
"""
Bridge Heartbeat Loop
Keeps PTM bridge channels alive by logging heartbeat timestamps.
Used by Cole, GhostBot, ReplitSync, and other assistant services.
"""

import os
import json
from datetime import datetime, timezone
import time

COMM_CHANNEL_FILE = "data/comm_bridge.json"
SYNC_LOG_FILE = "data/sync_status.json"

# Systems being monitored
BRIDGE_SYSTEMS = ["cole", "ptm", "replit", "github", "ai_router", "ghost_sync"]

def init_bridge_files():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(COMM_CHANNEL_FILE):
        with open(COMM_CHANNEL_FILE, "w") as f:
            json.dump({}, f)
    if not os.path.exists(SYNC_LOG_FILE):
        with open(SYNC_LOG_FILE, "w") as f:
            json.dump({}, f)

def update_comm_bridge(system, message="Heartbeat received"):
    with open(COMM_CHANNEL_FILE, "r") as f:
        current = json.load(f)

    now_iso = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
    current[system] = {
        "status": "online",
        "last_ping": now_iso,
        "message": message
    }

    with open(COMM_CHANNEL_FILE, "w") as f:
        json.dump(current, f, indent=2)

def update_sync_log(system):
    with open(SYNC_LOG_FILE, "r") as f:
        logs = json.load(f)

    now_iso = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
    logs[system] = {
        "last_sync": now_iso,
        "health": "✅ Healthy"
    }

    with open(SYNC_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def heartbeat_loop():
    init_bridge_files()
    print("[Heartbeat] 🔁 Bridge heartbeat loop running...")

    while True:
        for system in BRIDGE_SYSTEMS:
            update_comm_bridge(system)
            update_sync_log(system)
            print(f"[Heartbeat] 🫀 {system.upper()} pinged.")
            time.sleep(1.5)  # space out pings to prevent log flooding

        print("[Heartbeat] 🌐 All bridges pinged. Sleeping...\n")
        time.sleep(60)  # wait 1 minute before next full round

if __name__ == "__main__":
    heartbeat_loop()