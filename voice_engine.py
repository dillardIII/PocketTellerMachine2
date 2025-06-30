from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: voice_engine.py ===
"""
Triggers ElevenLabs voice playback based on Ghost profile.
"""

import os
import json
from elevenlabs import generate, play, save  # Requires ElevenLabs setup

PROFILE_FILE = "data/ghost_profile.json"
OUTPUT_AUDIO = "static/audio/output.mp3"

def speak_from_ghost_profile(message, profile=None):
    if not profile:
        with open(PROFILE_FILE, "r") as f:
            profile = json.load(f)

    voice_style = profile.get("voice_style", "aggressive")

    audio = generate(
        text=message,
        voice=profile.get("name", "Ghost Gamer"),
        model="eleven_monolingual_v1",
        stream=False
    )

    os.makedirs("static/audio", exist_ok=True)
    save(audio, OUTPUT_AUDIO)
    play(audio)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():