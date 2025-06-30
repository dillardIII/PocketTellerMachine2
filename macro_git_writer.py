# ⚙️ MacroGitWriter – writes random macros, commits & auto-preps for push
# Automates creation of .sh/.py macros, stages & commits them

import time
import random
import os

MACRO_DIR = "ptm_bridge"

def ensure_macro_dir():
    if not os.path.exists(MACRO_DIR):
        os.makedirs(MACRO_DIR)
        print(f"[MacroGitWriter] 🛠️ Created macro dir: {MACRO_DIR}")

def write_macro():
    macros = [
        "echo '[Macro] Checking vault integrity...'",
        "python3 spectre_bot.py",
        "python3 ghost_intel_officer.py",
        "python3 vault_viewer.py",
        "echo '[Macro] Restarting drop agent...'"
    ]
    content = random.choice(macros)
    filename = f"{MACRO_DIR}/ptm_macro_{int(time.time())}.sh"
    with open(filename, "w") as f:
        f.write("#!/bin/bash\n" + content)
    print(f"[MacroGitWriter] 📝 Created macro: {filename}")

def git_commit_macro():
    os.system("git add .")
    commit_msg = f"auto macro commit at {time.strftime('%Y-%m-%d %H:%M:%S')}"
    os.system(f"git commit -m \"{commit_msg}\"")
    print("[MacroGitWriter] ✅ Staged and committed macros.")

def macro_git_loop():
    ensure_macro_dir()
    print("[MacroGitWriter] 🚀 Running macro+git loop...")
    while True:
        write_macro()
        git_commit_macro()
        time.sleep(30)

if __name__ == "__main__":
    macro_git_loop()