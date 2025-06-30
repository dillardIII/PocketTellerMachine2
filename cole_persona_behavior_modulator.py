from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_behavior_modulator.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
BEHAVIOR_STATE_FILE = "data/persona_behavior_state.json"
BEHAVIOR_LOG_FILE = "data/persona_behavior_modulator_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Behavior Map ===
BEHAVIOR_MAP = {
    "happy": {"tone": "friendly", "attitude": "motivational"},
    "frustrated": {"tone": "direct", "attitude": "corrective"},
    "calm": {"tone": "neutral", "attitude": "analytical"},
    "angry": {"tone": "firm", "attitude": "aggressive"}
}

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_behavior_modulator_event(message):
    logs = []
    if os.path.exists(BEHAVIOR_LOG_FILE):
        try:
            with open(BEHAVIOR_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(BEHAVIOR_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load current mood ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Apply behavior based on mood ===
def adjust_behavior_based_on_mood(persona, mood):
    behavior = BEHAVIOR_MAP.get(mood, {"tone": "neutral", "attitude": "balanced"})
    log_behavior_modulator_event(f"[BEHAVIOR MODULATOR]: {persona} mood '{mood}' → tone: {behavior['tone']}, attitude: {behavior['attitude']}")
    return behavior

def update_behavior_state():
    mood_state = load_mood_state()
    behavior_state = {}

    for persona, mood in mood_state.items():
        behavior_state[persona] = adjust_behavior_based_on_mood(persona, mood)

    with open(BEHAVIOR_STATE_FILE, "w") as f:
        json.dump(behavior_state, f, indent=2)

# === Main Daemon Loop ===
def persona_behavior_modulator_loop():
    print("[BEHAVIOR MODULATOR]: Running...")
    while True:
        try:
            update_behavior_state()
        except Exception as e:
            log_behavior_modulator_event(f"[BEHAVIOR MODULATOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_behavior_modulator_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():