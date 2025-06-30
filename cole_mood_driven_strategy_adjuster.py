from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_mood_driven_strategy_adjuster.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
ADJUSTED_STRATEGY_FILE = "data/mood_driven_strategy_adjustments.json"
STRATEGY_LOG_FILE = "data/mood_driven_strategy_adjuster_log.json"
CHECK_INTERVAL = 900  # Every 15 minutes

# === Mood to Strategy Adjustment Map ===
MOOD_STRATEGY_MAP = {
    "happy": {"risk_level": "medium", "bias": "growth"},
    "frustrated": {"risk_level": "low", "bias": "defensive"},
    "calm": {"risk_level": "balanced", "bias": "neutral"},
    "angry": {"risk_level": "high", "bias": "aggressive"}
}

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_strategy_adjustment_event(message):
    logs = []
    if os.path.exists(STRATEGY_LOG_FILE):
        try:
            with open(STRATEGY_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(STRATEGY_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load mood state ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Apply strategy adjustment ===
def adjust_strategy(persona, mood):
    adjustment = MOOD_STRATEGY_MAP.get(mood, {"risk_level": "balanced", "bias": "neutral"})
    log_strategy_adjustment_event(f"[MOOD STRATEGY ADJUSTER]: {persona} mood '{mood}' → risk: {adjustment['risk_level']}, bias: {adjustment['bias']}")
    return adjustment

def update_strategy_adjustments():
    mood_state = load_mood_state()
    strategy_adjustments = {}

    for persona, mood in mood_state.items():
        strategy_adjustments[persona] = adjust_strategy(persona, mood)

    with open(ADJUSTED_STRATEGY_FILE, "w") as f:
        json.dump(strategy_adjustments, f, indent=2)

# === Main Daemon Loop ===
def mood_driven_strategy_adjuster_loop():
    print("[MOOD STRATEGY ADJUSTER]: Running...")
    while True:
        try:
            update_strategy_adjustments()
        except Exception as e:
            log_strategy_adjustment_event(f"[MOOD STRATEGY ADJUSTER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    mood_driven_strategy_adjuster_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():