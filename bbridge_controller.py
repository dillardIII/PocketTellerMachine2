# bridge_controller.py
# Handles cross-platform handshake logic and bridge activations

import socket
import threading
import time

BRIDGE_PORT = 5050
BRIDGE_HOST = "127.0.0.1"
BRIDGE_STATUS = {"online": False}

def _handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode()
        print(f"[BRIDGE] Received handshake: {data}")
        response = f"[BRIDGE] Handshake ACK: {data}"
        client_socket.send(response.encode())
    finally:
        client_socket.close()

def activate_bridge():
    if BRIDGE_STATUS["online"]:
        print("[BRIDGE] Already active.")
        return

    def bridge_server():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((BRIDGE_HOST, BRIDGE_PORT))
            server.listen()
            BRIDGE_STATUS["online"] = True
            print(f"[BRIDGE] Listening on {BRIDGE_HOST}:{BRIDGE_PORT}...")
            while True:
                client, addr = server.accept()
                client_thread = threading.Thread(target=_handle_client, args=(client,))
                client_thread.start()

    threading.Thread(target=bridge_server, daemon=True).start()
    time.sleep(1)

def bridge_status():
    return BRIDGE_STATUS["online"]