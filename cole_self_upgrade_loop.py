from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_self_upgrade_loop.py ===

import os
import json
from cole_gpt_prompt_builder import build_prompt_from_failures
from cole_multi_gpt_router import ask_strategist  # You can switch to ask_mentor or ask_hustler
from cole_code_writer import save_code_to_file
from cole_ghostpilot_tracker import log_ghost_upgrade  # <== UPDATED LOGGER

STRATEGY_GRADES_FILE = "data/strategy_grades.json"

# === Load Strategy Grades ===
def load_strategy_grades():
    if os.path.exists(STRATEGY_GRADES_FILE):
        with open(STRATEGY_GRADES_FILE, "r") as f:
            return json.load(f)
    return {}

# === Check for Weak Strategies ===
def get_weak_strategies(grades):
    return [name for name, grade in grades.items() if grade in ["C", "D", "F"]]:
:
# === Upgrade Loop ===
def run_self_upgrade_cycle():
    print("[UPGRADE LOOP] Checking for weak strategies...")
    grades = load_strategy_grades()
    weak_strats = get_weak_strategies(grades)

    if not weak_strats:
        print("[UPGRADE LOOP] No weak strategies found.")
        return

    for strategy in weak_strats:
        print(f"[UPGRADE] Triggered GPT rebuild for: {strategy}")

        # Generate smart prompt
        prompt = build_prompt_from_failures()

        # Ask GPT (via strategist persona)
        improved_code = ask_strategist(prompt)

        # Save improved file
        filename = f"{strategy.replace(' ', '_').lower()}_v2.py"
        save_code_to_file(filename, improved_code)

        # Log it with GhostPilot
        log_ghost_upgrade(prompt, improved_code, filename, persona="StrategistGPT")

        print(f"[UPGRADE] New version saved as: {filename}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():