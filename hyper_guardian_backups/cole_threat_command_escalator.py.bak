# cole_threat_command_escalator.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
THREAT_LOG_FILE = "data/threat_awareness_log.json"
ESCALATION_COMMAND_LOG_FILE = "data/threat_command_escalation_log.json"
ESCALATION_COMMAND_FILE = "data/threat_command_escalation.json"
CHECK_INTERVAL = 180  # Every 3 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load threat logs ===
def load_threat_logs():
    if os.path.exists(THREAT_LOG_FILE):
        try:
            with open(THREAT_LOG_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Escalate command ===
def escalate_command(threat):
    command = f"ACTIVATE_DEFENSIVE_MODE → reason: {threat.get('description', 'Unknown Threat')}"
    log_escalation(f"[COMMAND ESCALATED]: {command}")
    with open(ESCALATION_COMMAND_FILE, "w") as f:
        json.dump({"command": command, "triggered_by": threat, "timestamp": datetime.now().isoformat()}, f, indent=2)

# === Log escalation ===
def log_escalation(message):
    logs = []
    if os.path.exists(ESCALATION_COMMAND_LOG_FILE):
        try:
            with open(ESCALATION_COMMAND_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(ESCALATION_COMMAND_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Check for escalation needs ===
def check_threats_for_escalation():
    threats = load_threat_logs()
    if not threats:
        return

    for threat in threats[-5:]:
        if "CRITICAL" in threat.get("severity", "").upper():
            escalate_command(threat)

# === Daemon Loop ===
def threat_command_escalator_loop():
    print("[THREAT COMMAND ESCALATOR]: Monitoring for command escalation...")
    while True:
        try:
            check_threats_for_escalation()
        except Exception as e:
            log_escalation(f"[ERROR]: {e}")
            print(f"[ESCALATOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    threat_command_escalator_loop()