# cole_phase14_mood_to_voice_engine.py

import json
import os
from datetime import datetime
from cole_phase14_voice_style_manager import update_voice_style

MOOD_LOG_FILE = "data/mood_to_voice_log.json"
os.makedirs("data", exist_ok=True)

# === Mood to voice map ===
MOOD_VOICE_MAP = {
    "happy_win": "celebratory_excited",
    "frustrated_loss": "stern_corrective",
    "neutral": "calm_professional",
    "critical_error": "urgent_command",
    "motivational_push": "hype_coach",
    "teaching_moment": "calm_mentor",
    "casual": "laid_back"
}

# === Log mood changes ===
def log_mood_event(mood, action):
    logs = []
    if os.path.exists(MOOD_LOG_FILE):
        try:
            with open(MOOD_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "mood": mood, "action": action})
    with open(MOOD_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === React to mood and adjust persona voice ===
def react_to_mood(persona_name, mood):
    voice_style = MOOD_VOICE_MAP.get(mood, "default")
    update_voice_style(persona_name, voice_style)
    log_mood_event(mood, f"Adjusted {persona_name} to voice style {voice_style}")
    print(f"[MOOD ENGINE]: {persona_name} switched to {voice_style} due to {mood} mood.")

# === Example usage ===
if __name__ == "__main__":
    react_to_mood("Mo Cash", "happy_win")
    react_to_mood("Drill Instructor", "frustrated_loss")
    react_to_mood("Mentor", "teaching_moment")