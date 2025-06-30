from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_sync_controller.py ===
# 🧠 Bridge Sync Controller – Coordinates drop, pickup, and health threads for stable bridge activity.

import threading
import time
from bridge_drop_agent import drop_files_to_bridge
from bridge_pickup_agent import pick_up_from_bridge
from bridge_health_checker import check_bridge_health

def run_bridge_sync_loop():
    print("[Bridge Controller] 🔄 Bridge Sync Loop is starting...")

    # === Start Drop Agent Thread ===
    drop_thread = threading.Thread(target=drop_files_to_bridge, daemon=True)
    drop_thread.start()
    print("[Bridge Controller] 🚚 Drop Agent activated.")

    # === Start Pickup Agent Thread ===
    pickup_thread = threading.Thread(target=pick_up_from_bridge, daemon=True)
    pickup_thread.start()
    print("[Bridge Controller] 📦 Pickup Agent activated.")

    # === Start Health Check Loop ===
    def monitor_health():
        while True:
            check_bridge_health()
            time.sleep(15)

    health_thread = threading.Thread(target=monitor_health, daemon=True)
    health_thread.start()
    print("[Bridge Controller] ❤️ Health monitor thread started.")

if __name__ == "__main__":
    run_bridge_sync_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():