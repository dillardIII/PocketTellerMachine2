# cole_threat_awareness_adaptive_response_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
GHOST_LOG_FILE = "data/ghost_log.json"
THREAT_AWARENESS_LOG_FILE = "data/threat_awareness_log.json"
COMMAND_WEBHOOK_URL = "http://localhost:5050/cole_webhook"
CHECK_INTERVAL = 180  # every 3 minutes

# === Ensure data folder ===
os.makedirs("data", exist_ok=True)

# === Threat Detection Keywords ===
THREAT_KEYWORDS = [
    "market crash", "uncontrollable", "halt", "unexpected event", "black swan",
    "market panic", "flash crash", "anomaly detected", "high risk exposure"
]

# === Load ghost logs ===
def load_ghost_logs():
    if os.path.exists(GHOST_LOG_FILE):
        try:
            with open(GHOST_LOG_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Analyze logs for threats ===
def detect_threats(logs):
    threats_detected = []
    for log in logs[-50:]:
        message = log.get("message", "").lower()
        if any(keyword in message for keyword in THREAT_KEYWORDS):
            threats_detected.append(log)
    return threats_detected

# === Trigger defensive reaction ===
def trigger_defensive_mode(threat_details):
    import requests
    command = f"ACTIVATE_DEFENSIVE_MODE triggered by threat: {threat_details.get('message', '')}"
    payload = {"command": command}
    try:
        response = requests.post(COMMAND_WEBHOOK_URL, json=payload)
        log_threat_event(f"[DEFENSIVE MODE]: Triggered → {command}")
        print(f"[THREAT AWARENESS]: Defensive mode activated.")
    except Exception as e:
        log_threat_event(f"[ERROR]: Failed to trigger defensive mode → {e}")
        print(f"[THREAT AWARENESS ERROR]: {e}")

# === Logging ===
def log_threat_event(message):
    logs = []
    if os.path.exists(THREAT_AWARENESS_LOG_FILE):
        try:
            with open(THREAT_AWARENESS_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(THREAT_AWARENESS_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Daemon loop ===
def threat_awareness_loop():
    print("[THREAT AWARENESS DAEMON]: Running...")
    while True:
        try:
            logs = load_ghost_logs()
            threats = detect_threats(logs)
            if threats:
                for threat in threats:
                    trigger_defensive_mode(threat)
            else:
                log_threat_event("[CHECK]: No immediate threats detected.")
        except Exception as e:
            log_threat_event(f"[ERROR]: {e}")
            print(f"[THREAT AWARENESS ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    threat_awareness_loop()