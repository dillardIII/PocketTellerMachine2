# === what_if_engine.py ===
"""
What-If Engine – Alternate Timeline Simulator
Explores hypothetical outcomes by modifying conditions, decisions, or variables in simulations.

Used for:
- Strategy testing
- Counterfactual analysis
- Decision branching
- Parallel timeline modeling
"""

import os
import json
from datetime import datetime
from utils.logger import log_event
from utils.file_utils import save_file

WHATIF_LOG_FILE = "memory/what_if_log.json"
WHATIF_OUTPUT_DIR = "memory/alternate_realities/"
os.makedirs(WHATIF_OUTPUT_DIR, exist_ok=True)

class WhatIfEngine:
    def __init__(self):
        self.timeline_log = []
        self.load_log()

    def load_log(self):
        if os.path.exists(WHATIF_LOG_FILE):
            try:
                with open(WHATIF_LOG_FILE, "r") as f:
                    self.timeline_log = json.load(f)
            except json.JSONDecodeError:
                self.timeline_log = []

    def save_log(self):
        with open(WHATIF_LOG_FILE, "w") as f:
            json.dump(self.timeline_log[-300:], f, indent=2)

    def simulate_alternate(self, question, variable_changes, baseline=None):
        timestamp = datetime.utcnow().isoformat()
        outcome = self._build_simulated_outcome(question, variable_changes, baseline)

        output_path = f"{WHATIF_OUTPUT_DIR}{timestamp.replace(':', '-')}_whatif.json"
        report = {
            "timestamp": timestamp,
            "question": question,
            "variables_changed": variable_changes,
            "baseline": baseline or "None provided",
            "simulated_outcome": outcome,
            "output_file": output_path
        }

        save_file(output_path, json.dumps(report, indent=2))
        self.timeline_log.append(report)
        self.save_log()
        log_event("What-If Simulation Created", report)

        return report

    def _build_simulated_outcome(self, question, variables, baseline):
        """
        Placeholder logic for now – eventually replaced with predictive modeling or LLMs.
        """
        return (
            f"📌 If {', '.join(variables)} were changed, the outcome would shift significantly. "
            f"Question posed: '{question}'. Outcome generated using pattern echoing and historical deviation."
        )

# === TEST RUN ===
if __name__ == "__main__":
    engine = WhatIfEngine()
    test = engine.simulate_alternate(
        question="What if PTM had launched with full bridge sync from day 1?",
        variable_changes=["Bridge sync enabled", "Auto-deployment live"],
        baseline="Initial manual deployment process"
    )
    print(json.dumps(test, indent=2))