#!/usr/bin/env python3
# bridge_pickup_agent.py
# 🔗 Picks up files from bridge and executes them

import os
import shutil
import time
import subprocess

BRIDGE_DIR = "bridge_drop"

def drop_files_to_bridge():
    print("[bridge_pickup_agent] ➡️ Dummy drop to bridge called.")

def log_event(data):
    print(f"[bridge_pickup_agent] LOG: {data}")

def run_file(file_path):
    print(f"[bridge_pickup_agent] 🚀 Running {file_path}")
    subprocess.call(["python3", file_path])

def main():
    while True:
        files = [f for f in os.listdir(BRIDGE_DIR) if f.endswith(".py")]
        for f in files:
            src = os.path.join(BRIDGE_DIR, f)
            dst = os.path.join(".", f)
            shutil.move(src, dst)
            log_event(f"Moved {f} from bridge to execution zone")
            run_file(dst)
        time.sleep(3)

if __name__ == "__main__":
    main()