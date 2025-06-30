from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: mic_voice_trigger.py ===
# 🎙️ Mic Voice Trigger – Uses microphone input to trigger PTM commands live

import speech_recognition as sr
from voice_command_handler import VoiceCommandHandler

class MicVoiceTrigger:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.handler = VoiceCommandHandler()

    def listen_and_execute(self):
        with sr.Microphone() as source:
            print("🎧 Listening... Speak now.")
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio)
            print(f"[VoiceTrigger] 🧠 Heard: {command}")
            self.handler.handle(command)
        except sr.UnknownValueError:
            print("[VoiceTrigger] ❌ Could not understand audio.")
        except sr.RequestError as e:
            print(f"[VoiceTrigger] 🚫 Error with speech service: {e}")

if __name__ == "__main__":
    MicVoiceTrigger().listen_and_execute()

def log_event():ef drop_files_to_bridge():