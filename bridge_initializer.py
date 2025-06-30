from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_initializer.py ===
# 🚀 Bridge Initializer – Sets up folders and triggers initial bridge sync check.

import os
from bridge_test_packet import drop_test_packet
from bridge_sync_controller import run_bridge_sync_loop

def initialize_bridge():
    print("[Bridge Init] 🚧 Initializing bridge system...")

    required_folders = ["bridge/inbox", "bridge/outbox"]
    
    for folder in required_folders:
        try:
            os.makedirs(folder, exist_ok=True)
            print(f"[Bridge Init] 📂 Ensured folder exists: {folder}")
        except Exception as e:
            print(f"[Bridge Init] ❌ Error creating {folder}: {e}")

    print("[Bridge Init] 🧪 Dropping test packet...")
    drop_test_packet()

    print("[Bridge Init] 🔁 Launching sync controller...")
    run_bridge_sync_loop()

if __name__ == "__main__":
    initialize_bridge()

def log_event():ef drop_files_to_bridge():