# === FILE: command_listener.py ===
# 🕹️ Command Listener – Listens for and reacts to commands from inside or outside the system

import time
from utils.logger import log_event

def start_listener():
    print("[CommandListener] 🎧 Command listener online...")
    while True:
        # Placeholder for command input source
        command = None  # Replace with real interface like speech, API, or console

        if command:
            print(f"[CommandListener] 🧾 Received command: {command}")
            log_event("Command Received", {"command": command})

        time.sleep(3)