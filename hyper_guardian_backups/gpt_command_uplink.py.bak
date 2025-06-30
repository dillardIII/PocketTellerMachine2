# === FILE: gpt_command_uplink.py ===
# 🧠 GPT Command Uplink – Allows external AI or human orders to be written to the queue.

import os
import json
import time

QUEUE_FILE = "bridge/commands/command_queue.json"

def send_command(command_text):
    os.makedirs(os.path.dirname(QUEUE_FILE), exist_ok=True)

    commands = []
    if os.path.exists(QUEUE_FILE):
        try:
            with open(QUEUE_FILE, "r") as f:
                commands = json.load(f)
        except:
            commands = []

    commands.append(command_text)

    try:
        with open(QUEUE_FILE, "w") as f:
            json.dump(commands, f, indent=2)
        print(f"[CommandUplink] ✅ Sent command: {command_text}")
    except Exception as e:
        print(f"[CommandUplink] ❌ Failed to write command: {e}")

if __name__ == "__main__":
    while True:
        cmd = input("[CommandUplink] Type command (or 'exit'): ").strip()
        if cmd.lower() == "exit":
            break
        send_command(cmd)