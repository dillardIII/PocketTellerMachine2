import requests
import os

# Make sure the voices folder exists
os.makedirs("static/voices", exist_ok=True)

# Replace with your real ElevenLabs API key
API_KEY = "sk_57e909a160f2a40183a11e5135065097853c179aff7d8304"

# Replace with your chosen southern male voice ID from ElevenLabs
voice_id = "ErXwobaYiN019PkySvjV"

# Drill Instructor Quote (Southern Style)
text = "Get in gear, Devil Dog. This market ain't gonna wait for you!"

# ElevenLabs Text-to-Speech endpoint
TTS_ENDPOINT = "https://api.elevenlabs.io/v1/text-to-speech"

# Send request to ElevenLabs API
response = requests.post(
    f"{TTS_ENDPOINT}/{voice_id}",
    headers={
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    },
    json={
        "text": text,
        "voice_settings": {
            "stability": 0.65,
            "similarity_boost": 0.7
        }
    }
)

# Save voice MP3 or print error
if response.status_code == 200:
    with open("static/voices/drill_male_southern.mp3", "wb") as f:
        f.write(response.content)
    print("Voice file for drill_male_southern saved successfully.")
else:
    print("Error generating voice:", response.status_code, response.text)