# 🌐 Device Sync Mapper – Tracks active PTM-connected devices and assigns scan zones

import json
import time
from utils.logger import log_event

DEVICE_FILE = "data/device_map.json"
SCAN_ZONES = ["Northwest", "Northeast", "Southwest", "Southeast", "Skypiea", "DeepCore"]

DEFAULT_DEVICES = {
    "ZFold6": {"zone": "Northwest", "last_ping": 0},
    "Predator": {"zone": "Southeast", "last_ping": 0},
    "S10Ultra": {"zone": "Southwest", "last_ping": 0}
}

def load_devices():
    try:
        with open(DEVICE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_DEVICES

def save_devices(data):
    with open(DEVICE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def ping_device(device_name):
    devices = load_devices()
    if device_name not in devices:
        assigned_zone = SCAN_ZONES[len(devices) % len(SCAN_ZONES)]
        devices[device_name] = {"zone": assigned_zone, "last_ping": time.time()}
        log_event("DeviceSync", {"added": device_name, "zone": assigned_zone})
    else:
        devices[device_name]["last_ping"] = time.time()
        log_event("DeviceSync", {"ping": device_name})
    save_devices(devices)

def get_device_zone(device_name):
    devices = load_devices()
    return devices.get(device_name, {}).get("zone", "Unknown")

if __name__ == "__main__":
    # Manual test pings
    ping_device("ZFold6")
    ping_device("Predator")
    ping_device("S10Ultra")
    print("[DeviceSync] ✅ Devices mapped and synced.")