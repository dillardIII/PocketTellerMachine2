from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_dialogue_variation_enhancer.py

import os
import json
import random

# === Configurations ===
MOOD_ADAPTIVE_SETTINGS_FILE = "data/persona_mood_adaptive_settings.json"

# === Dialogue Variation Rules ===
DIALOGUE_VARIATIONS = {
    "upbeat": ["You got it!", "Absolutely!", "Sure thing!", "Sounds great!"],
    "direct": ["Done.", "Understood.", "On it.", "Confirmed."],
    "neutral": ["Okay.", "Alright.", "Noted.", "Proceeding."],
}

DIALOGUE_STYLES = {
    "friendly": lambda text: f"{text} :)",
    "short": lambda text: text.split(".")[0] if "." in text else text,:
    "balanced": lambda text: text,
    "default": lambda text: text,
}

# === Load Adaptive Settings ===
def load_adaptive_settings():
    if os.path.exists(MOOD_ADAPTIVE_SETTINGS_FILE):
        try:
            with open(MOOD_ADAPTIVE_SETTINGS_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Enhance Dialogue ===
def enhance_dialogue(persona, message):
    settings = load_adaptive_settings()
    persona_settings = settings.get(persona, {"tone": "neutral", "dialogue_style": "balanced"})

    tone = persona_settings.get("tone", "neutral")
    style = persona_settings.get("dialogue_style", "balanced")

    variation = random.choice(DIALOGUE_VARIATIONS.get(tone, ["Okay."]))
    styled_message = DIALOGUE_STYLES.get(style, lambda x: x)(message)

    enhanced_message = f"{variation} {styled_message}"
    return enhanced_message

# === Example Usage ===
if __name__ == "__main__":
    personas = ["Mentor", "Mo Cash", "Drill Instructor"]
    message = "Let's review the trade performance data."

    for persona in personas:
        enhanced = enhance_dialogue(persona, message)
        print(f"[{persona}]: {enhanced}")

def log_event():ef drop_files_to_bridge():