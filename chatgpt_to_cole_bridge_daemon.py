from ghost_env import INFURA_KEY, VAULT_ADDRESS
# chatgpt_to_cole_bridge_daemon.py

import os
import json
import time
from datetime import datetime
import requests

# === Configurations ===
CHATGPT_GENERATED_FILE = "data/chatgpt_generated_code.json"
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"
BRIDGE_LOG_FILE = "data/chatgpt_to_cole_bridge_log.json"
CHECK_INTERVAL = 300  # 5 minutes

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_bridge_event(message):
    logs = []
    if os.path.exists(BRIDGE_LOG_FILE):
        try:
            with open(BRIDGE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(BRIDGE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load ChatGPT generated code queue ===
def load_generated_code():
    if os.path.exists(CHATGPT_GENERATED_FILE):
        try:
            with open(CHATGPT_GENERATED_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Bridge Message Forwarding ===
def forward_code_to_cole(code_entry):
    filename = code_entry.get("filename")
    code_content = code_entry.get("code")
    if not filename or not code_content:
        log_bridge_event("[ERROR]: Missing filename or code content in entry.")
        return

    command = f"UPLOAD_CODE filename='{filename}' code='''{code_content}'''"
    try:
        response = requests.post(COLE_WEBHOOK_URL, json={"command": command})
        if response.ok:
            log_bridge_event(f"[BRIDGE]: Forwarded {filename} to Cole successfully.")
            print(f"[BRIDGE]: Forwarded {filename} to Cole.")
        else:
            log_bridge_event(f"[BRIDGE ERROR]: Failed to send code → {response.status_code}")
            print(f"[BRIDGE ERROR]: {response.status_code} - {response.text}")
    except Exception as e:
        log_bridge_event(f"[BRIDGE ERROR]: {e}")
        print(f"[BRIDGE ERROR]: {e}")

# === Main Bridge Loop ===
def bridge_daemon_loop():
    print("[CHATGPT → COLE BRIDGE DAEMON]: Running...")
    processed_ids = set()

    while True:
        try:
            code_list = load_generated_code()
            for entry in code_list:
                entry_id = entry.get("id") or entry.get("timestamp") or str(entry)
                if entry_id not in processed_ids:
                    forward_code_to_cole(entry)
                    processed_ids.add(entry_id)
        except Exception as e:
            log_bridge_event(f"[ERROR]: {e}")
            print(f"[BRIDGE ERROR]: {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    bridge_daemon_loop()

    # Optional simulation fallback
    # while True:
    #     print("[Daemon]: ChatGPT → Cole Bridge Daemon running... (simulated)")
    #     time.sleep(300)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():