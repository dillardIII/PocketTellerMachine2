# === FILE: ghost_evolution_loop.py ===

import time
from ghost_evolution_engine import evolve

def start_evolution_loop(interval=600):  # every 10 min
    print("[EvolutionLoop] 🧬 Ghost evolution running...")
    while True:
        evolve()
        time.sleep(interval)

if __name__ == "__main__":
    start_evolution_loop()