from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: telemetry_bridge.py ===
# 📡 Telemetry Bridge – Collects and broadcasts logs, metrics, and system health

import os
import json
import time
import socket
import threading
from datetime import datetime
from pathlib import Path

# === Configuration ===
LOG_DIR = "logs"
BRIDGE_HOST = "127.0.0.1"
SEND_PORT = 5055   # For sending logs
RECEIVE_PORT = 5053  # For receiving telemetry
BUFFER_SIZE = 2048
TELEMETRY_LISTENERS = []

# === Log Scanner + Sender ===
def format_log_entry(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()[-10:]
        return {
            "file": os.path.basename(file_path),
            "timestamp": datetime.utcnow().isoformat(),
            "log": lines
        }
    except Exception as e:
        return {
            "file": os.path.basename(file_path),
            "error": str(e)
        }

def scan_logs():
    logs = []
    for file in Path(LOG_DIR).glob("*.log"):
        logs.append(format_log_entry(file))
    return logs

def send_logs_to_host(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((BRIDGE_HOST, SEND_PORT))
            s.sendall(json.dumps(data).encode("utf-8"))
            print(f"[TELEMETRY] 📤 Sent telemetry logs")
    except Exception as e:
        print(f"[TELEMETRY] ❌ Failed to send logs: {e}")

def telemetry_loop():
    print("[TELEMETRY] 🔄 Starting telemetry loop...")
    while True:
        logs = scan_logs()
        send_logs_to_host({"type": "telemetry", "data": logs})
        time.sleep(60)

# === Listener + Broadcast Receiver ===
def register_telemetry_listener(func):
    TELEMETRY_LISTENERS.append(func)

def broadcast_telemetry(data):
    print(f"[TELEMETRY] 📈 Broadcasting data: {data}")
    for listener in TELEMETRY_LISTENERS:
        try:
            listener(data)
        except Exception as e:
            print(f"[TELEMETRY] ❌ Listener error: {e}")

def handle_telemetry(client_socket):
    try:
        raw = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        data = json.loads(raw)
        print(f"[TELEMETRY] 📩 Received: {data}")
        broadcast_telemetry(data)
    except Exception as e:
        print(f"[TELEMETRY] ⚠️ Error handling telemetry: {e}")
    finally:
        client_socket.close()

def telemetry_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((BRIDGE_HOST, RECEIVE_PORT))
        server.listen()
        print(f"[TELEMETRY] 🧭 Listening on {BRIDGE_HOST}:{RECEIVE_PORT}...")
        while True:
            client, _ = server.accept()
            threading.Thread(target=handle_telemetry, args=(client,), daemon=True).start()

# === Starter ===
def start_telemetry_bridge():
    threading.Thread(target=telemetry_loop, daemon=True).start()
    threading.Thread(target=telemetry_server, daemon=True).start()
    print("[TELEMETRY] ✅ Bridge online")

if __name__ == "__main__":
    start_telemetry_bridge()
    while True:
        time.sleep(60)

def log_event():ef drop_files_to_bridge():