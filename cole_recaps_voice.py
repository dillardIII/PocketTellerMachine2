from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import requests

RECAPS_FILE = "data/trade_recaps.json"
AUDIO_OUTPUT_DIR = "static/audio_recaps"
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_RECAP_VOICE_ID", "EXAVITQu4vr4xnSDxMaL")  # Default voice

# === Ensure Directory Exists ===
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)

# === Generate Voice Recap from Text ===
def generate_voice_recap(text, filename="recap.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.9
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        filepath = os.path.join(AUDIO_OUTPUT_DIR, filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
        return {"success": True, "file": filepath}
    else:
        return {"error": response.text}

# === Generate Latest Recap Audio ===
def generate_latest_audio_recap():
    if not os.path.exists(RECAPS_FILE):
        return {"error": "No recaps found."}
    
    with open(RECAPS_FILE, "r") as f:
        recaps = json.load(f).get("recaps", [])
    
    if not recaps:
        return {"error": "No recap entries available."}
    
    latest = recaps[-1]
    summary = latest.get("summary", "")
    timestamp = latest.get("timestamp", "latest")
    filename = f"recap_{timestamp.replace(':', '-').replace('.', '-')}.mp3"

    return generate_voice_recap(summary, filename)

# === Debug Run ===
if __name__ == "__main__":
    result = generate_latest_audio_recap()
    print(result)

def log_event():ef drop_files_to_bridge():