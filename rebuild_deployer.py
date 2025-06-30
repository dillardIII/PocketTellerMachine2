from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: rebuild_deployer.py ===
# 🧰 Fixed: Executes rebuild scripts using execute_file()

import os
from file_exec_engine import execute_file

REBUILD_SCRIPTS = [
    "rebuild_main.py",
    "rebuild_command_listener.py",
    "rebuild_reflex_engine.py",
    "rebuild_sweep_handler.py",
    "rebuild_auto_code_dropper.py",
    "rebuild_meta_dispatcher.py",
    "rebuild_bridge_pickup.py",
    "rebuild_bridge_drop.py",
    "rebuild_ghostforge_core.py",
    "rebuild_file_exec_engine.py",
    "rebuild_trigger_stack.py"
]

def deploy_all_rebuilders():
    print("[RebuildDeployer] 📦 Deploying all rebuild scripts...")
    for script in REBUILD_SCRIPTS:
        if os.path.exists(script):
            try:
                execute_file(script)
                print(f"[RebuildDeployer] ✅ Ran {script}")
            except Exception as e:
                print(f"[RebuildDeployer] ❌ Error running {script}: {e}")
        else:
            print(f"[RebuildDeployer] ⚠️ Missing: {script}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():