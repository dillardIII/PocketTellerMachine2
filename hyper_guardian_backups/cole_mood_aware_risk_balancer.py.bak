# cole_mood_aware_risk_balancer.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
RISK_SETTINGS_FILE = "data/mood_risk_balancer_settings.json"
BALANCER_LOG_FILE = "data/mood_risk_balancer_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Mood to Risk Mapping ===
MOOD_RISK_MAP = {
    "happy": "normal",
    "frustrated": "conservative",
    "calm": "steady",
    "angry": "pause"
}

# === Logging ===
def log_balancer_event(message):
    logs = []
    if os.path.exists(BALANCER_LOG_FILE):
        try:
            with open(BALANCER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(BALANCER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load current mood state ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Update risk settings based on mood ===
def adjust_risk_settings():
    mood_state = load_current_mood_state()
    new_risk_settings = {}

    for persona, mood in mood_state.items():
        risk_level = MOOD_RISK_MAP.get(mood, "normal")
        new_risk_settings[persona] = {"mood": mood, "risk_level": risk_level}
        log_balancer_event(f"[MOOD RISK BALANCER]: {persona} mood '{mood}' → risk level set to '{risk_level}'.")

    with open(RISK_SETTINGS_FILE, "w") as f:
        json.dump(new_risk_settings, f, indent=2)

# === Main Daemon Loop ===
def mood_aware_risk_balancer_loop():
    print("[MOOD RISK BALANCER]: Running mood-aware risk balancer...")
    while True:
        try:
            adjust_risk_settings()
        except Exception as e:
            log_balancer_event(f"[MOOD RISK BALANCER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    mood_aware_risk_balancer_loop()