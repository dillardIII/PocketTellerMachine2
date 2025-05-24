# autopilot_daemon.py
import time
from cole_autopilot_cycle import cole_autopilot_cycle

def start_daemon_loop(interval_minutes=5):
    print("[AUTOPILOT DAEMON] Starting persistent loop...")
    while True:
        try:
            cole_autopilot_cycle()
        except Exception as e:
            print(f"[AUTOPILOT DAEMON ERROR]: {e}")
        time.sleep(interval_minutes * 60)