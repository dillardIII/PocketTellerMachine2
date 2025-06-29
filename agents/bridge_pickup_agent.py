# === FILE: agents/bridge_pickup_agent.py ===

import os
import time
import shutil

def run_pickup_agent():
    print("[BridgePickup] 🚚 Monitoring bridge_pickup...")
    os.makedirs("bridge_pickup", exist_ok=True)
    os.makedirs("ptm_inbox", exist_ok=True)

    while True:
        for f in os.listdir("bridge_pickup"):
            src = os.path.join("bridge_pickup", f)
            dst = os.path.join("ptm_inbox", f)
            shutil.move(src, dst)
            print(f"[BridgePickup] 📨 Moved {f} to ptm_inbox")
        time.sleep(4)