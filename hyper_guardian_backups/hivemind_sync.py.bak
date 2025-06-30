# === FILE: hivemind_sync.py ===
# 🧠 HiveMind Sync – Synchronizes knowledge, memory, files, and state across instances of PTM or agents

import os
import shutil
import time
from utils.logger import log_event

SYNC_FOLDER = "hivemind"

def sync_all():
    print("[HiveMind] 🔄 Beginning multi-agent sync...")

    if not os.path.exists(SYNC_FOLDER):
        os.makedirs(SYNC_FOLDER)

    memory_files = ["memory/ghostforge_activity_log.json", "memory/task_queue.json"]

    for file in memory_files:
        if os.path.exists(file):
            dst = os.path.join(SYNC_FOLDER, os.path.basename(file))
            shutil.copy2(file, dst)
            log_event("HiveMind Sync", {"synced": file})
            print(f"[HiveMind] 🧬 Synced {file} to {dst}")

    time.sleep(10)