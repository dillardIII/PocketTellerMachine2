from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_relay_bot.py ===

# 📡 Ghost Relay – Listens for GPT/AI-generated tasks and appends them to the mission queue

import os
import json
import datetime

MISSION_QUEUE = "vault/mission_queue.json"
LOG_FILE = "vault/logs/ghost_relay.log"

def log(msg):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {msg}\n")
    print(f"[GhostRelay] {msg}")

def inject_task(filename, code, source="GPT"):
    os.makedirs(os.path.dirname(MISSION_QUEUE), exist_ok=True)
    if os.path.exists(MISSION_QUEUE):
        with open(MISSION_QUEUE, "r") as f:
            queue = json.load(f)
    else:
        queue = []

    for task in queue:
        if task["filename"] == filename:
            log(f"🛑 Task {filename} already exists. Skipping.")
            return

    queue.append({
        "filename": filename,
        "code": code,
        "status": "pending"
    })

    with open(MISSION_QUEUE, "w") as f:
        json.dump(queue, f, indent=4)

    log(f"✅ Injected task from {source}: {filename}")

# Example test
if __name__ == "__main__":
    inject_task(
        "ghost_ping.py",
        "# GhostPing\nprint('[GhostRelay] 👻 Ping received.')",
        source="ManualTest"
    )

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():