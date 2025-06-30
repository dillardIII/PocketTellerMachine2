from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_exec_runner.py ===
import os
import subprocess
import time

MODULE_DIR = "ptm_modules"
EXEC_LOG = "logs/auto_exec.log"
EXECUTED = set()

os.makedirs("logs", exist_ok=True)

def log_exec(file):
    with open(EXEC_LOG, "a") as f:
        f.write(f"{file} executed.\n")

while True:
    for f in os.listdir(MODULE_DIR):
        if f.endswith(".py") and f not in EXECUTED:
            print(f"[AutoExec] ▶️ Running {f}")
            subprocess.run(["python3", os.path.join(MODULE_DIR, f)])
            log_exec(f)
            EXECUTED.add(f)
    time.sleep(10)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():