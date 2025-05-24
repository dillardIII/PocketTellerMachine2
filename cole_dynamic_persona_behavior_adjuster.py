# cole_dynamic_persona_behavior_adjuster.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
PERSONA_BEHAVIOR_LOG = "data/persona_behavior_adjuster_log.json"
CHECK_INTERVAL = 300  # 5 minutes

# === Persona Behavioral Modifiers ===
BEHAVIOR_MAP = {
    "happy": "boost_confidence",
    "frustrated": "apply_caution",
    "calm": "stay_balanced"
}

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def adjust_behavior_for_personas():
    mood_state = load_current_mood_state()

    for persona, mood in mood_state.items():
        behavior = BEHAVIOR_MAP.get(mood, "default_behavior")
        log_event(f"[BEHAVIOR ADJUSTER]: {persona} behavior adjusted to '{behavior}' due to mood '{mood}'")

def log_event(message):
    logs = []
    if os.path.exists(PERSONA_BEHAVIOR_LOG):
        try:
            with open(PERSONA_BEHAVIOR_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PERSONA_BEHAVIOR_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    print("[BEHAVIOR ADJUSTER]: Starting...")
    adjust_behavior_for_personas()