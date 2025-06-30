from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: voice_utils.py ===

import os
import requests

# === Voice IDs (replace with yours if needed) ===:
VOICE_IDS = {
    "Mo Cash": "your_mo_cash_voice_id_here",
    "Mentor": "your_mentor_voice_id_here"
}

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
API_URL = "https://api.elevenlabs.io/v1/text-to-speech"

def generate_voice_mp3(text, persona, filename):
    voice_id = VOICE_IDS.get(persona)
    if not voice_id:
        print(f"[ERROR] Voice ID not found for {persona}")
        return None

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }

    response = requests.post(f"{API_URL}/{voice_id}/stream", headers=headers, json=payload)
    if response.status_code == 200:
        audio_path = f"static/audio/{filename}"
        os.makedirs("static/audio", exist_ok=True)
        with open(audio_path, "wb") as f:
            f.write(response.content)
        return audio_path
    else:
        print(f"[ERROR] ElevenLabs response: {response.status_code}")
        return None

def log_event():ef drop_files_to_bridge():