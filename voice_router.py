# === FILE: voice_router.py ===
# 🗣️ Voice Router – Directs output to appropriate voice based on assistant, mood, or context

import random
from mood_engine import get_mood

# === Sample voice registry ===
VOICE_MAP = {
    "neutral": ["mentor_voice_1", "strategist_voice_1"],
    "win": ["mo_cash_voice", "drill_voice"],
    "loss": ["mentor_voice_2", "optimist_voice"],
    "error": ["shadow_voice", "drill_voice"],
    "launch": ["hype_mode_voice", "og_voice"]
}

def pick_voice(state_override=None):
    mood = get_mood()
    state = state_override or mood["state"]
    voice_options = VOICE_MAP.get(state, VOICE_MAP["neutral"])
    chosen = random.choice(voice_options)
    print(f"[VoiceRouter] 🎙️ Selected voice for state '{state}': {chosen}")
    return chosen