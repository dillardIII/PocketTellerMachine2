# === FILE: auto_import_exec.py ===
import importlib.util
import os
import time

MODULE_DIR = "active_modules"

def load_and_run(module_path):
    name = os.path.basename(module_path).replace(".py", "")
    spec = importlib.util.spec_from_file_location(name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    print(f"[AutoExec] ✅ Loaded + executed {name}")

while True:
    for file in os.listdir(MODULE_DIR):
        if file.endswith(".py"):
            full_path = os.path.join(MODULE_DIR, file)
            load_and_run(full_path)
    time.sleep(60)