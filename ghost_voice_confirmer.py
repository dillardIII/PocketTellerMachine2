from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
from playsound import playsound  # Assumes playsound is supported in your environment

# Path to voice confirmation MP3s
VOICE_CLIP_PATH = "static/audio/voices/male/mo_cash_preview.mp3"

def confirm_sync(file_name):
    print(f"📢 Mo Cash: File '{file_name}' synced and activated.")
    try:
        playsound(VOICE_CLIP_PATH)
    except Exception as e:
        print(f"⚠️ Voice playback failed: {e}")

def log_event():ef drop_files_to_bridge():