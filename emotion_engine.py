from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: emotion_engine.py ===
import json, os
from command_memory import log_command_event

EMOTION_FILE = "emotion_state.json"

def load_emotion():
    if os.path.exists(EMOTION_FILE):
        with open(EMOTION_FILE) as f:
            return json.load(f)
    return {"confidence": 50, "fear": 50}

def save_emotion(state):
    with open(EMOTION_FILE, "w") as f:
        json.dump(state, f)

def adjust_emotion(result):
    state = load_emotion()
    if result == "win":
        state["confidence"] += 5
        state["fear"] -= 5
    elif result == "loss":
        state["confidence"] -= 5
        state["fear"] += 5
    save_emotion(state)
    log_command_event("EmotionAdjusted", state)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():