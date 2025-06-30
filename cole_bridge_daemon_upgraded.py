from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_bridge_daemon_upgraded.py

import os
import time
import json
from datetime import datetime
from cole_code_writer import cole_write_code
from cole_command_interpreter import cole_interpret_command

INBOX_FILE = "data/chatgpt_to_cole_inbox.json"
DIRECT_CODE_DIR = "data/chatgpt_direct_inbox"
BRIDGE_LOG_FILE = "data/cole_bridge_daemon_log.json"
CHECK_INTERVAL = 15  # seconds

os.makedirs(DIRECT_CODE_DIR, exist_ok=True)

def log_event(message):
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

def process_inbox_file():
    if not os.path.exists(INBOX_FILE):
        return

    try:
        with open(INBOX_FILE, "r") as f:
            inbox = json.load(f)
    except json.JSONDecodeError:
        log_event("[ERROR]: Invalid JSON in inbox file.")
        return

    if not inbox:
        return

    log_event(f"[BRIDGE]: Processing {len(inbox)} queued commands from inbox...")
    for item in inbox:
        command = item.get("command", "")
        if command:
            result = cole_interpret_command(command)
            log_event(f"[BRIDGE]: Executed command → {command} → {result}")

    # Clear inbox after processing
    with open(INBOX_FILE, "w") as f:
        json.dump([], f, indent=2)

def process_direct_code():
    files = [f for f in os.listdir(DIRECT_CODE_DIR) if f.endswith(".py")]:
    if not files:
        return

    log_event(f"[BRIDGE]: Processing {len(files)} direct code files...")
    for filename in files:
        filepath = os.path.join(DIRECT_CODE_DIR, filename)
        try:
            with open(filepath, "r") as f:
                code = f.read()
            cole_write_code(filename, code)
            log_event(f"[BRIDGE]: Forwarded code file {filename} to Cole Code Writer.")
            os.remove(filepath)
        except Exception as e:
            log_event(f"[ERROR]: Failed to process {filename}: {e}")

def bridge_loop():
    print("[BRIDGE DAEMON]: Upgraded Bridge Daemon running...")
    while True:
        try:
            process_inbox_file()
            process_direct_code()
        except Exception as e:
            log_event(f"[FATAL ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    bridge_loop()