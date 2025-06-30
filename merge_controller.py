from ghost_env import INFURA_KEY, VAULT_ADDRESS
# merge_controller.py
# Merges files between registered devices using GhostBridge protocol

import os
import json
import shutil
from datetime import datetime

DEVICE_PATHS = {
    "Z Fold 6": "/mnt/zfold6/ptm",
    "S10": "/mnt/s10/ptm",
    "Predator": "/mnt/predator/ptm",
    "SteamDeck": "/mnt/steamdeck/ptm",
    "Slate 7": "/mnt/slate7/ptm"
}

MERGE_LOG = "ghostbridge_sync/merge_log.json"

def log_merge(source, target, file):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "target": target,
        "file": file
    }
    if not os.path.exists(MERGE_LOG):
        history = []
    else:
        with open(MERGE_LOG, "r") as f:
            history = json.load(f)
    history.append(log_entry)
    with open(MERGE_LOG, "w") as f:
        json.dump(history[-300:], f, indent=2)

def sync_folder(source_device, target_device):
    src = DEVICE_PATHS[source_device]
    tgt = DEVICE_PATHS[target_device]

    if not os.path.exists(src) or not os.path.exists(tgt):
        print(f"[Merge] Missing path(s) → {src} or {tgt}")
        return

    for root, _, files in os.walk(src):
        for name in files:
            rel_path = os.path.relpath(os.path.join(root, name), src)
            dest_file = os.path.join(tgt, rel_path)
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            shutil.copy2(os.path.join(root, name), dest_file)
            log_merge(source_device, target_device, rel_path)
            print(f"[Merge] {rel_path} synced from {source_device} → {target_device}")

def full_sync():
    devices = list(DEVICE_PATHS.keys())
    for i in range(len(devices)):
        for j in range(i + 1, len(devices)):
            sync_folder(devices[i], devices[j])
            sync_folder(devices[j], devices[i])

if __name__ == "__main__":
    full_sync()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():