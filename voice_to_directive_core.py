from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Voice to Directive Core
Converts voice commands into PTM instructions.
Tied to assistant personas for context-aware execution.
"""

import speech_recognition as sr
import time
from assistant_directive_router import route_command
from utils.logger import log_event

class VoiceDirectiveCore:
    def __init__(self, persona="Spectra"):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.persona = persona

    def listen_and_convert(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            log_event(f"[🎙️ {self.persona}] Listening for command...")
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio)
            log_event(f"[🔊 {self.persona}] Heard: {command}")
            return command
        except sr.UnknownValueError:
            log_event(f"[⚠️ {self.persona}] Could not understand audio.")
        except sr.RequestError as e:
            log_event(f"[❌ {self.persona}] Voice service error: {e}")
        return None

    def run_loop(self):
        while True:
            command = self.listen_and_convert()
            if command:
                route_command(command, self.persona)
            time.sleep(1)

if __name__ == "__main__":
    vtc = VoiceDirectiveCore(persona="Spectra")
    vtc.run_loop()