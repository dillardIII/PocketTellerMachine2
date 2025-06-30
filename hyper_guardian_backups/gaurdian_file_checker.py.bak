# === FILE: guardian_file_checker.py ===
# 🛡️ Guardian File Checker – Auto-heals missing files using GhostForge + Execution

import os
from file_exec_engine import execute_file  # Manual execution tool

required_files = {
    "main.py":              "rebuild_main.py",
    "autonomy_trigger_stack.py": "rebuild_trigger_stack.py",
    "command_listener.py":  "rebuild_command_listener.py",
    "reflex_engine.py":     "rebuild_reflex_engine.py",
    "sweep_handler.py":     "rebuild_sweep_handler.py",
    "file_exec_engine.py":  "rebuild_file_exec_engine.py",
    "bridge_pickup_agent.py": "rebuild_bridge_pickup.py",
    "bridge_drop_agent.py":   "rebuild_bridge_drop.py",
    "ghostforge_core.py":   "rebuild_ghostforge_core.py",
    "auto_code_dropper.py": "rebuild_auto_code_dropper.py",
    "meta_dispatcher.py":   "rebuild_meta_dispatcher.py"
}

def guardian_status_check():
    print("[Guardian] 🔍 Scanning for required files...")

    for target_file, recovery_script in required_files.items():
        if not os.path.exists(target_file):
            print(f"[Guardian] ⚠️ MISSING: {target_file}")
            if os.path.exists(recovery_script):
                print(f"[Guardian] 🛠️ Running repair: {recovery_script}")
                try:
                    execute_file(recovery_script)
                except Exception as e:
                    print(f"[Guardian] ❌ Repair failed: {e}")
            else:
                print(f"[Guardian] ❌ No repair script found for: {target_file}")
        else:
            print(f"[Guardian] ✅ OK: {target_file}")

def guardian_run_command(command):
    """Allow external systems to trigger guardian actions."""
    if command == "scan":
        guardian_status_check()
    elif command.startswith("repair "):
        filename = command.split(" ")[1]
        if filename in required_files:
            recovery_script = required_files[filename]
            if os.path.exists(recovery_script):
                print(f"[Guardian] 🛠️ Rebuilding {filename}...")
                execute_file(recovery_script)
            else:
                print(f"[Guardian] ❌ No script for {filename}")
        else:
            print(f"[Guardian] ❌ Unknown file: {filename}")
    else:
        print(f"[Guardian] ❓ Unknown command: {command}")