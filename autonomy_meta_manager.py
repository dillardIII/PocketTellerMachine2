from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autonomy_meta_manager.py ===
# Adjusts roadmap based on system feedback and current AI performance

import json
import time

from system_status import get_current_status
from roadmap_generator import regenerate_roadmap
from phase_status_monitor import update_phase_progress

def review_and_reprioritize_roadmap():
    print("[Meta Manager] 📊 Reviewing system status and adjusting roadmap...")

    status = get_current_status()
    if not status:
        print("[Meta Manager] ⚠️ No current status available.")
        return

    priority_level = calculate_priority_level(status)
    new_roadmap = regenerate_roadmap(priority_level)

    save_new_roadmap(new_roadmap)
    update_phase_progress("roadmap", True)

    print(f"[Meta Manager] ✅ Roadmap updated at {time.ctime()}")

def calculate_priority_level(status):
    # Simulated priority algorithm
    if status.get("errors_detected"):
        return "critical"
    elif status.get("lagging_components"):
        return "high"
    else:
        return "normal"

def save_new_roadmap(roadmap):
    with open("system_roadmap.json", "w") as f:
        json.dump(roadmap, f, indent=4)
    print("[Meta Manager] 💾 New roadmap saved.")

def log_event():ef drop_files_to_bridge():