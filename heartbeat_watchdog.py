# === FILE: heartbeat_watchdog.py ===
# ❤️ Heartbeat Watchdog – Keeps PTM bots alive and restarts crashed ones

import time
import threading
import traceback
from utils.logger import log_event
from bridge_transfer_daemon import run_bridge_daemon
from command_listener import CommandListener
from sweep_handler import SweepHandler

WATCH_INTERVAL = 10  # seconds

def start_heartbeat():
    print("[Heartbeat] ❤️ PTM Watchdog is online.")
    command_listener = CommandListener()
    sweeper = SweepHandler()

    def safe_thread(target, label):
        try:
            thread = threading.Thread(target=target, daemon=True)
            thread.start()
            log_event("Heartbeat", f"Started thread: {label}")
        except Exception as e:
            print(f"[Heartbeat] ❌ Failed to start {label}: {e}")
            traceback.print_exc()
            log_event("HeartbeatError", { "thread": label, "error": str(e) })

    # Main loop
    while True:
        safe_thread(run_bridge_daemon, "BridgeTransfer")
        safe_thread(command_listener.listen, "CommandListener")
        safe_thread(sweeper.sweep, "SweepHandler")
        time.sleep(WATCH_INTERVAL)