from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_auto_threat_level_escalator_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
THREAT_LOG_FILE = "data/cole_threat_log.json"
ESCALATION_LOG_FILE = "data/threat_escalation_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load current threats ===
def load_threat_logs():
    if os.path.exists(THREAT_LOG_FILE):
        try:
            with open(THREAT_LOG_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Save updated threats ===
def save_threat_logs(threats):
    with open(THREAT_LOG_FILE, "w") as f:
        json.dump(threats[-500:], f, indent=2)

# === Escalate threat level logic ===
def escalate_threat_level(threat):
    current_level = threat.get("level", "LOW").upper()
    if current_level == "LOW":
        return "MEDIUM"
    elif current_level == "MEDIUM":
        return "HIGH"
    elif current_level == "HIGH":
        return "CRITICAL"
    return "CRITICAL"

# === Process escalation ===
def escalate_threats():
    threats = load_threat_logs()
    updated = False

    for threat in threats[-20:]:
        if "needs_escalation" in threat and threat["needs_escalation"]:
            old_level = threat["level"]
            threat["level"] = escalate_threat_level(threat)
            threat["escalated_at"] = datetime.now().isoformat()
            threat.pop("needs_escalation")
            log_event(f"[ESCALATION]: {threat.get('message')} escalated from {old_level} to {threat['level']}")
            updated = True

    if updated:
        save_threat_logs(threats)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(ESCALATION_LOG_FILE):
        try:
            with open(ESCALATION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(ESCALATION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def threat_escalation_loop():
    print("[THREAT ESCALATOR]: Running...")
    while True:
        try:
            escalate_threats()
        except Exception as e:
            log_event(f"[ERROR]: {e}")
            print(f"[THREAT ESCALATOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    threat_escalation_loop()