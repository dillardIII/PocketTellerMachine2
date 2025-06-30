# === FILE: ghost_forger_recursive.py ===
# 👻 PTM Recursive Ghost Forger
# Reads vault logs, mutates strategy generations, pushes to build queue, logs everything.

import json
import time
import re
from datetime import datetime
import random
from collections import Counter

LOGBOOK_FILE = "vault_logbook.txt"
BUILD_QUEUE_FILE = "build_queue.json"

def load_vault_logs():
    try:
        with open(LOGBOOK_FILE, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def extract_strategy_counts(log_lines):
    pattern = r"Auto-generated file: (\w+)_module\.py"
    strategies = []
    for line in log_lines:
        match = re.search(pattern, line)
        if match:
            strategies.append(match.group(1))
    return Counter(strategies)

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGBOOK_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def generate_strategy_module(strategy_name, parameters):
    filename = f"{strategy_name}_module.py"
    content = f"""
# === FILE: {filename} ===
# Forged by recursive GhostForger for strategy: {strategy_name}
# Parameters: {parameters}

def run():
    print("👻 Forged strategy {strategy_name} running with parameters: {parameters}")

if __name__ == "__main__":
    run()
"""
    write_file(filename, content)
    log_action(f"GhostForger forged: {filename}")
    print(f"[GhostForger] 🧬 Created {filename}")
    return filename

def push_to_build_queue(commands):
    try:
        with open(BUILD_QUEUE_FILE, "r") as f:
            current_queue = json.load(f)
    except FileNotFoundError:
        current_queue = []
    current_queue.extend(commands)
    with open(BUILD_QUEUE_FILE, "w") as f:
        json.dump(current_queue, f, indent=4)
    log_action(f"Queued for execution: {commands}")
    print(f"[GhostForger] ➕ Added to build_queue.json: {commands}")

def mutate_parameters():
    return {
        "risk": round(random.uniform(0.1, 2.5), 2),
        "lookback": random.randint(5, 60),
        "threshold": round(random.uniform(0.01, 0.5), 3)
    }

def main():
    print("[GhostForger] 👻 Starting recursive evolution loop...")
    while True:
        log_lines = load_vault_logs()
        strategy_counter = extract_strategy_counts(log_lines)
        
        if strategy_counter:
            # Decide which to mutate more often by weighting selection
            strategies = []
            for strat, count in strategy_counter.items():
                strategies.extend([strat] * count)  # more counts = more likely
            random.shuffle(strategies)

            # Forge new modules based on history
            commands = []
            for _ in range(random.randint(1, 3)):  # build 1-3 new mutations
                chosen_strategy = random.choice(strategies)
                params = mutate_parameters()
                module_file = generate_strategy_module(chosen_strategy, params)
                commands.append(f"python {module_file}")
            
            push_to_build_queue(commands)
        
        time.sleep(10)  # slightly slower loop to give empire time to execute

if __name__ == "__main__":
    main()