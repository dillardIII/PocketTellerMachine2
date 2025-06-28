"""
Whisper Microphone Handler – Real-time voice-to-text input using Whisper API
Captures audio from mic, transcribes, and injects into command dispatcher.
"""

import sounddevice as sd
import numpy as np
import requests
import wave
import uuid
import os

SAMPLE_RATE = 16000
DURATION = 5  # seconds
WHISPER_URL = "http://localhost:5052/transcribe"

def record_audio(filename="temp_voice.wav"):
    print("🎙️ Listening for voice input...")
    recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype=np.int16)
    sd.wait()

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(recording.tobytes())

    return filename

def transcribe_audio(file_path):
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(WHISPER_URL, files=files)
    if response.ok:
        return response.json().get("text", "")
    return "[Whisper ERROR]"

def capture_and_transcribe():
    temp_file = f"audio_input_{uuid.uuid4()}.wav"
    record_audio(temp_file)
    text = transcribe_audio(temp_file)
    print(f"🧠 Transcribed: {text}")
    os.remove(temp_file)
    return text

if __name__ == "__main__":
    capture_and_transcribe()