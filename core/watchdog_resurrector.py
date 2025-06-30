from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: core/watchdog_resurrector.py ===
"""
Watchdog Resurrector:
Monitors PTM subsystems for inactivity or crash loops. If detected, attempts restart or auto-patch.
"""

import time
import os
import json
from datetime import datetime, timedelta
from ghostforge_core import GhostForge

WATCHED_PROCESSES = {
    "bridge_listener": {"heartbeat_file": "memory/heartbeat_bridge.json", "max_idle_sec": 60},
    "reflex_engine": {"heartbeat_file": "memory/heartbeat_reflex.json", "max_idle_sec": 45},
    "ghostbrain": {"heartbeat_file": "memory/heartbeat_ghostbrain.json", "max_idle_sec": 90}
}

LOG_PATH = "memory/resurrector_log.json"

def log_resurrection(process_name):
    log = []
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            log = json.load(f)

    entry = {
        "process": process_name,
        "resurrected_at": datetime.utcnow().isoformat()
    }
    log.append(entry)
    with open(LOG_PATH, "w") as f:
        json.dump(log[-100:], f, indent=2)

def heartbeat_expired(path, max_age_sec):
    if not os.path.exists(path):
        return True
    with open(path, "r") as f:
        data = json.load(f)
    last_ping = datetime.fromisoformat(data.get("timestamp", "1970-01-01T00:00:00"))
    return (datetime.utcnow() - last_ping).total_seconds() > max_age_sec

def start_watchdog():
    print("[Watchdog] 🛡️ Watchdog is now active.")
    while True:
        for proc, meta in WATCHED_PROCESSES.items():
            if heartbeat_expired(meta["heartbeat_file"], meta["max_idle_sec"]):
                print(f"[Watchdog] ⚠️ {proc} is unresponsive. Triggering resurrection.")
                log_resurrection(proc)
                GhostForge(persona="Spectra").regenerate_module(proc)
        time.sleep(30)

if __name__ == "__main__":
    start_watchdog()