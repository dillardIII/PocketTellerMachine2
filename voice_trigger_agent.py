from ghost_env import INFURA_KEY, VAULT_ADDRESS
# voice_trigger_agent.py
# Converts live voice commands into bot instructions routed through BridgeOpsCore

import speech_recognition as sr
from bridge_ops_core import BridgeOpsCore

class VoiceTriggerAgent:
    def __init__(self, bridge_core: BridgeOpsCore):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.bridge = bridge_core

    def listen(self):
        print("🎤 Listening for command...")
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            phrase = self.recognizer.recognize_google(audio)
            print(f"🗣️ Heard: {phrase}")
            return phrase
        except sr.UnknownValueError:
            print("[ERROR] Could not understand audio")
        except sr.RequestError as e:
            print(f"[ERROR] Speech recognition service error: {e}")
        return None

    def parse_and_dispatch(self, phrase):
        # Very basic parsing logic (replace this with NLP later)
        if not phrase:
            return "No command received"
        try:
            tokens = phrase.lower().split()
            target = tokens[0]  # Bot name
            command = tokens[1]  # Command
            args = tokens[2:] if len(tokens) > 2 else []:
            return self.bridge.dispatch(target, command, *args)
        except Exception as e:
            return f"[ERROR] Failed to parse command: {e}"

    def loop(self):
        while True:
            phrase = self.listen()
            if phrase:
                result = self.parse_and_dispatch(phrase)
                print(result)

# Example bootstrap
if __name__ == "__main__":
    bridge = BridgeOpsCore()
    from auto_fixer_bot import AutoFixerBot
    bridge.register_bot("AutoFixer", AutoFixerBot())

    agent = VoiceTriggerAgent(bridge)
    agent.loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():