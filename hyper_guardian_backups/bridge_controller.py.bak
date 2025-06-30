# === FILE: bridge_controller.py ===
# 🔗 Bridge Controller – Activates drop and pickup agents for file transfers between devices (ChatGPT, Replit, Local)

import threading
from bridge_drop_agent import drop_files_to_bridge
from bridge_pickup_agent import pick_up_from_bridge
from utils.logger import log_event

class BridgeController:
    def __init__(self):
        self.active = False
        self.drop_thread = None
        self.pickup_thread = None

    def start(self):
        if self.active:
            print("[BridgeController] 🔁 Already running.")
            return

        print("[BridgeController] 🔗 Activating bridge agents...")

        # === Start Drop Agent ===
        self.drop_thread = threading.Thread(target=drop_files_to_bridge, daemon=True)
        self.drop_thread.start()
        print("[BridgeController] 🚚 Drop Agent running.")

        # === Start Pickup Agent ===
        self.pickup_thread = threading.Thread(target=pick_up_from_bridge, daemon=True)
        self.pickup_thread.start()
        print("[BridgeController] 📦 Pickup Agent running.")

        self.active = True
        log_event("Bridge Activated", {
            "status": "started",
            "mode": "threaded",
            "agents": ["drop", "pickup"]
        })

    def stop(self):
        # In current version, threads are daemonized – use future signal or flag-based shutdowns
        print("[BridgeController] 🛑 Manual stop called – agent threads will stop with process.")
        self.active = False
        log_event("Bridge Deactivated", {"status": "manual shutdown"})