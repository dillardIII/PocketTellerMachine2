from ghost_env import INFURA_KEY, VAULT_ADDRESS
# ⚙️ Macro Writer – auto-generates macros to run PTM tasks, Spectre ops, vault checks

import time
import random
import os

MACRO_DIR = "ptm_bridge"

def ensure_macro_dir():
    if not os.path.exists(MACRO_DIR):
        os.makedirs(MACRO_DIR)
        print(f"[MacroWriter] 🛠️ Created macro directory: {MACRO_DIR}")

def write_macro():
    macros = [
        "echo '[Macro] Running vault scan...'",
        "echo '[Macro] Restarting bridge agents...'",
        "python3 spectre_bot.py",
        "python3 ghost_intel_officer.py",
        "python3 vault_viewer.py"
    ]
    content = random.choice(macros)
    filename = f"{MACRO_DIR}/ptm_macro_{int(time.time())}.sh"
    with open(filename, "w") as f:
        f.write("#!/bin/bash\n" + content)
    print(f"[MacroWriter] 📝 Created macro: {filename}")

def macro_main_loop():
    ensure_macro_dir()
    print("[MacroWriter] 🚀 Starting macro generation loop...")
    while True:
        write_macro()
        time.sleep(15)

if __name__ == "__main__":
    macro_main_loop()

def log_event():ef drop_files_to_bridge():