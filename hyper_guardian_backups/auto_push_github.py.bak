# 🚀 AutoPush GitHub – commits & pushes PTM repo to GitHub on loop
# Used for autonomous self-versioning and remote backups

import os
import time

def run_command(cmd):
    result = os.system(cmd)
    if result != 0:
        print(f"[AutoPush] ⚠️ Command failed: {cmd}")
    else:
        print(f"[AutoPush] ✅ Ran: {cmd}")

def auto_push_loop():
    print("[AutoPush] 🚀 Starting autonomous GitHub commit & push loop...")
    while True:
        timestamp_msg = f"auto commit at {time.strftime('%Y-%m-%d %H:%M:%S')}"
        run_command("git add .")
        run_command(f"git commit -m \"{timestamp_msg}\"")
        run_command("git push")
        print("[AutoPush] 🌍 Pushed changes to GitHub.")
        time.sleep(120)  # push every 2 minutes

if __name__ == "__main__":
    auto_push_loop()