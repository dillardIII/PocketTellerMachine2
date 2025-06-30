#=== FILE: strategy_module_loader.py ===

#Loads strategy modules and makes them available to GPT and Cole

import os import importlib.util

STRATEGY_DIR = "strategies"

def get_strategy_modules(): modules = []

if not os.path.exists(STRATEGY_DIR):
    print(f"[Strategy Loader] ⚠️ Strategy directory '{STRATEGY_DIR}' not found.")
    return modules

for filename in os.listdir(STRATEGY_DIR):
    if filename.endswith(".py") and not filename.startswith("__"):
        filepath = os.path.join(STRATEGY_DIR, filename)
        module_name = filename[:-3]

        try:
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            modules.append(module)
            print(f"[Strategy Loader] ✅ Loaded strategy module: {module_name}")
        except Exception as e:
            print(f"[Strategy Loader] ❌ Failed to load '{module_name}': {e}")

return modules

