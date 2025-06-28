# === FILE: agents/bridge_team_launcher.py ===

# 🚀 Bridge Team Launcher – Starts both Drop and Pickup agents as threads
# This allows GPT-side and Replit-side to sync files without manual triggers

import threading
from bridge_drop_agent import drop_files_to_bridge
from bridge_pickup_agent import pick_up_from_bridge

def start_bridge_team():
    print("[Bridge Launcher] 🔗 Activating bridge drop and pickup agents...")

    # === Drop Agent Thread (GPT side) ===
    drop_thread = threading.Thread(target=drop_files_to_bridge, daemon=True)
    drop_thread.start()
    print("[Bridge Launcher] 🚚 Drop Agent running.")

    # === Pickup Agent Thread (Replit side) ===
    pickup_thread = threading.Thread(target=pick_up_from_bridge, daemon=True)
    pickup_thread.start()
    print("[Bridge Launcher] 📥 Pickup Agent running.")

# Optional standalone launcher
if __name__ == "__main__":
    start_bridge_team()
    # Keep alive if running standalone
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[Bridge Launcher] ⛔ Stopping Bridge Team.")