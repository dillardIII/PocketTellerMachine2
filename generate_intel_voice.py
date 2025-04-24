# generate_intel_voice.py

import requests
from ghostbot.ghost_intel import get_market_intel
from ghostbot.malik_voice_response import style_as_malik
import os

# === YOUR VOICE ID FOR MALIK ===
MALIK_VOICE_ID = "fTZ8X7yIbkNFAYWAdCCl"  # Your selected voice
ELEVEN_API_KEY = "sk_57e909a160f2a40183a11e5135065097853c179aff7d8304"  # Replace this with your real key
TTS_ENDPOINT = "https://api.elevenlabs.io/v1/text-to-speech"

def generate_malik_intel_mp3(ticker="TSLA"):
    intel = get_market_intel(ticker)
    malik_response = style_as_malik(intel, ticker)

    print(f"[+] Generating Malik's voice for {ticker} intel...")

    headers = {
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": malik_response,
        "voice_settings": {
            "stability": 0.65,
            "similarity_boost": 0.8
        }
    }

    response = requests.post(
        f"{TTS_ENDPOINT}/{MALIK_VOICE_ID}",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        os.makedirs("static/voices", exist_ok=True)
        file_path = "static/voices/intel_malik.mp3"
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"[✓] Malik's voice saved to {file_path}")
    else:
        print(f"[✗] Failed: {response.status_code} | {response.text}")

if __name__ == "__main__":
    generate_malik_intel_mp3("TSLA")  # Change "TSLA" to test other tickers