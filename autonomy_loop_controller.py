# === FILE: autonomy_loop_controller.py ===

import time
from cole_autopilot_cycle import cole_autopilot_cycle

def start_autonomy_daemon():
    print("[Autonomy Loop Controller] Starting...")
    while True:
        try:
            print("[Autonomy Loop Controller] Running Cole Autopilot Cycle...")
            cole_autopilot_cycle()
        except Exception as e:
            print(f"[Autonomy Loop Controller] ERROR: {e}")
        time.sleep(60)