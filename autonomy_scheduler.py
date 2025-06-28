# === FILE: autonomy_scheduler.py ===
# ⏱️ Autonomy Scheduler – Monitors conditions and executes macros at the right time

import time
import threading
from macro_executor import MacroExecutor
from utils.logger import log_event

class AutonomyScheduler:
    def __init__(self):
        self.executor = MacroExecutor()
        self.running = False
        self.thread = None
        self.conditions = []  # Each condition is a dict with 'check', 'macro_name'

    def add_condition(self, condition_func, macro_name):
        self.conditions.append({
            "check": condition_func,
            "macro_name": macro_name
        })
        log_event("Scheduler Condition Added", {"macro": macro_name})

    def start(self):
        if not self.running:
            print("[Scheduler] 🕒 Starting scheduler thread...")
            self.running = True
            self.thread = threading.Thread(target=self._run_loop)
            self.thread.daemon = True
            self.thread.start()

    def stop(self):
        self.running = False
        print("[Scheduler] ⏹️ Stopped scheduler.")

    def _run_loop(self):
        while self.running:
            for condition in self.conditions:
                try:
                    if condition["check"]():
                        print(f"[Scheduler] ✅ Condition met for macro: {condition['macro_name']}")
                        self.executor.execute_macro(condition["macro_name"])
                except Exception as e:
                    print(f"[Scheduler] ⚠️ Error checking condition: {e}")
            time.sleep(5)  # Check every 5 seconds

    def list_conditions(self):
        return [c["macro_name"] for c in self.conditions]