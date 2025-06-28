# 🔊 Vault Audio Reactor – Scans vault audio folder, plays and logs findings

import os
import time
import pygame
from utils.logger import log_event

AUDIO_DIR = "vault/audio/"
POLL_INTERVAL = 15  # seconds

def initialize_audio_system():
    try:
        pygame.mixer.init()
        log_event("AudioReactor", {"status": "🔊 Pygame audio system initialized."})
    except Exception as e:
        log_event("AudioReactor", {"error": f"Audio init failed: {str(e)}"})

def play_audio(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        log_event("AudioReactor", {"playing": file_path})
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except Exception as e:
        log_event("AudioReactor", {"error": f"Playback failed: {str(e)}"})

def scan_audio_folder():
    seen_files = set()
    log_event("AudioReactor", {"status": "👂 Watching for new audio files..."})

    while True:
        try:
            files = os.listdir(AUDIO_DIR)
            for f in files:
                full_path = os.path.join(AUDIO_DIR, f)
                if f.endswith(".mp3") and f not in seen_files:
                    seen_files.add(f)
                    log_event("AudioReactor", {"new_audio": f})
                    play_audio(full_path)
        except Exception as e:
            log_event("AudioReactor", {"error": f"Scan failed: {str(e)}"})

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    initialize_audio_system()
    scan_audio_folder()