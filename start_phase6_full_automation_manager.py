import subprocess
import time
import webbrowser
import threading

# === Step 1: Start Cole Flask API Server ===
print("[BOOT]: Starting Cole Flask API server...")
cole_api = subprocess.Popen(["python", "app.py"])
time.sleep(5)  # Wait for API server to be fully up

# === Step 2: Start ChatGPT to Cole Bridge Daemon ===
print("[BOOT]: Starting ChatGPT → Cole Bridge Daemon...")
bridge_daemon = subprocess.Popen(["python", "bridge/chatgpt_to_cole_bridge_daemon.py"])

# === Step 3: Start Brain Auto Executor Daemon ===
print("[BOOT]: Starting Cole Brain Auto Executor Daemon...")
brain_daemon = subprocess.Popen(["python", "cole_brain_auto_executor.py"])

# === Step 4: Start JSON Cleaner Daemon ===
print("[BOOT]: Starting Cole JSON Cleaner Daemon...")
cleaner_daemon = subprocess.Popen(["python", "cole_tools/cole_cleaner_daemon.py"])

# === Step 5: Start Trade Review Generator Daemon ===
print("[BOOT]: Starting Cole Trade Review Daemon...")
trade_review_daemon = subprocess.Popen(["python", "cole_tools/trade_review_daemon.py"])

# === Step 6: Start Voice Summary Daemon ===
print("[BOOT]: Starting Cole Voice Summary Daemon...")
voice_summary_daemon = subprocess.Popen(["python", "cole_tools/voice_summary_daemon.py"])

# === Step 7: Launch Phase 6 Controller UI in Browser ===
print("[BOOT]: Launching Phase 6 Controller UI...")
time.sleep(2)
webbrowser.open("http://localhost:5000/cole_phase6_controller")

# === Optional: Simulate ChatGPT command (for test) ===
def delayed_chatgpt_simulation():
    time.sleep(10)
    print("[SIMULATION]: Sending test code to Cole...")
    subprocess.run(["python", "bridge/send_code_to_inbox.py"])

threading.Thread(target=delayed_chatgpt_simulation).start()

# === Step 8: Monitor all daemons ===
try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("[SHUTDOWN]: Stopping all services...")
    cole_api.terminate()
    bridge_daemon.terminate()
    brain_daemon.terminate()
    cleaner_daemon.terminate()
    trade_review_daemon.terminate()
    voice_summary_daemon.terminate()
    print("[SHUTDOWN]: All services stopped.")