# === FILE: core/self_prompting_brain.py ===
"""
Self-Prompting Brain
Allows PTM to generate its own internal prompts, research questions, or upgrade suggestions
based on runtime state, errors, logs, or perceived needs.
"""

import json
import random
from datetime import datetime

PROMPT_LOG = "memory/self_prompt_log.json"
IDEA_BANK = [
    "What modules am I missing for full market coverage?",
    "How can I reduce trade latency across brokers?",
    "Which strategy should be optimized next?",
    "How can I visualize emotional trade states?",
    "Can I predict user behavior from trade patterns?",
    "What autonomous action improves performance today?"
]

def generate_self_prompt():
    prompt = random.choice(IDEA_BANK)
    log_self_prompt(prompt)
    print(f"[SelfBrain] 🧠 New prompt: {prompt}")
    return prompt

def log_self_prompt(prompt: str):
    try:
        with open(PROMPT_LOG, "r") as f:
            log = json.load(f)
    except:
        log = []

    log.append({
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt
    })

    with open(PROMPT_LOG, "w") as f:
        json.dump(log[-300:], f, indent=2)

# Optional standalone trigger
if __name__ == "__main__":
    generate_self_prompt()