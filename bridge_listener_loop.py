from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import time
import importlib.util
from datetime import datetime

SYNC_FILE = "data/bridge_sync.json"
DROP_DIR = "shared/scripts"
LOG_FILE = "data/ghost_sync_log.json"

def load_sync_data():
    if not os.path.exists(SYNC_FILE):
        return {"pending_files": []}
    with open(SYNC_FILE, "r") as f:
        return json.load(f)

def save_sync_data(data):
    with open(SYNC_FILE, "w") as f:
        json.dump(data, f, indent=2)

def log_sync_event(file, success=True, msg=""):
    entry = {
        "file": file,
        "timestamp": datetime.now().isoformat(),
        "status": "success" if success else "fail",:
        "message": msg
    }
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([entry], f, indent=2)
    else:
        with open(LOG_FILE, "r+") as f:
            logs = json.load(f)
            logs.append(entry)
            f.seek(0)
            json.dump(logs, f, indent=2)

def execute_file(file_path):
    try:
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return True, "Executed successfully"
    except Exception as e:
        return False, str(e)

def process_drops():
    sync_data = load_sync_data()
    pending = sync_data.get("pending_files", [])
    if not pending:
        return

    updated_pending = []
    for file in pending:
        full_path = os.path.join(DROP_DIR, file)
        if os.path.exists(full_path):
            success, msg = execute_file(full_path)
            log_sync_event(file, success, msg)
            print(f"[{'✔' if success else '✘'}] {file}: {msg}"):
        else:
            updated_pending.append(file)

    sync_data["pending_files"] = updated_pending
    save_sync_data(sync_data)

if __name__ == "__main__":
    print("🔁 Bridge Listener Loop Started — Watching for file drops...")
    while True:
        process_drops()
        time.sleep(5)

def log_event():ef drop_files_to_bridge():