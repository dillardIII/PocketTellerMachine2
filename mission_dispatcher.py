from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: mission_dispatcher.py ===
# 🛰️ Mission Dispatcher – Routes commands to appropriate bots on Replit side.

import time
from command_queue_handler import get_next_command

def dispatch_loop():
    print("[Mission Dispatcher] 🚀 Starting command dispatch loop...")

    while True:
        command = get_next_command()
        if command:
            if command == "INSTALL_ALL":
                print("[Mission Dispatcher] 🛠️ Triggering full install process...")
                from replit_bot_installer import install_files
                install_files()
            else:
                print(f"[Mission Dispatcher] 🤖 Unknown command: {command}")
        time.sleep(5)

if __name__ == "__main__":
    dispatch_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():