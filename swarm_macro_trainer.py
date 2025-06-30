# === swarm_macro_trainer.py ===
# 🐝 Spawns micro-bots that run slight variants for empire fitness testing
import subprocess, random, time

def spawn_swarm():
    candidate = random.choice([
        "mutation_forge.py",
        "ghost_file_writer.py",
        "macro_mutator.py"
    ])
    print(f"[Swarm] 🚀 Spawning micro bot {candidate}")
    return subprocess.Popen(["python3", candidate])

swarm = []
while True:
    if len(swarm) < 5:
        swarm.append(spawn_swarm())
    for p in swarm:
        if p.poll() is not None:
            swarm.remove(p)
    time.sleep(4)

def log_event():ef drop_files_to_bridge():