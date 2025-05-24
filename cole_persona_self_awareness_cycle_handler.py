# cole_persona_self_awareness_cycle_handler.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
TRADE_REVIEW_FILE = "data/trade_review_report.json"
SELF_AWARENESS_LOG_FILE = "data/persona_self_awareness_log.json"
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

# === Load trades ===
def load_recent_trades():
    if os.path.exists(TRADE_REVIEW_FILE):
        try:
            with open(TRADE_REVIEW_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Log event ===
def log_self_awareness(message):
    logs = []
    if os.path.exists(SELF_AWARENESS_LOG_FILE):
        try:
            with open(SELF_AWARENESS_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SELF_AWARENESS_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Persona Self Reflection ===
def persona_self_reflection(persona, mood, trades):
    trade_summary = [t for t in trades if t.get("executed_by") == persona]
    total = len(trade_summary)
    wins = len([t for t in trade_summary if "win" in t.get("result", "").lower()])
    losses = len([t for t in trade_summary if "loss" in t.get("result", "").lower()])

    reflection = (
        f"[{persona} SELF-AWARENESS]: Current mood is '{mood}'. "
        f"I have executed {total} trades, with {wins} wins and {losses} losses. "
        "I will adjust my strategy accordingly and stay aware of my tendencies."
    )
    print(reflection)
    log_self_awareness(reflection)

# === Main Daemon Loop ===
def persona_self_awareness_cycle():
    print("[PERSONA SELF-AWARENESS]: Running...")
    while True:
        try:
            moods = load_current_mood_state()
            trades = load_recent_trades()

            if moods:
                for persona, mood in moods.items():
                    persona_self_reflection(persona, mood, trades)
            else:
                log_self_awareness("[SELF-AWARENESS]: No mood data found.")
        except Exception as e:
            log_self_awareness(f"[SELF-AWARENESS ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_self_awareness_cycle()