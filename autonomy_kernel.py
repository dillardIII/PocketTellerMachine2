# autonomy_kernel.py
# Purpose: Continuous core loop for autonomy. Watches events, heals, builds, and evolves system.

import time
import traceback
from core.event_reactor import EventReactor
from core.task_orchestrator import TaskOrchestrator
from utils.logger import log_event

class AutonomyKernel:
    def __init__(self):
        self.reactor = EventReactor()
        self.orchestrator = TaskOrchestrator()
        self.last_heartbeat = time.time()
        self.active = True
        self.heartbeat_interval = 60  # seconds

    def run_heartbeat(self):
        log_event("Kernel Heartbeat", {"status": "alive", "timestamp": time.time()})
        self.orchestrator.run_full_diagnostic_sequence()

    def watch_and_respond(self):
        """Core AI evolution loop. Runs in background indefinitely."""
        log_event("Autonomy Kernel Started", {})
        while self.active:
            try:
                # Check heartbeat interval
                now = time.time()
                if now - self.last_heartbeat > self.heartbeat_interval:
                    self.run_heartbeat()
                    self.last_heartbeat = now

                # === Simulated Events (to be replaced with real watchers)
                if self.simulate_event():
                    event = self.simulate_event()
                    self.reactor.receive_event(event["type"], event.get("payload"))

                time.sleep(10)

            except Exception as e:
                log_event("Kernel Error", {"error": str(e), "trace": traceback.format_exc()})
                self.reactor.receive_event("error_detected", {"error": str(e)})

    def simulate_event(self):
        """TEMP: Simulate a rotating test of trade events and triggers."""
        import random
        options = [
            {"type": "trade_loss", "payload": {"symbol": "NFLX", "pnl": -50}},
            {"type": "trade_win", "payload": {"symbol": "AMZN", "pnl": 120}},
            {"type": "error_detected", "payload": {"error": "Mock failure"}},
            None
        ]
        return random.choice(options)

# === Manual Run ===
if __name__ == "__main__":
    kernel = AutonomyKernel()
    kernel.watch_and_respond()