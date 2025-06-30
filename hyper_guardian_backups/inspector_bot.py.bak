# === FILE: inspector_bot.py ===

import os
import importlib.util

ESSENTIAL_FILES = [
    "auto_code_dropper.py",
    "bridge_drop_agent.py",
    "bridge_pickup_agent.py",
    "ghostforge_writer.py",
    "reflex_mutator.py",
    "sweep_handler.py",
    "file_exec_engine.py",
    "main.py"
]

def check_modules():
    print("[InspectorBot] 🔍 Beginning inspection of essential modules...")
    for file in ESSENTIAL_FILES:
        if not os.path.exists(file):
            print(f"[InspectorBot] ❌ Missing file: {file}")
        else:
            try:
                spec = importlib.util.spec_from_file_location("mod", file)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                print(f"[InspectorBot] ✅ Loaded successfully: {file}")
            except Exception as e:
                print(f"[InspectorBot] ⚠️ Load error in {file}: {e}")

if __name__ == "__main__":
    check_modules()