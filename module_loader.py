from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Module Loader – Dynamic Plugin and Hot Reload System for PTM

Allows the system to load new modules, reload updated ones,
and plug in assistant upgrades on the fly. Enables growth
without rebooting core logic.
"""

import importlib
import traceback

LOADED_MODULES = {}

def load_module(name: str):
    try:
        if name in LOADED_MODULES:
            print(f"[🔁 Reload] {name}")
            LOADED_MODULES[name] = importlib.reload(LOADED_MODULES[name])
        else:
            print(f"[📦 Load] {name}")
            LOADED_MODULES[name] = importlib.import_module(name)
        print(f"[✅ Module Active] {name}")
        return LOADED_MODULES[name]
    except Exception as e:
        print(f"[❌ ERROR] Failed to load module '{name}'")
        traceback.print_exc()
        return None

def unload_module(name: str):
    if name in LOADED_MODULES:
        del LOADED_MODULES[name]
        print(f"[❌ Unloaded] {name}")
    else:
        print(f"[WARN] Module '{name}' not loaded.")

def list_loaded_modules():
    return list(LOADED_MODULES.keys())

# Manual run
if __name__ == "__main__":
    print("📦 PTM Module Loader")
    while True:
        cmd = input("loader> ").strip().lower()
        if cmd in ["exit", "quit"]:
            break
        elif cmd.startswith("load "):
            load_module(cmd.split("load ")[1])
        elif cmd.startswith("unload "):
            unload_module(cmd.split("unload ")[1])
        elif cmd == "list":
            print("Loaded:", list_loaded_modules())
        else:
            print("Commands: load <name>, unload <name>, list, exit")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():