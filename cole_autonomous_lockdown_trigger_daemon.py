from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_autonomous_lockdown_trigger_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
THREAT_ASSESSMENT_FILE = "data/threat_assessment_summary.json"
LOCKDOWN_LOG_FILE = "data/lockdown_log.json"
LOCKDOWN_TRIGGER_FILE = "data/lockdown_state.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

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

# === Load Threat Assessment ===
def load_threat_assessment():
    if os.path.exists(THREAT_ASSESSMENT_FILE):
        try:
            with open(THREAT_ASSESSMENT_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Apply Lockdown State ===
def apply_lockdown(state):
    with open(LOCKDOWN_TRIGGER_FILE, "w") as f:
        json.dump({"state": state, "timestamp": datetime.now().isoformat()}, f)
    log_event(f"[LOCKDOWN TRIGGER]: System set to {state} mode.")

# === Lockdown Trigger Logic ===
def check_and_trigger_lockdown():
    assessment = load_threat_assessment()
    risk_level = assessment.get("system_risk_level", "NORMAL")
    
    if risk_level == "CRITICAL":
        apply_lockdown("FULL_LOCKDOWN")
    elif risk_level == "HIGH":
        apply_lockdown("CAUTIOUS_MODE")
    else:
        apply_lockdown("NORMAL_MODE")

# === Main Daemon Loop ===
def lockdown_trigger_loop():
    print("[LOCKDOWN TRIGGER DAEMON]: Monitoring...")
    while True:
        try:
            check_and_trigger_lockdown()
        except Exception as e:
            log_event(f"[LOCKDOWN TRIGGER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    lockdown_trigger_loop()