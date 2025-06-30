from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autobuild_inbox_monitor.py ===
import os
import json
from replit_autobuilder import execute_build_payload

INBOX_DIR = "bridge_packets"

def check_autobuild_inbox(team_name):
    for filename in os.listdir(INBOX_DIR):
        if team_name.lower() in filename.lower():
            file_path = os.path.join(INBOX_DIR, filename)
            with open(file_path, "r") as f:
                packet = json.load(f)

            print(f"[INBOX MONITOR] Processing build task: {packet['task_name']}")
            execute_build_payload(packet)

            # Archive or delete packet
            os.remove(file_path)
            print(f"[INBOX MONITOR] Task complete. Removed: {filename}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():