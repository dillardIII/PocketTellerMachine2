# autonomy_core.py
# Central logic router for full AI autonomy stack
# Activates bridges, agents, listeners, and more

import threading
import time
from bridge_controller import start_bridge
from autofixer_agent import run_fixer
from command_listener import start_listener
from deploy_orchestrator import deploy_all
from self_replicator import replicate_if_needed
from sandbox_monitor import monitor_sandboxes
from hivemind_sync import sync_all
from executor_engine import execute_pending_tasks
from guardian_watchdog import start_guardian

class AutonomyCore:
    def __init__(self):
        self.running = False

    def start_all_systems(self):
        print("[AUTONOMY CORE] Activating all systems...")
        self.running = True
        threading.Thread(target=start_bridge).start()
        threading.Thread(target=run_fixer).start()
        threading.Thread(target=start_listener).start()
        threading.Thread(target=deploy_all).start()
        threading.Thread(target=replicate_if_needed).start()
        threading.Thread(target=monitor_sandboxes).start()
        threading.Thread(target=sync_all).start()
        threading.Thread(target=execute_pending_tasks).start()
        threading.Thread(target=start_guardian).start()
        print("[AUTONOMY CORE] All modules deployed.")

    def loop(self):
        while self.running:
            print("[AUTONOMY CORE] Scanning for updates...")
            time.sleep(60)  # Heartbeat
            # Future: Trigger real-time event handlers

if __name__ == "__main__":
    core = AutonomyCore()
    core.start_all_systems()
    core.loop()