from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: file_listener_writer.py ===
import os
import time
import shutil
from datetime import datetime

INBOX_DIR = "ptm_inbox"
TARGET_DIR = "ptm_modules"
LOG_FILE = "logs/file_listener.log"

os.makedirs(INBOX_DIR, exist_ok=True)
os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs("logs", exist_ok=True)

def log_event(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.utcnow()}] {message}\n")

def move_and_log(file):
    src = os.path.join(INBOX_DIR, file)
    dst = os.path.join(TARGET_DIR, file)
    shutil.move(src, dst)
    log_event(f"Moved {file} to {TARGET_DIR}")
    print(f"[FileListener] 📦 Moved {file} to {TARGET_DIR}")

while True:
    for f in os.listdir(INBOX_DIR):
        if f.endswith(".py"):
            move_and_log(f)
    time.sleep(3)