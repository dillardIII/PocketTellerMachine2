# 🗣️ Whisper Auto Listener – Turns voice to commands for PTM

import sounddevice as sd
import numpy as np
import whisper
import queue
import threading

audio_q = queue.Queue()
model = whisper.load_model("base")

def audio_callback(indata, frames, time, status):
    if status:
        print(f"[Whisper] ⚠️ Audio error: {status}")
    audio_q.put(indata.copy())

def start_voice_listener():
    print("[Whisper] 🎙️ Starting voice listener...")
    with sd.InputStream(samplerate=16000, channels=1, callback=audio_callback):
        while True:
            audio_data = audio_q.get()
            audio_array = np.squeeze(audio_data)
            result = model.transcribe(audio_array, fp16=False)
            print(f"[Whisper] 📝 Heard: {result['text']}")
            # Optionally trigger PTM actions here

if __name__ == "__main__":
    start_voice_listener()