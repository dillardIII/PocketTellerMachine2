from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_instinct_trigger.py ===

# 🧬 AutoInstinct – Kicks off internal instinct loops like feeding commands or writing files

import threading
from auto_command_feeder import start_command_loop
from auto_mutator import mutate_code

def start_instincts():
    print("[Instinct] 🔮 Internal drive systems initializing...")
    
    # 1. Autonomous Command Generator
    threading.Thread(target=start_command_loop, daemon=True).start()

    # (Optional) add more future instincts here
    print("[Instinct] ✅ Instinct loop activated.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():