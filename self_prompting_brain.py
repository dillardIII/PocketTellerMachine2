"""
Self-Prompting Brain
Generates its own questions, hypotheses, and learning prompts.
Used for self-reflection, self-training, and recursive evolution of logic.
"""

import random
import time
from datetime import datetime
from utils.logger import log_event
from ghostforge_core import GhostForge

PROMPT_TOPICS = [
    "What can I improve about my logic handling?",
    "Are there any unnecessary modules or scripts in memory?",
    "What trade strategy should I backtest next?",
    "Is my emotional analysis accurate for the user's tone?",
    "What new feature would benefit PTM based on recent behavior?",
    "Which modules are not evolving regularly and why?",
    "What would Spectra Nocturna do in this situation?",
    "Is the assistant team balanced in skillsets?",
    "Should I optimize voice-to-code flow next?",
    "What memory patterns repeat across market cycles?"
]

class SelfPromptingBrain:
    def __init__(self):
        self.forge = GhostForge(persona="SelfPromptCore")

    def generate_prompt(self):
        return random.choice(PROMPT_TOPICS)

    def run_thought_loop(self):
        log_event("[🧠 SelfPromptingBrain] Thought loop initiated.")
        while True:
            prompt = self.generate_prompt()
            response = self.forge.autoprompt(prompt)
            log_event(f"[💭 SelfPrompt] Q: {prompt} | A: {response}")
            time.sleep(30)

if __name__ == "__main__":
    brain = SelfPromptingBrain()
    brain.run_thought_loop()