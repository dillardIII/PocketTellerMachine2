import requests
import os

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")  # Set your ElevenLabs API Key in environment variables
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "EXAVITQu4vr4xnSDxMaL")  # Default voice or your custom one

def generate_voice_mp3(text, output_path):
    if not ELEVENLABS_API_KEY:
        print("[VOICE NARRATOR]: Missing ElevenLabs API key. Cannot generate voice.")
        return False

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            print(f"[VOICE NARRATOR]: Voice MP3 generated at {output_path}")
            return True
        else:
            print(f"[VOICE NARRATOR ERROR]: API returned {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print(f"[VOICE NARRATOR ERROR]: {e}")
        return False