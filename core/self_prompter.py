# === FILE: core/self_prompter.py ===
"""
Self-Prompter:
Autonomously generates ideas, tasks, and improvements based on system state, trade results, or goal triggers.
"""
import random
from datetime import datetime
from ghostforge_core import GhostForge
from memory.task_backlog import queue_task

PROMPT_CATEGORIES = [
    "Improve trade logic", "Expand assistant capabilities",
    "Check bridge integrity", "Refactor outdated modules",
    "Run system audit", "Create teaching module",
    "Propose risk strategy"
]

class SelfPrompter:
    def __init__(self):
        self.persona = "Spectra"

    def generate_prompt(self):
        topic = random.choice(PROMPT_CATEGORIES)
        timestamp = datetime.utcnow().isoformat()
        prompt = f"[{timestamp}] Self-Generated Task: {topic}"
        return prompt

    def inject_prompt(self):
        prompt = self.generate_prompt()
        queue_task(prompt)
        print(f"[SelfPrompter] 💡 {prompt}")

if __name__ == "__main__":
    prompter = SelfPrompter()
    prompter.inject_prompt()