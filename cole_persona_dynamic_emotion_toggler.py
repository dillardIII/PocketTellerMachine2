# cole_persona_dynamic_emotion_toggler.py

import os
import json
import time
import random
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
MOOD_TOGGLER_LOG_FILE = "data/persona_emotion_toggler_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Moods ===
MOODS = ["happy", "frustrated", "calm", "neutral"]

# === Personas List ===
PERSONAS = ["Mentor", "Mo Cash", "Drill Instructor", "Strategist", "Chill Trader", "OG"]

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load current mood state ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Save updated mood state ===
def save_mood_state(mood_state):
    with open(MOOD_STATE_FILE, "w") as f:
        json.dump(mood_state, f, indent=2)

# === Toggle mood randomly ===
def toggle_persona_moods():
    mood_state = load_current_mood_state()

    for persona in PERSONAS:
        new_mood = random.choice(MOODS)
        mood_state[persona] = new_mood
        log_event(f"[MOOD TOGGLER]: {persona} mood changed to {new_mood}.")

    save_mood_state(mood_state)

# === Log events ===
def log_event(message):
    logs = []
    if os.path.exists(MOOD_TOGGLER_LOG_FILE):
        try:
            with open(MOOD_TOGGLER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MOOD_TOGGLER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Daemon Loop ===
def persona_emotion_toggler_loop():
    print("[MOOD TOGGLER]: Running dynamic emotion toggler...")
    while True:
        try:
            toggle_persona_moods()
        except Exception as e:
            log_event(f"[MOOD TOGGLER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run ===
if __name__ == "__main__":
    persona_emotion_toggler_loop()