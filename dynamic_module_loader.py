# 🧬 Loads and executes new empire modules dynamically
import os
import time
import subprocess

MODULES_DIR = "ptm_modules"
os.makedirs(MODULES_DIR, exist_ok=True)

print("[Loader] 🧬 Dynamic loader watching modules...")
while True:
    for f in os.listdir(MODULES_DIR):
        if f.endswith(".py"):
            filepath = os.path.join(MODULES_DIR, f)
            print(f"[Loader] 🚀 Launching: {f}")
            subprocess.Popen(["python3", filepath])
            os.remove(filepath)
    time.sleep(10)