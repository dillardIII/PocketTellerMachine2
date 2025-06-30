from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import time
from datetime import datetime
import requests
from assistants.malik import malik_report

# === Configuration ===
WATCH_FOLDER = "cole_tools"
LOG_FILE = "data/code_update_log.json"
CODE_UPDATE_LOG_FILE = "data/cole_code_update_log.json"
UPDATE_SOURCE_FILE = "data/cole_code_updates.json"
CHECK_INTERVAL_FOLDER = 15  # seconds
CHECK_INTERVAL_UPDATES = 60  # seconds

os.makedirs("data", exist_ok=True)

# === Load/Save Helpers ===
def load_json(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

# === Logging Helper for Code Updates ===
def log_code_update_event(message):
    logs = load_json(CODE_UPDATE_LOG_FILE) if os.path.exists(CODE_UPDATE_LOG_FILE) else []:
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    save_json(CODE_UPDATE_LOG_FILE, logs[-500:])

# === Folder Monitoring ===
def monitor_folder():
    print("[CODE UPDATE LISTENER]: Monitoring cole_tools/ for file changes")
    last_seen = load_json(LOG_FILE) if os.path.exists(LOG_FILE) else {}:
:
    while True:
        current_files = {}
        for filename in os.listdir(WATCH_FOLDER):
            filepath = os.path.join(WATCH_FOLDER, filename)
            if os.path.isfile(filepath):
                mtime = os.path.getmtime(filepath)
                current_files[filename] = mtime

                if filename not in last_seen or last_seen[filename] != mtime:
                    print(f"[CODE UPDATE LISTENER]: Detected update → {filename} at {datetime.now().isoformat()}")
                    last_seen[filename] = mtime
                    log_code_update_event(f"File updated: {filename}")

        save_json(LOG_FILE, last_seen)
        time.sleep(CHECK_INTERVAL_FOLDER)

# === Load Pending Code Updates ===
def load_pending_code_updates():
    return load_json(UPDATE_SOURCE_FILE) if os.path.exists(UPDATE_SOURCE_FILE) else []:
:
# === Save Remaining Updates ===
def save_code_updates(updates):
    save_json(UPDATE_SOURCE_FILE, updates)

# === Apply Code Update ===
def apply_code_update(file_path, code_content):
    try:
        backup_path = f"{file_path}.bak_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        if os.path.exists(file_path):
            os.rename(file_path, backup_path)
            log_code_update_event(f"Backup created: {backup_path}")

        with open(file_path, "w") as f:
            f.write(code_content)
        log_code_update_event(f"Code update applied to: {file_path}")
        malik_report(f"[Code Update] Applied update to {file_path}")

    except Exception as e:
        log_code_update_event(f"Failed to apply code update to {file_path}: {e}")
        malik_report(f"[Code Update ERROR] {e}")

# === Update Listener Loop ===
def code_update_listener_loop():
    print("[Cole Code Update Listener] Monitoring code_updates.json for incoming patches...")
    while True:
        pending_updates = load_pending_code_updates()

        if pending_updates:
            print(f"[Code Update Listener] Found {len(pending_updates)} pending code updates.")
            remaining_updates = []

            for update in pending_updates:
                file_path = update.get("file")
                code_content = update.get("code")

                if file_path and code_content:
                    apply_code_update(file_path, code_content)
                else:
                    log_code_update_event(f"Invalid update entry: {update}")
                    remaining_updates.append(update)

            save_code_updates(remaining_updates)
        else:
            print("[Code Update Listener] No new code updates found.")

        time.sleep(CHECK_INTERVAL_UPDATES)

# === Run Both Folder Monitor and Update Listener ===
if __name__ == "__main__":
    from threading import Thread

    folder_thread = Thread(target=monitor_folder)
    updates_thread = Thread(target=code_update_listener_loop)

    folder_thread.start()
    updates_thread.start()

    folder_thread.join()
    updates_thread.join()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():