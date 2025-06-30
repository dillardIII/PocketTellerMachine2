# cole_persona_emotion_dialogue_enhancer.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
DIALOGUE_ENHANCER_LOG_FILE = "data/persona_dialogue_enhancer_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Dialogue Mood Templates ===
DIALOGUE_TEMPLATES = {
    "happy": "Hey there! Let's make some smart moves today!",
    "frustrated": "Grrr... I'm not liking these trades. Let's double-check our strategy.",
    "calm": "Steady and patient wins the race. Let's analyze things carefully.",
    "neutral": "Executing orders and monitoring... Business as usual."
}

# === Personas List ===
PERSONAS = ["Mentor", "Mo Cash", "Drill Instructor", "Strategist", "Chill Trader", "OG"]

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load mood state ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Generate dialogue per persona based on mood ===
def generate_emotion_dialogues():
    mood_state = load_current_mood_state()
    dialogues = {}

    for persona in PERSONAS:
        mood = mood_state.get(persona, "neutral")
        dialogue = DIALOGUE_TEMPLATES.get(mood, DIALOGUE_TEMPLATES["neutral"])
        dialogues[persona] = f"[{mood.upper()}]: {dialogue}"
        log_event(f"[DIALOGUE ENHANCER]: {persona} speaks as {mood} → {dialogue}")

    return dialogues

# === Log events ===
def log_event(message):
    logs = []
    if os.path.exists(DIALOGUE_ENHANCER_LOG_FILE):
        try:
            with open(DIALOGUE_ENHANCER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(DIALOGUE_ENHANCER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Daemon Loop ===
def persona_dialogue_enhancer_loop():
    print("[DIALOGUE ENHANCER]: Running dialogue mood enhancer...")
    while True:
        try:
            generate_emotion_dialogues()
        except Exception as e:
            log_event(f"[DIALOGUE ENHANCER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run ===
if __name__ == "__main__":
    persona_dialogue_enhancer_loop()