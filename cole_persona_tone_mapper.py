# cole_persona_tone_mapper.py

import os
import json
from datetime import datetime

# === Configurations ===
PERSONA_TONE_MAP_FILE = "data/persona_tone_map.json"
PERSONA_TONE_LOG_FILE = "data/persona_tone_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Persona to Tone Mapping ===
PERSONA_TONE_MAP = {
    "Mo Cash": "aggressive",
    "Mentor": "encouraging",
    "Drill Instructor": "strict",
    "Optimist": "cheerful",
    "Chill Trader": "relaxed",
    "Strategist": "analytical",
    "OG": "classic",
    "Shadow": "mysterious"
}

# === Save persona tone map ===
def save_persona_tone_map():
    with open(PERSONA_TONE_MAP_FILE, "w") as f:
        json.dump(PERSONA_TONE_MAP, f, indent=2)
    log_event("[PERSONA TONE MAPPER]: Persona tone map saved.")

# === Logging helper ===
def log_event(message):
    logs = []
    if os.path.exists(PERSONA_TONE_LOG_FILE):
        try:
            with open(PERSONA_TONE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PERSONA_TONE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example usage ===
if __name__ == "__main__":
    save_persona_tone_map()
    print("[PERSONA TONE MAPPER]: Persona tone map initialized.")