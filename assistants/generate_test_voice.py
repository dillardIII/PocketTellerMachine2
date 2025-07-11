from ghost_env import INFURA_KEY, VAULT_ADDRESS
import requests

# Replace with your actual ElevenLabs API key and Malik's voice ID
ELEVENLABS_API_KEY = "sk_aa6d4f0e9748584264862c38e0fd502b02ce7a27b77957ab"
MALIK_VOICE_ID = "malik.mp3"

text = "This is Malik. If you hear this voice, your ElevenLabs connection works perfectly."

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

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    with open("static/audio/test_malik.mp3", "wb") as f:
        f.write(response.content)
    print("Test MP3 generated successfully.")
else:
    print(f"Error: {response.status_code} - {response.text}")