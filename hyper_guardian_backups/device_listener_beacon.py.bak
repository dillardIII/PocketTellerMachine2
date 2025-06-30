"""
Device Listener Beacon – PTM Device Mesh Registration + Status

Each device runs this to report its identity, status, and readiness
to the main PTM brain. Enables real-time mapping of available devices.
"""

import os
import socket
import json
from datetime import datetime

DEVICE_REGISTRY = "data/device_mesh.json"

def get_device_name():
    return socket.gethostname()

def register_device(name=None, status="online", role="general"):
    device_name = name or get_device_name()

    device_entry = {
        "name": device_name,
        "status": status,
        "role": role,
        "last_seen": datetime.utcnow().isoformat()
    }

    if not os.path.exists(DEVICE_REGISTRY):
        with open(DEVICE_REGISTRY, "w") as f:
            json.dump([], f)

    with open(DEVICE_REGISTRY, "r") as f:
        registry = json.load(f)

    # Check for existing entry
    updated = False
    for entry in registry:
        if entry["name"] == device_name:
            entry.update(device_entry)
            updated = True
            break

    if not updated:
        registry.append(device_entry)

    with open(DEVICE_REGISTRY, "w") as f:
        json.dump(registry, f, indent=4)

def beacon():
    # Call this in a loop/timer/thread
    register_device()
    print(f"[Beacon] {get_device_name()} is online and reporting for duty.")

if __name__ == "__main__":
    beacon()