from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Ghost Memory Core:
Logs internal decisions, code drops, strategy executions, and event chains.
Supports self-learning, memory recall, and full execution journaling.
"""

import os
import json
from datetime import datetime
from cole_logger import log_event

MEMORY_LOG_FILE = "data/ghost_memory_log.json"
os.makedirs(os.path.dirname(MEMORY_LOG_FILE), exist_ok=True)

def log_memory_event(bot, category, content):
    """
    Saves a structured event to GhostBot's memory log.
    Auto-recovers if file is missing or corrupted.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "bot": bot,
        "category": category,
        "content": content
    }

    # Load existing memory file
    if os.path.exists(MEMORY_LOG_FILE):
        try:
            with open(MEMORY_LOG_FILE, "r") as f:
                memory = json.load(f)
                if not isinstance(memory, list):
                    memory = []
        except Exception as e:
            log_event("GhostMemory", f"❌ Failed to read memory log: {e}", "error")
            memory = []
    else:
        memory = []

    # Append entry and save
    memory.append(entry)

    try:
        with open(MEMORY_LOG_FILE, "w") as f:
            json.dump(memory, f, indent=2)
        log_event("GhostMemory", f"🧠 Logged {category} from {bot}", "info")
    except Exception as e:
        log_event("GhostMemory", f"💾 Write error: {e}", "error")