from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_mood_engine_dynamic_state_updater.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
TRADE_REVIEW_FILE = "data/trade_review_report.json"
MOOD_LOG_FILE = "data/mood_engine_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Mood Engine Logic ===
MOOD_MAP = {
    "win": "happy",
    "loss": "frustrated",
    "neutral": "calm"
}

def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_mood_state(mood_state):
    with open(MOOD_STATE_FILE, "w") as f:
        json.dump(mood_state, f, indent=2)

def load_recent_trades():
    if os.path.exists(TRADE_REVIEW_FILE):
        try:
            with open(TRADE_REVIEW_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def determine_mood_from_trade(trade):
    result = trade.get("result", "").lower()
    if "win" in result:
        return "happy"
    elif "loss" in result or "bad" in result:
        return "frustrated"
    return "calm"

def update_mood_based_on_trades():
    trades = load_recent_trades()
    mood_state = load_current_mood_state()

    if not trades:
        return mood_state

    for trade in trades[-10:]:
        persona = trade.get("executed_by", "DefaultPersona")
        new_mood = determine_mood_from_trade(trade)
        mood_state[persona] = new_mood
        log_event(f"[MOOD ENGINE]: {persona} mood updated to {new_mood} based on trade: {trade.get('result')}")

    save_mood_state(mood_state)
    return mood_state

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(MOOD_LOG_FILE):
        try:
            with open(MOOD_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MOOD_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def mood_engine_loop():
    print("[MOOD ENGINE]: Starting mood updater...")
    while True:
        try:
            update_mood_based_on_trades()
        except Exception as e:
            log_event(f"[MOOD ENGINE ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    mood_engine_loop()