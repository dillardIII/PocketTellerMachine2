from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import requests

# Replace this with your real ElevenLabs API key
API_KEY = "sk_57e909a160f2a40183a11e5135065097853c179aff7d8304"

# Folder to save generated MP3s
OUTPUT_DIR = "static/voices"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load voice map and persona quotes
with open("settings/voice_map.json") as vf:
    voice_map = json.load(vf)

with open("settings/quotes.json") as qf:
    quote_map = json.load(qf)

# Loop through each persona, gender, and style
for persona, genders in voice_map.items():
    quote = quote_map.get(persona, "This is a preview of my voice as your financial assistant.")

    for gender, styles in genders.items():
        for style, voice_id in styles.items():
            filename = f"{persona}_{gender}_{style}.mp3"
            filepath = os.path.join(OUTPUT_DIR, filename)

            if os.path.exists(filepath):
                print(f"✓ Already exists: {filename}")
                continue

            print(f"Generating: {filename}")

            response = requests.post(
                f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
                headers={
                    "xi-api-key": API_KEY,
                    "Content-Type": "application/json"
                },
                json={
                    "text": quote,
                    "voice_settings": {
                        "stability": 0.65,
                        "similarity_boost": 0.75
                    }
                }
            )

            if response.status_code == 200:
                with open(filepath, "wb") as f:
                    f.write(response.content)
                print(f"✓ Saved: {filename}")
            else:
                print(f"✗ Failed: {filename} | Status: {response.status_code} | {response.text}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():