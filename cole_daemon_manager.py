from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import time
import requests
import subprocess

# === Cole Daemon Master ===
def is_cole_alive():
    try:
        response = requests.get("http://localhost:5000/trade_health", timeout=5)
        return response.ok
    except:
        return False

def start_cole_server():
    print("[COLE DAEMON]: Attempting to start Cole...")
    subprocess.Popen(["python", "app.py"])
    time.sleep(5)

def run_daemon_loop():
    print("[COLE DAEMON]: Daemon Manager started.")
    while True:
        if not is_cole_alive():
            print("[COLE DAEMON]: Cole is offline. Restarting...")
            start_cole_server()
        else:
            print("[COLE DAEMON]: Cole is online and healthy.")
        time.sleep(60)

if __name__ == "__main__":
    run_daemon_loop()

def log_event():ef drop_files_to_bridge():