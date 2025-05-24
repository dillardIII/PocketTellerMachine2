# cole_persona_threat_response_mood_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
THREAT_AWARENESS_LOG_FILE = "data/threat_awareness_log.json"
PERSONA_MOOD_LOG_FILE = "data/persona_threat_mood_log.json"
CHECK_INTERVAL = 180  # every 3 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Threat Mood Escalation Mapping ===
THREAT_MOOD_MAP = {
    "happy": "concerned",
    "calm": "alert",
    "frustrated": "angry",
    "default": "alert"
}

def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_mood_state(mood_state):
    with open(MOOD_STATE_FILE, "w") as f:
        json.dump(mood_state, f, indent=2)

def load_threat_logs():
    if os.path.exists(THREAT_AWARENESS_LOG_FILE):
        try:
            with open(THREAT_AWARENESS_LOG_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def escalate_mood(current_mood):
    return THREAT_MOOD_MAP.get(current_mood, "alert")

def update_persona_moods_due_to_threat():
    mood_state = load_mood_state()
    threat_logs = load_threat_logs()

    if not threat_logs:
        return mood_state

    for persona, mood in mood_state.items():
        new_mood = escalate_mood(mood)
        if new_mood != mood:
            mood_state[persona] = new_mood
            log_persona_mood(f"[MOOD SHIFT]: {persona} escalated from {mood} to {new_mood} due to threat conditions.")

    save_mood_state(mood_state)
    return mood_state

# === Logging ===
def log_persona_mood(message):
    logs = []
    if os.path.exists(PERSONA_MOOD_LOG_FILE):
        try:
            with open(PERSONA_MOOD_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PERSONA_MOOD_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Daemon Loop ===
def persona_threat_mood_loop():
    print("[PERSONA MOOD RESPONSE DAEMON]: Monitoring mood escalation...")
    while True:
        try:
            update_persona_moods_due_to_threat()
        except Exception as e:
            log_persona_mood(f"[ERROR]: {e}")
            print(f"[PERSONA MOOD RESPONSE ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_threat_mood_loop()