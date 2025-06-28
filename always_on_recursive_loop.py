"""
Always-On Recursive Loop
Keeps PTM's brain modules running on a continuous loop.
Runs self-analysis, evolution triggers, and memory syncing in background threads.
"""

import threading
import time
from ghostforge_core import GhostForge
from utils.logger import log_event

CHECK_INTERVAL = 10  # seconds between recursive cycles
MODULES_TO_EVALUATE = [
    "core/self_prompting_brain.py",
    "core/strategy_engine.py",
    "core/trade_memory_loop.py",
    "core/ghostbridge_listener.py"
]

class RecursiveLoop:
    def __init__(self):
        self.running = True
        self.forge = GhostForge(persona="LoopDaemon")

    def run_cycle(self):
        log_event("[🧠 RecursiveLoop] Starting infinite evolution cycle...")
        while self.running:
            for module in MODULES_TO_EVALUATE:
                try:
                    self.forge.evolve_modules({module: open(module).read()})
                    log_event(f"[🔁 Loop] Evolved: {module}")
                except Exception as e:
                    log_event(f"[⚠️ Loop Error] {module}: {str(e)}")
            time.sleep(CHECK_INTERVAL)

    def start(self):
        loop_thread = threading.Thread(target=self.run_cycle)
        loop_thread.daemon = True
        loop_thread.start()
        log_event("[🔥 RecursiveLoop] Thread launched. Loop is now always-on.")

if __name__ == "__main__":
    daemon = RecursiveLoop()
    daemon.start()
    while True:
        time.sleep(60)  # Keeps main thread alive