from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_defensive_mode_system_handler.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
DEFENSIVE_MODE_FILE = "data/defensive_mode_status.json"
THREAT_AWARENESS_LOG_FILE = "data/threat_awareness_log.json"
DEFENSIVE_MODE_LOG_FILE = "data/defensive_mode_log.json"
CHECK_INTERVAL = 120  # every 2 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Defensive Mode States ===
DEFENSIVE_STATES = {
    "inactive": "ACTIVE",
    "ACTIVE": "REINFORCED"
}

def load_defensive_status():
    if os.path.exists(DEFENSIVE_MODE_FILE):
        try:
            with open(DEFENSIVE_MODE_FILE, "r") as f:
                return json.load(f)
        except:
            return {"status": "inactive", "last_triggered": None}
    return {"status": "inactive", "last_triggered": None}

def save_defensive_status(status):
    with open(DEFENSIVE_MODE_FILE, "w") as f:
        json.dump(status, f, indent=2)

def load_threat_logs():
    if os.path.exists(THREAT_AWARENESS_LOG_FILE):
        try:
            with open(THREAT_AWARENESS_LOG_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def check_and_escalate_defense():
    status = load_defensive_status()
    threats = load_threat_logs()

    if not threats:
        return status

    # Basic escalation logic based on number of recent threats
    recent_threats = [t for t in threats if "CRITICAL" in t.get("severity", "").upper()]:
:
    if recent_threats:
        new_status = DEFENSIVE_STATES.get(status["status"], "REINFORCED")
        if status["status"] != new_status:
            log_defensive(f"[DEFENSE]: Status escalated from {status['status']} to {new_status} due to threats.")
            status["status"] = new_status
            status["last_triggered"] = datetime.now().isoformat()
            save_defensive_status(status)

    return status

# === Logging ===
def log_defensive(message):
    logs = []
    if os.path.exists(DEFENSIVE_MODE_LOG_FILE):
        try:
            with open(DEFENSIVE_MODE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(DEFENSIVE_MODE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Daemon Loop ===
def defensive_mode_loop():
    print("[DEFENSIVE MODE HANDLER]: Monitoring defensive status...")
    while True:
        try:
            check_and_escalate_defense()
        except Exception as e:
            log_defensive(f"[ERROR]: {e}")
            print(f"[DEFENSIVE MODE ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    defensive_mode_loop()

def log_event():ef drop_files_to_bridge():