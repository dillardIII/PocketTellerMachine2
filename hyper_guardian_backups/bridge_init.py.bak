# === FILE: bridge_init.py ===
# 🧱 Bridge Init – Ensures folder structure for bridge system exists

import os

FOLDERS = [
    "bridge/inbox",
    "bridge/outbox",
    "ptm_inbox",
    "ptm_outbox",
    "system_logs",
]

def ensure_bridge_folders():
    for folder in FOLDERS:
        try:
            os.makedirs(folder, exist_ok=True)
            print(f"[Bridge Init] ✅ Ensured folder exists: {folder}")
        except Exception as e:
            print(f"[Bridge Init] ❌ Could not create {folder}: {e}")