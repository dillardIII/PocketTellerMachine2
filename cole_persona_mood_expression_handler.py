from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_mood_expression_handler.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
EXPRESSION_LOG_FILE = "data/persona_expression_handler_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Expression presets based on mood ===
EXPRESSION_MAP = {
    "happy": "smile",
    "frustrated": "frown",
    "calm": "neutral",
    "default": "neutral"
}

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def apply_expression_adjustments():
    mood_state = load_current_mood_state()

    for persona, mood in mood_state.items():
        expression = EXPRESSION_MAP.get(mood, EXPRESSION_MAP["default"])
        log_event(f"[EXPRESSION HANDLER]: {persona} avatar expression set to '{expression}' due to mood '{mood}'.")

def log_event(message):
    logs = []
    if os.path.exists(EXPRESSION_LOG_FILE):
        try:
            with open(EXPRESSION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(EXPRESSION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    print("[EXPRESSION HANDLER]: Starting...")
    apply_expression_adjustments()