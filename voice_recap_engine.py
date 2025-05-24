# === FILE: voice_recap_engine.py ===

import os
import datetime
from elevenlabs import generate, save
from assistants.malik import malik_report  # or switch to Mo Cash, Mentor, etc.

VOICE_NAME = "Mo Cash"  # Change this per assistant
VOICE_FOLDER = "audio_recaps"
os.makedirs(VOICE_FOLDER, exist_ok=True)

def create_voice_recap(text, filename=None):
    if not filename:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{VOICE_FOLDER}/recap_{timestamp}.mp3"

    try:
        audio = generate(text=text, voice=VOICE_NAME)
        save(audio, filename)
        print(f"[VoiceRecap] Recap saved to {filename}")
        return filename
    except Exception as e:
        print(f"[VoiceRecap] Error generating audio: {e}")
        return None

def recap_trade(trade):
    summary = f"""
    Trade completed using strategy {trade['strategy']}.
    Result: {trade['result']}.
    Grade: {trade['grade']}.
    Good work, boss.
    """
    create_voice_recap(summary.strip())

def recap_build(feature_name):
    summary = f"Feature {feature_name} was successfully built and added to the platform."
    create_voice_recap(summary)

def speak(text):
    create_voice_recap(text)