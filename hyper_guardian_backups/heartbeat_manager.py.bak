# 💓 Heartbeat Manager – Sends alive signals and restart warnings to PTM bots

import os
import time
from datetime import datetime
from utils.logger import log_event

HEARTBEAT_FILE = "bridge/status/heartbeat.txt"
HEARTBEAT_INTERVAL = 30  # seconds

os.makedirs(os.path.dirname(HEARTBEAT_FILE), exist_ok=True)

def write_heartbeat():
    timestamp = datetime.utcnow().isoformat()
    with open(HEARTBEAT_FILE, "w") as f:
        f.write(f"💓 PTM ALIVE: {timestamp}\n")
    log_event("Heartbeat", {"timestamp": timestamp})

def start_heartbeat_loop():
    print("[Heartbeat] 💓 Starting PTM heartbeat loop...")
    while True:
        try:
            write_heartbeat()
        except Exception as e:
            log_event("Heartbeat", {"error": str(e)})
        time.sleep(HEARTBEAT_INTERVAL)

if __name__ == "__main__":
    start_heartbeat_loop()