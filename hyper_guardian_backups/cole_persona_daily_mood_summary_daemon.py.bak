# cole_persona_daily_mood_summary_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
EMOTIONAL_MEMORY_FILE = "data/emotional_memory_log.json"
DAILY_SUMMARY_FILE = "data/persona_daily_summary.json"
CHECK_INTERVAL = 86400  # Every 24 hours

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Load emotional memory ===
def load_emotional_memory():
    if os.path.exists(EMOTIONAL_MEMORY_FILE):
        try:
            with open(EMOTIONAL_MEMORY_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Save daily summary ===
def save_daily_summary(summaries):
    with open(DAILY_SUMMARY_FILE, "w") as f:
        json.dump(summaries, f, indent=2)

# === Generate daily mood summary per persona ===
def generate_daily_summary():
    memory = load_emotional_memory()
    persona_summary = {}

    today_date = datetime.now().date().isoformat()

    for log in memory:
        timestamp = log.get("timestamp", "")
        if not timestamp.startswith(today_date):
            continue

        persona = log.get("persona", "Unknown")
        mood = log.get("mood", "neutral")

        if persona not in persona_summary:
            persona_summary[persona] = {"happy": 0, "frustrated": 0, "calm": 0}

        if mood in persona_summary[persona]:
            persona_summary[persona][mood] += 1

    print(f"[DAILY MOOD SUMMARY]: Generated summary for {len(persona_summary)} personas.")
    save_daily_summary(persona_summary)

# === Main Daemon Loop ===
def daily_mood_summary_loop():
    print("[DAILY MOOD SUMMARY DAEMON]: Running...")
    while True:
        try:
            generate_daily_summary()
        except Exception as e:
            print(f"[DAILY MOOD SUMMARY ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    daily_mood_summary_loop()