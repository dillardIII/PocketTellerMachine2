# cole_emotional_reaction_speech_generator.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
SPEECH_LOG_FILE = "data/emotional_reaction_speech_log.json"
OUTPUT_SPEECH_FILE = "data/emotional_reaction_speech.json"
os.makedirs("data", exist_ok=True)

# === Reaction Templates ===
SPEECH_TEMPLATES = {
    "happy": [
        "That was a fantastic trade! I'm feeling great!",
        "Another win under my belt. Let's keep this going!",
        "I'm on fire today!"
    ],
    "frustrated": [
        "That didn't go as planned... I need to adjust my strategy.",
        "Ugh, that was a loss. I'll do better next time.",
        "Frustrating outcome. I have to rethink this."
    ],
    "calm": [
        "Steady as always. Reviewing my moves.",
        "Nothing major, staying in observation mode.",
        "Market's quiet. I'm keeping my cool."
    ]
}

def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def generate_reaction_speech():
    mood_state = load_mood_state()
    speech_output = {}

    for persona, mood in mood_state.items():
        speech = select_speech_for_mood(mood)
        speech_output[persona] = {
            "mood": mood,
            "speech": speech,
            "timestamp": datetime.now().isoformat()
        }
        log_event(f"[SPEECH]: {persona} ({mood}) says → {speech}")

    with open(OUTPUT_SPEECH_FILE, "w") as f:
        json.dump(speech_output, f, indent=2)

    return speech_output

def select_speech_for_mood(mood):
    return SPEECH_TEMPLATES.get(mood, ["I'm analyzing the market."])[0]

def log_event(message):
    logs = []
    if os.path.exists(SPEECH_LOG_FILE):
        try:
            with open(SPEECH_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SPEECH_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Run as one-shot speech generator ===
if __name__ == "__main__":
    result = generate_reaction_speech()
    print(json.dumps(result, indent=2))