from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: hotloader.py ===
# ♻️ Hotloader – Dynamically imports or reloads modules dropped into the system without restarting PTM

import importlib.util
import os
import sys
import time

WATCH_FOLDER = "generated_modules"  # Where GhostForge or bridge drops new code
LOADED_MODULES = {}

def load_module_from_file(filepath):
    module_name = os.path.splitext(os.path.basename(filepath))[0]
    if module_name in LOADED_MODULES:
        print(f"[Hotloader] 🔁 Reloading module: {module_name}")
        importlib.reload(LOADED_MODULES[module_name])
    else:
        print(f"[Hotloader] 🆕 Loading module: {module_name}")
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        LOADED_MODULES[module_name] = module
        sys.modules[module_name] = module
    return module_name

def watch_and_load(interval=5):
    print("[Hotloader] 🔥 Watching for module drops...")
    while True:
        try:
            for file in os.listdir(WATCH_FOLDER):
                if file.endswith(".py"):
                    full_path = os.path.join(WATCH_FOLDER, file)
                    load_module_from_file(full_path)
            time.sleep(interval)
        except Exception as e:
            print(f"[Hotloader] ⚠️ Error loading module: {e}")

def log_event():ef drop_files_to_bridge():