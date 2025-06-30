# === FILE: system_status_dashboard.py ===
# 🧭 PTM System Status Dashboard
# Prints active threads and what they're doing in real time.

import threading
import time

def print_system_status():
    print("[SystemDashboard] 🧭 Starting PTM System Status Monitor...")
    while True:
        print("\n=== 🛰️ PTM ACTIVE THREAD STATUS ===")
        for thread in threading.enumerate():
            print(f"[THREAD] Name: {thread.name}, Alive: {thread.is_alive()}")
        print("====================================\n")
        time.sleep(5)

if __name__ == "__main__":
    print_system_status()