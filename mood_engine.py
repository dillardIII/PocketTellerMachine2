# === FILE: mood_engine.py ===
# 😶‍🌫️ Mood Engine – Controls PTM assistant emotional tone and mood state

import json
import os
from pathlib import Path

MOOD_FILE = "state/mood_state.json"

DEFAULT_MOOD = {
    "state": "neutral",
    "intensity": 0.5,
    "source": "system"
}

# === Set persistent mood with detailed state ===
def set_mood(state, intensity=0.5, source="system"):
    mood = {
        "state": state,
        "intensity": round(float(intensity), 2),
        "source": source
    }
    Path("state").mkdir(parents=True, exist_ok=True)
    with open(MOOD_FILE, "w", encoding="utf-8") as f:
        json.dump(mood, f, indent=2)

    # Also trigger feedback tone
    _print_mood_reaction(state)
    print(f"[MoodEngine] 🎭 Mood set → {mood}")

# === Get mood object ===
def get_mood():
    if not os.path.exists(MOOD_FILE):
        return DEFAULT_MOOD
    with open(MOOD_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# === Get human-readable summary ===
def mood_summary():
    mood = get_mood()
    return f"Current mood: {mood['state']} (intensity {mood['intensity']} from {mood['source']})"

# === Optional emoji-based reactions ===
def _print_mood_reaction(state):
    mood_map = {
        "win": "😎 Confident and hyped!",
        "loss": "😤 Frustrated but learning.",
        "neutral": "🤖 Focused and monitoring.",
        "error": "🚨 Alert mode – issues detected!",
        "launch": "🚀 Ready for deployment!"
    }
    mood = mood_map.get(state, "🧘 Default calm mode.")
    print(f"[MoodEngine] Mood set to '{state}': {mood}")