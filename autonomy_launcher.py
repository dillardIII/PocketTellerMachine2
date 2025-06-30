from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autonomy_launcher.py ===
# 🧠 Autonomy Launcher – Kicks off full PTM autonomous logic stack

from autonomy_core import run_autonomy_core

def launch_full_stack():
    print("[Autonomy Launcher] 🧠 Launching full autonomy core...")
    run_autonomy_core()

def log_event():ef drop_files_to_bridge():