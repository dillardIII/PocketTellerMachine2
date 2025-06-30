from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: wallet_voice_generator.py ===
# 🗣️ PTM Wallet Voice Generator – Live TTS summary with ElevenLabs integration

import os
import requests
from wallet_api_mesh import fetch_all_balances
from utils.logger import log_event

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # You can replace this later

def generate_summary_text():
    balances = fetch_all_balances()
    lines = []

    for label, data in balances.items():
        line = f"{label} has {data['native']:.4f} native coins."
        for token, amount in data["tokens"].items():
            line += f" Plus {amount:.2f} {token}."
        lines.append(line)

    summary = "Here’s your wallet breakdown. " + " ".join(lines)
    log_event("Generated Wallet Summary Text", {"summary": summary})
    return summary

def speak_wallet_summary():
    summary = generate_summary_text()
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": summary,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        with open("static/audio/voices/summary_output.mp3", "wb") as f:
            f.write(response.content)
        log_event("Wallet Summary MP3 Generated", {"status": "success"})
        return "✅ Voice summary generated."
    else:
        error = response.text
        log_event("TTS Generation Failed", {"status": "error", "details": error})
        return f"❌ Failed to generate voice summary: {error}"