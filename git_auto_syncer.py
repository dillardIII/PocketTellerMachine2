# === git_auto_syncer.py ===
# 🔗 Git Auto-Syncer
# Commits new files, pushes them, and pulls latest from GitHub on a loop.

import os
import time

def sync_git():
    os.system("git add .")
    os.system("git commit -m '🤖 Auto: new files by GhostBot'")
    os.system("git push")
    os.system("git pull")
    print("[GitSync] 🔄 Repo synced.")

def main():
    while True:
        sync_git()
        time.sleep(60)  # sync every minute

if __name__ == "__main__":
    main()

def log_event():ef drop_files_to_bridge():