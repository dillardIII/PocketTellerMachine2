from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_ai_emotional_response_composer.py

import os
import json
from cole_persona_mood_voice_style_adjuster import get_voice_style_for_persona

# === Example persona library ===
PERSONAS = ["MoCash", "Mentor", "DrillInstructor"]

# === Tone Templates ===
TONE_TEMPLATES = {
    "upbeat": "Hey there! {message} Let's keep the energy going!",
    "stern": "Listen up. {message} Stay sharp.",
    "soothing": "Everything's under control. {message} Take a breath and proceed calmly.",
    "neutral": "{message}"
}

# === Compose response based on mood/voice style ===
def compose_emotional_response(persona, message):
    voice_style = get_voice_style_for_persona(persona)
    template = TONE_TEMPLATES.get(voice_style, TONE_TEMPLATES["neutral"])
    response = template.format(message=message)
    return response

# === Example usage ===
if __name__ == "__main__":
    for persona in PERSONAS:
        sample_message = "The system is running optimally."
        emotional_response = compose_emotional_response(persona, sample_message)
        print(f"[{persona} RESPONSE]: {emotional_response}")

def log_event():ef drop_files_to_bridge():