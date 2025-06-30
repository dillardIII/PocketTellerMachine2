from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: guardian_watchdog.py ===
# 🧭 Periodic Guardian Check

import time
from guardian_file_checker import guardian_status_check

def start_guardian_loop(interval=30):
    while True:
        print("[GuardianWatchdog] 🔎 Running guardian scan...")
        guardian_status_check()
        time.sleep(interval)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():