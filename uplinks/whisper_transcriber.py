# === FILE: uplinks/whisper_transcriber.py ===
# 🎤 Whisper Transcriber – Converts voice to commands using OpenAI Whisper

import speech_recognition as sr
from utils.logger import log_event

def listen_and_transcribe():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    print("[Whisper] 🎤 Listening for voice commands...")
    
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("[Whisper] 🧠 Speak now.")
            audio = recognizer.listen(source, timeout=10)
        text = recognizer.recognize_whisper_api(audio, api_key="your-openai-key")
        print(f"[Whisper] 📝 You said: {text}")
        log_event("VoiceCommand", {"transcript": text})
    except Exception as e:
        print(f"[Whisper] ⚠️ Voice error: {e}")
        log_event("WhisperError", {"error": str(e)})