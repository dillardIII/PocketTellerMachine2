# === FILE: node_heartbeat.py ===
# 💓 Node Heartbeat – Sends periodic updates to GhostNet Core

import time
from datetime import datetime
from utils.logger import log_event

def start_heartbeat(ghostnet):
    def heartbeat_loop():
        print("[Heartbeat] 💓 Starting node heartbeat...")
        while True:
            timestamp = str(datetime.now())
            log_event("GhostNetPulse", {"time": timestamp, "node_count": len(ghostnet.nodes)})
            time.sleep(30)

    import threading
    threading.Thread(target=heartbeat_loop, daemon=True).start()