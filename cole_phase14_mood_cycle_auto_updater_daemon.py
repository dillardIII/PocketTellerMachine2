from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase14_mood_cycle_auto_updater_daemon.py

import os
import json
import time
from datetime import datetime

from cole_phase14_unified_mood_reactor import set_mood_state

# === Configurations ===
TRADE_LOG_FILE = "data/trade_review_report.json"
MOOD_UPDATE_LOG_FILE = "data/mood_cycle_update_log.json"
CHECK_INTERVAL = 900  # 15 minutes

os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_mood_update(message):
    logs = []
    if os.path.exists(MOOD_UPDATE_LOG_FILE):
        try:
            with open(MOOD_UPDATE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MOOD_UPDATE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Mood Logic Based on Recent Trade Performance ===
def analyze_recent_trades_and_update_mood():
    if not os.path.exists(TRADE_LOG_FILE):
        log_mood_update("No trade review log found.")
        return

    try:
        with open(TRADE_LOG_FILE, "r") as f:
            trades = json.load(f)
    except:
        log_mood_update("Error loading trade review log.")
        return

    recent_trades = trades[-10:]
    wins = sum(1 for t in recent_trades if t.get("result", "").lower() == "win"):
    losses = sum(1 for t in recent_trades if t.get("result", "").lower() == "loss"):
:
    if wins > losses:
        set_mood_state("Mo Cash", "celebration")
        set_mood_state("Mentor", "happy")
        set_mood_state("Drill Instructor", "motivational_push")
        log_mood_update(f"More wins ({wins}) than losses ({losses}) → Happy/Positive moods set.")
    elif losses > wins:
        set_mood_state("Mo Cash", "sad")
        set_mood_state("Mentor", "neutral")
        set_mood_state("Drill Instructor", "angry")
        log_mood_update(f"More losses ({losses}) than wins ({wins}) → Corrective moods set.")
    else:
        set_mood_state("Mo Cash", "neutral")
        set_mood_state("Mentor", "neutral")
        set_mood_state("Drill Instructor", "neutral")
        log_mood_update(f"Balanced or no trades → Neutral moods set.")

# === Daemon Loop ===
def mood_cycle_auto_updater_loop():
    print("[MOOD CYCLE AUTO UPDATER]: Running...")
    while True:
        try:
            analyze_recent_trades_and_update_mood()
        except Exception as e:
            log_mood_update(f"[ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    mood_cycle_auto_updater_loop()

def log_event():ef drop_files_to_bridge():