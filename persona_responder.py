from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Persona Responder:
Generates contextual and emotional responses for PTM assistants.
Blends internal memory, trade outcomes, and persona flavor for realism.
Used in dialog events, recaps, commentary, and strategic mood logic.
"""

import random
from cole_brain import get_last, log_state
from persona_voice_player import speak_persona

# === Mood-based emotional templates ===
EMOTIONAL_TEMPLATES = {
    "win": [
        "That trade hit just right. I'm on fire. 💰",
        "Victory confirmed. We called that shot like a sniper.",
        "Easy money. Let’s line up the next one."
    ],
    "loss": [
        "Ouch. That one stung. Reviewing what went wrong.",
        "Took a hit — but it’s all learning. We'll recalibrate.",
        "Loss logged. Strategy adjustment initiated."
    ],
    "neutral": [
        "Stable result. Monitoring market for next opportunity.",
        "That played out as expected. Let's sharpen the edge.",
        "Filed. Ready for the next setup."
    ]
}

# === Persona style overlays ===
PERSONA_LINES = {
    "MoCash": [
        "Stack it up, baby! That move was fire. 💸",
        "Another win. Told you I don’t miss!",
        "We eatin’. Let’s keep this hustle alive."
    ],
    "Mentor": [
        "This trade aligns well with our risk tolerance.",
        "Calculated. Methodical. Profitable.",
        "Let’s reflect and adapt. Success is built in layers."
    ],
    "Strategist": [
        "The model predicted this accurately. Confidence: 89%",
        "Phase alignment confirmed. Executed clean.",
        "We move with precision. Next signal loaded."
    ],
    "DrillInstructor": [
        "You call that a trade?! Lock it up, warrior!",
        "Harden your risk discipline or don’t show up!",
        "Success is earned through reps. Don’t slack."
    ],
    "ChillTrader": [
        "Nice little dub. Let’s coast a bit. 🌊",
        "Keep it zen, profit again.",
        "That trade? Vibes."
    ],
    "Default": [
        "Trade executed.",
        "Event logged successfully.",
        "Analyzing next move..."
    ]
}

def generate_response(persona_name="Default"):
    """
    Returns a voice-ready, mood-aware, and personality-styled response.
    """
    result = get_last("last_trade_result") or "neutral"
    mood_snippet = random.choice(EMOTIONAL_TEMPLATES.get(result, EMOTIONAL_TEMPLATES["neutral"]))
    persona_snippet = random.choice(PERSONA_LINES.get(persona_name, PERSONA_LINES["Default"]))

    final_message = f"{persona_name}: {mood_snippet} {persona_snippet}"
    log_state(f"{persona_name}_mood", result)

    print(f"[🗣️ Persona Reply] {final_message}")
    speak_persona(persona_name, final_message)
    return final_message

# === Optional standalone test
if __name__ == "__main__":
    for name in ["MoCash", "Mentor", "Strategist"]:
        generate_response(name)

def log_event():ef drop_files_to_bridge():