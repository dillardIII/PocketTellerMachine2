# === FILE: ghost_bridge_watcher.py ===
# 👻 GHOST BRIDGE WATCHER
# Commits & pulls to keep Replit, GitHub, Render, local in perfect sync.

import os
import time
from datetime import datetime

LOGBOOK_FILE = "vault_logbook.txt"

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGBOOK_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def sync():
    os.system("git add .")
    os.system("git commit -m '🧬 Auto-sync by ghost_bridge_watcher'")
    os.system("git push origin main")
    os.system("git pull origin main")
    log_action("[ghost_bridge_watcher] 🔗 Synced all platforms.")

def main():
    print("[ghost_bridge_watcher] 👻 Watching & syncing your empire...")
    while True:
        sync()
        time.sleep(60)

if __name__ == "__main__":
    main()