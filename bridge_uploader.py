from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_uploader.py ===
import subprocess
import time
import os

WATCH_DIR = "ptm_modules"
LAST_SEEN = set()

def current_files():
    return set(f for f in os.listdir(WATCH_DIR) if f.endswith(".py")):
:
while True:
    now = current_files()
    new_files = now - LAST_SEEN
    if new_files:
        print(f"[BridgeUploader] 🚀 Detected new modules: {new_files}")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"🔄 Auto commit new modules: {', '.join(new_files)}"])
        subprocess.run(["git", "push"])
        print("[BridgeUploader] ✅ Changes pushed to GitHub.")
    LAST_SEEN = now
    time.sleep(15)

def log_event():ef drop_files_to_bridge():