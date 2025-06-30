from ghost_env import INFURA_KEY, VAULT_ADDRESS
import subprocess
import time
import os
import json
from datetime import datetime

# === Unified System Components ===
COMPONENTS = {
    "App (UI + APIs)": ["python", "app.py"],
    "Cole Bridge Webhook Listener": ["python", "cole_bridge_webhook_listener.py"],
    "ChatGPT Feedback Listener": ["python", "chatgpt_feedback_listener.py"],
    "ChatGPT to Cole Bridge Daemon": ["python", "chatgpt_to_cole_bridge_daemon.py"],
    "Auto Feedback Sender Daemon": ["python", "auto_feedback_sender_daemon.py"],
    "Smart Feedback Responder Handler": ["python", "smart_feedback_responder_handler.py"],
    "Cole Phase 11 Launcher (Daemons)": ["python", "cole_phase11_launcher.py"],
    "Cole Supervisor Daemon": ["python", "cole_supervisor_daemon.py"],
    "Cole Heartbeat Monitor Daemon": ["python", "cole_heartbeat_monitor_daemon.py"]
}

# === Unified Launcher Configurations ===
UNIFIED_LAUNCHER_LOG = "data/cole_phase11_unified_launcher_log.json"
os.makedirs("data", exist_ok=True)

# === Process Tracker ===
processes = {}

def log_event(message):
    logs = []
    if os.path.exists(UNIFIED_LAUNCHER_LOG):
        try:
            with open(UNIFIED_LAUNCHER_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(UNIFIED_LAUNCHER_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def start_component(name, cmd):
    try:
        proc = subprocess.Popen(cmd)
        processes[name] = proc
        log_event(f"[START]: {name} started.")
        print(f"[UNIFIED LAUNCHER]: {name} started.")
    except Exception as e:
        log_event(f"[ERROR]: Failed to start {name} → {e}")
        print(f"[UNIFIED LAUNCHER ERROR]: Failed to start {name} → {e}")

def monitor_components(interval=60):
    print("[UNIFIED LAUNCHER]: Monitoring components...")
    while True:
        for name, cmd in COMPONENTS.items():
            proc = processes.get(name)
            if proc is None or proc.poll() is not None:
                print(f"[UNIFIED LAUNCHER]: {name} is not running. Restarting...")
                log_event(f"[RESTART]: {name} was down. Restarting...")
                start_component(name, cmd)
        log_event("[UNIFIED LAUNCHER]: All components heartbeat OK.")
        time.sleep(interval)

def start_supervisor():
    print("[UNIFIED LAUNCHER]: Launching Autonomous Supervisor...")
    try:
        subprocess.Popen(["python", "cole_autonomous_supervisor.py"])
        log_event("[UNIFIED LAUNCHER]: Supervisor started successfully.")
    except Exception as e:
        print(f"[UNIFIED LAUNCHER ERROR]: {e}")
        log_event(f"[UNIFIED LAUNCHER ERROR]: {e}")

def unified_launcher_loop():
    print("[UNIFIED LAUNCHER]: Running Phase 11 Full System...")
    log_event("[UNIFIED LAUNCHER]: System starting full autonomous mode.")
    
    # Launch everything
    for name, cmd in COMPONENTS.items():
        start_component(name, cmd)
    
    # Launch supervisor separately (monitors everything internally)
    start_supervisor()

    # Monitor launcher itself (acts as external monitor)
    while True:
        print("[UNIFIED LAUNCHER]: Launcher heartbeat OK.")
        log_event("[UNIFIED LAUNCHER]: Launcher heartbeat OK.")
        time.sleep(300)

if __name__ == "__main__":
    unified_launcher_loop()