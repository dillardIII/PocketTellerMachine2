#!/usr/bin/env python3
# auto_clean_bridge_launcher.py
# 🚀 Auto-launches file cleanser + bridge pickup in parallel

import subprocess
import threading
import time

def run_cleanser_watcher():
    subprocess.call(["python3", "auto_file_cleanser_watcher.py"])

def run_bridge_pickup():
    subprocess.call(["python3", "bridge_pickup_agent.py"])

if __name__ == "__main__":
    t1 = threading.Thread(target=run_cleanser_watcher)
    t2 = threading.Thread(target=run_bridge_pickup)

    t1.start()
    t2.start()

    print("[auto_clean_bridge_launcher] ⚡ Empire auto ignition active")

    while True:
        time.sleep(5)

def log_event(data): print(f'[GhostEmpire] LOG: {data}')
def mutate(*args, **kwargs): print('[GhostEmpire] Dummy mutate called')
def drop_files_to_bridge(*args, **kwargs): print('[GhostEmpire] Dummy drop_files_to_bridge called')
