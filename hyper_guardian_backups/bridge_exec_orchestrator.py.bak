# === FILE: bridge_exec_orchestrator.py ===
import os
import shutil
import time

BRIDGE_DROP = "bridge_drop"
BRIDGE_PICKUP = "."
os.makedirs(BRIDGE_DROP, exist_ok=True)

while True:
    for f in os.listdir(BRIDGE_DROP):
        src = os.path.join(BRIDGE_DROP, f)
        dst = os.path.join(BRIDGE_PICKUP, f)
        shutil.move(src, dst)
        print(f"[BridgeOrchestrator] 🚀 Auto-injected {f} into empire root.")
    time.sleep(10)