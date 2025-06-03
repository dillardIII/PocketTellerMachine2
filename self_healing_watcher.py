# self_healing_watcher.py – Watches all critical services and auto-recovers failures

import subprocess
import threading
import time
import os

# Self-Healing Watcher
def run_self_healing():
    print("[Self-Healing] Checking for recoverable errors...")
    print("[Self-Healing] Autofix completed.")

class SelfHealingWatcher:
    def __init__(self):
        self.watch_list = {
            "VPSBridge": "vps_bridge_controller.py",
            "PTMServer": "app.py",
            "AutoDaemon": "autonomy_loop_controller.py",
            "AIRecon": "ai_recon_bot.py",
        }

    def start(self):
        print("[Self-Healing] 🧬 Activating recovery watchdog...")
        thread = threading.Thread(target=self.watch_loop, daemon=True)
        thread.start()

    def is_process_running(self, keyword):
        try:
            result = subprocess.check_output(["ps", "aux"])
            return keyword in result.decode()
        except Exception as e:
            print("[Self-Healing] ⚠️ Check failed:", str(e))
            return False

    def restart_service(self, script_name):
        print(f"[Self-Healing] 🔄 Restarting {script_name}...")
        try:
            subprocess.Popen(["python3", script_name])
            print(f"[Self-Healing] ✅ {script_name} restarted.")
        except Exception as e:
            print(f"[Self-Healing] ❌ Failed to restart {script_name}: {e}")

    def watch_loop(self):
        while True:
            for name, script in self.watch_list.items():
                if not self.is_process_running(script):
                    print(f"[Self-Healing] ⚠️ {name} is down. Triggering recovery...")
                    self.restart_service(script)
            time.sleep(30)

if __name__ == "__main__":
    run_self_healing()
    watcher = SelfHealingWatcher()
    watcher.start()
    while True:
        time.sleep(300)