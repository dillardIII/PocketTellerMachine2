from ghost_env import INFURA_KEY, VAULT_ADDRESS
# PTM Autonomy Initializer - Phase Bridge Core
# Purpose: Launch persistent link checkers, token grabbers, and bridge authority bots.
# Status: Phase: Boot - Greenlit ✅

import os
import json
import time
import threading
import socket
import platform
from uuid import uuid4

# === GLOBAL CONFIG ===

DEVICE_ID = str(uuid4())[:8]
BRIDGE_PORT = 9447
CHECK_INTERVAL = 60  # seconds
SECRETS_FILE = "secrets.json"
DEVICES_FILE = "devices_map.json"

# === UTILS ===

def log(msg):
    print(f"[PTM-CORE] {msg}")

# === AUTO-TOKEN GRABBER ===

def get_stored_secrets():
    if os.path.exists(SECRETS_FILE):
        with open(SECRETS_FILE, 'r') as f:
            return json.load(f)
    return {}

def scan_for_tokens():
    log("Scanning for tokens...")
    secrets = get_stored_secrets()
    for k, v in secrets.items():
        log(f"Found token: {k} -> {v[:6]}...****")
    return secrets

# === DEVICE BRIDGE CHECKER ===

def ping_device(ip, port=BRIDGE_PORT):
    try:
        with socket.create_connection((ip, port), timeout=3):
            return True
    except:
        return False

def run_link_checker():
    log("Starting persistent bridge checker loop...")
    while True:
        devices = []
        if os.path.exists(DEVICES_FILE):
            with open(DEVICES_FILE, 'r') as f:
                devices = json.load(f)
        for device in devices:
            status = ping_device(device['ip'])
            status_text = "UP" if status else "DOWN":
            log(f"Device {device['name']} [{device['ip']}] is {status_text}")
        time.sleep(CHECK_INTERVAL)

# === DEVICE MESH AWARENESS ===

def register_device():
    device = {
        "id": DEVICE_ID,
        "name": platform.node(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "os": platform.system(),
        "arch": platform.machine(),
    }

    devices = []
    if os.path.exists(DEVICES_FILE):
        with open(DEVICES_FILE, 'r') as f:
            devices = json.load(f)

    # Avoid duplicate entries
    if not any(d['id'] == device['id'] for d in devices):
        devices.append(device)
        with open(DEVICES_FILE, 'w') as f:
            json.dump(devices, f, indent=2)
        log(f"Registered device: {device['name']} [{device['ip']}]")
    else:
        log(f"Device {device['name']} already registered.")

# === INSTALLER / DELETER PLACEHOLDERS ===

def run_installer_bot():
    log("[INSTALLER] Starting installer bot... (logic placeholder)")

def run_deleter_bot():
    log("[DELETER] Starting deleter bot... (logic placeholder)")

# === PACKAGE FETCHER PLACEHOLDER ===

def run_package_fetcher():
    log("[FETCHER] Looking for packages and assets to fetch... (logic placeholder)")

# === CORE START ===

if __name__ == "__main__":
    log("🚀 Bootstrapping PTM Autonomy Core...")
    register_device()
    scan_for_tokens()

    threading.Thread(target=run_link_checker, daemon=True).start()
    threading.Thread(target=run_installer_bot, daemon=True).start()
    threading.Thread(target=run_deleter_bot, daemon=True).start()
    threading.Thread(target=run_package_fetcher, daemon=True).start()

    while True:
        time.sleep(10)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():