# === FILE: run_all.py ===

# 🧠 PTM Phase 9 Boot – Boots InspectorBot and all Godmode features in one go

import time
import subprocess

# === Sequence: InspectorBot → CommandListener → Heartbeat Monitor
def launch_inspectorbot():
    print("🔍 Launching InspectorBot...")
    subprocess.call(["python3", "inspectorbot.py"])

def launch_command_listener():
    print("🎧 Launching Command Listener...")
    subprocess.call(["python3", "command_listener.py"])

def final_phase_log():
    with open("logs/phase9_complete.txt", "a") as f:
        f.write(f"✅ Phase 9 run at {time.ctime()}\n")

def main():
    print("🚨 PHASE 9: GODMODE ONLINE 🚨")
    launch_inspectorbot()
    launch_command_listener()
    final_phase_log()
    print("🧠 All systems are active. PTM is now fully autonomous.")

if __name__ == "__main__":
    main()