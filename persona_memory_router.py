from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Persona Memory Router – Role-Based Memory Management System

Controls how memory is routed to each persona, including
filtering what they remember, forget, or specialize in.
Enables distinct learning paths across the PTM assistant team.
"""

import json
import os
from datetime import datetime

MEMORY_FILE = "data/persona_memory_map.json"

DEFAULT_RULES = {
    "Mentor": {"keep": ["failures", "strategy", "lessons"], "forget": ["profits"]},
    "MoCash": {"keep": ["profits", "wins"], "forget": ["failures"]},
    "DrillInstructor": {"keep": ["discipline", "errors", "warnings"], "forget": []},
    "Strategist": {"keep": ["entries", "exits", "ratios"], "forget": []},
    "ChillTrader": {"keep": ["vibes", "patterns"], "forget": ["stress"]},
}

def load_rules():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    else:
        return DEFAULT_RULES

def store_memory_for_persona(persona, memory_type, content):
    rules = load_rules()
    persona_rules = rules.get(persona, {})

    keep = persona_rules.get("keep", [])
    forget = persona_rules.get("forget", [])

    if memory_type in forget:
        print(f"[MemoryRouter] {persona} skips '{memory_type}' memory.")
        return

    if keep and memory_type not in keep:
        print(f"[MemoryRouter] {persona} is not configured to store '{memory_type}' memory.")
        return

    log_path = f"data/memory_{persona.lower()}.json"
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": memory_type,
        "content": content
    }

    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            mem_log = json.load(f)
    else:
        mem_log = []

    mem_log.append(entry)

    with open(log_path, "w") as f:
        json.dump(mem_log, f, indent=4)

    print(f"[MemoryRouter] Stored '{memory_type}' memory for {persona}.")

# Manual test hook
if __name__ == "__main__":
    store_memory_for_persona("MoCash", "profits", "Closed $NVDA for $1400 gain")
    store_memory_for_persona("Mentor", "failures", "Missed entry on $TSLA breakout")

def log_event():ef drop_files_to_bridge():