from ghost_env import INFURA_KEY, VAULT_ADDRESS
# start_phase7_full_automation_manager.py

import subprocess
import time
import webbrowser
import threading

# === Step 1: Start Cole Flask API Server ===
print("[BOOT]: Starting Cole Flask API server...")
cole_api = subprocess.Popen(["python", "app.py"])
time.sleep(5)  # Wait for API server to be fully up

# === Step 2: Start ChatGPT → Cole Bridge Daemon ===
print("[BOOT]: Starting ChatGPT → Cole Bridge Daemon...")
bridge_daemon = subprocess.Popen(["python", "bridge/chatgpt_to_cole_bridge_daemon.py"])

# === Step 3: Start Brain Auto Executor Daemon ===
print("[BOOT]: Starting Cole Brain Auto Executor Daemon...")
brain_daemon = subprocess.Popen(["python", "cole_brain_auto_executor.py"])

# === Step 4: Start JSON Cleaner Daemon ===
print("[BOOT]: Starting Cole JSON Cleaner Daemon...")
cleaner_daemon = subprocess.Popen(["python", "cole_tools/cole_cleaner_daemon.py"])

# === Step 5: Start Trade Review Generator Daemon ===
print("[BOOT]: Starting Trade Review Generator Daemon...")
trade_review_daemon = subprocess.Popen(["python", "cole_tools/trade_review_daemon.py"])

# === Step 6: Start Voice Summary Generator Daemon ===
print("[BOOT]: Starting Voice Summary Generator Daemon...")
voice_summary_daemon = subprocess.Popen(["python", "cole_tools/voice_summary_daemon.py"])

# === Step 7: Start Voice Narrator Daemon (NEW Phase 7 feature) ===
print("[BOOT]: Starting Voice Narrator Daemon...")
voice_narrator_daemon = subprocess.Popen(["python", "cole_tools/voice_narrator_daemon.py"])

# === Step 8: Launch Phase 7 Controller UI in browser ===
print("[BOOT]: Launching Phase 7 Controller UI...")
time.sleep(2)
webbrowser.open("http://localhost:5000/cole_phase7_controller")

# === Optional: Simulate ChatGPT command (for testing) ===
def delayed_chatgpt_simulation():
    time.sleep(10)
    print("[SIMULATION]: Sending test code to Cole...")
    subprocess.run(["python", "bridge/send_code_to_inbox.py"])

threading.Thread(target=delayed_chatgpt_simulation).start()

# === Step 9: Monitor everything ===
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
    voice_narrator_daemon.terminate()
    print("[SHUTDOWN]: All services stopped.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():