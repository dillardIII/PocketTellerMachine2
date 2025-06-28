# === FILE: bridge_path_debugger.py ===
# 🛠️ Bridge Path Debugger – Verifies presence of key bridge-side files (Replit side)

import os

required_files = [
    "file_exec_engine.py",
    "ghostforge_core.py",
    "bridge_pickup_agent.py",
    "bridge_drop_agent.py",
    "bridge_team_launcher.py",
    "bridge_folder_init.py",
    "app.py"
]

print("[BridgePathDebugger] 🔎 Checking for required core files in Replit workspace...\n")

workspace_root = "/home/runner/workspace/"
found_any = False

for filename in required_files:
    full_path = os.path.join(workspace_root, filename)
    if os.path.exists(full_path):
        print(f"✅ Found: {filename}")
        found_any = True
    else:
        print(f"❌ Missing: {filename}")

if not found_any:
    print("⚠️ No core bridge files found. Check if sync failed or file locations are incorrect.")