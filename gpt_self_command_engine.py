# === FILE: gpt_self_command_engine.py ===

from ptm_gpt_agent import run_ptm_gpt_agent
from cole_gpt_advisor import ask_gpt
from datetime import datetime
import random
import json
import os

LOG_FILE = "logs/self_commands_log.json"
PROMPT_HISTORY = []

def generate_self_command():
    base_prompt = """
You are the self-command brain for PTM.

Your job is to create a useful improvement prompt that will help PTM evolve, learn, or gain a new skill.

Only generate commands that make sense for an AI trading assistant and system builder. Avoid redundancy.

Example format:
"Add a trading dashboard to compare crypto vs stocks."

Now create one new command PTM can work on.
"""

    # === GPT generates the next command
    response = ask_gpt(base_prompt).strip()

    if response:
        PROMPT_HISTORY.append(response)
        print(f"[GPT Command Engine] Submitting: {response}")
        result = run_ptm_gpt_agent(response)
        log_command(response, result)
        return result
    else:
        print("[GPT Command Engine] Empty response. Skipping.")
        return None

def log_command(prompt, result):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "result": result
    }
    os.makedirs("logs", exist_ok=True)

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-200:], f, indent=2)