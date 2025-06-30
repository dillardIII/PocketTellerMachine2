from ghost_env import INFURA_KEY, VAULT_ADDRESS
# persona_scheduler.py
# Purpose: Schedule autonomous persona activity across PTM system
# Each persona runs their task cycle on a timer or based on mood/triggers

import json
import random
from datetime import datetime, timedelta
from ghostforge_core import GhostForge
from auto_architect import AutoArchitect
from utils.logger import log_event

class PersonaScheduler:
    def __init__(self, persona_name="Mentor"):
        self.persona = persona_name
        self.last_run_path = f"memory/{self.persona.lower()}_last_run.json"
        self.ghostforge = GhostForge(self.persona)
        self.architect = AutoArchitect()

    def get_last_run_time(self):
        try:
            with open(self.last_run_path, "r") as f:
                data = json.load(f)
                return datetime.fromisoformat(data["last_run"])
        except:
            return datetime.min

    def update_last_run_time(self):
        with open(self.last_run_path, "w") as f:
            json.dump({"last_run": str(datetime.now())}, f)

    def should_run(self, cooldown_minutes=15):
        return datetime.now() > self.get_last_run_time() + timedelta(minutes=cooldown_minutes)

    def execute_cycle(self):
        if not self.should_run():
            return f"[{self.persona}] Waiting on cooldown..."

        log_event("Persona Cycle Start", {"persona": self.persona, "time": str(datetime.now())})
        self.update_last_run_time()

        decision = random.choice(["generate", "refactor", "idle"])

        if decision == "generate":
            module_name = f"{self.persona.lower()}_task_{datetime.now().strftime('%H%M%S')}"
            purpose = f"Routine task loop by {self.persona}"
            base_code = f"def run():
            path = self.ghostforge.generate_module(module_name, purpose, base_code, trigger_source="auto-cycle")
            return f"[{self.persona}] Generated: {path}"

        elif decision == "refactor":
            target = "core/main.py"
            result = self.architect.propose_refactor(target)
            return f"[{self.persona}] Refactor Attempt: {result.get('ideas')}"

        else:
            return f"[{self.persona}] Chose to idle this cycle."

# === Run Cycle Manually ===
if __name__ == "__main__":
    for persona in ["Mentor", "MoCash", "Strategist", "DrillInstructor"]:
        scheduler = PersonaScheduler(persona_name=persona)
        print(scheduler.execute_cycle())