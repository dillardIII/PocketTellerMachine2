from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase12_avatar_voice_loader.py

import os
import json

# === Paths ===
AVATAR_VOICE_FILE = "data/cole_persona_avatar_voice.json"

# === Load Avatar & Voice Data ===
def load_avatar_voice_data():
    if not os.path.exists(AVATAR_VOICE_FILE):
        return {}

    try:
        with open(AVATAR_VOICE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# === Get persona's avatar and voice ===
def get_persona_avatar_voice(persona_name):
    data = load_avatar_voice_data()
    persona_data = data.get(persona_name)
    if not persona_data:
        return {
            "avatar_url": "https://default_avatar_url.com/default.png",
            "voice_id": "default_voice",
            "avatar_style": "default"
        }
    return persona_data

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():