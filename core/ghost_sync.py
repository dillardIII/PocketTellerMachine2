from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Ghost Sync – Handles syncing GhostBot memory and decisions across PTM.

This module pulls, reads, and stores shared memory data
from GhostBot’s long-term log and updates internal PTM syncs.
"""

import os
import json
from cole_logger import log_event
from cole_brain import log_state

GHOST_MEMORY_FILE = "data/ghost_memory_log.json"

def sync_brain_state():
    """
    Sync Ghost memory file into local PTM assistant logic.
    Updates short-term state and stores relevant insights.
    """
    if not os.path.exists(GHOST_MEMORY_FILE):
        log_event("Ghost Sync", "⚠️ Ghost memory file not found.", "warn")
        log_state("ghost_sync", "missing")
        return

    try:
        with open(GHOST_MEMORY_FILE, "r") as f:
            ghost_data = json.load(f)

        if not isinstance(ghost_data, list):
            raise ValueError("Ghost memory log is not a list.")

        latest = ghost_data[-1] if ghost_data else None

        if latest:
            log_event("Ghost Sync", f"✅ Synced latest: {latest['category']}", "info")
            log_state("ghost_sync", {
                "timestamp": latest.get("timestamp"),
                "category": latest.get("category"),
                "bot": latest.get("bot")
            })
        else:
            log_event("Ghost Sync", "⚠️ Ghost log is empty.", "warn")
            log_state("ghost_sync", "empty")

    except Exception as e:
        log_event("Ghost Sync", f"❌ Error syncing: {e}", "error")
        log_state("ghost_sync", "corrupted")


# === Optional test mode ===
if __name__ == "__main__":
    sync_brain_state()