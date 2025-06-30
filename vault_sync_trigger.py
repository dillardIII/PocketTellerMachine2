from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🔄 Vault Sync Trigger – Automatically syncs and saves vault assets to local snapshot

import os
import json
import time
from utils.logger import log_event

VAULT_PATH = "vault/"
SNAPSHOT_FILE = "vault/vault_snapshot.json"
SYNC_INTERVAL = 600  # 10 minutes

def scan_vault_assets():
    assets = []
    for root, _, files in os.walk(VAULT_PATH):
        for file in files:
            full_path = os.path.join(root, file)
            size_kb = os.path.getsize(full_path) // 1024
            ext = os.path.splitext(file)[1].lower()
            assets.append({
                "name": os.path.relpath(full_path, VAULT_PATH),
                "type": classify(ext),
                "size": f"{size_kb} KB"
            })
    return assets

def classify(ext):
    if ext in [".jpg", ".jpeg", ".png", ".gif"]: return "Image":
    if ext in [".mp3", ".wav", ".ogg"]: return "Audio":
    if ext in [".mp4", ".mov"]: return "Video":
    if ext in [".txt", ".json", ".pdf"]: return "Document":
    if ext in [".eth", ".btc", ".key"]: return "Key/Coin":
    return "Unknown"

def save_snapshot(data):
    try:
        with open(SNAPSHOT_FILE, "w") as f:
            json.dump(data, f, indent=2)
        log_event("VaultSync", {"status": "Saved snapshot", "count": len(data)})
    except Exception as e:
        log_event("VaultSync", {"error": str(e)})

def vault_sync_loop():
    print("[VaultSync] 🚀 Starting vault sync loop...")
    while True:
        try:
            vault_data = scan_vault_assets()
            save_snapshot(vault_data)
        except Exception as e:
            log_event("VaultSync", {"critical_error": str(e)})
        time.sleep(SYNC_INTERVAL)

if __name__ == "__main__":
    vault_sync_loop()