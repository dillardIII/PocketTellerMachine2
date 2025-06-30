from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: mission_generator_loop.py ===

import time
from mission_generator import generate_random_mission
from ghost_relay_bot import inject_task

def start_mission_loop(interval=300):  # every 5 min
    print("[MissionLoop] 🔁 Mission generator started.")
    while True:
        filename, code = generate_random_mission()
        inject_task(filename, code, source="MissionLoop")
        print(f"[MissionLoop] 🧠 Dropped new mission: {filename}")
        time.sleep(interval)

if __name__ == "__main__":
    start_mission_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():