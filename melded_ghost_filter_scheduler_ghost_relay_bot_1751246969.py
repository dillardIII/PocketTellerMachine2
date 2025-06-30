from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_filter_scheduler.py ===

# ⏱️ GhostFilter Scheduler – Runs ghost_filter.scan() on a timed loop

import threading
import time
from ghost_filter import GhostFilter

def start_ghostfilter_daemon(interval_seconds=300):

# === MELD BREAK ===

    for task in queue:
        if task["filename"] == filename:
            log(f"🛑 Task {filename} already exists. Skipping.")
            return

    queue.append({
        "filename": filename,
        "code": code,
        "status": "pending"
    })

    with open(MISSION_QUEUE, "w") as f:
        json.dump(queue, f, indent=4)

    log(f"✅ Injected task from {source}: {filename}")

# Example test
if __name__ == "__main__":
    inject_task(
        "ghost_ping.py",
        "# GhostPing\nprint('[GhostRelay] 👻 Ping received.')",
        source="ManualTest"
    )

def log_event():ef drop_files_to_bridge():