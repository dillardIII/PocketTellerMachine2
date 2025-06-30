from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import requests

# === CONFIGURATION ===
ELEVENLABS_API_KEY = "sk_aa6d4f0e9748584264862c38e0fd502b02ce7a27b77957ab"      # <-- Insert your API key
MALIK_VOICE_ID = "fTZ8X7yIbkNFAYWAdCCl"   # <-- Insert Malik's ElevenLabs voice ID

# === TEXT TO GENERATE ===
text = "This is Malik. If you hear this voice, your ElevenLabs connection works perfectly."

# === API REQUEST SETUP ===
url = f"https://api.elevenlabs.io/v1/text-to-speech/{MALIK_VOICE_ID}"
headers = {
    "xi-api-key": ELEVENLABS_API_KEY,
    "Content-Type": "application/json",
    "Accept": "audio/mpeg"
}
payload = {
    "text": text,
    "voice_settings": {
        "stability": 0.7,
        "similarity_boost": 0.8
    }
}

# === MAKE REQUEST & SAVE FILE ===
response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    os.makedirs("static/audio", exist_ok=True)  # Ensure folder exists
    with open("static/audio/test_malik.mp3", "wb") as f:
        f.write(response.content)
    print("Test MP3 generated successfully.")
else:
    print(f"Error: {response.status_code} - {response.text}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():