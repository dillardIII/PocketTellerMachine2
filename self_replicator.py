# === FILE: self_replicator.py ===
# 🧬 Self Replicator – Creates clones, backups, or secondary instances of core PTM files for resilience

import os
import shutil
import time

# === Config ===
SOURCE_DIR = "."
BACKUP_DIR = "replica"
EXTENSIONS = [".py", ".json", ".txt"]

def replicate_if_needed():
    print("[Replicator] 🔁 Checking replication state...")
    try:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        replicated_files = 0

        for root, dirs, files in os.walk(SOURCE_DIR):
            for file in files:
                if any(file.endswith(ext) for ext in EXTENSIONS):
                    src_path = os.path.join(root, file)
                    rel_path = os.path.relpath(src_path, SOURCE_DIR)
                    dest_path = os.path.join(BACKUP_DIR, rel_path)

                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.copy2(src_path, dest_path)
                    replicated_files += 1

        print(f"[Replicator] ✅ {replicated_files} files replicated to '{BACKUP_DIR}'.")
    except Exception as e:
        print(f"[Replicator] ❌ Replication failed: {e}")