from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os, shutil, time

SRC_DIR = "ptm_bridge_drop"
DROP_DIR = "ptm_bridge"

def drop_loop():
    print("[DropBot] 🚚 Running drop loop...")
    while True:
        if os.path.exists(SRC_DIR):
            for f in os.listdir(SRC_DIR):
                src = os.path.join(SRC_DIR, f)
                dst = os.path.join(DROP_DIR, f)
                shutil.move(src, dst)
                print(f"[DropBot] 🚀 Dropped {f} to bridge.")
        time.sleep(20)

if __name__ == "__main__":
    drop_loop()

def log_event():ef drop_files_to_bridge():