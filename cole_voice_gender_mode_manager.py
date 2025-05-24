# cole_voice_gender_mode_manager.py

import os
import json
from datetime import datetime

# === Configurations ===
VOICE_GENDER_MODE_FILE = "data/voice_gender_modes.json"
LOG_FILE = "data/voice_gender_mode_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Default Modes ===
DEFAULT_GENDER_MODES = {
    "Default": "neutral",
    "UserPreferred": "masculine",
    "PersonaSpecific": {
        "Mentor": "feminine",
        "Mo Cash": "masculine",
        "Drill Instructor": "masculine"
    }
}

# === Load Modes ===
def load_gender_modes():
    if os.path.exists(VOICE_GENDER_MODE_FILE):
        try:
            with open(VOICE_GENDER_MODE_FILE, "r") as f:
                return json.load(f)
        except:
            return DEFAULT_GENDER_MODES
    return DEFAULT_GENDER_MODES

# === Save Modes ===
def save_gender_modes(modes):
    with open(VOICE_GENDER_MODE_FILE, "w") as f:
        json.dump(modes, f, indent=2)

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

# === Update Mode ===
def update_gender_mode(persona, mode):
    modes = load_gender_modes()
    if "PersonaSpecific" not in modes:
        modes["PersonaSpecific"] = {}
    modes["PersonaSpecific"][persona] = mode
    save_gender_modes(modes)
    log_event(f"[VOICE GENDER]: {persona} set to {mode}")

# === Get Current Modes ===
def get_current_modes():
    return load_gender_modes()

# Example Usage (testable)
if __name__ == "__main__":
    update_gender_mode("Mentor", "feminine")
    print(get_current_modes())