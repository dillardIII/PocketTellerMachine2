# cole_voice_tone_adjuster.py

import os
import json
from datetime import datetime

# === Configurations ===
VOICE_SETTINGS_FILE = "data/voice_tone_settings.json"
VOICE_LOG_FILE = "data/voice_tone_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Default Voice Tones ===
DEFAULT_VOICE_TONES = {
    "Mo Cash": {
        "tone": "streetwise",
        "pitch": "deep",
        "style": "bold"
    },
    "Mentor": {
        "tone": "calm",
        "pitch": "neutral",
        "style": "gentle"
    },
    "Drill Instructor": {
        "tone": "intense",
        "pitch": "commanding",
        "style": "aggressive"
    }
}

# === Save voice tones ===
def save_voice_tones():
    with open(VOICE_SETTINGS_FILE, "w") as f:
        json.dump(DEFAULT_VOICE_TONES, f, indent=2)
    log_event("[VOICE TONE ADJUSTER]: Voice tone settings saved.")

# === Logging helper ===
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

# === Example usage ===
if __name__ == "__main__":
    save_voice_tones()
    print("[VOICE TONE ADJUSTER]: Voice tones initialized.")