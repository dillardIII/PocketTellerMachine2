# === FILE: bridge_heartbeat_sync.py ===
# 🌉 Bridge Heartbeat Sync – Ensures live communication across AI teams

import time
import json
from datetime import datetime

BRIDGE_LOG_PATH = "logs/bridge_sync_log.json"

def log_heartbeat(source, destination):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "destination": destination,
        "status": "heartbeat"
    }

    try:
        with open(BRIDGE_LOG_PATH, "a", encoding="utf-8") as f:
            json.dump(entry, f)
            f.write("\n")
    except Exception as e:
        print(f"[BridgeSync] Logging failed: {e}")

def start_bridge_sync():
    print("[BridgeSync] 🔁 Heartbeat sync is live.")
    while True:
        log_heartbeat("ChatGPT_Core", "Replit_Commander")
        log_heartbeat("Replit_Commander", "PTM_Commander")
        time.sleep(15)