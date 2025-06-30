from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_adaptive_risk_communication_assistant.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
LOCKDOWN_TRIGGER_FILE = "data/lockdown_state.json"
RISK_COMMUNICATION_LOG = "data/risk_communication_log.json"
CHECK_INTERVAL = 180  # Every 3 minutes

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_communication(message):
    logs = []
    if os.path.exists(RISK_COMMUNICATION_LOG):
        try:
            with open(RISK_COMMUNICATION_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(RISK_COMMUNICATION_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load current system lockdown state ===
def load_lockdown_state():
    if os.path.exists(LOCKDOWN_TRIGGER_FILE):
        try:
            with open(LOCKDOWN_TRIGGER_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Communicate current system state ===
def communicate_risk_state():
    state_info = load_lockdown_state()
    state = state_info.get("state", "NORMAL_MODE")

    if state == "FULL_LOCKDOWN":
        message = "Attention: The system is in FULL LOCKDOWN due to detected critical risks."
    elif state == "CAUTIOUS_MODE":
        message = "Notice: The system is in CAUTIOUS MODE. All actions are under strict supervision."
    else:
        message = "The system is operating in NORMAL MODE."

    log_communication(f"[COMMUNICATION]: {message}")
    print(f"[RISK COMMUNICATION]: {message}")

# === Main Daemon Loop ===
def risk_communication_loop():
    print("[RISK COMMUNICATION ASSISTANT]: Active...")
    while True:
        try:
            communicate_risk_state()
        except Exception as e:
            log_communication(f"[RISK COMMUNICATION ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    risk_communication_loop()

def log_event():ef drop_files_to_bridge():