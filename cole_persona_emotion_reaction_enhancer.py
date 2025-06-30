from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_emotion_reaction_enhancer.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
REACTION_LOG_FILE = "data/persona_reaction_log.json"

# === Reaction Templates ===
REACTIONS = {
    "happy": {
        "win": "That was amazing! Let's keep this streak going!",
        "loss": "We'll bounce back stronger! Don't worry.",
        "neutral": "Feeling good, let's stay focused."
    },
    "frustrated": {
        "win": "Finally, something good happened. Let's stay sharp.",
        "loss": "This is unacceptable. Fix it NOW.",
        "neutral": "Meh. Let's see if we can shake things up.":
    },
    "calm": {
        "win": "Excellent result. Stay steady and controlled.",
        "loss": "Losses happen. Let's review and adjust calmly.",
        "neutral": "Everything is balanced. Monitoring as usual."
    },
    "neutral": {
        "win": "Good work.",
        "loss": "That didn't go well.",
        "neutral": "System standing by."
    }
}

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load Mood State ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Generate Reaction ===
def generate_reaction(persona, event_type):
    mood_state = load_current_mood_state()
    current_mood = mood_state.get(persona, "neutral")
    mood_reactions = REACTIONS.get(current_mood, REACTIONS["neutral"])
    reaction = mood_reactions.get(event_type, "...")
    log_reaction(persona, current_mood, event_type, reaction)
    return reaction

# === Logging Reaction ===
def log_reaction(persona, mood, event, reaction):
    logs = []
    if os.path.exists(REACTION_LOG_FILE):
        try:
            with open(REACTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "persona": persona,
        "mood": mood,
        "event": event,
        "reaction": reaction
    })
    with open(REACTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example Usage ===
if __name__ == "__main__":
    personas = ["Mentor", "Mo Cash", "Drill Instructor"]
    events = ["win", "loss", "neutral"]

    for persona in personas:
        for event in events:
            reaction = generate_reaction(persona, event)
            print(f"[{persona} - {event}]: {reaction}")

def log_event():ef drop_files_to_bridge():