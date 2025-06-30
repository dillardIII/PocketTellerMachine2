# task_orchestrator.py
# Purpose: Orchestrate recursive tasks across AI subsystems (GhostForge, Architect, Schedulers)
# Triggered by personas, macro commands, moods, or risk states

import json
from datetime import datetime
from persona_scheduler import PersonaScheduler
from macro_processor import MacroProcessor
from ghostforge_core import GhostForge
from utils.logger import log_event

class TaskOrchestrator:
    def __init__(self):
        self.scheduler_personas = ["Mentor", "MoCash", "Strategist", "DrillInstructor"]
        self.macro_engine = MacroProcessor()
        self.ghostforge = GhostForge()
        self.cycle_log_path = "memory/task_orchestration_log.json"
        self.history = self.load_history()

    def load_history(self):
        try:
            with open(self.cycle_log_path, "r") as f:
                return json.load(f)
        except:
            return []

    def save_history(self):
        with open(self.cycle_log_path, "w") as f:
            json.dump(self.history[-50:], f, indent=2)

    def run_all_personas(self):
        results = []
        for name in self.scheduler_personas:
            scheduler = PersonaScheduler(persona_name=name)
            result = scheduler.execute_cycle()
            results.append(result)
        return results

    def process_macro_commands(self, commands):
        output = []
        for command in commands:
            result = self.macro_engine.process(command)
            output.append((command, result))
        return output

    def perform_recursive_pass(self, trigger_reason="manual"):
        log_event("Recursive Pass Initiated", {"trigger": trigger_reason})
        timestamp = str(datetime.now())

        persona_results = self.run_all_personas()
        macro_results = self.process_macro_commands(["build risk guardian", "spawn ghost telemetry"])

        cycle = {
            "timestamp": timestamp,
            "trigger": trigger_reason,
            "personas": persona_results,
            "macros": macro_results
        }

        self.history.append(cycle)
        self.save_history()

        return cycle

# === Manual Trigger ===
if __name__ == "__main__":
    orchestrator = TaskOrchestrator()
    results = orchestrator.perform_recursive_pass()
    print(json.dumps(results, indent=2))