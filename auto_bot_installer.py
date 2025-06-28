# === FILE: auto_bot_installer.py ===
# 🤖 Auto Bot Installer – ensures empire modules run forever

import os
import subprocess
import time

EMPIRE_FILES = [
    "meta_dispatcher.py",
    "ghost_memory_matrix.py",
    "hyperforge_pipeline.py",
    "quantum_brain.py",
    "vault_announcer.py",
    "simulated_whisper.py",
    "gpt_auto_seed_bot.py",
    "self_forge_guardian.py",
    "drop_bot_loop.py",
    "pickup_bot_loop.py",
    "infinite_builder.py"
]

running_processes = {}

def ensure_bots_running():
    for file in EMPIRE_FILES:
        if os.path.exists(file):
            if file not in running_processes or running_processes[file].poll() is not None:
                print(f"[AutoInstaller] 🛠️ Starting {file} ...")
                proc = subprocess.Popen(["python3", file])
                running_processes[file] = proc

def bot_installer_loop():
    print("[AutoInstaller] 🔄 Auto bot install loop engaged...")
    while True:
        ensure_bots_running()
        time.sleep(15)

if __name__ == "__main__":
    bot_installer_loop()