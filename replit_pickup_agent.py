# === FILE: replit_pickup_agent.py ===
# 🤖 Pickup Agent – Replit bot pulls from bridge and installs into PTM

import os
import shutil
import time

BRIDGE_OUTBOX = "bridge/outbox"
PTM_DIR = "ptm"

def pick_up_from_bridge():
    print("[Pickup Agent] 🤖 Monitoring bridge/outbox for files...")

    os.makedirs(BRIDGE_OUTBOX, exist_ok=True)
    os.makedirs(PTM_DIR, exist_ok=True)

    while True:
        try:
            files = os.listdir(BRIDGE_OUTBOX)
            for file in files:
                src = os.path.join(BRIDGE_OUTBOX, file)
                dst = os.path.join(PTM_DIR, file)

                if os.path.isfile(src):
                    shutil.copy2(src, dst)
                    print(f"[Pickup Agent] 📥 Picked up and installed: {file}")
                    os.remove(src)
        except Exception as e:
            print(f"[Pickup Agent] ❌ Error: {e}")

        time.sleep(5)