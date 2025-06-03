# device_mesh_controller.py – Manages device status, sync, and awareness

import json

devices = {}

def register_device(device_id, device_type, status="offline"):
    devices[device_id] = {
        "type": device_type,
        "status": status
    }
    print(f"[Device Mesh] ✅ Registered {device_id} as {device_type}.")

def update_device_status(device_id, new_status):
    if device_id in devices:
        devices[device_id]["status"] = new_status
        print(f"[Device Mesh] 🔄 {device_id} status updated to {new_status}.")
    else:
        print(f"[Device Mesh] ⚠️ {device_id} not found.")

def get_device_status(device_id):
    return devices.get(device_id, {}).get("status", "unknown")

def list_all_devices():
    return json.dumps(devices, indent=2)

def is_device_online(device_id):
    return devices.get(device_id, {}).get("status") == "online"