# === FILE: command_listener.py ===
# 🎙️ Command Listener – Monitors input channels and dispatches commands into the PTM system

import threading
import time
from bridge_controller import post_command

# === Simulated Input Source (replace with real socket, CLI, or web input later) ===
def simulate_command_input():
    sample_commands = [
        "run diagnostics",
        "summarize performance",
        "restart reflex",
        "dispatch alert",
        "generate report",
        None,
        None,
    ]
    return sample_commands[int(time.time()) % len(sample_commands)]

# === Command Listener Loop ===
def start_listener():
    print("[CommandListener] 🎧 Listening for incoming commands...")
    while True:
        command = simulate_command_input()
        if command:
            print(f"[CommandListener] 📥 Received command: {command}")
            post_command(command)
        time.sleep(10)