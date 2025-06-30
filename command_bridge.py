from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: command_bridge.py ===
# 🧠 Command Bridge – Routes and processes remote/internal commands across agents, devices, and modules

import socket
import json
import threading
from queue import Queue

# === Configuration ===
COMMAND_PORT = 5051
COMMAND_HOST = "127.0.0.1"
BUFFER_SIZE = 2048

# === Listener Registry and Queue ===
COMMAND_LISTENERS = []
command_queue = Queue()

# === Listener Registration ===
def register_listener(func):
    COMMAND_LISTENERS.append(func)

# === Broadcast to Registered Listeners ===
def broadcast_command(command):
    print(f"[COMMAND BRIDGE] 📡 Broadcasting command: {command}")
    for listener in COMMAND_LISTENERS:
        try:
            listener(command)
        except Exception as e:
            print(f"[COMMAND BRIDGE] ❌ Error in listener: {e}")

# === Handle Incoming Socket Connections ===
def handle_client(client_socket):
    try:
        data = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        command = json.loads(data)
        print(f"[COMMAND BRIDGE] 📨 Received: {command}")
        broadcast_command(command)
        command_queue.put(command)
    except Exception as e:
        print(f"[COMMAND BRIDGE] ⚠️ Invalid command: {e}")
    finally:
        client_socket.close()

# === Socket Server Setup ===
def command_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((COMMAND_HOST, COMMAND_PORT))
        server.listen()
        print(f"[COMMAND BRIDGE] 🧭 Listening on {COMMAND_HOST}:{COMMAND_PORT}...")
        while True:
            client, _ = server.accept()
            threading.Thread(target=handle_client, args=(client,), daemon=True).start()

# === Command Processing Loop ===
def command_loop():
    while True:
        if not command_queue.empty():
            cmd = command_queue.get()
            print(f"[COMMAND BRIDGE] 🛠️ Processing: {cmd}")
            # TODO: Execute or route command as needed
        else:
            threading.Event().wait(2)

# === Entry Point ===
def start_command_bridge():
    threading.Thread(target=command_server, daemon=True).start()
    threading.Thread(target=command_loop, daemon=True).start()
    print("[COMMAND BRIDGE] ✅ Bridge active")

if __name__ == "__main__":
    start_command_bridge()
    while True:
        threading.Event().wait(60)

def log_event():ef drop_files_to_bridge():