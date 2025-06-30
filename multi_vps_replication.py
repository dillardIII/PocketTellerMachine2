from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: multi_vps_replication.py ===
# 🌐 Multi-VPS Replicator – pushes empire files to additional remote VPS hosts
# 🔒 Keeps your empire synced across multiple servers for redundancy and power

import os
import subprocess
import time

# === List of VPS destinations ===
VPS_LIST = [
    "root@198.51.100.1:/root/ptm/",
    "root@203.0.113.5:/root/ptm/"
]

# === Main replication loop ===
while True:
    for vps in VPS_LIST:
        print(f"[Replicator] 🌐 Syncing to {vps}")
        try:
            # Run rsync to copy files, excluding git metadata
            subprocess.run(["rsync", "-az", "--exclude", ".git", ".", vps], check=True)
            print(f"[Replicator] ✅ Successfully synced to {vps}")
        except subprocess.CalledProcessError as e:
            print(f"[Replicator] ❌ Rsync process failed for {vps}: {e}")
        except Exception as e:
            print(f"[Replicator] 🚨 Unexpected error syncing to {vps}: {e}")
    # Wait 10 minutes before next replication cycle
    time.sleep(600)

def log_event():ef drop_files_to_bridge():