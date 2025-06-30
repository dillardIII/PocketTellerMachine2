from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: reflex_scheduler.py ===

# ⏰ Reflex Scheduler – Triggers feedback loop every 10 minutes

import time
from reflex_feedback_loop import monitor_and_adapt

def reflex_loop(interval=600):  # 600 sec = 10 minutes
    print("[ReflexScheduler] 🧠 Scheduled reflex training started.")
    while True:
        monitor_and_adapt()
        time.sleep(interval)

def log_event():ef drop_files_to_bridge():