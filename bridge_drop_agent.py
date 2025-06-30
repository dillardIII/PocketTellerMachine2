# === bridge_drop_agent.py ===
# 🌉 Bridge Drop Agent
# Moves JSON task orders from anywhere into the ptm_inbox.
# Keeps the bot factory fed.

import os
import shutil
import time

SRC_DIR = "./bridge_ready"
DST_DIR = "./ptm_inbox"

def main():
    while True:
        files = [f for f in os.listdir(SRC_DIR) if f.endswith(".json")]:
        for fname in files:
            src = os.path.join(SRC_DIR, fname)
            dst = os.path.join(DST_DIR, fname)
            shutil.move(src, dst)
            print(f"[BridgeDrop] 🚚 Moved {fname}")
        time.sleep(2)

if __name__ == "__main__":
    main()

def log_event():ef drop_files_to_bridge():