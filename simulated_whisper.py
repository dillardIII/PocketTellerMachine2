from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import time

INPUT_FILE = "whisper_sim_input.txt"

def whisper_loop():
    print("[SimulatedWhisper] 🎤 Listening for simulated commands...")
    last_command = ""
    while True:
        if os.path.exists(INPUT_FILE):
            with open(INPUT_FILE, "r") as f:
                command = f.read().strip()
            if command and command != last_command:
                print(f"[SimulatedWhisper] 🔊 Heard: {command}")
                last_command = command
        else:
            print("[SimulatedWhisper] ⚠️ No input file found.")
        time.sleep(10)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():