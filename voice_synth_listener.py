from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🗣️ Voice Synth + Whisper Listener – Speak to it, it responds, learns context.

import speech_recognition as sr
from gtts import gTTS
import os

def listen_and_respond():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    while True:
        print("[VoiceAI] 🎤 Listening...")
        with mic as source:
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"[VoiceAI] 🗣️ Heard: {text}")
            respond_with_voice(f"Hello Boo. You said: {text}")
        except Exception as e:
            print(f"[VoiceAI] ❌ {e}")

def respond_with_voice(text):
    tts = gTTS(text=text)
    fname = f"voice_{int(time.time())}.mp3"
    tts.save(fname)
    os.system(f"mpg123 {fname}")

if __name__ == "__main__":
    listen_and_respond()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():