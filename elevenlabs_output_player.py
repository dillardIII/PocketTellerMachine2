from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
ElevenLabs Output Player – Converts text to speech and plays it back
Used by PTM assistants to speak aloud their thoughts or decisions.
"""

import requests
import uuid
import os
import pygame

ELEVENLABS_URL = "http://localhost:5053/voice"
AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def speak_text(text: str, voice_id="default"):
    payload = {
        "text": text,
        "voice_id": voice_id  # Optional: map persona to specific voice
    }

    try:
        response = requests.post(ELEVENLABS_URL, json=payload)
        if response.status_code == 200:
            filename = f"{uuid.uuid4()}.mp3"
            filepath = os.path.join(AUDIO_DIR, filename)
            with open(filepath, "wb") as f:
                f.write(response.content)
            _play_audio(filepath)
            return filename
        else:
            print(f"[🛑 ElevenLabs ERROR] Status {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Voice output failed: {e}")

def _play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()

if __name__ == "__main__":
    speak_text("System online. Welcome back, Boo.")

def log_event():ef drop_files_to_bridge():