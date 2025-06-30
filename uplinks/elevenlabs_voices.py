from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: uplinks/elevenlabs_voice.py ===
# 🗣️ ElevenLabs Voice – Speaks messages in AI voice

import requests
from utils.logger import log_event

ELEVENLABS_API_KEY = "your-elevenlabs-key"
VOICE_ID = "your-voice-id"

def speak_response(text):
    print(f"[Voice] 🗣️ Speaking: {text}")
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}
        }
        response = requests.post(url, json=payload, headers=headers)
        with open("voice_response.mp3", "wb") as f:
            f.write(response.content)
        print("[Voice] ✅ MP3 response saved.")
        log_event("VoiceGenerated", {"text": text})
    except Exception as e:
        print(f"[Voice] ⚠️ Error: {e}")
        log_event("VoiceError", {"error": str(e)})