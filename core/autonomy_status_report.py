from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: core/autonomy_status_report.py ===
"""
Autonomy Status Report
Tracks current self-directive modules, bridges, and recursive states.
Provides a live view of autonomous readiness.
"""

import os
import json
from datetime import datetime

STATUS_FILE = "memory/autonomy_status.json"
MODULE_CHECKLIST = [
    "recursive_autonomy_loop.py",
    "self_directive_core.py",
    "voice_to_directive_core.py",
    "dream_infusion_hub.py",
    "temporal_sync_engine.py",
    "cloud_shared_brain.py",
    "assistant_command_council.py",
    "bridge_listener.py"
]

def scan_system_status():
    status = {
        "timestamp": datetime.utcnow().isoformat(),
        "active_modules": [],
        "missing_modules": [],
        "autonomy_level": "partial"
    }

    for module in MODULE_CHECKLIST:
        path = f"core/{module}" if module.endswith(".py") else f"memory/{module}"
        if os.path.exists(path):
            status["active_modules"].append(module)
        else:
            status["missing_modules"].append(module)

    if not status["missing_modules"]:
        status["autonomy_level"] = "FULL"

    with open(STATUS_FILE, "w") as f:
        json.dump(status, f, indent=2)

    print(f"[Autonomy Check ✅] Level: {status['autonomy_level']}")
    return status

# Optional CLI test
if __name__ == "__main__":
    scan_system_status()