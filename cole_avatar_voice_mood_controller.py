# cole_avatar_voice_mood_controller.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_LOG_FILE = "data/avatar_voice_mood_controller_log.json"

# === Voice mood presets ===
VOICE_PRESETS = {
    "happy": {"pitch": 1.2, "speed": 1.1, "tone": "cheerful"},
    "frustrated": {"pitch": 0.9, "speed": 1.2, "tone": "stern"},
    "calm": {"pitch": 1.0, "speed": 0.95, "tone": "soft"}
}

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def adjust_voice_based_on_mood():
    mood_state = load_current_mood_state()

    for persona, mood in mood_state.items():
        preset = VOICE_PRESETS.get(mood, VOICE_PRESETS["calm"])
        log_event(f"[VOICE CONTROLLER]: {persona} voice adjusted → Pitch: {preset['pitch']} | Speed: {preset['speed']} | Tone: {preset['tone']}")

def log_event(message):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    print("[VOICE MOOD CONTROLLER]: Adjusting voices...")
    adjust_voice_based_on_mood()