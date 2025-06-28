# === command_interpreter.py ===
"""
Command Interpreter – Decodes broadcasted botnet commands and triggers matching actions.
Routes instructions to the proper PTM subsystems (forge, heal, scout, mine, evolve, etc).
"""

import json
import os
from datetime import datetime
from utils.logger import log_event
from ghostforge_core import GhostForge
from botnet_sync import BotnetSync

COMMAND_QUEUE = "memory/command_queue.json"
INTERPRET_LOG = "memory/command_interpret_log.json"

class CommandInterpreter:
    def __init__(self):
        self.sync = BotnetSync()
        self.forge = GhostForge()
        self.interpret_log = self.load_log()
        self.node_id = "PTM_CORE"

    def load_log(self):
        if not os.path.exists(INTERPRET_LOG):
            return []
        with open(INTERPRET_LOG, "r") as f:
            return json.load(f)

    def save_log(self):
        with open(INTERPRET_LOG, "w") as f:
            json.dump(self.interpret_log[-500:], f, indent=2)

    def interpret_commands(self):
        commands = self.sync.get_pending_commands(self.node_id)
        actions_triggered = []

        for cmd in commands:
            command_text = cmd["command"].upper()
            timestamp = datetime.utcnow().isoformat()

            if command_text == "SELF_HEAL":
                result = self.forge.run_self_heal()
                actions_triggered.append("SELF_HEAL")
                log_event("Command Action: SELF_HEAL", result)

            elif command_text == "EVOLVE":
                plan = {
                    "generated_modules/evolved_module.py": "# Auto-evolved code goes here\nprint('Evolved successfully')"
                }
                feedback = self.forge.evolve_modules(plan)
                actions_triggered.append("EVOLVE")
                log_event("Command Action: EVOLVE", feedback)

            elif command_text == "SCAN_ERRORS":
                broken = self.forge.scan_codebase()
                log_event("Command Action: SCAN_ERRORS", {"broken": broken})
                actions_triggered.append("SCAN_ERRORS")

            elif command_text == "SELF_TEST_ALL":
                result = self.forge.diagnostics_and_repair()
                log_event("Command Action: SELF_TEST_ALL", result)
                actions_triggered.append("SELF_TEST_ALL")

            elif command_text == "MINE":
                log_event("Command Action: MINE", {"status": "🔧 Mining module coming soon"})
                actions_triggered.append("MINE")

            elif command_text == "REPLICATE":
                new_file = self.forge.generate_module("replica", "Test duplicate from command", 'print("Clone online.")')
                actions_triggered.append("REPLICATE")
                log_event("Command Action: REPLICATE", {"file": new_file})

            else:
                log_event("Unknown Command", {"command": command_text})
                actions_triggered.append(f"UNKNOWN: {command_text}")

        self.interpret_log.append({
            "timestamp": datetime.utcnow().isoformat(),
            "node": self.node_id,
            "actions": actions_triggered
        })

        self.save_log()
        self.sync.clear_commands(self.node_id)

if __name__ == "__main__":
    ci = CommandInterpreter()
    ci.interpret_commands()
    print("🧠 Commands interpreted and executed.")