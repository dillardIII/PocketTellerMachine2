from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_sensory.py ===
# 👻 GHOST SENSORY NERVES
# Uses CPU, RAM, I/O as pseudo-biological nerve signals to steer your AI empire.

import json
import time
import psutil
from datetime import datetime
import random

NERVES_FILE = "GhostNerves.json"
LOGBOOK_FILE = "vault_logbook.txt"
BUILD_QUEUE_FILE = "build_queue.json"

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGBOOK_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def sample_nerves():
    cpu = psutil.cpu_percent(interval=0.5) / 100.0  # normalize to 0-1
    ram = psutil.virtual_memory().percent / 100.0
    io_counters = psutil.disk_io_counters()
    io_pulse = (io_counters.read_bytes + io_counters.write_bytes) % 1000000 / 1000000.0
    return cpu, ram, io_pulse

def combined_neural_signal(cpu, ram, io):
    # Example: sum of stresses
    return cpu + ram + io

def record_nerves(cpu, ram, io, signal):
    try:
        with open(NERVES_FILE, "r") as f:
            nerves_history = json.load(f)
    except FileNotFoundError:
        nerves_history = []
    nerves_history.append({
        "time": datetime.now().isoformat(),
        "cpu": cpu,
        "ram": ram,
        "io": io,
        "signal": signal
    })
    with open(NERVES_FILE, "w") as f:
        json.dump(nerves_history, f, indent=4)

def decide_next_mutations(signal):
    modules = ["VaultViewer", "GhostFilter", "GhostTrader", "GhostGamer", "AutoFarmer", "EntropyHunter"]
    weighted = []
    for mod in modules:
        if random.random() < (signal % 1):  # pseudo nerve spike:
            weighted.append(mod)
    if not weighted:
        weighted.append(random.choice(modules))
    return weighted

def push_to_queue(commands):
    try:
        with open(BUILD_QUEUE_FILE, "r") as f:
            queue = json.load(f)
    except FileNotFoundError:
        queue = []
    queue.extend(commands)
    with open(BUILD_QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=4)
    log_action(f"[GhostSensory] Queued from nerves: {commands}")

def main():
    print("[GhostSensory] 👻 Starting nerve system with CPU, RAM, I/O sensing...")
    while True:
        cpu, ram, io = sample_nerves()
        signal = combined_neural_signal(cpu, ram, io)
        record_nerves(cpu, ram, io, signal)
        log_action(f"[GhostSensory] Neural signal: {signal:.4f} (CPU:{cpu:.2f}, RAM:{ram:.2f}, IO:{io:.2f})")
        next_mutations = decide_next_mutations(signal)
        cmds = [f"python {mod}_mut_{random.randint(1000,9999)}.py" for mod in next_mutations]
        push_to_queue(cmds)
        time.sleep(10)

if __name__ == "__main__":
    main()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():