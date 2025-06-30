from ghost_env import INFURA_KEY, VAULT_ADDRESS
import subprocess
import time
import webbrowser
import threading

# === Step 1: Start Cole Flask API Server ===
print("[BOOT]: Starting Cole Flask API server...")
cole_api = subprocess.Popen(["python", "app.py"])
time.sleep(5)

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
print("[BOOT]: Starting Cole Trade Review Generator Daemon...")
trade_review_daemon = subprocess.Popen(["python", "cole_tools/trade_review_daemon.py"])

# === Step 6: Start Voice Summary Generator Daemon ===
print("[BOOT]: Starting Cole Voice Summary Generator Daemon...")
voice_summary_daemon = subprocess.Popen(["python", "cole_tools/voice_summary_daemon.py"])

# === Step 7: Start Voice Narrator Daemon ===
print("[BOOT]: Starting Cole Voice Narrator Daemon...")
voice_narrator_daemon = subprocess.Popen(["python", "cole_tools/voice_narrator_daemon.py"])

# === Step 8: Start Smart Auto Code Trigger Daemon ===
print("[BOOT]: Starting Smart Auto Code Trigger Daemon...")
auto_code_trigger_daemon = subprocess.Popen(["python", "cole_tools/cole_smart_code_trigger_daemon.py"])

# === Step 9: Start Voice Assistant Logger Daemon ===
print("[BOOT]: Starting Voice Assistant Logger Daemon...")
assistant_logger_daemon = subprocess.Popen(["python", "cole_tools/cole_voice_assistant_logger_daemon.py"])

# === Step 10: Start Self Awareness Daemon (NEW Phase 10 feature) ===
print("[BOOT]: Starting Cole Self Awareness Daemon...")
self_awareness_daemon = subprocess.Popen(["python", "cole_tools/cole_self_awareness_daemon.py"])

# === Step 11: Launch Phase 10 Controller UI ===
print("[BOOT]: Launching Phase 10 Controller UI...")
time.sleep(2)
webbrowser.open("http://localhost:5000/cole_phase10_controller")

# === Optional Simulation ===
def delayed_chatgpt_simulation():
    time.sleep(10)
    print("[SIMULATION]: Sending test code to Cole...")
    subprocess.run(["python", "bridge/send_code_to_inbox.py"])

threading.Thread(target=delayed_chatgpt_simulation).start()

# === Monitor all daemons ===
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
    auto_code_trigger_daemon.terminate()
    assistant_logger_daemon.terminate()
    self_awareness_daemon.terminate()
    print("[SHUTDOWN]: All services stopped.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():