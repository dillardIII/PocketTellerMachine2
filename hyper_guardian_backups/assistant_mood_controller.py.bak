"""
Assistant Mood Controller:
Applies mood-based filters to assistant behavior, tone, and response logic.
Used for tailoring assistant personality outputs based on emotion history.
"""

from cole_brain import get_last

MOOD_BEHAVIOR_MAP = {
    "win": {
        "tone": "excited",
        "speed": "fast",
        "voice_effect": "echo"
    },
    "loss": {
        "tone": "serious",
        "speed": "slow",
        "voice_effect": "reverb"
    },
    "neutral": {
        "tone": "calm",
        "speed": "normal",
        "voice_effect": "none"
    },
    "discipline": {
        "tone": "stern",
        "speed": "sharp",
        "voice_effect": "grit"
    },
    "unknown": {
        "tone": "default",
        "speed": "normal",
        "voice_effect": "none"
    }
}

def get_mood_settings(persona):
    """
    Determines the assistant’s current mood settings from brain memory.
    """
    mood = get_last(f"{persona}_mood") or "unknown"
    return MOOD_BEHAVIOR_MAP.get(mood, MOOD_BEHAVIOR_MAP["unknown"])

# === Debug
if __name__ == "__main__":
    for p in ["MoCash", "Mentor", "Strategist"]:
        print(f"{p} mood settings ➤", get_mood_settings(p))