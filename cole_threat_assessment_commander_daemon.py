from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_threat_assessment_commander_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
THREAT_LOG_FILE = "data/cole_threat_log.json"
THREAT_ASSESSMENT_FILE = "data/threat_assessment_summary.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Load Threats ===
def load_threats():
    if os.path.exists(THREAT_LOG_FILE):
        try:
            with open(THREAT_LOG_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Threat Assessment Engine ===
def assess_threats(threats):
    summary = {
        "timestamp": datetime.now().isoformat(),
        "total_threats": len(threats),
        "high": 0,
        "medium": 0,
        "low": 0,
        "critical_warnings": []
    }

    for threat in threats[-100:]:
        level = threat.get("level", "LOW").upper()
        if level == "HIGH":
            summary["high"] += 1
        elif level == "MEDIUM":
            summary["medium"] += 1
        else:
            summary["low"] += 1

        if threat.get("needs_escalation"):
            summary["critical_warnings"].append(threat)

    # Dynamic risk level
    if summary["high"] > 5 or len(summary["critical_warnings"]) > 10:
        summary["system_risk_level"] = "CRITICAL"
    elif summary["high"] > 2 or summary["medium"] > 5:
        summary["system_risk_level"] = "HIGH"
    else:
        summary["system_risk_level"] = "NORMAL"

    return summary

# === Save Threat Assessment ===
def save_assessment(assessment):
    with open(THREAT_ASSESSMENT_FILE, "w") as f:
        json.dump(assessment, f, indent=2)

# === Main Threat Commander Loop ===
def threat_commander_loop():
    print("[THREAT COMMANDER]: Running...")
    while True:
        try:
            threats = load_threats()
            if threats:
                assessment = assess_threats(threats)
                save_assessment(assessment)
                print(f"[THREAT COMMANDER]: Risk Level → {assessment['system_risk_level']}")
            else:
                print("[THREAT COMMANDER]: No threats detected.")
        except Exception as e:
            print(f"[THREAT COMMANDER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    threat_commander_loop()

def log_event():ef drop_files_to_bridge():