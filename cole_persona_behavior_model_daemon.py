# cole_persona_behavior_model_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
BEHAVIOR_MODEL_FILE = "data/persona_behavior_model.json"
MOOD_STATE_FILE = "data/mood_state.json"
BEHAVIOR_LOG_FILE = "data/persona_behavior_model_log.json"
CHECK_INTERVAL = 900  # Every 15 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(BEHAVIOR_LOG_FILE):
        try:
            with open(BEHAVIOR_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(BEHAVIOR_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load Mood State ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load Behavior Model ===
def load_behavior_model():
    if os.path.exists(BEHAVIOR_MODEL_FILE):
        try:
            with open(BEHAVIOR_MODEL_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Save Behavior Model ===
def save_behavior_model(model):
    with open(BEHAVIOR_MODEL_FILE, "w") as f:
        json.dump(model, f, indent=2)

# === Adjust Behavior Based on Mood ===
def adjust_behavior_model():
    mood_state = load_mood_state()
    behavior_model = load_behavior_model()

    for persona, mood in mood_state.items():
        behavior = mood_to_behavior(mood)
        behavior_model[persona] = {"current_behavior": behavior}
        log_event(f"[BEHAVIOR MODEL]: {persona} behavior set to {behavior} due to mood {mood}")

    save_behavior_model(behavior_model)

def mood_to_behavior(mood):
    if mood == "happy":
        return "Encouraging and Motivating"
    elif mood == "frustrated":
        return "Direct and Strict"
    elif mood == "calm":
        return "Reflective and Supportive"
    else:
        return "Neutral and Balanced"

# === Main Daemon Loop ===
def persona_behavior_model_loop():
    print("[PERSONA BEHAVIOR MODEL]: Running persona behavior model daemon...")
    while True:
        try:
            adjust_behavior_model()
        except Exception as e:
            log_event(f"[BEHAVIOR MODEL ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_behavior_model_loop()