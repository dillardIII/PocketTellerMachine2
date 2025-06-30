# system_monitor.py
# Monitors system health, file changes, and AI status

import os
import psutil
import time
from datetime import datetime

LOG_PATH = "autonomy_status.log"

def log(msg):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as log_file:
        log_file.write(f"[{timestamp}] {msg}\n")
    print(f"[MONITOR] {msg}")

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def scan_directory_changes(path="."):
    snapshot = {}
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                snapshot[full_path] = os.path.getmtime(full_path)
            except:
                pass
    return snapshot

def monitor_loop(delay=10):
    log("System Monitor Initialized.")
    baseline = scan_directory_changes()
    while True:
        mem = get_memory_usage()
        cpu = get_cpu_usage()
        log(f"Memory: {mem}% | CPU: {cpu}%")

        current_snapshot = scan_directory_changes()
        changes = [f for f in current_snapshot if f not in baseline or current_snapshot[f] != baseline[f]]
        if changes:
            log(f"File Changes Detected: {changes}")
            baseline = current_snapshot

        time.sleep(delay)

if __name__ == "__main__":
    monitor_loop()