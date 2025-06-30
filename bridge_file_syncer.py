from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🔁 Syncs files from bridge/outbox to working dir and vice versa

import os
import shutil
import time

BRIDGE_OUTBOX = "bridge/outbox"
PTM_INBOX = "ptm_inbox"
SYNC_INTERVAL = 5  # seconds

def sync_bridge_to_ptm():
    print("[BridgeSync] 🔁 Watching for file transfers...")
    while True:
        for filename in os.listdir(BRIDGE_OUTBOX):
            src = os.path.join(BRIDGE_OUTBOX, filename)
            dst = os.path.join(PTM_INBOX, filename)
            if os.path.isfile(src):
                shutil.move(src, dst)
                print(f"[BridgeSync] 📦 Synced file: {filename}")
        time.sleep(SYNC_INTERVAL)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():