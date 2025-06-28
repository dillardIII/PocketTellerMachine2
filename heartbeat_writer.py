# === FILE: heartbeat_writer.py ===
# ❤️ Heartbeat Writer – Keeps heartbeat.txt alive for watchdog

import time
import os

HEARTBEAT_PATH = "bridge/heartbeat.txt"
INTERVAL = 5  # seconds

def write_heartbeat():
    print("[HeartbeatWriter] ❤️ Starting heartbeat writer...")
    while True:
        try:
            with open(HEARTBEAT_PATH, "w") as f:
                f.write("alive")
            print("[HeartbeatWriter] 💓 Heartbeat written.")
        except Exception as e:
            print(f"[HeartbeatWriter] ❌ Failed to write heartbeat: {e}")
        time.sleep(INTERVAL)