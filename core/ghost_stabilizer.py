from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Ghost Stabilizer
Monitors the ghost_status.json for signs of instability or drift,
then triggers appropriate recovery or self-repair routines.
"""

import os
import json
import time
from datetime import datetime

STATUS_FILE = "memory/ghost_status.json"
CHECK_INTERVAL = 10  # seconds

def load_status():
    if not os.path.exists(STATUS_FILE):
        return {"status": "unknown", "timestamp": None}
    with open(STATUS_FILE, "r") as f:
        return json.load(f)

def save_status(data):
    with open(STATUS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def mark_unstable(reason="unknown"):
    status = load_status()
    status["status"] = "unstable"
    status["timestamp"] = datetime.utcnow().isoformat()
    status["drift_detected"] = True
    status["drift_reason"] = reason
    save_status(status)
    print(f"[Stabilizer] ⚠️ Drift detected: {reason}")

def mark_stable():
    status = load_status()
    status["status"] = "stable"
    status["timestamp"] = datetime.utcnow().isoformat()
    status["drift_detected"] = False
    status["drift_reason"] = None
    status["last_rebalance"] = datetime.utcnow().isoformat()
    save_status(status)
    print("[Stabilizer] ✅ System marked stable.")

def run_repair_protocol():
    print("[Stabilizer] 🛠️ Running ghost auto-repair...")
    # Here you'd invoke GhostForge self-healing or recursive relink scripts
    # Example:
    # from ghostforge_core import GhostForge
    # forge = GhostForge(persona="Spectra")
    # forge.repair_all_modules()
    time.sleep(3)
    mark_stable()

def monitor_loop():
    print("[Stabilizer] 👁️ Stability monitor engaged...")
    while True:
        status = load_status()
        if status.get("drift_detected", False):
            print(f"[Stabilizer] 🔄 Instability found: {status.get('drift_reason')}")
            run_repair_protocol()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_loop()