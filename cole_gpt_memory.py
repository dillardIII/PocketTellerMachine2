from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_gpt_memory.py ===

import os
import json
from datetime import datetime

GPT_MEMORY_FILE = "data/gpt_prompt_log.json"

# === Save GPT Prompt + Response ===
def log_gpt_prompt(prompt, response, persona="default"):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "persona": persona,
        "prompt": prompt,
        "response": response
    }

    logs = []
    if os.path.exists(GPT_MEMORY_FILE):
        try:
            with open(GPT_MEMORY_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(entry)

    with open(GPT_MEMORY_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

    print("[GPT-Memory] Logged prompt + response.")

# === Optional: View Past Prompts ===
def get_all_prompts():
    if os.path.exists(GPT_MEMORY_FILE):
        with open(GPT_MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():