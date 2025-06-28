# === FILE: mission_launcher.py ===

# 🚀 Mission Launcher – Drops predefined code or logic files into PTM for execution

import json
from ghostforge_core import ghostforge_write

MISSIONS = {
    "build_greeter": {
        "filename": "greeter.py",
        "code": "print('Hello Boo, this is your PTM speaking.')"
    },
    "trigger_log_dump": {
        "filename": "log_dump.py",
        "code": "print('Dumping log files...')"
    }
}

def launch_mission(name):
    mission = MISSIONS.get(name)
    if not mission:
        print(f"[MissionLauncher] ❌ Unknown mission: {name}")
        return

    ghostforge_write(mission['filename'], mission['code'])
    print(f"[MissionLauncher] 🚀 Mission '{name}' launched.")

if __name__ == "__main__":
    launch_mission("build_greeter")