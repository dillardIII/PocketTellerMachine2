# 💀 GhostMeld – fuses existing modules into new hybrid AI constructs
# Creates brand new .py files from combining parts of old modules

import os
import random
import time

SOURCE_DIR = "."
OUTPUT_DIR = "ptm_bridge"

def get_ghost_files():
    return [f for f in os.listdir(SOURCE_DIR) if f.startswith("ghost_") and f.endswith(".py")]

def meld_files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.readlines()
        content2 = f2.readlines()
    
    midpoint1 = len(content1) // 2
    midpoint2 = len(content2) // 2

    new_content = content1[:midpoint1] + ["\n# === MELD BREAK ===\n"] + content2[midpoint2:]

    new_filename = f"{OUTPUT_DIR}/melded_{file1.replace('.py', '')}_{file2.replace('.py', '')}_{int(time.time())}.py"
    with open(new_filename, "w") as nf:
        nf.writelines(new_content)
    print(f"[GhostMeld] 🔥 Created fused module: {new_filename}")

def ghost_meld_loop():
    print("[GhostMeld] 👻 Starting GhostMeld fusion loop...")
    while True:
        ghost_files = get_ghost_files()
        if len(ghost_files) >= 2:
            f1, f2 = random.sample(ghost_files, 2)
            meld_files(f1, f2)
        else:
            print("[GhostMeld] ⚠️ Not enough ghost modules to meld.")
        time.sleep(120)

if __name__ == "__main__":
    ghost_meld_loop()