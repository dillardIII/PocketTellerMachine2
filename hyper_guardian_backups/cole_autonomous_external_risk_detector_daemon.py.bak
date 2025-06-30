# cole_autonomous_external_risk_detector_daemon.py

import os
import json
import time
from datetime import datetime
import random

# === Configurations ===
THREAT_LOG_FILE = "data/cole_threat_log.json"
EXTERNAL_RISK_LOG_FILE = "data/external_risk_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Simulated external risk events ===
SIMULATED_RISKS = [
    "Breaking News: Tech market downturn detected.",
    "Regulatory risk: New restrictions on trading platforms.",
    "Security breach in financial systems reported.",
    "AI system drift warning in models.",
    "Major financial institution collapse rumors."
]

# === Add external risks to threat log ===
def inject_external_risk_event():
    risk = random.choice(SIMULATED_RISKS)
    threat = {
        "timestamp": datetime.now().isoformat(),
        "type": "EXTERNAL_RISK",
        "message": risk,
        "level": "LOW",
        "source": "ExternalRiskScanner",
        "needs_escalation": True
    }

    threats = []
    if os.path.exists(THREAT_LOG_FILE):
        try:
            with open(THREAT_LOG_FILE, "r") as f:
                threats = json.load(f)
        except:
            threats = []

    threats.append(threat)
    with open(THREAT_LOG_FILE, "w") as f:
        json.dump(threats[-500:], f, indent=2)

    log_event(f"[EXTERNAL RISK]: {risk} injected into threat log.")

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(EXTERNAL_RISK_LOG_FILE):
        try:
            with open(EXTERNAL_RISK_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(EXTERNAL_RISK_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def external_risk_monitor_loop():
    print("[EXTERNAL RISK MONITOR]: Running...")
    while True:
        try:
            inject_external_risk_event()
        except Exception as e:
            log_event(f"[ERROR]: {e}")
            print(f"[EXTERNAL RISK MONITOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    external_risk_monitor_loop()