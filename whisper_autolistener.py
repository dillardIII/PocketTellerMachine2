# === FILE: whisper_autolistener.py ===

# 🎙️ Whisper AutoListener – Uses speech_recognition + Whisper for audio transcription

import os
import threading
import queue
import time
import whisper
import speech_recognition as sr

# === Globals ===
audio_queue = queue.Queue()
model = whisper.load_model("base")
AUDIO_FILE_PATH = "temp_voice_input.wav"

# === Record and Save Audio using SpeechRecognition ===
def record_audio():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("[WhisperListener] 🎙️ Voice input system ready.")
    while True:
        try:
            print("[WhisperListener] 🔴 Listening for voice...")
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=10)

            with open(AUDIO_FILE_PATH, "wb") as f:
                f.write(audio.get_wav_data())
            print("[WhisperListener] 💾 Audio saved, queuing for transcription.")
            audio_queue.put(AUDIO_FILE_PATH)

        except sr.WaitTimeoutError:
            print("[WhisperListener] ⏱️ No speech detected (timeout). Listening again...")
        except Exception as e:
            print(f"[WhisperListener] ❌ Mic error: {e}")

# === Transcribe Audio Using Whisper ===
def transcribe_audio():
    while True:
        try:
            audio_path = audio_queue.get()
            print("[WhisperListener] 🧠 Transcribing audio...")
            result = model.transcribe(audio_path)
            print(f"[WhisperListener] ✅ Transcription: {result['text']}")
        except Exception as e:
            print(f"[WhisperListener] ❌ Transcription error: {e}")

# === Start Voice Listener System ===
def start_voice_listener():
    print("[WhisperListener] 🔊 Initializing SpeechRecognition+Whisper...")
    threading.Thread(target=record_audio, daemon=True).start()
    threading.Thread(target=transcribe_audio, daemon=True).start()
    print("[WhisperListener] 🚀 System is online and listening...")

# === Auto-start for testing ===
if __name__ == "__main__":
    start_voice_listener()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[WhisperListener] ⛔ Voice listener shutdown.")