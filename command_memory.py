from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: command_memory.py ===
# 🧠 Command Memory Core – Phase 3 Memory AI

import json
import os
from datetime import datetime

MEMORY_FILE = "command_memory_log.json"

def log_command_event(event_type, detail):
    memory = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)

    entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        "detail": detail
    }
    memory.append(entry)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

    print(f"[CommandMemory] 🧠 Logged {event_type}: {detail}")

def show_memory_log():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
            print("[CommandMemory] 🧠 MEMORY LOG:")
            for entry in memory[-10:]:
                print(f"- [{entry['timestamp']}] {entry['event']} | {entry['detail']}")
    else:
        print("[CommandMemory] 🧠 No memory yet.")

def log_event():ef drop_files_to_bridge():