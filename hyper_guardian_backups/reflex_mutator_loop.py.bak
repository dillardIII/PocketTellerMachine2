# === FILE: reflex_mutator_loop.py ===

import time
from reflex_mutator import mutate

def start_mutation_loop(interval=900):  # every 15 min
    print("[MutatorLoop] 🔄 Mutation cycle running...")
    while True:
        mutate()
        time.sleep(interval)

if __name__ == "__main__":
    start_mutation_loop()