from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: git_sync_pull.py ===
import os
import time

def sync_loop():
    print("[GitSync] 🔄 Keeping Predator in sync with your empire...")
    while True:
        os.system("git pull origin main")
        time.sleep(60)

if __name__ == "__main__":
    sync_loop()

def log_event():ef drop_files_to_bridge():