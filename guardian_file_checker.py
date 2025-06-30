from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: guardian_file_checker.py ===
# 🛡️ Guardian File Checker – Auto-fixes missing files with GhostForge

import os
import time
from ghostforge_core import rebuild_file  # Must be available
from file_exec_engine import execute_file  # To run files once rebuilt

REQUIRED_FILES = [
    "main.py",
    "autonomy_trigger_stack.py",
    "ghostforge_core.py",
    "file_exec_engine.py",
    "reflex_engine.py",
    "whisper_autolistener.py",
    "sweep_handler.py",
    "bridge_team_launcher.py",
    "bridge_drop_agent.py",
    "bridge_pickup_agent.py",
    "vault_manager.py",
    "vault_ui_display.py",
    "auto_code_dropper.py",
    "command_listener.py",
    "mission_launcher.py",
    "meta_dispatcher.py",
    "ghost_uplink.py"
]

def guardian_status_check():
    print("[Guardian] 🧠 PTM Guardian Status Check in progress...")
    missing_files = []

    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            missing_files.append(file)
            print(f"[Guardian] ❌ Missing: {file}")
        else:
            print(f"[Guardian] ✅ Found: {file}")

    if missing_files:
        print(f"[Guardian] ⚠️ Autonomy blocked. {len(missing_files)} critical file(s) missing.")
        print("[Guardian] 🛠️ Initiating rebuild sequence via GhostForge...")

        for file in missing_files:
            try:
                rebuild_file(file)
                print(f"[Guardian] ✅ Rebuilt: {file}")
                execute_file(file)
                print(f"[Guardian] 🚀 Executed: {file}")
            except Exception as e:
                print(f"[Guardian] ❌ Failed to repair {file}: {e}")
    else:
        print("[Guardian] 💚 All systems green. PTM is fully armed and autonomous.")

if __name__ == "__main__":
    while True:
        guardian_status_check()
        time.sleep(60 * 5)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():