# === FILE: bridge_pickup_agent.py ===

# 📥 Bridge Pickup Agent – Pulls files from ptm_bridge into ptm_inbox

import os
import shutil
import threading
import time

BRIDGE_DIR = "ptm_bridge"
INBOX_DIR = "ptm_inbox"

# === Threaded Agent Starter ===
def run_pickup_agent():
    print("[BridgePickup] 📥 Pickup agent starting...")

    def pickup_loop():
        while True:
            try:
                if not os.path.exists(BRIDGE_DIR):
                    os.makedirs(BRIDGE_DIR)
                    print(f"[BridgePickup] 📁 Created bridge directory: {BRIDGE_DIR}")
                if not os.path.exists(INBOX_DIR):
                    os.makedirs(INBOX_DIR)
                    print(f"[BridgePickup] 📁 Created inbox directory: {INBOX_DIR}")

                for filename in os.listdir(BRIDGE_DIR):
                    src_path = os.path.join(BRIDGE_DIR, filename)
                    dst_path = os.path.join(INBOX_DIR, filename)
                    shutil.move(src_path, dst_path)
                    print(f"[BridgePickup] 🚚 Moved file: {filename} → inbox")

                time.sleep(2)
            except Exception as e:
                print(f"[BridgePickup] ❌ Error in pickup loop: {e}")
                time.sleep(5)

    thread = threading.Thread(target=pickup_loop, daemon=True)
    thread.start()

# === Direct Loop Runner (non-threaded) ===
def pick_up_from_bridge():
    print("[PickupAgent] 📥 Starting pickup loop...")
    while True:
        try:
            if not os.path.exists(BRIDGE_DIR):
                os.makedirs(BRIDGE_DIR)
                print(f"[PickupAgent] 📁 Created bridge: {BRIDGE_DIR}")
            if not os.path.exists(INBOX_DIR):
                os.makedirs(INBOX_DIR)
                print(f"[PickupAgent] 📁 Created inbox: {INBOX_DIR}")

            for filename in os.listdir(BRIDGE_DIR):
                src = os.path.join(BRIDGE_DIR, filename)
                dst = os.path.join(INBOX_DIR, filename)
                shutil.move(src, dst)
                print(f"[PickupAgent] 📦 Moved {filename} → inbox")

            time.sleep(2)
        except Exception as e:
            print(f"[PickupAgent] ❌ Pickup loop error: {e}")
            time.sleep(5)

# === Standalone Test ===
if __name__ == "__main__":
    pick_up_from_bridge()