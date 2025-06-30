from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: overmind_controller.py ===
import time
from meta_dispatcher import MetaDispatcher

def overmind_loop():
    dispatcher = MetaDispatcher()
    print("[Overmind] 🧠 Overmind loop scanning for new empire expansions...")
    while True:
        dispatcher.list_status()
        time.sleep(30)

def log_event():ef drop_files_to_bridge():