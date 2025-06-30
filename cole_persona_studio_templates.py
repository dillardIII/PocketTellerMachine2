from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_studio_templates.py

import json
import os

# === Configurations ===
PERSONA_TEMPLATE_FILE = "data/persona_templates.json"
MOOD_TEMPLATE_FILE = "data/mood_templates.json"
VOICE_TEMPLATE_FILE = "data/voice_templates.json"
AVATAR_TEMPLATE_FILE = "data/avatar_templates.json"

os.makedirs("data", exist_ok=True)

# === Persona Templates ===
personas = {
    "Mentor": {
        "description": "A calm, wise, and patient teacher persona. Focused on knowledge and guidance.",
        "default_mood": "calm",
        "default_voice": "smooth_deep",
        "default_avatar": "mentor_avatar.png"
    },
    "Mo Cash": {
        "description": "A hustler, street-smart persona. Always energetic, motivational, and upbeat.",
        "default_mood": "hype",
        "default_voice": "energetic_slang",
        "default_avatar": "mocash_avatar.png"
    },
    "Drill Sergeant": {
        "description": "Tough, disciplined, intense military-style persona. Commands respect and urgency.",
        "default_mood": "strict",
        "default_voice": "intense_drill",
        "default_avatar": "drill_avatar.png"
    }
}

# === Mood Templates ===
moods = {
    "happy": "Positive tone, cheerful, encouraging.",
    "frustrated": "Irritated tone, slightly aggressive, pushes harder.",
    "calm": "Neutral tone, smooth, peaceful.",
    "strict": "Commanding tone, serious, fast-paced.",
    "hype": "Over-the-top excitement, loud, intense."
}

# === Voice Templates ===
voices = {
    "smooth_deep": "Deep, calm, warm voice style.",
    "energetic_slang": "Fast, street-style slang, hype voice.",
    "intense_drill": "Military, intense, yelling style voice.",
    "soft_spoken": "Whisper mode, very calm and careful.",
    "sarcastic_edge": "Casual tone, playful, with sarcasm."
}

# === Avatar Templates ===
avatars = {
    "mentor_avatar.png": "Classic professor-style avatar with glasses and calm smile.",
    "mocash_avatar.png": "Cool hustler in flashy outfit, gold chains, confident smile.",
    "drill_avatar.png": "Marine drill instructor avatar with uniform and aggressive pose."
}

# === Save Templates ===
with open(PERSONA_TEMPLATE_FILE, "w") as f:
    json.dump(personas, f, indent=2)

with open(MOOD_TEMPLATE_FILE, "w") as f:
    json.dump(moods, f, indent=2)

with open(VOICE_TEMPLATE_FILE, "w") as f:
    json.dump(voices, f, indent=2)

with open(AVATAR_TEMPLATE_FILE, "w") as f:
    json.dump(avatars, f, indent=2)

print("[PERSONA STUDIO TEMPLATES]: Persona, Mood, Voice, and Avatar templates saved successfully.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():