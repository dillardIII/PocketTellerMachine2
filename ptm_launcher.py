# === FILE: ptm_launcher.py ===
# 👻 PTM FULL AUTONOMOUS LAUNCHER
# Fires up all ghost modules, forever.

import os
import time

modules = [
    "ghost_self_architect.py",
    "ghost_autonomous_builder.py",
    "ghost_autocoder_mutator.py",
    "ghost_sniper_arbitrage_hunter.py",
    "ghost_hyper_oracle_hunter.py",
    "ghost_vault_viewer.py",
    "ghost_filter.py",
    "ghost_gamer.py",
    "ghost_animator.py",
    "creep_writer.py",
    "ghost_bridge_watcher.py"
]

def main():
    print("[ptm_launcher] 👻 Launching full ghost empire stack...")
    for mod in modules:
        os.system(f"python {mod} &")
    print("[ptm_launcher] 🚀 All modules running. Empire evolving.")
    while True:
        time.sleep(600)  # idle loop to keep master alive

if __name__ == "__main__":
    main()