from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_voice_reaction_handler.py

import os
import json
import random
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_REACTION_LOG_FILE = "data/persona_voice_reaction_log.json"

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Voice reactions based on mood ===
MOOD_VOICE_RESPONSES = {
    "happy": [
        "Let's keep the good vibes going!",
        "Feeling on top of the world!",
        "Nice win! Let's do it again!"
    ],
    "frustrated": [
        "Grrr... that trade stung. Regrouping...",
        "Okay, let's pause and adjust our approach.",
        "Frustrated but focused. We'll bounce back."
    ],
    "calm": [
        "Analyzing the market with clarity.",
        "Staying balanced and composed.",
        "Patience is key right now."
    ]
}

# === Load current mood state ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Log voice reaction ===
def log_voice_reaction(persona, mood, reaction):
    logs = []
    if os.path.exists(VOICE_REACTION_LOG_FILE):
        try:
            with open(VOICE_REACTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "persona": persona,
        "mood": mood,
        "reaction": reaction
    })
    with open(VOICE_REACTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)
    print(f"[VOICE REACTION]: {persona} ({mood}) says: '{reaction}'")

# === Trigger persona voice reaction ===
def trigger_voice_reactions():
    moods = load_current_mood_state()
    if not moods:
        print("[VOICE REACTION]: No mood state found.")
        return

    for persona, mood in moods.items():
        responses = MOOD_VOICE_RESPONSES.get(mood, ["Ready for the next move."])
        selected_reaction = random.choice(responses)
        log_voice_reaction(persona, mood, selected_reaction)

# === Example direct usage ===
if __name__ == "__main__":
    trigger_voice_reactions()

def log_event():ef drop_files_to_bridge():