# === FILE: bot_task_trigger.py ===
import os, time, subprocess

def watch_trigger():
    path = "ptm_inbox/run_mission.txt"
    while True:
        if os.path.exists(path):
            print("[Trigger] 🚀 Starting mission_launcher.py")
            os.remove(path)
            subprocess.Popen(["python3", "mission_launcher.py"])
        time.sleep(5)

if __name__ == "__main__":
    watch_trigger()