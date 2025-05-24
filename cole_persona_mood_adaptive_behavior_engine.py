# cole_persona_mood_adaptive_behavior_engine.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
DAILY_SUMMARY_FILE = "data/persona_daily_summary.json"
MOOD_ADAPTIVE_SETTINGS_FILE = "data/persona_mood_adaptive_settings.json"
CHECK_INTERVAL = 3600  # Every hour

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Load daily mood summary ===
def load_daily_summary():
    if os.path.exists(DAILY_SUMMARY_FILE):
        try:
            with open(DAILY_SUMMARY_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Save mood-adaptive behavior settings ===
def save_adaptive_settings(settings):
    with open(MOOD_ADAPTIVE_SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)

# === Calculate adaptive settings based on mood ===
def calculate_adaptive_settings(daily_summary):
    adaptive_settings = {}

    for persona, moods in daily_summary.items():
        total = sum(moods.values())
        if total == 0:
            continue

        happy_ratio = moods.get("happy", 0) / total
        frustrated_ratio = moods.get("frustrated", 0) / total
        calm_ratio = moods.get("calm", 0) / total

        if happy_ratio > 0.5:
            tone = "upbeat"
            style = "friendly"
            risk_level = "moderate"
        elif frustrated_ratio > 0.4:
            tone = "direct"
            style = "short"
            risk_level = "conservative"
        else:
            tone = "neutral"
            style = "balanced"
            risk_level = "default"

        adaptive_settings[persona] = {
            "tone": tone,
            "dialogue_style": style,
            "decision_weighting": risk_level
        }

    return adaptive_settings

# === Main Mood Adaptive Engine Loop ===
def mood_adaptive_engine_loop():
    print("[MOOD ADAPTIVE ENGINE]: Running...")
    while True:
        try:
            daily_summary = load_daily_summary()
            adaptive_settings = calculate_adaptive_settings(daily_summary)
            save_adaptive_settings(adaptive_settings)
            print(f"[MOOD ADAPTIVE ENGINE]: Updated adaptive behavior for {len(adaptive_settings)} personas.")
        except Exception as e:
            print(f"[MOOD ADAPTIVE ENGINE ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    mood_adaptive_engine_loop()