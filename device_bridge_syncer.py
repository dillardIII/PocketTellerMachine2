from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: device_bridge_syncer.py ===
# 🌉 Device Bridge Syncer – Syncs files between devices using the shared bridge folder

import os
import shutil
import time
from utils.logger import log_event

DEVICE_ID = os.getenv("DEVICE_ID", "UNNAMED_DEVICE")
BRIDGE_OUTBOX = "bridge/outbox"
BRIDGE_INBOX = f"bridge/inbox/{DEVICE_ID}"
LOCAL_SYNC_DIRS = ["memory", "vault", "generated_modules"]

def ensure_dirs():
    os.makedirs(BRIDGE_OUTBOX, exist_ok=True)
    os.makedirs(BRIDGE_INBOX, exist_ok=True)

def push_to_bridge():
    for folder in LOCAL_SYNC_DIRS:
        if not os.path.exists(folder):
            continue
        for filename in os.listdir(folder):
            src = os.path.join(folder, filename)
            dst = os.path.join(BRIDGE_OUTBOX, f"{DEVICE_ID}__{filename}")
            shutil.copy2(src, dst)
            log_event("Pushed File", {"device": DEVICE_ID, "file": filename})

def pull_from_bridge():
    for filename in os.listdir(BRIDGE_INBOX):
        src = os.path.join(BRIDGE_INBOX, filename)
        dst = os.path.join("vault", filename)
        shutil.copy2(src, dst)
        os.remove(src)
        log_event("Pulled File", {"device": DEVICE_ID, "file": filename})

def start_sync_loop():
    ensure_dirs()
    print(f"[BridgeSyncer] 🔁 Running bridge sync for: {DEVICE_ID}")
    while True:
        try:
            push_to_bridge()
            pull_from_bridge()
        except Exception as e:
            print(f"[BridgeSyncer] ⚠️ Sync error: {e}")
        time.sleep(10)