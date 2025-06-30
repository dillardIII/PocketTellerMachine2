from ghost_env import INFURA_KEY, VAULT_ADDRESS
import subprocess
import time
import webbrowser
import threading
import requests

print("[BOOT]: Starting Cole Flask API server...")
cole_api = subprocess.Popen(["python", "app.py"])
time.sleep(5)

print("[BOOT]: Starting ChatGPT → Cole Bridge Daemon...")
bridge_daemon = subprocess.Popen(["python", "bridge/chatgpt_to_cole_bridge_daemon.py"])

print("[BOOT]: Starting Cole Webhook Listener...")
cole_webhook_daemon = subprocess.Popen(["python", "cole_bridge_webhook_listener.py"])

print("[BOOT]: Starting ChatGPT Feedback Listener...")
feedback_listener_daemon = subprocess.Popen(["python", "chatgpt_feedback_listener.py"])

print("[BOOT]: Starting Auto Feedback Sender Daemon...")
auto_feedback_sender_daemon = subprocess.Popen(["python", "auto_feedback_sender_daemon.py"])

print("[BOOT]: Starting Smart Feedback Responder Daemon...")
smart_feedback_responder_daemon = subprocess.Popen(["python", "smart_feedback_responder_handler.py"])

print("[BOOT]: Starting Smart Self-Triggered Code Requestor Daemon...")
smart_requestor_daemon = subprocess.Popen(["python", "cole_smart_code_requestor_daemon.py"])

print("[BOOT]: Starting Cole Brain Auto Executor Daemon...")
brain_daemon = subprocess.Popen(["python", "cole_brain_auto_executor.py"])

print("[BOOT]: Starting Cole JSON Cleaner Daemon...")
cleaner_daemon = subprocess.Popen(["python", "cole_tools/cole_cleaner_daemon.py"])

print("[BOOT]: Starting Cole Trade Review Generator Daemon...")
trade_review_daemon = subprocess.Popen(["python", "cole_tools/trade_review_daemon.py"])

print("[BOOT]: Starting Cole Voice Summary Generator Daemon...")
voice_summary_daemon = subprocess.Popen(["python", "cole_tools/voice_summary_daemon.py"])

print("[BOOT]: Starting Cole Voice Narrator Daemon...")
voice_narrator_daemon = subprocess.Popen(["python", "cole_tools/voice_narrator_daemon.py"])

print("[BOOT]: Starting Smart Auto Code Trigger Daemon...")
auto_code_trigger_daemon = subprocess.Popen(["python", "cole_tools/cole_smart_code_trigger_daemon.py"])

print("[BOOT]: Starting Voice Assistant Logger Daemon...")
assistant_logger_daemon = subprocess.Popen(["python", "cole_tools/cole_voice_assistant_logger_daemon.py"])

print("[BOOT]: Starting Self Awareness Daemon...")
self_awareness_daemon = subprocess.Popen(["python", "cole_tools/cole_self_awareness_daemon.py"])

print("[BOOT]: Starting Autonomous Execution Handler...")
autonomous_execution_handler = subprocess.Popen(["python", "cole_autonomous_execution_handler.py"])

print("[BOOT]: Starting Self-Improving Strategy Loop...")
self_improving_strategy_loop = subprocess.Popen(["python", "cole_self_improving_strategy_loop_daemon.py"])

print("[BOOT]: Starting Self-Correction Loop...")
self_correction_loop = subprocess.Popen(["python", "cole_tools/cole_auto_correction_loop_daemon.py"])

print("[BOOT]: Starting Smart GPT-4o Decision Trigger Daemon...")
smart_decision_trigger_daemon = subprocess.Popen(["python", "cole_smart_decision_trigger_daemon.py"])

print("[BOOT]: Starting Self-Healing Error Watcher Daemon...")
self_healing_daemon = subprocess.Popen(["python", "cole_self_healing_error_watcher_daemon.py"])

print("[BOOT]: Starting Heartbeat Monitor Daemon...")
heartbeat_monitor_daemon = subprocess.Popen(["python", "cole_heartbeat_monitor_daemon.py"])

print("[BOOT]: Starting Code Update Listener Daemon...")
code_update_listener_daemon = subprocess.Popen(["python", "cole_code_update_listener_daemon.py"])

print("[BOOT]: Launching Phase 11 Unified Command Center UI...")
time.sleep(2)
webbrowser.open("http://localhost:5000")

def delayed_chatgpt_simulation():
    time.sleep(10)
    try:
        print("[SIMULATION]: Sending test command to Cole Webhook...")
        response = requests.post("http://localhost:5050/cole_webhook", json={"command": "status check"})
        print("[SIMULATION]: Cole Webhook response:", response.json())
    except Exception as e:
        print(f"[SIMULATION ERROR]: {e}")

threading.Thread(target=delayed_chatgpt_simulation).start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print("[SHUTDOWN]: Stopping all services gracefully...")
    cole_api.terminate()
    bridge_daemon.terminate()
    cole_webhook_daemon.terminate()
    feedback_listener_daemon.terminate()
    auto_feedback_sender_daemon.terminate()
    smart_feedback_responder_daemon.terminate()
    smart_requestor_daemon.terminate()
    brain_daemon.terminate()
    cleaner_daemon.terminate()
    trade_review_daemon.terminate()
    voice_summary_daemon.terminate()
    voice_narrator_daemon.terminate()
    auto_code_trigger_daemon.terminate()
    assistant_logger_daemon.terminate()
    self_awareness_daemon.terminate()
    autonomous_execution_handler.terminate()
    self_improving_strategy_loop.terminate()
    self_correction_loop.terminate()
    smart_decision_trigger_daemon.terminate()
    self_healing_daemon.terminate()
    heartbeat_monitor_daemon.terminate()
    code_update_listener_daemon.terminate()
    print("[SHUTDOWN]: All services stopped.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():