from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_file_listener_writer.py ===
import os
import time
import shutil

SOURCE_DIR = "ptm_modules"
TARGET_DIR = "active_modules"

os.makedirs(TARGET_DIR, exist_ok=True)

def copy_new_modules():
    files = os.listdir(SOURCE_DIR)
    for f in files:
        if f.endswith(".py") and not os.path.exists(os.path.join(TARGET_DIR, f)):
            shutil.copy2(os.path.join(SOURCE_DIR, f), os.path.join(TARGET_DIR, f))
            print(f"[AutoFileWriter] 🚀 Moved {f} into active modules.")

while True:
    copy_new_modules()
    time.sleep(30)

def log_event():ef drop_files_to_bridge():