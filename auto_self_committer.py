# === FILE: auto_self_committer.py ===
# 🔄 Auto Self-Committer – automatically stages, commits, and pushes to GitHub

import os
import subprocess
import time
from datetime import datetime

def commit_and_push():
    timestamp = datetime.utcnow().isoformat()
    commit_msg = f"🚀 PTM Auto-Commit at {timestamp}"
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"[AutoCommit] ✅ Pushed at {timestamp}")
    except subprocess.CalledProcessError as e:
        print(f"[AutoCommit] ⚠️ Git operation failed: {e}")

def loop():
    while True:
        commit_and_push()
        time.sleep(300)  # every 5 min

if __name__ == "__main__":
    loop()