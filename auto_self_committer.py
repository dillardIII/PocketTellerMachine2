# === FILE: auto_self_committer.py ===
# 💾 Auto commits & pushes all mutations to GitHub

import subprocess
import time
from datetime import datetime

def auto_commit():
    while True:
        ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"🧬 Auto mutation commit at {ts}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"[AutoCommitter] ✅ Pushed to GitHub at {ts}")
        time.sleep(600)

if __name__ == "__main__":
    auto_commit()