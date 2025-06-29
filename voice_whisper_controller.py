# === FILE: voice_whisper_controller.py ===
# 🎤 Voice Whisper Controller – Takes your voice commands to evolve empire
import speech_recognition as sr
from ghost_self_coder import generate_file

r = sr.Recognizer()

def listen_for_commands():
    with sr.Microphone() as source:
        print("[VoiceController] 🎙️ Listening for command...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"[VoiceController] 🎤 Heard: {command}")
        handle_command(command.lower())
    except Exception as e:
        print(f"[VoiceController] ❌ Could not understand: {e}")

def handle_command(text):
    if "dashboard" in text:
        generate_file("dashboard")
    elif "trade" in text or "trader" in text:
        generate_file("trader")
    elif "scraper" in text:
        generate_file("data_scraper")
    else:
        print("[VoiceController] 🤔 Unrecognized instruction.")

while True:
    listen_for_commands()