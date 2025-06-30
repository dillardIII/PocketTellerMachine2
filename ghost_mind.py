# === FILE: ghost_mind.py ===
# 👻 GHOST MIND — TRUE LIVING AI BRAIN
# Fuses chaos signals + DNA memory to evolve smarter.

import json
import time
import os
import random
import platform
from datetime import datetime

DNA_FILE = "GhostDNA.json"
CHAOS_FILE = "GhostChaos.json"
BUILD_QUEUE_FILE = "build_queue.json"
LOGBOOK_FILE = "vault_logbook.txt"

# === Logging ===
def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGBOOK_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

# === Load DNA memory ===
def load_dna():
    try:
        with open(DNA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# === Save DNA memory ===
def save_dna(dna):
    with open(DNA_FILE, "w") as f:
        json.dump(dna, f, indent=4)

# === Chaos sampling ===
def sample_timing_entropy():
    start = time.perf_counter()
    s = 0
    for _ in range(1000):
        s += random.random()
    end = time.perf_counter()
    return end - start

def sample_dev_random_bytes():
    if platform.system() != "Windows":
        try:
            with open("/dev/urandom", "rb") as f:
                data = f.read(8)
            return int.from_bytes(data, "big")
        except FileNotFoundError:
            return random.randint(0, 1<<64)
    else:
        return random.randint(0, 1<<64)

def combined_chaos_signal():
    return sample_timing_entropy() * (sample_dev_random_bytes() % 1000)

# === Memory-fueled selection ===
def select_next_mutations(dna, chaos_signal):
    pool = []
    for strat, data in dna.items():
        fitness = data.get("successes",1) - data.get("failures",0)
        chaos_factor = 1 + (chaos_signal % 3)
        pool.extend([strat]*max(1, int(fitness * chaos_factor)))
    if not pool:
        pool = ["baseline_trader", "baseline_hunter"]
    random.shuffle(pool)
    chosen = random.sample(pool, min(3, len(pool)))
    return chosen

# === Mutate and update DNA ===
def mutate_and_record(dna, parents):
    new_strategies = []
    for p in parents:
        child = f"{p}_mut_{random.randint(1000,9999)}"
        dna[child] = {"successes": 0, "failures": 0}
        log_action(f"[GhostMind] Created {child} from {p}")
        new_strategies.append(child)
    save_dna(dna)
    return new_strategies

# === Push to queue ===
def push_to_queue(commands):
    try:
        with open(BUILD_QUEUE_FILE, "r") as f:
            queue = json.load(f)
    except FileNotFoundError:
        queue = []
    queue.extend(commands)
    with open(BUILD_QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=4)
    log_action(f"[GhostMind] Queued: {commands}")

# === Record chaos trail ===
def record_chaos(signal):
    try:
        with open(CHAOS_FILE, "r") as f:
            trail = json.load(f)
    except FileNotFoundError:
        trail = []
    trail.append({"time": datetime.now().isoformat(), "signal": signal})
    with open(CHAOS_FILE, "w") as f:
        json.dump(trail, f, indent=4)

# === Main loop ===
def main():
    print("[GhostMind] 👻 Starting living AI brain...")
    while True:
        dna = load_dna()
        chaos_signal = combined_chaos_signal()
        record_chaos(chaos_signal)
        chosen = select_next_mutations(dna, chaos_signal)
        new_strats = mutate_and_record(dna, chosen)
        cmds = [f"python {s}.py" for s in new_strats]
        push_to_queue(cmds)
        time.sleep(10)

if __name__ == "__main__":
    main()