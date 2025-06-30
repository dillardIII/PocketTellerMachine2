from ghost_env import INFURA_KEY, VAULT_ADDRESS
# event_reactor.py
# Purpose: React to system events and route them to proper routines or modules

import datetime
from core.task_orchestrator import TaskOrchestrator
from core.ai_registry import AIRegistry
from utils.logger import log_event

class EventReactor:
    def __init__(self):
        self.orchestrator = TaskOrchestrator()
        self.registry = AIRegistry()
        self.routes = self.default_routes()

    def default_routes(self):
        return {
            "error_detected": self.route_error,
            "trade_loss": self.route_trade_loss,
            "trade_win": self.route_trade_win,
            "system_idle": self.route_idle_check,
            "new_command": self.route_new_command
        }

    def receive_event(self, event_type, payload=None):
        handler = self.routes.get(event_type)
        if handler:
            log_event("Event Received", {"type": event_type, "payload": payload})
            return handler(payload)
        else:
            log_event("Unhandled Event", {"type": event_type})
            return False

    def route_error(self, payload):
        log_event("Routing Error", {"payload": payload})
        return self.orchestrator.run_full_diagnostic_sequence()

    def route_trade_loss(self, payload):
        reason = "Triggered by trade loss"
        module = "mood_reactor"
        self.registry.call_tool(module)
        self.orchestrator.run_full_diagnostic_sequence()
        return self.orchestrator.trigger_new_module("loss_response", reason, "def run():ef route_trade_win(self, payload):
        reason = "Triggered by trade win"
        module = "celebration_reactor"
        self.registry.call_tool(module)
        return self.orchestrator.trigger_new_module("win_response", reason, "def run():ef route_idle_check(self, payload):
        return self.orchestrator.run_full_diagnostic_sequence()

    def route_new_command(self, payload):
        # This will eventually respond to live voice input and mapped triggers
        command = payload.get("command")
        log_event("Voice Command", {"command": command})
        if command == "heal":
            return self.orchestrator.run_full_diagnostic_sequence()
        elif command == "scan":
            return self.orchestrator.orchestrator.ghostforge.scan_codebase()
        return False

# === Manual Test ===
if __name__ == "__main__":
    reactor = EventReactor()
    reactor.receive_event("trade_loss", {"symbol": "AAPL", "pnl": -40})
    reactor.receive_event("trade_win", {"symbol": "TSLA", "pnl": 130})
    reactor.receive_event("error_detected", {"error": "Connection dropped."})