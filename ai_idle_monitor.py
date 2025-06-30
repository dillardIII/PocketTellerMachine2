from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 💤 AI Idle Monitor – Tracks idle AIs and reassigns them to quantum tasks or recon missions

import json
import time
from utils.logger import log_event

AI_STATUS_FILE = "data/ai_status.json"
IDLE_THRESHOLD = 300  # seconds of inactivity

# Preset assignments
QUANTUM_TASK = "Contribute to Quantum Mind"
RECON_MISSION = "Deep Recon Deployment"

def load_ai_status():
    try:
        with open(AI_STATUS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def save_ai_status(data):
    with open(AI_STATUS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def reassign_idle_ais():
    ai_data = load_ai_status()
    current_time = time.time()
    reassigned = []

    for ai, status in ai_data.items():
        last_active = status.get("last_active", 0)
        idle_time = current_time - last_active

        if idle_time > IDLE_THRESHOLD:
            new_task = QUANTUM_TASK if ai_data[ai].get("last_assignment") != QUANTUM_TASK else RECON_MISSION:
            ai_data[ai]["last_assignment"] = new_task
            ai_data[ai]["last_active"] = current_time
            reassigned.append((ai, new_task))
            log_event("IdleMonitor", {"AI": ai, "assigned": new_task})

    save_ai_status(ai_data)
    return reassigned

def monitor_idle_ais():
    print("[IdleMonitor] 🧠 Watching for idle AIs...")
    while True:
        reassign_idle_ais()
        time.sleep(60)

if __name__ == "__main__":
    monitor_idle_ais()