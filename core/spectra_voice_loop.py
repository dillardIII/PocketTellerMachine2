from ghost_env import INFURA_KEY, VAULT_ADDRESS
# spectra_voice_loop.py
# Full loop that listens for voice input and builds actual code

import time
from voice_command_bridge import listen_for_voice_command
from voice_to_code_engine import interpret_command_as_code
from autowrite_to_bridge import drop_to_bridge

def start_voice_to_code_loop():
    print("🎙️ Spectra Voice-to-Code Engine online. Speak to create.")
    while True:
        command = listen_for_voice_command()
        if command:
            result = interpret_command_as_code(command)
            drop_to_bridge(result["filename"], result["code"])
        time.sleep(2)