from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase13_avatar_voice_mood_response.py

import os
import json
from datetime import datetime

VOICE_MOOD_RESPONSE_FILE = "data/avatar_voice_mood_responses.json"
os.makedirs("data", exist_ok=True)

default_responses = {
    "happy": "I'm feeling great and ready to assist you!",
    "frustrated": "Hmm, something didn't go as expected. Let's adjust our strategy.",
    "calm": "Steady as she goes. I'm analyzing data quietly.",
    "idle": "I'm standing by for your command."
}

def load_voice_mood_responses():
    if os.path.exists(VOICE_MOOD_RESPONSE_FILE):
        with open(VOICE_MOOD_RESPONSE_FILE, "r") as f:
            return json.load(f)
    else:
        with open(VOICE_MOOD_RESPONSE_FILE, "w") as f:
            json.dump(default_responses, f, indent=2)
        return default_responses

def get_response_for_mood(mood):
    responses = load_voice_mood_responses()
    return responses.get(mood, "I'm here and ready for action.")

def update_voice_mood_response(mood, response):
    responses = load_voice_mood_responses()
    responses[mood] = response
    with open(VOICE_MOOD_RESPONSE_FILE, "w") as f:
        json.dump(responses, f, indent=2)

def log_voice_response_event(mood, avatar_name):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "avatar": avatar_name,
        "mood": mood,
        "response": get_response_for_mood(mood)
    }
    if not os.path.exists("data/avatar_voice_response_log.json"):
        with open("data/avatar_voice_response_log.json", "w") as f:
            json.dump([log_entry], f, indent=2)
    else:
        with open("data/avatar_voice_response_log.json", "r") as f:
            logs = json.load(f)
        logs.append(log_entry)
        with open("data/avatar_voice_response_log.json", "w") as f:
            json.dump(logs[-100:], f, indent=2)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():