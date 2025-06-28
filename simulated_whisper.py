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