#=== FILE: recursive_brain_loop.py ===

""" Recursive Brain Loop Continuously self-generates prompts, goals, and tasks for PTM to evolve and improve. Should be run as a daemon or scheduled task to achieve full autonomous operation. """

import time from ghostforge_core import GhostForge from utils.logger import log_event

LOOP_INTERVAL = 300  # seconds DEFAULT_PROMPT = "Improve PTM's logic, autonomy, or intelligence. Generate code or plans."

class RecursiveBrain: def init(self): self.forge = GhostForge(persona="GhostBrain")

def think_and_generate(self):
    log_event("🧠 GhostBrain Loop triggered")
    task_prompt = DEFAULT_PROMPT
    filename = f"auto_{int(time.time())}.py"
    generated = self.forge.generate_module(filename, task_prompt, base_code="", trigger_source="recursive_loop")
    log_event(f"📄 Generated module: {filename}")

def run_loop(self):
    while True:
        self.think_and_generate()
        time.sleep(LOOP_INTERVAL)

if name == "main": RecursiveBrain().run_loop()

