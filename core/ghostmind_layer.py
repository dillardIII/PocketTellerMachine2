from ghost_env import INFURA_KEY, VAULT_ADDRESS
# ghostmind_layer.py
# Handles distributed AI thought memory and recursion

from datetime import datetime
import json
import os

MEMORY_PATH = "memory/ghostmind_log.json"

def inject_idea(idea):
    entry = {
        "timestamp": str(datetime.utcnow()),
        "thought": idea
    }

    if not os.path.exists("memory"):
        os.makedirs("memory")

    if not os.path.exists(MEMORY_PATH):
        history = []
    else:
        with open(MEMORY_PATH, "r") as f:
            try:
                history = json.load(f)
            except:
                history = []

    history.append(entry)

    with open(MEMORY_PATH, "w") as f:
        json.dump(history[-300:], f, indent=2)