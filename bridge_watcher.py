from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_watcher.py ===
# Watches the bridge/outbox folder and auto-syncs to Replit project

import os
import shutil
import time

BRIDGE_FOLDER = "bridge/outbox"
REPO_FOLDER = "."

def auto_sync():
    print("[BridgeWatcher] Watching for files...")
    while True:
        for fname in os.listdir(BRIDGE_FOLDER):
            full_path = os.path.join(BRIDGE_FOLDER, fname)
            dest_path = os.path.join(REPO_FOLDER, fname)

            if os.path.isfile(full_path):
                shutil.copy(full_path, dest_path)
                print(f"[BridgeWatcher] Synced: {fname}")
                os.remove(full_path)

        time.sleep(5)

if __name__ == "__main__":
    auto_sync()

def log_event():ef drop_files_to_bridge():