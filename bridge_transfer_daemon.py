from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_transfer_daemon.py ===
# 📡 Bridge Transfer Daemon – Transfers files between GPT-side and Replit-side bridges in real time

import os
import time
import shutil
from utils.logger import log_event

BRIDGE_INBOX = "bridge/inbox"
BRIDGE_OUTBOX = "bridge/outbox"
BRIDGE_PICKUP = "bridge/pickup"
SYNC_INTERVAL = 3  # seconds

def ensure_folders():
    for folder in [BRIDGE_INBOX, BRIDGE_OUTBOX, BRIDGE_PICKUP]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"[BridgeDaemon] 📂 Created folder: {folder}")

def transfer_outbox_to_pickup():
    files = os.listdir(BRIDGE_OUTBOX)
    for filename in files:
        src = os.path.join(BRIDGE_OUTBOX, filename)
        dst = os.path.join(BRIDGE_PICKUP, filename)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
            os.remove(src)
            print(f"[BridgeDaemon] 🚚 File dropped to pickup: {filename}")
            log_event("Bridge Drop", filename)

def transfer_inbox_to_system():
    files = os.listdir(BRIDGE_INBOX)
    for filename in files:
        src = os.path.join(BRIDGE_INBOX, filename)
        dst = os.path.join(".", filename)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
            os.remove(src)
            print(f"[BridgeDaemon] 📥 File received from inbox: {filename}")
            log_event("Bridge Receive", filename)

def run_bridge_daemon():
    print("[BridgeDaemon] 🛰️ Bridge transfer daemon running...")
    ensure_folders()

    while True:
        try:
            transfer_outbox_to_pickup()
            transfer_inbox_to_system()
        except Exception as e:
            print(f"[BridgeDaemon] ❌ Error during transfer: {e}")
        time.sleep(SYNC_INTERVAL)