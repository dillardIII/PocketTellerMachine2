# === FILE: voice_mic_listener.py ===
# 🎙️ Voice Mic Listener – Listens to microphone input and sends commands to AssistantDispatch

import speech_recognition as sr
from assistant_dispatch import AssistantDispatch

class VoiceMicListener:
    def __init__(self):
        self.dispatch = AssistantDispatch()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        print("[VoiceMicListener] 🎧 Microphone initialized.")

    def listen_loop(self):
        print("[VoiceMicListener] 🔁 Starting voice command loop. Say something...")

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

            while True:
                try:
                    print("[VoiceMicListener] 🎤 Listening...")
                    audio = self.recognizer.listen(source, timeout=5)

                    print("[VoiceMicListener] ⏳ Processing...")
                    text = self.recognizer.recognize_google(audio)

                    print(f"[VoiceMicListener] ✅ You said: {text}")
                    self.dispatch.process_voice_command(text)

                except sr.WaitTimeoutError:
                    print("[VoiceMicListener] ⌛ Timeout waiting for speech...")
                except sr.UnknownValueError:
                    print("[VoiceMicListener] ❌ Couldn’t understand you.")
                except sr.RequestError as e:
                    print(f"[VoiceMicListener] 🔌 Request error: {e}")
                except Exception as e:
                    print(f"[VoiceMicListener] 💥 Error: {e}")