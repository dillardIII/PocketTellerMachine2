from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: gpt_cole_sync.py ===

import os
import json
from datetime import datetime
from ptm_gpt_agent import run_ptm_gpt_agent
from cole_gpt_advisor import ask_gpt

COLE_LOG_FILE = "logs/autonomy_loop.log"
SYNC_LOG_FILE = "logs/gpt_cole_sync_log.json"

def run_gpt_cole_sync():
    print("[GPT-Cole Sync] Reading last 30 lines of Cole's loop...")

    if not os.path.exists(COLE_LOG_FILE):
        print("[GPT-Cole Sync] No Cole log found.")
        return

    with open(COLE_LOG_FILE, "r") as f:
        lines = f.readlines()[-30:]

    context = "\n".join(lines)

    prompt = f"""
You are a diagnostic AI inside PTM. Here's the recent Cole activity log:

{context}

Analyze what PTM (Cole) is doing. Suggest:
- 1 improvement prompt
- 1 healing or correction idea
- 1 build or strategy it should prioritize next

Respond in this format:
{{
  "improvement": "...",
  "fix": "...",
  "strategy": "..."
}}
"""

    response = ask_gpt(prompt)

    try:
        result = json.loads(response)
        print("[GPT-Cole Sync] GPT generated tasks:")
        print(json.dumps(result, indent=2))

        for key, idea in result.items():
            run_ptm_gpt_agent(idea)

        log_sync(result)

    except Exception as e:
        print("[GPT-Cole Sync] GPT failed to return proper JSON:", e)
        print("Raw response:", response)

def log_sync(result):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "result": result
    }
    os.makedirs("logs", exist_ok=True)

    if os.path.exists(SYNC_LOG_FILE):
        with open(SYNC_LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(entry)
    with open(SYNC_LOG_FILE, "w") as f:
        json.dump(logs[-100:], f, indent=2)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():