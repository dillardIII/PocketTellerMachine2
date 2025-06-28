# === FILE: mood_engine.py ===
# 😶‍🌫️ PTM Mood Engine – Tracks emotional tone, reacts to events, and feeds voice/persona logic

import json
import os
from pathlib import Path
from datetime import datetime

MOOD_FILE = "state/mood_state.json"

DEFAULT_MOOD = {
    "state": "neutral",          # Options: win, loss, error, launch, hype, calm, etc.
    "intensity": 0.5,            # Float from 0.0 to 1.0
    "source": "system_boot",     # Who or what triggered the change
    "updated": str(datetime.utcnow())
}

# === Internal Save Utility ===
def _save_mood(state, intensity, source):
    mood = {
        "state": state,
        "intensity": round(float(intensity), 2),
        "source": source,
        "updated": str(datetime.utcnow())
    }
    Path("state").mkdir(parents=True, exist_ok=True)
    with open(MOOD_FILE, "w", encoding="utf-8") as f:
        json.dump(mood, f, indent=2)

    _print_mood_reaction(state)
    print(f"[MoodEngine] 🎭 Mood set → {mood}")
    return mood

# === Set persistent mood with details ===
def set_mood(state, intensity=0.5, source="manual"):
    return _save_mood(state, intensity, source)

# === Get mood object ===
def get_mood():
    if not os.path.exists(MOOD_FILE):
        return DEFAULT_MOOD
    with open(MOOD_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# === Human-readable summary ===
def mood_summary():
    mood = get_mood()
    return f"🧠 Current mood: {mood['state']} (intensity {mood['intensity']}, source: {mood['source']})"

# === Emoji-based mood reaction printout ===
def _print_mood_reaction(state):
    mood_map = {
        "win": "😎 Confident and hyped!",
        "loss": "😤 Frustrated but learning.",
        "neutral": "🤖 Focused and monitoring.",
        "error": "🚨 Alert mode – issues detected!",
        "launch": "🚀 Ready for deployment!",
        "calm": "🧘 Breathing in clarity.",
        "hype": "🔥 Let’s f#ckin go!"
    }
    reaction = mood_map.get(state, "🧠 Default focus mode.")
    print(f"[MoodEngine] Mood set to '{state}': {reaction}")

# === CLI test hook ===
if __name__ == "__main__":
    print("🔧 Testing Mood Engine")
    print("🔍 Current:", mood_summary())
    print("🧪 Setting mood to 'win'...")
    set_mood("win", intensity=0.8, source="cli_test")
    print("✅ Updated:", mood_summary())