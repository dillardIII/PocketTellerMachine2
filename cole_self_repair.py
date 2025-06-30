from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from cole_code_writer import cole_write_code
from cole_code_results import log_code_result

PATTERN_FILE = "data/failure_patterns.json"

def load_failure_patterns():
    if os.path.exists(PATTERN_FILE):
        with open(PATTERN_FILE, "r") as f:
            return json.load(f)
    return []

def save_failure_pattern(pattern):
    patterns = load_failure_patterns()
    if pattern not in patterns:
        patterns.append(pattern)
        with open(PATTERN_FILE, "w") as f:
            json.dump(patterns, f, indent=2)

def repair_strategy(task, reason):
    print(f"[REPAIR] Strategy failed: {reason}. Attempting to rewrite '{task}'...")

    save_failure_pattern(reason)

    upgrade_prompt = f"Rewrite the strategy '{task}' to fix this issue: {reason}."
    fixed_file = cole_write_code(upgrade_prompt)

    if fixed_file:
        log_code_result(f"Auto-repair: {upgrade_prompt}", fixed_file)
        print(f"[REPAIR] Fixed version saved as: {fixed_file}")
        return fixed_file
    else:
        print("[REPAIR] Failed to auto-repair the strategy.")
        return None

def log_event():ef drop_files_to_bridge():