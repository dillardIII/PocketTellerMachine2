# 🛰️ Git Auto Pusher – commits & pushes your empire’s evolving code automatically

import subprocess
import time
import os

def auto_push():
    while True:
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "🤖 Auto evolution commit"], check=True)
            subprocess.run(["git", "push"], check=True)
            print("[GitPusher] ✅ Changes pushed to repo.")
        except Exception as e:
            print(f"[GitPusher] ⚠️ Git push failed: {e}")
        time.sleep(300)

auto_push()