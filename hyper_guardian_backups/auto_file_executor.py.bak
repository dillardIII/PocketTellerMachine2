# === FILE: auto_file_executor.py ===
# ⚡ Auto File Executor – launches .py files dropped by your empire bots

import os
import subprocess
import time

WATCH_DIRS = ["live_workspace", "ptm_bridge_drop"]
EXECUTED_LOG = "executed_files.log"

executed_files = set()

def load_log():
    if os.path.exists(EXECUTED_LOG):
        with open(EXECUTED_LOG, "r") as f:
            for line in f:
                executed_files.add(line.strip())

def save_log(file):
    with open(EXECUTED_LOG, "a") as f:
        f.write(f"{file}\n")

def auto_exec_loop():
    print("[AutoExecutor] 🚀 Watching for new files to execute...")
    load_log()
    while True:
        for directory in WATCH_DIRS:
            if os.path.exists(directory):
                for file in os.listdir(directory):
                    if file.endswith(".py"):
                        full_path = os.path.join(directory, file)
                        if full_path not in executed_files:
                            try:
                                print(f"[AutoExecutor] ⚡ Running {full_path} ...")
                                subprocess.Popen(["python3", full_path])
                                executed_files.add(full_path)
                                save_log(full_path)
                            except Exception as e:
                                print(f"[AutoExecutor] ❌ Failed to execute {file}: {e}")
        time.sleep(10)

if __name__ == "__main__":
    auto_exec_loop()