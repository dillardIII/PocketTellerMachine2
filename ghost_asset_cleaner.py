from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🧹 Ghost Asset Cleaner – Removes outdated or corrupted files from PTM data folders

import os
import time
from utils.logger import log_event

# === Folders to scan for cleanup ===
TARGET_DIRECTORIES = [
    "vault/",
    "core/",
    "bots/",
    "routes/",
    "scripts/",
    "voices/",
    "data/",
    "ui/",
]

# === File types and keywords considered junk or expired ===
JUNK_EXTENSIONS = [".tmp", ".bak", ".old", ".log"]
JUNK_KEYWORDS = ["_corrupt", "_broken", "_backup"]

def is_junk_file(file_name):
    return (
        any(file_name.endswith(ext) for ext in JUNK_EXTENSIONS) or
        any(keyword in file_name for keyword in JUNK_KEYWORDS)
    )

def clean_assets():
    print("[AssetCleaner] 🧹 Starting asset scan...")
    deleted = 0
    for folder in TARGET_DIRECTORIES:
        if not os.path.exists(folder):
            continue
        for root, _, files in os.walk(folder):
            for file_name in files:
                if is_junk_file(file_name):
                    full_path = os.path.join(root, file_name)
                    try:
                        os.remove(full_path)
                        log_event("AssetCleanup", {"deleted": full_path})
                        deleted += 1
                    except Exception as e:
                        log_event("AssetCleanup", {"error": str(e), "file": full_path})
    print(f"[AssetCleaner] ✅ Cleanup complete. Removed: {deleted} junk files.")

if __name__ == "__main__":
    clean_assets()