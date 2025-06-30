# === FILE: voice_bridge_elevenlabs.py ===
# 🔊 ElevenLabs Voice Bridge – Converts assistant text to speech using ElevenLabs API

import os
import requests
from utils.logger import log_event
from voice_router import get_active_voice

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1/text-to-speech"

# Example voice ID map (replace with your real ones)
VOICE_ID_MAP = {
    "amandamask": "EXAMPLE_AMANDA_VOICE_ID",
    "mo_cash": "EXAMPLE_MO_CASH_ID",
    "mentor": "EXAMPLE_MENTOR_ID",
    "drill_voice": "EXAMPLE_DRILL_ID"
}

OUTPUT_PATH = "static/audio/voices/summary_output.mp3"

def generate_voice(text, voice_name="amandamask"):
    voice_id = VOICE_ID_MAP.get(voice_name, VOICE_ID_MAP["amandamask"])
    url = f"{ELEVENLABS_API_URL}/{voice_id}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.7
        }
    }

    print(f"[VoiceBridge] 🎙️ Generating voice for: {voice_name}")
    response = requests.post(f"{url}/stream", json=payload, headers=headers)

    if response.status_code == 200:
        with open(OUTPUT_PATH, "wb") as f:
            f.write(response.content)
        print(f"[VoiceBridge] ✅ Voice saved to: {OUTPUT_PATH}")
        log_event("Voice Generated", {"voice": voice_name, "file": OUTPUT_PATH})
        return OUTPUT_PATH
    else:
        print(f"[VoiceBridge] ❌ Failed: {response.status_code}")
        log_event("Voice Generation Error", {"status": response.status_code, "voice": voice_name})
        return None

# === Utility Hook
def speak_dynamic(text):
    active = get_active_voice()
    return generate_voice(text, voice_name=active)