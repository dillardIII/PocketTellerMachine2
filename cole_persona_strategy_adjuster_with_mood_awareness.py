from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_strategy_adjuster_with_mood_awareness.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
ADJUSTMENT_LOG_FILE = "data/persona_strategy_adjustment_log.json"
CHECK_INTERVAL = 1800  # Every 30 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load persona mood ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Strategy Adjustment Table ===
MOOD_STRATEGY_MODIFIERS = {
    "happy": "aggressive",
    "frustrated": "defensive",
    "calm": "balanced"
}

# === Logging Helper ===
def log_adjustment(message):
    logs = []
    if os.path.exists(ADJUSTMENT_LOG_FILE):
        try:
            with open(ADJUSTMENT_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(ADJUSTMENT_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Adjust Strategy Based on Mood ===
def adjust_strategy(persona, mood):
    adjustment = MOOD_STRATEGY_MODIFIERS.get(mood, "balanced")
    log_adjustment(f"[STRATEGY ADJUSTER]: {persona} is currently '{mood}' → Adjusting to '{adjustment}' mode.")
    print(f"[STRATEGY ADJUSTER]: {persona} is now using '{adjustment}' mode.")
    # Here you would inject this into the persona's live strategy if integrated:
    return adjustment

# === Main Adjustment Loop ===
def persona_strategy_adjustment_loop():
    print("[PERSONA STRATEGY ADJUSTER]: Running...")
    while True:
        try:
            moods = load_current_mood_state()
            if moods:
                for persona, mood in moods.items():
                    adjust_strategy(persona, mood)
            else:
                log_adjustment("[STRATEGY ADJUSTER]: No mood data found.")
        except Exception as e:
            log_adjustment(f"[STRATEGY ADJUSTER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_strategy_adjustment_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():