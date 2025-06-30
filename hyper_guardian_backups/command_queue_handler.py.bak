# === FILE: command_queue_handler.py ===
# 📬 Command Queue Handler – Reads and manages incoming command orders.

import os
import json

QUEUE_FILE = "bridge/commands/command_queue.json"

def get_next_command():
    if not os.path.exists(QUEUE_FILE):
        print("[CommandQueue] ⚠️ No command queue found.")
        return None

    try:
        with open(QUEUE_FILE, "r") as f:
            commands = json.load(f)
        
        if commands:
            next_cmd = commands.pop(0)
            with open(QUEUE_FILE, "w") as f:
                json.dump(commands, f, indent=2)
            print(f"[CommandQueue] 🎯 Pulled command: {next_cmd}")
            return next_cmd
        else:
            return None
    except Exception as e:
        print(f"[CommandQueue] ❌ Failed to read queue: {e}")
        return None