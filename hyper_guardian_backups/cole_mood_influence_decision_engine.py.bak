# cole_mood_influence_decision_engine.py

import os
import json

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"

# === Influence table ===
MOOD_INFLUENCE_MAP = {
    "happy": {
        "risk_tolerance": "high",
        "dialogue_style": "enthusiastic",
        "strategy_preference": "aggressive"
    },
    "frustrated": {
        "risk_tolerance": "low",
        "dialogue_style": "defensive",
        "strategy_preference": "safe"
    },
    "calm": {
        "risk_tolerance": "balanced",
        "dialogue_style": "neutral",
        "strategy_preference": "balanced"
    }
}

# === Load mood state ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Determine influence ===
def determine_influence(persona):
    moods = load_current_mood_state()
    mood = moods.get(persona, "calm")
    influence = MOOD_INFLUENCE_MAP.get(mood, MOOD_INFLUENCE_MAP["calm"])
    return influence

# === Example influence test ===
if __name__ == "__main__":
    personas = ["MoCash", "Mentor", "DrillInstructor"]
    for persona in personas:
        influence = determine_influence(persona)
        print(f"[MOOD INFLUENCE]: {persona} mood influence → {influence}")