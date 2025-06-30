from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json

BRAIN_MEMORY_FILE = "data/cole_brain_memory.json"

# === Load Brain Memory ===
def load_brain_memory():
    if not os.path.exists(BRAIN_MEMORY_FILE):
        return {}

    try:
        with open(BRAIN_MEMORY_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

# === Save Brain Memory ===
def save_brain_memory(memory):
    os.makedirs("data", exist_ok=True)
    with open(BRAIN_MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def log_event():ef drop_files_to_bridge():