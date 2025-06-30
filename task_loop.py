from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: task_loop.py ===
# 🔁 Task Loop – Keeps PTM's brain active, scanning, generating, and improving

import time
import traceback
from executor_engine import execute_pending_tasks
from reflex_engine import ReflexEngine
from ghostforge_core import GhostForge
from assistant_dispatch import AssistantDispatch
from utils.logger import log_event

class TaskLoop:
    def __init__(self, interval=10):
        self.interval = interval  # seconds
        self.reflex = ReflexEngine()
        self.forge = GhostForge()
        self.assist = AssistantDispatch()
        self.running = False

    def start(self):
        self.running = True
        log_event("🌀 TaskLoop initialized. Autonomy engine starting...")
        while self.running:
            try:
                # 👁️ Reflex check (PTM scans for triggers or stimuli)
                self.reflex.scan_environment()

                # 🔧 Execute tasks queued by other systems
                execute_pending_tasks()

                # 🧠 Autogenerate improvements or fallback routines
                self.forge.generate_module_if_triggered()

                # 🗣️ Let assistants broadcast any queued updates
                self.assist.run_updates()

                # Wait before next loop
                time.sleep(self.interval)

            except Exception as e:
                error_msg = f"💥 TaskLoop error: {str(e)}\n{traceback.format_exc()}"
                log_event(error_msg)
                time.sleep(5)  # Brief pause before trying again

    def stop(self):
        self.running = False
        log_event("🛑 TaskLoop stopped.")

# Optional trigger if standalone run:
if __name__ == "__main__":
    loop = TaskLoop()
    loop.start()