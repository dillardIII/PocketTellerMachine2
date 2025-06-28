# 🚀 AutoBoot – Launches full PTM stack and sync bridge system

import threading
import time

# === PTM Core Boot Modules ===
from app import app
from bridge_team_launcher import start_bridge_team
from auto_sync_engine import start_hourly_sync

def launch_ptm():
    print("[AutoBoot] 💰 Starting PTM Flask App...")
    app.run(host="0.0.0.0", port=5000, debug=True)

def launch_bridge():
    print("[AutoBoot] 🔁 Starting Bridge Team...")
    start_bridge_team()

def launch_wallet_sync():
    print("[AutoBoot] ⏱️ Starting Hourly Wallet Sync...")
    start_hourly_sync()

# === Main Launcher ===
if __name__ == "__main__":
    print("[AutoBoot] ⚙️ Initializing PTM AutoBoot Sequence...")

    # Flask App (Main UI + Routes)
    flask_thread = threading.Thread(target=launch_ptm, daemon=True)
    flask_thread.start()

    # Bridge Team (GPT <--> Replit Sync)
    bridge_thread = threading.Thread(target=launch_bridge, daemon=True)
    bridge_thread.start()

    # Wallet Sync Engine
    sync_thread = threading.Thread(target=launch_wallet_sync, daemon=True)
    sync_thread.start()

    # === Keep Alive ===
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("[AutoBoot] 🛑 Shutdown signal received.")