# === FILE: ping_all_nodes.py ===
# 🛰️ Node Pinger – Announces device status and registers presence in the HiveMind network

import os
import time
import socket
from utils.logger import log_event

DEVICE_ID = os.getenv("DEVICE_ID", "UNNAMED_DEVICE")

def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "unknown"

def start_pinging():
    print(f"[Pinger] 📡 Broadcasting node: {DEVICE_ID}")
    while True:
        status = {
            "device": DEVICE_ID,
            "ip": get_ip(),
            "status": "online"
        }
        log_event("Device Ping", status)
        time.sleep(30)