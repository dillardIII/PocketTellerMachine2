# 🎧 Vault Audio Viewer – Auto-plays new audio files added to the vault

import os
import time
import pygame
from utils.logger import log_event

AUDIO_DIR = "vault/audio/"
SUPPORTED_FORMATS = [".mp3", ".wav"]
POLL_INTERVAL = 15  # seconds

def play_audio(file_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"\n🎶 [Playing: {os.path.basename(file_path)}]")
        log_event("AudioViewer", {"played": file_path})

        while pygame.mixer.music.get_busy():
            time.sleep(1)

        pygame.mixer.music.unload()
    except Exception as e:
        log_event("AudioViewer", {"error": f"Audio play failed: {str(e)}"})

def scan_audio_folder():
    seen = set()
    log_event("AudioViewer", {"status": "🎙️ Watching for new audio logs..."})

    while True:
        try:
            for f in os.listdir(AUDIO_DIR):
                full_path = os.path.join(AUDIO_DIR, f)
                if f not in seen and os.path.isfile(full_path):
                    if any(f.endswith(ext) for ext in SUPPORTED_FORMATS):
                        seen.add(f)
                        play_audio(full_path)
        except Exception as e:
            log_event("AudioViewer", {"error": f"Audio scan error: {str(e)}"})

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    scan_audio_folder()