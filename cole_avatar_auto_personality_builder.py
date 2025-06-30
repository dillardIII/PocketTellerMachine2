from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_auto_personality_builder.py

import os
import json
import random
from datetime import datetime

# === Configurations ===
PERSONALITY_FILE = "data/avatar_personalities.json"
MOOD_STATE_FILE = "data/mood_state.json"
TRADE_REVIEW_FILE = "data/trade_review_report.json"
PERSONALITY_LOG_FILE = "data/avatar_personality_builder_log.json"

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

def load_current_personalities():
    if os.path.exists(PERSONALITY_FILE):
        try:
            with open(PERSONALITY_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_personalities(personalities):
    with open(PERSONALITY_FILE, "w") as f:
        json.dump(personalities, f, indent=2)

def load_trade_patterns():
    if os.path.exists(TRADE_REVIEW_FILE):
        try:
            with open(TRADE_REVIEW_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def build_new_personality():
    trade_patterns = load_trade_patterns()
    mood_state = load_current_mood_state()

    new_personality = {
        "nickname": f"AutoPersona_{datetime.now().strftime('%H%M%S')}",
        "style": random.choice(["Optimistic", "Pessimistic", "Calm", "Aggressive"]),
        "speech_tone": random.choice(["Friendly", "Direct", "Playful", "Serious"]),
        "default_mood": random.choice(list(mood_state.values()) if mood_state else ["calm"]),:
        "trading_focus": random.choice(["Risk Management", "Momentum", "Pattern Recognition", "Trend Following"])
    }

    return new_personality

def update_personality_pool():
    personalities = load_current_personalities()
    new_personality = build_new_personality()
    personalities[new_personality["nickname"]] = new_personality
    save_personalities(personalities)
    log_event(f"[AUTO PERSONA BUILDER]: Created new personality → {new_personality['nickname']}")
    return new_personality

def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def log_event(message):
    logs = []
    if os.path.exists(PERSONALITY_LOG_FILE):
        try:
            with open(PERSONALITY_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PERSONALITY_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    print("[AUTO PERSONA BUILDER]: Generating new persona...")
    update_personality_pool()