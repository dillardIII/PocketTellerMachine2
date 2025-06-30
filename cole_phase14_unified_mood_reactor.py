from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase14_unified_mood_reactor.py

import os
import json
from datetime import datetime

MOOD_STATE_FILE = "data/assistant_mood_state.json"
MOOD_REACTION_LOG_FILE = "data/assistant_mood_reaction_log.json"
os.makedirs("data", exist_ok=True)

# === Ensure state file exists ===
if not os.path.exists(MOOD_STATE_FILE):
    with open(MOOD_STATE_FILE, "w") as f:
        json.dump({}, f, indent=2)

# === Load mood state ===
def load_mood_state():
    with open(MOOD_STATE_FILE, "r") as f:
        return json.load(f)

# === Set mood state ===
def set_mood_state(assistant_name, mood):
    moods = load_mood_state()
    moods[assistant_name] = {"mood": mood, "timestamp": datetime.now().isoformat()}
    with open(MOOD_STATE_FILE, "w") as f:
        json.dump(moods, f, indent=2)
    log_mood_reaction(assistant_name, mood)

# === Get mood state ===
def get_mood_state(assistant_name):
    moods = load_mood_state()
    return moods.get(assistant_name, {}).get("mood", "neutral")

# === Mood to tone mapping ===
def get_reaction_tone_from_mood(mood):
    mapping = {
        "happy": "enthusiastic, uplifting",
        "neutral": "calm, steady",
        "sad": "soft, empathetic",
        "angry": "firm, corrective",
        "motivational_push": "high energy, pushy coach",
        "celebration": "cheerful, excited"
    }
    return mapping.get(mood, "neutral")

# === Log mood reactions ===
def log_mood_reaction(assistant_name, mood):
    logs = []
    if os.path.exists(MOOD_REACTION_LOG_FILE):
        try:
            with open(MOOD_REACTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "assistant": assistant_name,
        "mood": mood,
        "reaction_tone": get_reaction_tone_from_mood(mood)
    })
    with open(MOOD_REACTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example usage ===
if __name__ == "__main__":
    set_mood_state("Mo Cash", "motivational_push")
    set_mood_state("Mentor", "celebration")
    set_mood_state("Drill Instructor", "angry")

    print(load_mood_state())
    print(get_reaction_tone_from_mood("angry"))

def log_event():ef drop_files_to_bridge():