from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: guardian_forge_loop.py ===
# 🛡️ Guardian Forge Loop – monitors all PTM directories & heals by invoking self-forge

import os
import time
import subprocess

WATCH_DIRS = [
    "ptm_strategy_prompts",
    "ptm_bridge_drop",
    "sample_strategies",
    "."
]

def trigger_self_forge():
    print("[GuardianForge] 🛠️ Calling SelfForge Installer...")
    subprocess.Popen(["python3", "self_forge_installer.py"])

def guardian_loop():
    while True:
        any_issue = False
        for d in WATCH_DIRS:
            if not os.path.exists(d):
                print(f"[GuardianForge] ⚠️ Missing directory: {d} — recreating.")
                os.makedirs(d)
                any_issue = True

        critical_files = [
            "auto_strategy_scheduler.py",
            "auto_code_dropper.py",
            "meta_dispatcher.py",
            "ghostforge_core.py",
            "vault_sync_manager.py"
        ]
        for f in critical_files:
            if not os.path.exists(f):
                print(f"[GuardianForge] 🚨 Critical file missing: {f}")
                any_issue = True

        if any_issue:
            trigger_self_forge()

        time.sleep(45)  # Check every 45 seconds
if __name__ == "__main__":
    guardian_loop()

def log_event():ef drop_files_to_bridge():