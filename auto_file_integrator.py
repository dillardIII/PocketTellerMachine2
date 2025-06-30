from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_file_integrator.py ===
# 🤖 Auto File Integrator – Monitors ptm_bridge and executes or installs incoming files

import os
import shutil
import time
import subprocess

BRIDGE_DIR = "ptm_bridge"
TARGET_DIR = "."  # Or wherever your main bot files live

def integrate_file(filename):
    src = os.path.join(BRIDGE_DIR, filename)
    dst = os.path.join(TARGET_DIR, filename)

    try:
        shutil.copy2(src, dst)
        print(f"[Integrator] 📥 Integrated: {filename}")

        if filename.endswith(".py"):
            print(f"[Integrator] 🚀 Executing {filename}...")
            subprocess.run(["python3", dst], check=True)

        os.remove(src)
    except Exception as e:
        print(f"[Integrator] ❌ Failed to integrate {filename}: {e}")

def watch_bridge():
    print("[Integrator] 🔍 Watching ptm_bridge for new files...")
    os.makedirs(BRIDGE_DIR, exist_ok=True)

    while True:
        try:
            for file in os.listdir(BRIDGE_DIR):
                if file.endswith(".py"):
                    integrate_file(file)
            time.sleep(3)
        except Exception as e:
            print(f"[Integrator] ⚠️ Error during watch: {e}")
            time.sleep(5)

if __name__ == "__main__":
    watch_bridge()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():