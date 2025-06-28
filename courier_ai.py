# === courier_ai.py ===
"""
Courier AI – Autonomous Bridge File Transporter
Delivers payloads between drop zones (bridges) inside PTM or across synced devices.
"""

import os
import shutil
import json
from datetime import datetime
from utils.logger import log_event

COURIER_LOG = "memory/courier_activity_log.json"
BRIDGE_CONFIG = "memory/bridge_config.json"
INBOX_DIR = "bridge/inbox"

class CourierAI:
    def __init__(self, persona="CourierBot"):
        self.persona = persona
        self.bridges = self.load_bridges()
        self.ensure_inbox()
        self.history = self.load_log()

    def ensure_inbox(self):
        os.makedirs(INBOX_DIR, exist_ok=True)

    def load_bridges(self):
        if not os.path.exists(BRIDGE_CONFIG):
            return []
        with open(BRIDGE_CONFIG, "r") as f:
            return json.load(f).get("bridges", [])

    def load_log(self):
        if not os.path.exists(COURIER_LOG):
            return []
        with open(COURIER_LOG, "r") as f:
            return json.load(f)

    def save_log(self):
        with open(COURIER_LOG, "w") as f:
            json.dump(self.history[-500:], f, indent=2)

    def deliver_file(self, filename, destination_bridge_name):
        source_path = os.path.join(INBOX_DIR, filename)
        bridge = next((b for b in self.bridges if b["name"] == destination_bridge_name), None)

        if not bridge:
            log_event("Courier Delivery Failed", {"error": "Bridge not found", "target": destination_bridge_name})
            return False

        dest_path = os.path.join(bridge["folder"], filename)

        try:
            shutil.copy2(source_path, dest_path)
            log_event("Courier Delivered", {
                "file": filename,
                "from": INBOX_DIR,
                "to": bridge["folder"],
                "timestamp": datetime.utcnow().isoformat()
            })
            self.history.append({
                "file": filename,
                "target": destination_bridge_name,
                "delivered_at": datetime.utcnow().isoformat()
            })
            self.save_log()
            return True
        except Exception as e:
            log_event("Courier Delivery Error", {"error": str(e), "file": filename})
            return False

    def run_auto_delivery(self):
        delivered = 0
        for file in os.listdir(INBOX_DIR):
            if file.endswith(".py") or file.endswith(".json"):
                for bridge in self.bridges:
                    if self.deliver_file(file, bridge["name"]):
                        delivered += 1
                        break
        print(f"[CourierAI] 📦 Delivered {delivered} file(s).")

if __name__ == "__main__":
    courier = CourierAI()
    courier.run_auto_delivery()