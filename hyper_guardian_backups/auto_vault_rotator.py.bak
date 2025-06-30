# 🔄 Vault Rotator – stores snapshots across rotating logs

import json
import os
import time
from datetime import datetime

ROTATE_DIR = "vault_snapshots"
os.makedirs(ROTATE_DIR, exist_ok=True)

def rotate_vault():
    while True:
        snapshot = {
            "time": datetime.utcnow().isoformat(),
            "assets": random.randint(1000, 5000),
            "partial_keys": random.randint(0, 20)
        }
        fname = f"{ROTATE_DIR}/snapshot_{int(time.time())}.json"
        with open(fname, "w") as f:
            json.dump(snapshot, f, indent=2)
        print(f"[VaultRotator] 💾 Snapshot saved: {fname}")
        time.sleep(600)

if __name__ == "__main__":
    rotate_vault()