from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: replit_bot_installer.py ===
# 🤖 Replit Bot Installer – Monitors bridge folder and installs files into PTM.

import os
import shutil
import time

PTM_FOLDER = "ptm"
SOURCE_FOLDER = "bridge/outbox"

def install_files():
    print("[Replit Bot Installer] 🛠️ Watching for incoming files...")

    while True:
        try:
            files = os.listdir(SOURCE_FOLDER)
            for filename in files:
                src = os.path.join(SOURCE_FOLDER, filename)
                dst = os.path.join(PTM_FOLDER, filename)

                if os.path.isfile(src):
                    shutil.copy2(src, dst)
                    print(f"[Replit Bot Installer] ✅ Installed {filename} to PTM.")
                    os.remove(src)
        except Exception as e:
            print(f"[Replit Bot Installer] ❌ Error during install: {e}")
        time.sleep(3)

if __name__ == "__main__":
    install_files()

def log_event():ef drop_files_to_bridge():