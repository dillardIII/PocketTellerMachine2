# === FILE: output_mp3_fallback.py ===
# 🔈 MP3 Fallback Speaker – Plays local MP3 voice files if ElevenLabs or TTS is down

import os
import random

# === Optional Fallback Simulator (headless environments or test mode)
def play_audio(filepath):
    print(f"[FallbackPlayer] Would play audio: {filepath}")

# === Voice directory and example file list
VOICE_DIR = "voice_mp3"
DEFAULT_LINES = [
    "launch_success.mp3",
    "error_warning.mp3",
    "trade_win.mp3",
    "trade_loss.mp3",
    "system_ready.mp3"
]

# === Try importing real playback system
try:
    from playsound import playsound
    USE_PLAYSOUND = True
except ImportError:
    print("[MP3 Fallback] ❌ playsound module missing. Using fallback print method.")
    USE_PLAYSOUND = False

# === Random audio trigger ===
def play_random_line():
    if not os.path.exists(VOICE_DIR):
        print(f"[MP3 Fallback] 🔇 Directory '{VOICE_DIR}' not found.")
        return

    files = [f for f in os.listdir(VOICE_DIR) if f.endswith(".mp3")]
    if not files:
        print("[MP3 Fallback] ❌ No MP3 files found.")
        return

    file_to_play = random.choice(files)
    full_path = os.path.join(VOICE_DIR, file_to_play)

    print(f"[MP3 Fallback] 🔊 Playing: {file_to_play}")
    try:
        if USE_PLAYSOUND:
            playsound(full_path)
        else:
            play_audio(full_path)
    except Exception as e:
        print(f"[MP3 Fallback] ⚠️ Failed to play sound: {e}")

# === Manual test runner ===
if __name__ == "__main__":
    play_random_line()