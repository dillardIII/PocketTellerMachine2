import os
import time
import subprocess
import requests

# === CONFIG ===
COLE_API_HEALTH_URL = "http://localhost:5000/trade_health"
COLE_BRAIN_PROCESS = None
COLE_APP_PROCESS = None

# === Check if Cole API is running ===
def is_cole_online():
    try:
        response = requests.get(COLE_API_HEALTH_URL, timeout=5)
        return response.ok
    except:
        return False

# === Start Cole Flask App ===
def start_cole_app():
    global COLE_APP_PROCESS
    if COLE_APP_PROCESS is None or COLE_APP_PROCESS.poll() is not None:
        print("[DAEMON]: Starting Cole App Server...")
        COLE_APP_PROCESS = subprocess.Popen(["python", "app.py"])
        time.sleep(5)

# === Start Cole Brain Daemon ===
def start_cole_brain_daemon():
    global COLE_BRAIN_PROCESS
    if COLE_BRAIN_PROCESS is None or COLE_BRAIN_PROCESS.poll() is not None:
        print("[DAEMON]: Starting Cole Brain Auto Executor...")
        COLE_BRAIN_PROCESS = subprocess.Popen(["python", "cole_brain_auto_executor.py"])
        time.sleep(5)

# === Daemon Loop ===
def run_daemon_loop():
    print("[DAEMON]: Phase 5 Full Bridge Daemon Launcher Started.")
    while True:
        if not is_cole_online():
            print("[DAEMON WARNING]: Cole is offline. Attempting to recover...")
            start_cole_app()
            start_cole_brain_daemon()
        else:
            print("[DAEMON]: Cole is healthy and running.")
        
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    run_daemon_loop()