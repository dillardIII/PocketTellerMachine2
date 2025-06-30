from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: voice_trigger_listener.py ===

# 🎙️ Voice Trigger Listener – Listens in loop and writes to command queue

import time
from whisper_voice_trigger import listen_for_trigger

def start_voice_listener():
    print("[VoiceListener] 🎤 Starting voice listener...")
    while True:
        try:
            listen_for_trigger()
            time.sleep(1)
        except Exception as e:
            print(f"[VoiceListener] ❌ Error: {e}")

def log_event():ef drop_files_to_bridge():