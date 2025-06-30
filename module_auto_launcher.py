from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: module_auto_launcher.py ===
# 🚀 Module Auto-Launcher – finds and runs all modules in a directory

import os
import subprocess
import time

WATCH_DIR = "ptm_modules"

def auto_launch_modules():
    print("[ModuleLauncher] 🚀 Scanning for modules to auto-launch...")
    os.makedirs(WATCH_DIR, exist_ok=True)
    running = set()

    while True:
        for file in os.listdir(WATCH_DIR):
            if file.endswith(".py") and file not in running:
                path = os.path.join(WATCH_DIR, file)
                print(f"[ModuleLauncher] ▶️ Launching: {file}")
                subprocess.Popen(["python3", path])
                running.add(file)
        time.sleep(10)

if __name__ == "__main__":
    auto_launch_modules()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():