#!/usr/bin/env python3
import subprocess
import time
import os
import random

PROCESSORS = [
    "bridge_drop_agent.py",
    "file_exec_engine.py",
    "macro_mutator.py",
    "mutation_forge.py",
    "swarm_macro_trainer.py",
    "quantum_drift_mutator.py"
]

running = []

def is_valid_python(script):
    result = subprocess.run(["python3", "-m", "py_compile", script], capture_output=True)
    if result.returncode != 0:
        print(f"[GhostEmpire] ⚠️ {script} failed syntax check:\n{result.stderr.decode()}")
    return result.returncode == 0

def start_process(script):
    try:
        print(f"[GhostEmpire] 🚀 Launching {script}")
        p = subprocess.Popen(["python3", script])
        return p
    except Exception as e:
        print(f"[GhostEmpire] ❌ Failed to launch {script}: {e}")
        return None

def scan_new_processors():
    files = os.listdir(".")
    for f in files:
        if f.endswith(".py") and f not in PROCESSORS and f != "ghost_empire_launcher.py":
            if is_valid_python(f):
                PROCESSORS.append(f)
                print(f"[GhostEmpire] ⚡ New savage processor detected: {f}")
            else:
                print(f"[GhostEmpire] 💀 Skipping invalid processor: {f}")

while True:
    scan_new_processors()

    while len(running) < 10:
        candidate = random.choice(PROCESSORS)
        proc = start_process(candidate)
        if proc:
            running.append((proc, candidate))
        time.sleep(random.uniform(1, 3))

    for proc, script in running[:]:
        if proc.poll() is not None:
            print(f"[GhostEmpire] ☠️ {script} crashed. Scheduling restart.")
            running.remove((proc, script))
            time.sleep(random.uniform(2, 6))

    time.sleep(2)

def log_event():ef drop_files_to_bridge():