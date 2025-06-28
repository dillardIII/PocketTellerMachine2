# === FILE: bridge_drop_agent.py ===

# 📤 Bridge Drop Agent – Moves files from ptm_outbox to ptm_bridge

import os
import shutil
import threading
import time

OUTBOX_DIR = "ptm_outbox"
BRIDGE_DIR = "ptm_bridge"

# === Core drop loop
def drop_files_to_bridge():
    print("[DropAgent] 📤 Starting drop loop...")
    while True:
        try:
            if not os.path.exists(OUTBOX_DIR):
                os.makedirs(OUTBOX_DIR)
                print(f"[DropAgent] 📁 Created outbox: {OUTBOX_DIR}")
            if not os.path.exists(BRIDGE_DIR):
                os.makedirs(BRIDGE_DIR)
                print(f"[DropAgent] 📁 Created bridge: {BRIDGE_DIR}")

            for filename in os.listdir(OUTBOX_DIR):
                src = os.path.join(OUTBOX_DIR, filename)
                dst = os.path.join(BRIDGE_DIR, filename)
                shutil.move(src, dst)
                print(f"[DropAgent] 🚀 Moved {filename} → bridge")

            time.sleep(2)
        except Exception as e:
            print(f"[DropAgent] ❌ Drop loop error: {e}")
            time.sleep(5)

# === Threaded starter wrapper (for compatibility)
def run_drop_agent():
    thread = threading.Thread(target=drop_files_to_bridge, daemon=True)
    thread.start()

# Optional direct test
if __name__ == "__main__":
    drop_files_to_bridge()