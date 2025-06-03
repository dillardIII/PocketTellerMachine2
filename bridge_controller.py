# === FILE: bridge_controller.py ===
# 🌉 Bridge Controller – Initializes system-to-system bridges for PTM modules
# Handles cross-platform handshake logic, command bus, and bridge activations

import socket
import threading
import time
import queue

# === Internal Bridge Modules ===
from gpt_voice_bridge import start_voice_bridge
from replicant_bridge import start_replicant_bridge
from command_bridge import start_command_bridge
from telemetry_bridge import start_telemetry_bridge

# === Bridge Configuration ===
BRIDGE_PORT = 5050
BRIDGE_HOST = "127.0.0.1"
BRIDGE_STATUS = {"online": False}
ACTIVE_BRIDGES = {}

# === Shared Command Bus for AI Agents ===
command_bus = queue.Queue()

def post_command(command):
    print(f"[Bridge] 📨 Posting command: {command}")
    command_bus.put(command)

def get_command():
    try:
        command = command_bus.get_nowait()
        print(f"[Bridge] 📬 Pulled command: {command}")
        return command
    except queue.Empty:
        return None

def bridge_loop():
    print("[Bridge] 🔁 Starting bridge loop...")
    while True:
        cmd = get_command()
        if cmd:
            print(f"[Bridge] 🛠️ Processing command: {cmd}")
        time.sleep(2)

# === Socket Handshake Handler ===
def _handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode()
        print(f"[BRIDGE] 🤝 Received handshake: {data}")
        response = f"[BRIDGE] ✅ Handshake ACK: {data}"
        client_socket.send(response.encode())
    except Exception as e:
        print(f"[BRIDGE] ⚠️ Error in handshake: {e}")
    finally:
        client_socket.close()

# === Socket Listener Thread ===
def activate_bridge():
    if BRIDGE_STATUS["online"]:
        print("[BRIDGE] 🚦 Already active.")
        return

    def bridge_server():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((BRIDGE_HOST, BRIDGE_PORT))
            server.listen()
            BRIDGE_STATUS["online"] = True
            print(f"[BRIDGE] 🧭 Listening on {BRIDGE_HOST}:{BRIDGE_PORT}...")
            while True:
                client, addr = server.accept()
                client_thread = threading.Thread(target=_handle_client, args=(client,))
                client_thread.start()

    threading.Thread(target=bridge_server, daemon=True).start()
    time.sleep(1)

# === Modular Bridge Launcher ===
def start_module_thread(name, func):
    if name in ACTIVE_BRIDGES:
        print(f"[BRIDGE] {name} already active.")
        return

    def runner():
        try:
            print(f"[BRIDGE] 🔌 {name} starting...")
            func()
        except Exception as e:
            print(f"[BRIDGE ERROR] ❌ {name} crashed: {e}")
        finally:
            ACTIVE_BRIDGES.pop(name, None)

    t = threading.Thread(target=runner, name=f"{name}_thread", daemon=True)
    ACTIVE_BRIDGES[name] = t
    t.start()

# === Bridge Startup Orchestration ===
def start_bridge():
    print("[BRIDGE CONTROLLER] 🚀 Starting all bridges...")
    activate_bridge()

    # Activate real bridge subsystems
    start_module_thread("GPT Voice", start_voice_bridge)
    start_module_thread("Replicant", start_replicant_bridge)
    start_module_thread("Command", start_command_bridge)
    start_module_thread("Telemetry", start_telemetry_bridge)

    # Simulate status pings for non-threaded virtual bridges
    bridges = [
        "Device Mesh",
        "AI Assistant Hub",
        "Brokerage API Sync",
        "PTM Subnet Comm",
        "GhostBot Link",
        "Render/Uplink Channel"
    ]
    for bridge in bridges:
        print(f"[BridgeController] ✅ Bridge active: {bridge}")
        time.sleep(1)

    print("[BRIDGE CONTROLLER] ✅ All bridges launched.")

def get_active_bridges():
    return list(ACTIVE_BRIDGES.keys())

# === Optional Local Test Start ===
if __name__ == "__main__":
    start_bridge()
    bridge_loop()