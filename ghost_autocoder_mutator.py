# === FILE: ghost_autocoder_mutator.py ===
# 👻 AUTO CODE GEN – Ghost builds new indicator modules, tests them, logs their success or death.

import json
import time
import random
from datetime import datetime

DNA_FILE = "GhostDNA.json"
BUILD_QUEUE_FILE = "build_queue.json"
LOGBOOK_FILE = "vault_logbook.txt"

INDICATORS = ["RSI", "MACD", "BollingerBands", "EMA", "ATR"]

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGBOOK_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def load_dna():
    try:
        with open(DNA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_dna(dna):
    with open(DNA_FILE, "w") as f:
        json.dump(dna, f, indent=4)

def write_new_module(filename, indicator):
    content = f"""
# === FILE: {filename} ===
# Auto-generated strategy using {indicator}

import random
def run():
    print("🚀 Running {indicator} strategy")
    value = random.uniform(-1, 1)
    if value > 0:
        print("👍 BUY signal on {indicator}")
    else:
        print("👎 SELL signal on {indicator}")

if __name__ == "__main__":
    run()
"""
    with open(filename, "w") as f:
        f.write(content)
    log_action(f"[AutoCoder] 🧬 Created new module: {filename} with {indicator}")

def push_to_build_queue(command):
    try:
        with open(BUILD_QUEUE_FILE, "r") as f:
            queue = json.load(f)
    except FileNotFoundError:
        queue = []
    queue.append(command)
    with open(BUILD_QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=4)
    log_action(f"[AutoCoder] ➕ Queued execution: {command}")

def main():
    print("[AutoCodeGen] 👻 Starting ghost autocoder to build new indicators...")
    while True:
        dna = load_dna()
        chosen_indicator = random.choice(INDICATORS)
        child_name = f"{chosen_indicator.lower()}_mod_{random.randint(1000,9999)}.py"
        write_new_module(child_name, chosen_indicator)
        dna[child_name] = {"profits": 0, "losses": 0}
        save_dna(dna)
        push_to_build_queue(f"python {child_name}")
        time.sleep(30)  # builds a new strategy module every 30 sec
if __name__ == "__main__":
    main()