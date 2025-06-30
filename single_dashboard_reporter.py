from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: single_dashboard_reporter.py ===
# 🧭 PTM Single Dashboard Reporter
# Prints thread status to console and writes to PTMHealth.json simultaneously.

import threading
import time
import json
from datetime import datetime

HEALTH_FILE = "PTMHealth.json"

def get_health_snapshot():
    threads = threading.enumerate()
    thread_info = []
    for thread in threads:
        thread_info.append({
            "name": thread.name,
            "alive": thread.is_alive()
        })
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "active_threads": thread_info
    }

def dashboard_reporter():
    print("[SingleDashboard] 🧭 Starting unified console + JSON reporter...")
    while True:
        health_data = get_health_snapshot()

        # Print to console
        print("\n=== 🛰️ PTM ACTIVE THREAD STATUS ===")
        for t in health_data["active_threads"]:
            print(f"[THREAD] Name: {t['name']}, Alive: {t['alive']}")
        print(f"Snapshot taken at: {health_data['timestamp']}")
        print("====================================\n")

        # Write to JSON
        with open(HEALTH_FILE, "w") as f:
            json.dump(health_data, f, indent=4)
        time.sleep(5)

if __name__ == "__main__":
    dashboard_reporter()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():