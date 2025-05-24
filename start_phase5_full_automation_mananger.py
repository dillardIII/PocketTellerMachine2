# start_phase5_full_automation_manager.py

import subprocess
import time
import webbrowser
import threading

# === Step 1: Start Cole API Server ===
print("[BOOT]: Starting Cole Flask API server...")
cole_api = subprocess.Popen(["python", "app.py"])
time.sleep(5)  # Ensure the API server is up

# === Step 2: Start ChatGPT → Cole Bridge Daemon ===
print("[BOOT]: Starting ChatGPT → Cole Bridge Daemon...")
bridge_daemon = subprocess.Popen(["python", "bridge/chatgpt_to_cole_bridge_daemon.py"])

# === Step 3: Open Phase 5 Controller UI ===
print("[BOOT]: Launching Phase 5 Controller UI...")
time.sleep(2)
webbrowser.open("http://localhost:5000/cole_phase5_controller")

# === Step 4: Optional simulation task to show end-to-end bridge working ===
def delayed_chatgpt_simulation():
    time.sleep(10)
    print("[SIMULATION]: Sending demo code to Cole from ChatGPT bridge...")
    subprocess.run(["python", "bridge/send_code_to_inbox.py"])

# Run the optional simulation in background (can be removed in production)
threading.Thread(target=delayed_chatgpt_simulation).start()

# === Step 5: Monitor services forever ===
try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("[SHUTDOWN]: Stopping all services...")
    cole_api.terminate()
    bridge_daemon.terminate()
    print("[SHUTDOWN]: All services stopped.")