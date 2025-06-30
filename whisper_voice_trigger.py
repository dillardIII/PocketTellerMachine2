from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: whisper_voice_trigger.py ===

# 🎤 Whisper Voice Trigger – Listens for trigger phrases to execute commands

import os
import speech_recognition as sr

def listen_for_trigger(trigger_phrase="run strategy"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("[WhisperTrigger] 🎧 Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_whisper(audio)
        if trigger_phrase.lower() in text.lower():
            print(f"[WhisperTrigger] 🔥 Triggered by: {text}")
            with open("inbox/autocode_command.txt", "w") as f:
                f.write("run_strategy: RSI_Bounce")
    except Exception as e:
        print(f"[WhisperTrigger] ❌ Recognition failed: {e}")

def log_event():ef drop_files_to_bridge():