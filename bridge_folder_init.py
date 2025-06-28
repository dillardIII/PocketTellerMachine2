# === FILE: bridge_folder_init.py ===

# 📁 Bridge Folder Init – Creates required folders on startup

import os

def init_bridge_folders():
    required_folders = [
        "ptm_bridge",
        "ptm_inbox",
        "ptm_bridge_pending",
        "vault",
        "inbox"
    ]

    for folder in required_folders:
        os.makedirs(folder, exist_ok=True)
        print(f"[BridgeInit] 📁 Ensured folder: {folder}")