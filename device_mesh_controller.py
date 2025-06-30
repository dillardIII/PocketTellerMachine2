from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: device_mesh_controller.py ===
"""
Device Mesh Controller:
Tracks registered PTM-compatible devices and their roles in the AI mesh.
Supports real-world awareness of tablets, wearables, keyboards, and more.
"""

import os
import json
from datetime import datetime

DEVICE_FILE = "data/ptm_devices.json"
os.makedirs("data", exist_ok=True)

# === Known role types (for classification)
DEVICE_TYPES = [
    "mobile", "tablet", "watch", "vr", "glasses", "keyboard", "pc", "deck", "hub", "sensor", "mic", "speaker"
]

def load_devices():
    if not os.path.exists(DEVICE_FILE):
        with open(DEVICE_FILE, "w") as f:
            json.dump({}, f)
    with open(DEVICE_FILE, "r") as f:
        return json.load(f)

def save_devices(data):
    with open(DEVICE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def register_device(name, device_type, tags=None, description=""):
    if device_type not in DEVICE_TYPES:
        print(f"[⚠️ Device Mesh] Unknown device type: {device_type}")
        return False

    mesh = load_devices()
    mesh[name] = {
        "type": device_type,
        "tags": tags or [],
        "description": description,
        "status": "active",
        "last_seen": datetime.utcnow().isoformat()
    }
    save_devices(mesh)
    print(f"[🔌 Device Registered] {name} as {device_type}")
    return True

def update_status(name, status="active"):
    mesh = load_devices()
    if name in mesh:
        mesh[name]["status"] = status
        mesh[name]["last_seen"] = datetime.utcnow().isoformat()
        save_devices(mesh)
        print(f"[🔄 Device Status] {name} → {status}")
    else:
        print(f"[❌ Device Not Found] {name}")

def get_device(name):
    return load_devices().get(name)

def list_devices():
    return load_devices()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():