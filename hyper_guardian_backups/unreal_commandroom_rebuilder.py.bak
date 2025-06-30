# === FILE: unreal_commandroom_rebuilder.py ===

# 🧱 Unreal Command Room Rebuilder – Compiles or regenerates CommandRoom project

import subprocess
import os
import json

CONFIG_FILE = "predator_target_path.json"
LOG_FILE = "vault/logs/commandroom_rebuild.log"

def log(msg):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{msg}\n")
    print(f"[Rebuilder] {msg}")

def rebuild():
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            project_path = config.get("uproject_path")
            ue_build_tool = config.get("ue_build_tool")  # e.g., path to `UnrealBuildTool.exe`

        if not os.path.exists(project_path):
            log("❌ Project file not found.")
            return

        if not os.path.exists(ue_build_tool):
            log("❌ UnrealBuildTool not found.")
            return

        log("🔨 Building Command Room...")
        subprocess.run([
            ue_build_tool,
            "CommandRoom",
            "Win64",
            "Development",
            f"-Project={project_path}",
            "-WaitMutex"
        ], check=True)

        log("✅ Command Room built successfully.")

    except Exception as e:
        log(f"❌ Build failed: {e}")

if __name__ == "__main__":
    rebuild()