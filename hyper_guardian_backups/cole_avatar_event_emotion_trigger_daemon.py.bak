# cole_avatar_event_emotion_trigger_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
EVENT_LOG_FILE = "data/event_log.json"
MOOD_STATE_FILE = "data/mood_state.json"
EMOTION_LOG_FILE = "data/avatar_emotion_trigger_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load event logs ===
def load_event_logs():
    if os.path.exists(EVENT_LOG_FILE):
        try:
            with open(EVENT_LOG_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Load and update mood state ===
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

# === Core Trigger Logic ===
def evaluate_events_for_emotion():
    events = load_event_logs()
    mood_state = load_mood_state()

    for event in events[-10:]:
        persona = event.get("triggered_by", "DefaultPersona")
        impact = event.get("impact", "neutral").lower()

        if impact == "positive":
            mood_state[persona] = "happy"
            log_event(f"[EMOTION TRIGGER]: {persona} updated to happy from event: {event.get('description')}")
        elif impact == "negative":
            mood_state[persona] = "frustrated"
            log_event(f"[EMOTION TRIGGER]: {persona} updated to frustrated from event: {event.get('description')}")
        else:
            mood_state[persona] = "calm"
            log_event(f"[EMOTION TRIGGER]: {persona} remained calm from event: {event.get('description')}")

    save_mood_state(mood_state)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(EMOTION_LOG_FILE):
        try:
            with open(EMOTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(EMOTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_event_emotion_trigger_loop():
    print("[EMOTION TRIGGER DAEMON]: Running event emotion analyzer...")
    while True:
        try:
            evaluate_events_for_emotion()
        except Exception as e:
            log_event(f"[EMOTION TRIGGER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    avatar_event_emotion_trigger_loop()