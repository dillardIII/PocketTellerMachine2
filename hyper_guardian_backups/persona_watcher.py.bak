# === FILE: persona_watcher.py ===
# 👁️ Persona Watcher – Monitors each AI assistant's operational status

import json
import os
import time
from datetime import datetime

WATCH_PATH = "assistants/"
LOG_FILE = "logs/persona_watch.log"
STATUS_FILE = "ui/persona_status.json"

def get_persona_files():
    return [f for f in os.listdir(WATCH_PATH) if f.endswith(".json")]

def check_persona(file):
    try:
        with open(os.path.join(WATCH_PATH, file), "r", encoding="utf-8") as f:
            data = json.load(f)
            return {
                "name": data.get("name"),
                "status": data.get("status", "unknown"),
                "last_updated": data.get("last_updated", "unknown"),
                "file": file
            }
    except Exception as e:
        return {
            "name": file,
            "status": "error",
            "last_updated": None,
            "error": str(e)
        }

def write_persona_status(statuses):
    os.makedirs(os.path.dirname(STATUS_FILE), exist_ok=True)
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(statuses, f, indent=2)

def log_status_update(statuses):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"\n[{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}]\n")
        for persona in statuses:
            log.write(json.dumps(persona) + "\n")

def persona_watch_loop():
    print("[WATCHER] 🕵️ Persona Watcher loop started.")
    while True:
        statuses = [check_persona(p) for p in get_persona_files()]
        write_persona_status(statuses)
        log_status_update(statuses)
        time.sleep(60)