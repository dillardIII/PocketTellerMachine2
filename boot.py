from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: boot.py ===

# 🚀 PTM Boot – Launches core system auditors, repair agents, and monitors.
# This is the main entry point to activate InspectorBot, GhostForge Watcher, and the Autobuilder.

import time
import threading
from bots.inspector_bot import full_system_inspect
from bots.ghostforge_autobuilder import autobuild
from ghostforge_repair_watcher import process_repair_requests

def run_inspectorbot():
    print("[BOOT] 🕵️ Starting InspectorBot...")
    full_system_inspect()

def run_autobuilder():
    print("[BOOT] 🧱 Starting GhostForge Autobuilder...")
    autobuild()

def run_repair_watcher():
    print("[BOOT] 👁️ Starting GhostForge Repair Watcher...")
    process_repair_requests()

def start_all_systems():
    print("[BOOT] 🔥 Launch sequence initiated.")

    # === InspectorBot (Audit & Heartbeat)
    inspector_thread = threading.Thread(target=run_inspectorbot)
    inspector_thread.start()

    # === GhostForge Watcher (Reads Repair Queue)
    repair_thread = threading.Thread(target=run_repair_watcher)
    repair_thread.start()

    # === GhostForge Autobuilder (Fixes files)
    autobuild_thread = threading.Thread(target=run_autobuilder)
    autobuild_thread.start()

    # Optional: Wait for all to complete
    inspector_thread.join()
    repair_thread.join()
    autobuild_thread.join()

    print("[BOOT] ✅ All PTM watchdogs have completed.")

# === Entry point ===
if __name__ == "__main__":
    print("[PTM] 💻 System booting up...")
    start_all_systems()
    print("[PTM] 🚀 System is live.")

def log_event():ef drop_files_to_bridge():