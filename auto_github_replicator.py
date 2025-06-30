# === FILE: auto_github_replicator.py ===
# 🚀 Automatically pushes all empire updates to GitHub periodically.

import subprocess
import time
from datetime import datetime

while True:
    timestamp = datetime.utcnow().isoformat()
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"🚀 Auto-sync at {timestamp}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"[GitReplicator] ✅ Pushed changes at {timestamp}")
    except Exception as e:
        print(f"[GitReplicator] ⚠️ Git push failed: {e}")
    time.sleep(300)