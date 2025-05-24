# cole_voice_dialect_mode_manager.py

import os
import json
from datetime import datetime

# === Configurations ===
DIALECT_MODE_FILE = "data/voice_dialect_modes.json"
LOG_FILE = "data/voice_dialect_mode_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Default Dialect Modes ===
DEFAULT_DIALECT_MODES = {
    "Default": "standard",
    "UserPreferred": "southern",
    "PersonaSpecific": {
        "Mentor": "new_yorker",
        "Mo Cash": "urban",
        "Drill Instructor": "military"
    }
}

# === Load Modes ===
def load_dialect_modes():
    if os.path.exists(DIALECT_MODE_FILE):
        try:
            with open(DIALECT_MODE_FILE, "r") as f:
                return json.load(f)
        except:
            return DEFAULT_DIALECT_MODES
    return DEFAULT_DIALECT_MODES

# === Save Modes ===
def save_dialect_modes(modes):
    with open(DIALECT_MODE_FILE, "w") as f:
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
def update_dialect_mode(persona, mode):
    modes = load_dialect_modes()
    if "PersonaSpecific" not in modes:
        modes["PersonaSpecific"] = {}
    modes["PersonaSpecific"][persona] = mode
    save_dialect_modes(modes)
    log_event(f"[VOICE DIALECT]: {persona} dialect set to {mode}")

# === Get Current Modes ===
def get_current_modes():
    return load_dialect_modes()

# Example Usage (testable)
if __name__ == "__main__":
    update_dialect_mode("Mo Cash", "urban")
    print(get_current_modes())