from ghost_env import INFURA_KEY, VAULT_ADDRESS
# malik_voice_response.py

import os
import requests

def generate_malik_voice(text, tag):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = os.getenv("MALIK_VOICE_ID", "EXAVITQu4vr4xnSDxMaL")
    safe_tag = tag.replace(":", "_").replace(" ", "_")
    filename = f"intel_{safe_tag}.mp3"
    folder = os.path.join("static", "audio", "recaps")
    path = os.path.join(folder, filename)

    try:
        headers = {
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg"
        }
        payload = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }

        response = requests.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            os.makedirs(folder, exist_ok=True)
            with open(path, "wb") as f:
                f.write(response.content)
            return f"audio/recaps/{filename}"
        else:
            print("Malik voice error:", response.status_code)
    except Exception as e:
        print("Voice gen failed:", e)

    return ""