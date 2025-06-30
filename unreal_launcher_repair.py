from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: unreal_launcher_repair.py ===

# 🛠️ Unreal Launcher Repair – Attempts to verify path, fix launcher issues, and relaunch UE

import os
import subprocess
import json
import datetime

CONFIG_FILE = "predator_target_path.json"
LOG_FILE = "vault/logs/unreal_repair.log"

def log(msg):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {msg}\n")
    print(f"[UnrealRepair] {msg}")

def load_target_path():
    try:
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
            return config.get("command_room_path", None)
    except Exception as e:
        log(f"⚠️ Failed to load config: {e}")
        return None

def repair_unreal():
    path = load_target_path()
    if not path:
        log("❌ No valid Unreal path provided.")
        return

    if not os.path.exists(path):
        log(f"❌ Path does not exist: {path}")
        return

    try:
        log(f"🔧 Attempting to run: {path}")
        subprocess.run([path], check=True)
        log("✅ Unreal Engine launched successfully.")
    except subprocess.CalledProcessError as e:
        log(f"❌ Unreal failed to launch: {e}")
    except Exception as e:
        log(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    repair_unreal()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():