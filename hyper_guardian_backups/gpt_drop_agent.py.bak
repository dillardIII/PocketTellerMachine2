# === FILE: gpt_drop_agent.py ===
# 🚚 Drop Agent – ChatGPT side drops files into the bridge

import os
import shutil
import time

SOURCE_DIR = "gpt_outbound"
BRIDGE_OUTBOX = "bridge/outbox"

def drop_files_to_bridge():
    print("[Drop Agent] 🚚 Watching for outbound files...")

    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(BRIDGE_OUTBOX, exist_ok=True)

    while True:
        try:
            files = os.listdir(SOURCE_DIR)
            for file in files:
                src = os.path.join(SOURCE_DIR, file)
                dst = os.path.join(BRIDGE_OUTBOX, file)

                if os.path.isfile(src):
                    shutil.copy2(src, dst)
                    print(f"[Drop Agent] ✅ Dropped: {file}")
                    os.remove(src)
        except Exception as e:
            print(f"[Drop Agent] ❌ Error: {e}")

        time.sleep(5)