# === FILE: ghost_file_listener_writer.py ===
# 👻 Ghost File Listener & Writer – watches for new AI files and drops them to the bridge

import os
import time
import shutil

AI_CODE_DIR = "ai_code_drop"
BRIDGE_DROP_DIR = "bridge_drop"

os.makedirs(AI_CODE_DIR, exist_ok=True)
os.makedirs(BRIDGE_DROP_DIR, exist_ok=True)

print("[GhostFileWriter] 🕵️ Watching for new AI code to push to bridge...")

while True:
    for file in os.listdir(AI_CODE_DIR):
        if file.endswith(".py"):
            src = os.path.join(AI_CODE_DIR, file)
            dst = os.path.join(BRIDGE_DROP_DIR, file)
            shutil.move(src, dst)
            print(f"[GhostFileWriter] 🚀 Moved {file} to bridge_drop.")
    time.sleep(5)