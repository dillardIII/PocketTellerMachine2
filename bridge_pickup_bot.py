from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_pickup_bot.py ===
# 🚚 Bridge Pickup Bot – moves files from bridge into your live repo

import os
import shutil
import time

BRIDGE_DIR = "ptm_bridge_drop"
LIVE_DIR = "."

def pickup_files_from_bridge():
    if not os.path.exists(BRIDGE_DIR):
        os.makedirs(BRIDGE_DIR)
    files = [f for f in os.listdir(BRIDGE_DIR) if f.endswith(".py")]:
    for f in files:
        src = os.path.join(BRIDGE_DIR, f)
        dest = os.path.join(LIVE_DIR, f)
        shutil.move(src, dest)
        print(f"[BridgePickupBot] 🚀 Moved {f} into live workspace.")

def run_bridge_pickup_loop():
    while True:
        pickup_files_from_bridge()
        time.sleep(10)  # check every 10 sec

if __name__ == "__main__":
    run_bridge_pickup_loop()

def log_event():ef drop_files_to_bridge():