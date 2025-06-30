from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: whisper_loop_watchdog.py ===

# 🎙️ Whisper Watchdog – Keeps Whisper engine always running

import threading
from whisper_listener import start_whisper_listener

def watchdog_loop():
    print("[WhisperWatchdog] 🔊 Starting loop...")
    while True:
        try:
            start_whisper_listener()
        except Exception as e:
            print(f"[WhisperWatchdog] ❌ Restarting Whisper due to error: {e}")

def log_event():ef drop_files_to_bridge():