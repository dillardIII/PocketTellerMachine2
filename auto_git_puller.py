# 🔄 Auto Git Puller for Replit
import subprocess
import time

print("[AutoPull] 🔄 Starting auto git pull loop...")
while True:
    try:
        subprocess.run(["git", "pull"], check=True)
        print("[AutoPull] ✅ Pulled latest changes from GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"[AutoPull] ⚠️ Pull failed: {e}")
    time.sleep(60)  # pulls every 60 sec