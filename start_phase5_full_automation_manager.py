from ghost_env import INFURA_KEY, VAULT_ADDRESS
# start_phase5_full_automation_manager.py

import subprocess
import time
import webbrowser
import threading

# === Step 1: Start Cole Flask API Server ===
print("[BOOT]: Starting Cole Flask API server...")
cole_api = subprocess.Popen(["python", "app.py"])
time.sleep(5)  # Ensure API server is fully running before proceeding

# === Step 2: Start ChatGPT → Cole Bridge Daemon ===
print("[BOOT]: Starting ChatGPT → Cole Bridge Daemon...")
bridge_daemon = subprocess.Popen(["python", "bridge/chatgpt_to_cole_bridge_daemon.py"])

# === Step 3: Start Cole Brain Auto Executor Daemon ===
print("[BOOT]: Starting Cole Brain Auto Executor Daemon...")
brain_daemon = subprocess.Popen(["python", "cole_brain_auto_executor.py"])

# === Step 4: Start Cole Cleaner Daemon ===
print("[BOOT]: Starting Cole Cleaner Daemon...")
cleaner_daemon = subprocess.Popen(["python", "cole_tools/cole_cleaner_daemon.py"])

# === Step 5: Open Phase 5 Control Panel UI in browser ===
print("[BOOT]: Launching Phase 5 Controller UI...")
time.sleep(2)
webbrowser.open("http://localhost:5000/cole_phase5_controller")

# === Step 6: Optional - Simulate ChatGPT sending a command after delay ===
def delayed_chatgpt_simulation():
    time.sleep(10)
    print("[SIMULATION]: Sending test code to Cole from ChatGPT bridge...")
    subprocess.run(["python", "bridge/send_code_to_inbox.py"])

threading.Thread(target=delayed_chatgpt_simulation).start()

# === Step 7: Monitor all processes indefinitely ===
try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("[SHUTDOWN]: Stopping all services gracefully...")
    cole_api.terminate()
    bridge_daemon.terminate()
    brain_daemon.terminate()
    cleaner_daemon.terminate()
    print("[SHUTDOWN]: All services have been stopped.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():