from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_code_results.py ===

import os
import json
from datetime import datetime

RESULTS_LOG_PATH = "logs/code_generation_results.json"

def save_code_generation_result(result):
    os.makedirs(os.path.dirname(RESULTS_LOG_PATH), exist_ok=True)
    try:
        with open(RESULTS_LOG_PATH, "a") as f:
            f.write(json.dumps({
                "timestamp": datetime.utcnow().isoformat(),
                "result": result
            }) + "\n")
    except Exception as e:
        print(f"[ERROR] Failed to save code generation result: {e}")

def get_code_generation_results(limit=10):
    if not os.path.exists(RESULTS_LOG_PATH):
        return []

    try:
        with open(RESULTS_LOG_PATH, "r") as f:
            lines = f.readlines()
        entries = [json.loads(line.strip()) for line in lines[-limit:]]
        return entries
    except Exception as e:
        print(f"[ERROR] Failed to read code generation results: {e}")
        return []

def evaluate_last_code_results():
    results = get_code_generation_results(limit=1)
    if not results:
        return {"status": "no results"}
    
    last = results[0]
    print(f"[Cole Results] Last generation timestamp: {last['timestamp']}")
    print(f"[Cole Results] Last result summary: {last['result']}")
    return last

def log_event():ef drop_files_to_bridge():