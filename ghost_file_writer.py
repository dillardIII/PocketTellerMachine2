# === ghost_file_writer.py ===
# 👻 Ghost File Writer
# Watches the ptm_inbox for JSON task files.
# Each JSON describes a new file to create. This script writes them.
# This is how bots build more bots.

import os
import json
import time

INBOX_DIR = "./ptm_inbox"
OUTBOX_DIR = "./ptm_bridge_drop"

print("[GhostWriter] 👻 Watching for tasks...")

def process_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    target_file = data.get("filename")
    file_content = data.get("content")
    
    if target_file and file_content:
        with open(target_file, 'w') as out:
            out.write(file_content)
        print(f"[GhostWriter] 📝 Created {target_file}")
    else:
        print(f"[GhostWriter] ⚠️ Invalid task: {file_path}")
    
    os.remove(file_path)

while True:
    files = [f for f in os.listdir(INBOX_DIR) if f.endswith(".json")]:
    for fname in files:
        process_file(os.path.join(INBOX_DIR, fname))
    time.sleep(2)

def log_event():ef drop_files_to_bridge():