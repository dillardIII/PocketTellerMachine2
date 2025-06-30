# recursive_builder_loop.py
# Continuously evolves PTM by triggering recursive GhostForge module generation

import time
from ghostforge_core import GhostForge
from self_updater import bulk_write

LOOP_INTERVAL = 60  # in seconds

def evolve_cycle():
    forge = GhostForge(persona="RecursiveCore")
    base_modules = forge.suggest_next()

    module_dict = {}
    for mod_name, purpose in base_modules:
        filename = f"auto_{mod_name}"
        base_code = f"# Placeholder for {filename}\n\nprint('Running {filename}')"
        module_dict[f"core/{filename}.py"] = f"# {purpose}\n{base_code}"

    results = bulk_write(module_dict)
    for res in results:
        print(res)

if __name__ == "__main__":
    print("[RecursiveLoop] Starting evolution cycle...")
    while True:
        evolve_cycle()
        time.sleep(LOOP_INTERVAL)