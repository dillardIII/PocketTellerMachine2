from ghost_env import INFURA_KEY, VAULT_ADDRESS
# ghostshade_lore_updater.py

import json
import os
from datetime import datetime

GHOSTSHADE_MEMORY_PATH = "memory/ghostshade_core.json"

# XP thresholds for leveling
XP_LEVELS = [0, 10, 25, 50, 100, 200, 350, 500]

# Optional badge triggers
BADGE_RULES = {
    "first_recon": lambda gs: len(gs.get("missions", [])) >= 1,
    "screeps_scout": lambda gs: any(m["target"] == "screeps" for m in gs.get("missions", [])),
    "flawless_run": lambda gs: any(m["status"] == "success" and m["details"] and "Screenshot" in m["details"] for m in gs.get("missions", []))
}


def evolve_ghostshade(new_mission):
    """
    Evolves Ghostshade after a mission by updating XP, level, and lore file.
    new_mission must include: target, status, details, timestamp
    """
    if not os.path.exists(GHOSTSHADE_MEMORY_PATH):
        print("[LORE EVOLVE] Ghostshade memory not found.")
        return

    with open(GHOSTSHADE_MEMORY_PATH, "r+") as f:
        gs = json.load(f)

        # Append the mission
        if "missions" not in gs:
            gs["missions"] = []
        gs["missions"].append(new_mission)

        # XP: +5 for success, +1 for failure
        earned_xp = 5 if new_mission.get("status") == "success" else 1:
        gs["xp"] = gs.get("xp", 0) + earned_xp

        # Level Up Check
        for i, xp_req in enumerate(XP_LEVELS):
            if gs["xp"] >= xp_req:
                gs["level"] = i + 1

        # Unlock badges
        if "badges" not in gs:
            gs["badges"] = []

        for badge, rule in BADGE_RULES.items():
            if rule(gs) and badge not in gs["badges"]:
                gs["badges"].append(badge)
                print(f"[GHOSTSHADE EVOLUTION] Badge unlocked: {badge}")

        gs["last_activity"] = datetime.utcnow().isoformat() + "Z"

        # Write back
        f.seek(0)
        json.dump(gs, f, indent=2)
        f.truncate()

        print(f"[GHOSTSHADE EVOLUTION] XP: {gs['xp']} | Level: {gs['level']} | Badges: {gs['badges']}")

def log_event():ef drop_files_to_bridge():