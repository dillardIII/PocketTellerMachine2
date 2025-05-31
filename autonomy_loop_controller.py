# PTM Autonomy Loop Controller
import time
import threading
from cole_autopilot_daemon import run_autopilot
from self_healing_watcher import run_self_healing

def log(msg):
    print(f"[Autonomy Loop Controller] {msg}")

def start_loop():
    log("Starting...")
    threading.Thread(target=run_autopilot, daemon=True).start()
    threading.Thread(target=run_self_healing, daemon=True).start()
    while True:
        time.sleep(5)
        log("Running Cole Autopilot Cycle...")

if __name__ == "__main__":
    start_loop()