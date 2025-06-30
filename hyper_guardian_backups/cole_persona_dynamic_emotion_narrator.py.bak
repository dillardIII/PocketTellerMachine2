# cole_persona_dynamic_emotion_narrator.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
NARRATION_LOG_FILE = "data/persona_emotion_narration_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Narration Templates ===
EMOTION_MESSAGES = {
    "happy": [
        "I'm feeling confident and optimistic today!",
        "Our strategies are paying off. Let's keep it up!",
        "Feeling good about the market."
    ],
    "frustrated": [
        "Hmm, these losses are making me rethink the approach.",
        "We hit some bumps. Time to adjust strategies carefully.",
        "Not the best day, but we will learn and improve."
    ],
    "calm": [
        "Remaining calm and neutral. Let's observe the patterns.",
        "Market's a little unpredictable today, staying steady.",
        "Keeping a balanced mindset for optimal decision-making."
    ]
}

# === Logging ===
def log_narration(message):
    logs = []
    if os.path.exists(NARRATION_LOG_FILE):
        try:
            with open(NARRATION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(NARRATION_LOG_FILE, "w") as f:
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

# === Narrate persona mood ===
def narrate_mood(persona, mood):
    messages = EMOTION_MESSAGES.get(mood, ["I'm feeling neutral."])
    selected_message = messages[datetime.now().second % len(messages)]
    narration = f"[{persona.upper()} NARRATION]: {selected_message}"
    print(narration)
    log_narration(narration)

# === Narrator Loop ===
def persona_emotion_narrator_loop():
    print("[PERSONA EMOTION NARRATOR]: Running...")
    while True:
        try:
            moods = load_current_mood_state()
            if moods:
                for persona, mood in moods.items():
                    narrate_mood(persona, mood)
            else:
                log_narration("[NARRATOR]: No mood data found.")
        except Exception as e:
            log_narration(f"[NARRATOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_emotion_narrator_loop()