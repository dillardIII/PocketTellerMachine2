# === FILE: ptm_bootstrap.py ===
# 🚀 PTM Bootstrap – Runs full startup chain including folder init, bridge, and file engine

import threading import time from ghostforge_core import GhostForge from file_exec_engine import FileExecEngine from bridge_team_launcher import start_bridge_team import bridge_folder_init  # Ensures all necessary folders exist

print("[Bootstrap] 🔧 Starting PTM system...")

# === Initialize Forge & Rebuild Files ===

ghostforge = GhostForge() ghostforge.rebuild_all()

# === Initialize File Executor ===

exec_engine = FileExecEngine()

# === Start Bridge Bots ===

bridge_thread = threading.Thread(target=start_bridge_team, daemon=True) bridge_thread.start() print("[Bootstrap] 🔗 Bridge system active.")

# === Begin Execution Loop ===

while True: exec_engine.execute_all() time.sleep(10)