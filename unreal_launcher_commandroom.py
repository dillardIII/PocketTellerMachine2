from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: unreal_launcher_commandroom.py ===

# 🎮 Unreal Uplink – Launches the 3D Command Room with AI Avatars

import os
import subprocess

CONFIG_PATH = "predator_target_path.json"

def get_unreal_path():
    if os.path.exists(CONFIG_PATH):
        import json
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
            return config.get("command_room_path")
    return None

def launch_command_room():
    path = get_unreal_path()
    if not path:
        print("[UnrealUplink] ❌ Command Room path not set.")
        return
    if not os.path.exists(path):
        print(f"[UnrealUplink] ❌ Path does not exist: {path}")
        return
    try:
        subprocess.run([path], check=True)
        print("[UnrealUplink] 🛸 Command Room launched.")
    except Exception as e:
        print(f"[UnrealUplink] ❌ Launch failed: {e}")

if __name__ == "__main__":
    launch_command_room()

def log_event():ef drop_files_to_bridge():