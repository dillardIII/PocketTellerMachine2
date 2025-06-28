"""
Cole Brain:
Core memory and state management system for PTM assistant.
Logs persistent memory events, real-time states, and reasoning artifacts.
Also stores short-term memory states and assistant condition flags.
Used to track current context, phase, errors, and trade logic memory.
"""

import os
import json
from datetime import datetime
from cole_logger import log_event

MEMORY_FILE = "data/cole_memory.json"
STATE_FILE = "data/cole_state.json"
BRAIN_STATE_FILE = "data/cole_brain_state.json"

# Ensure directory exists
os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
os.makedirs(os.path.dirname(BRAIN_STATE_FILE), exist_ok=True)

def log_memory(category, content):
    """
    Logs long-term memory entries from Cole's thought process.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "category": category,
        "content": content
    }

    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                memory = json.load(f)
                if not isinstance(memory, list):
                    memory = []
        except Exception as e:
            log_event("ColeBrain", f"❌ Failed reading memory: {e}", "error")
            memory = []
    else:
        memory = []

    memory.append(entry)

    try:
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=2)
        log_event("ColeBrain", f"🧠 Memory saved: {category}", "info")
    except Exception as e:
        log_event("ColeBrain", f"💾 Write error: {e}", "error")


def log_state(key, value):
    """
    Stores transient state like last sync, active strategy, etc.
    Writes to both general and brain-specific state files.
    """
    # === Write to cole_state.json ===
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                state = json.load(f)
        except:
            state = {}
    else:
        state = {}

    state[key] = {
        "value": value,
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)
        log_event("ColeBrain", f"📍 State updated: {key}", "info")
    except Exception as e:
        log_event("ColeBrain", f"❌ Failed saving state: {e}", "error")

    # === Write to cole_brain_state.json for short-term tracking ===
    try:
        if os.path.exists(BRAIN_STATE_FILE):
            with open(BRAIN_STATE_FILE, "r") as f:
                brain_state = json.load(f)
        else:
            brain_state = {}

        brain_state[key] = {
            "value": value,
            "timestamp": datetime.utcnow().isoformat()
        }

        with open(BRAIN_STATE_FILE, "w") as f:
            json.dump(brain_state, f, indent=2)

    except Exception as e:
        log_event("ColeBrain", f"❌ Error saving brain state: {e}", "error")


def load_state():
    """
    Loads the short-term memory state from cole_brain_state.json.
    """
    if not os.path.exists(BRAIN_STATE_FILE):
        return {}
    try:
        with open(BRAIN_STATE_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        log_event("ColeBrain", f"❌ Error loading brain state: {e}", "error")
        return {}

# Manual test
if __name__ == "__main__":
    log_memory("test", {"thought": "This is a memory test."})
    log_state("last_strategy", "Scalping123")
    log_state("startup_test", "complete")