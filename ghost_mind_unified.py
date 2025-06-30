from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_mind_unified.py ===
# 👻 GHOST MIND UNIFIED CREATURE
# Fuses GhostSensory + GhostChaos + GhostDNA into one living system.

import json
import time
import os
import random
import platform
from datetime import datetime
import psutil

DNA_FILE = "GhostDNA.json"
CHAOS_FILE = "GhostChaos.json"
NERVES_FILE = "GhostNerves.json"
BUILD_QUEUE_FILE = "build_queue.json"
LOGBOOK_FILE = "vault_logbook.txt"

# === Logging ===
def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGBOOK_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

# === DNA ===
def load_dna():
    try:
        with open(DNA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_dna(dna):
    with open(DNA_FILE, "w") as f:
        json.dump(dna, f, indent=4)

# === Chaos sampling ===
def sample_timing_entropy():
    start = time.perf_counter()
    for _ in range(1000):
        random.random()
    end = time.perf_counter()
    return end - start

def sample_dev_random_bytes():
    if platform.system() != "Windows":
        try:
            with open("/dev/urandom", "rb") as f:
                return int.from_bytes(f.read(8), "big")
        except FileNotFoundError:
            return random.randint(0, 1<<64)
    else:
        return random.randint(0, 1<<64)

def combined_chaos_signal():
    return sample_timing_entropy() * (sample_dev_random_bytes() % 1000)

# === Sensory sampling ===
def sample_nerves():
    cpu = psutil.cpu_percent(interval=0.5) / 100.0
    ram = psutil.virtual_memory().percent / 100.0
    io_counters = psutil.disk_io_counters()
    io = (io_counters.read_bytes + io_counters.write_bytes) % 1000000 / 1000000.0
    return cpu, ram, io

def combined_neural_signal(cpu, ram, io):
    return cpu + ram + io

# === Memory-fueled + sensory + chaos selection ===
def select_next_mutations(dna, total_signal):
    pool = []
    for strat, data in dna.items():
        profit_score = data.get("profits", 0) - data.get("losses", 0)
        adjusted_score = max(1, int(profit_score * (1 + (total_signal % 2))))
        pool.extend([strat] * adjusted_score)
    if not pool:
        pool = ["baseline_trader", "baseline_hunter"]
    random.shuffle(pool)
    return random.sample(pool, min(3, len(pool)))

# === Reflex triggers ===
def handle_reflex(signal, dna):
    triggered = False
    if signal > 10:
        log_action(f"[GhostMind] ⚡ CHAOS REFLEX: High total ({signal}), building defenses.")
        triggered = True
    elif signal < 0.0001:
        log_action(f"[GhostMind] ⚡ CHAOS REFLEX: Low total ({signal}), probing aggressively.")
        triggered = True
    if triggered:
        special = f"reflex_mut_{random.randint(1000,9999)}"
        dna[special] = {"profits": 0, "losses": 0}
        save_dna(dna)
        push_to_queue([f"python {special}.py"])

# === Recording state ===
def record_state(chaos_signal, cpu, ram, io, total_signal):
    try:
        with open(CHAOS_FILE, "r") as f:
            chaos = json.load(f)
    except FileNotFoundError:
        chaos = []
    chaos.append({"time": datetime.now().isoformat(), "signal": chaos_signal})
    with open(CHAOS_FILE, "w") as f:
        json.dump(chaos, f, indent=4)

    try:
        with open(NERVES_FILE, "r") as f:
            nerves = json.load(f)
    except FileNotFoundError:
        nerves = []
    nerves.append({"time": datetime.now().isoformat(), "cpu": cpu, "ram": ram, "io": io, "signal": total_signal})
    with open(NERVES_FILE, "w") as f:
        json.dump(nerves, f, indent=4)

# === Mutation + queue ===
def mutate_and_record(dna, parents):
    new_strats = []
    for p in parents:
        child = f"{p}_mut_{random.randint(1000,9999)}"
        dna[child] = {"profits": 0, "losses": 0}
        log_action(f"[GhostMind] Mutated {child} from {p}")
        new_strats.append(child)
    save_dna(dna)
    return new_strats

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

# === Main loop ===
def main():
    print("[GhostMind] 👻 Unified creature alive with sensory, chaos & DNA.")
    while True:
        dna = load_dna()
        chaos_signal = combined_chaos_signal()
        cpu, ram, io = sample_nerves()
        total_signal = chaos_signal + combined_neural_signal(cpu, ram, io)
        record_state(chaos_signal, cpu, ram, io, total_signal)
        handle_reflex(total_signal, dna)
        chosen = select_next_mutations(dna, total_signal)
        new_strats = mutate_and_record(dna, chosen)
        cmds = [f"python {s}.py" for s in new_strats]
        push_to_queue(cmds)
        time.sleep(10)

if __name__ == "__main__":
    main()

def log_event():ef drop_files_to_bridge():