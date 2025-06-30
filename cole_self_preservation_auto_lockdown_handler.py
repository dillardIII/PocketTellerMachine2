from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_self_preservation_auto_lockdown_handler.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
LOCKDOWN_STATE_FILE = "data/lockdown_state.json"
THREAT_LOG_FILE = "data/cole_threat_log.json"
LOCKDOWN_LOG_FILE = "data/lockdown_log.json"
CHECK_INTERVAL = 60  # Every 1 minute

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load current lockdown state ===
def load_lockdown_state():
    if os.path.exists(LOCKDOWN_STATE_FILE):
        try:
            with open(LOCKDOWN_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {"status": "UNLOCKED"}
    return {"status": "UNLOCKED"}

def save_lockdown_state(state):
    with open(LOCKDOWN_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

# === Load threat logs ===
def load_threat_logs():
    if os.path.exists(THREAT_LOG_FILE):
        try:
            with open(THREAT_LOG_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Lockdown Trigger Logic ===
def trigger_lockdown(reason):
    state = {"status": "LOCKED_DOWN", "triggered_at": datetime.now().isoformat(), "reason": reason}
    save_lockdown_state(state)
    log_event(f"[LOCKDOWN]: System entered lockdown mode due to: {reason}")
    print(f"[LOCKDOWN]: SYSTEM LOCKED DOWN: {reason}")

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(LOCKDOWN_LOG_FILE):
        try:
            with open(LOCKDOWN_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(LOCKDOWN_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Threat Assessment Logic ===
def assess_threats():
    logs = load_threat_logs()
    for log in logs[-10:]:
        if "CRITICAL" in log.get("level", "").upper():
            return log.get("message")
    return None

# === Main Daemon Loop ===
def lockdown_handler_loop():
    print("[LOCKDOWN HANDLER]: Running...")
    while True:
        try:
            current_state = load_lockdown_state()
            if current_state.get("status") != "LOCKED_DOWN":
                threat_reason = assess_threats()
                if threat_reason:
                    trigger_lockdown(threat_reason)
        except Exception as e:
            log_event(f"[ERROR]: {e}")
            print(f"[LOCKDOWN HANDLER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    lockdown_handler_loop()