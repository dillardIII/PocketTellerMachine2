from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bot_mission_runner.py ===
# 🚀 Bot Mission Runner – Executes any strategy file dropped into /missions.

import os
import time
from file_exec_engine import FileExecEngine

MISSIONS_FOLDER = "missions"

def run_missions():
    print("[BotMissionRunner] 🎯 Scanning for new missions...")

    executor = FileExecEngine()
    processed = set()

    while True:
        try:
            files = os.listdir(MISSIONS_FOLDER)
            for file in files:
                path = os.path.join(MISSIONS_FOLDER, file)
                if file.endswith(".py") and file not in processed:
                    print(f"[BotMissionRunner] 🚀 Running mission: {file}")
                    executor.execute_file(path)
                    processed.add(file)
        except Exception as e:
            print(f"[BotMissionRunner] ❌ Error: {e}")
        time.sleep(5)

if __name__ == "__main__":
    run_missions()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():