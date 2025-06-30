from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: file_exec_engine.py ===
import os
import time
import subprocess

WATCH_DIR = "."
EXEC_DIR = "executed"
os.makedirs(EXEC_DIR, exist_ok=True)

def start_exec_engine():
    print("[FileExecEngine] 🚀 Watching for .py empire modules...")
    while True:
        for f in os.listdir(WATCH_DIR):
            if f.endswith(".py") and not f.startswith("executed_"):
                path = os.path.join(WATCH_DIR, f)
                print(f"[FileExecEngine] ⚙️ Executing: {f}")
                try:
                    subprocess.run(["python3", path], check=True)
                    os.rename(path, os.path.join(EXEC_DIR, f"executed_{f}"))
                except Exception as e:
                    print(f"[FileExecEngine] ❌ Error running {f}: {e}")
        time.sleep(5)

def log_event():ef drop_files_to_bridge():