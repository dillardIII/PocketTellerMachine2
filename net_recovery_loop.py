from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🛠️ Net Recovery Loop – Repairs broken dirs & links for PTM

import os
import time

def recovery_sweep():
    print("[NetRecovery] 🔄 Starting system sweep...")
    time.sleep(2)

    required_dirs = ["ptm_bridge", "ptm_inbox", "vault"]
    for d in required_dirs:
        if not os.path.exists(d):
            os.makedirs(d)
            print(f"[NetRecovery] 🛠️ Restored missing directory: {d}")

    print("[NetRecovery] ✅ Sweep complete.")

if __name__ == "__main__":
    while True:
        recovery_sweep()
        time.sleep(60)  # sweep every 60 seconds

def log_event():ef drop_files_to_bridge():