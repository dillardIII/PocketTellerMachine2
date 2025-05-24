# cole_voice_emotion_tone_manager.py

import os
import json
from datetime import datetime

# === Configurations ===
EMOTION_TONE_FILE = "data/voice_emotion_tone.json"
LOG_FILE = "data/voice_emotion_tone_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Default Emotion Tones ===
DEFAULT_EMOTION_TONES = {
    "happy": "cheerful",
    "frustrated": "stern",
    "calm": "soft",
    "sad": "melancholic"
}

# === Load Tones ===
def load_emotion_tones():
    if os.path.exists(EMOTION_TONE_FILE):
        try:
            with open(EMOTION_TONE_FILE, "r") as f:
                return json.load(f)
        except:
            return DEFAULT_EMOTION_TONES
    return DEFAULT_EMOTION_TONES

# === Save Tones ===
def save_emotion_tones(tones):
    with open(EMOTION_TONE_FILE, "w") as f:
        json.dump(tones, f, indent=2)

# === Log Event ===
def log_event(message):
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Update Tone ===
def update_emotion_tone(emotion, tone):
    tones = load_emotion_tones()
    tones[emotion] = tone
    save_emotion_tones(tones)
    log_event(f"[VOICE EMOTION]: {emotion} tone set to {tone}")

# === Get Current Tones ===
def get_current_tones():
    return load_emotion_tones()

# Example Usage (testable)
if __name__ == "__main__":
    update_emotion_tone("frustrated", "strict")
    print(get_current_tones())