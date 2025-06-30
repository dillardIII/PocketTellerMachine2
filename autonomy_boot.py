from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autonomy_boot.py ===
"""
Autonomy Boot:
Launches the PTM autonomy stack — assistant logic, strategy routing, memory sync, and more.
"""

from master_autonomy_loop import master_autonomy_loop
from assistant_message_router import route_bot_tasks
from cole_brain import log_state
import time

ACTIVE_ASSISTANTS = ["Mentor", "MoCash", "Strategist", "DrillInstructor"]

def boot_all_systems():
    print("\n[BOOT] Starting background services...")

    # === Log current boot cycle
    log_state("ptm_status", "booting")
    log_state("boot_time", time.strftime("%Y-%m-%d %H:%M:%S"))

    # === Start Assistant Routers
    for bot in ACTIVE_ASSISTANTS:
        print(f"[Autonomy Boot] 🔁 Routing tasks for: {bot}")
        route_bot_tasks(bot)

    # === Launch Master Autonomy Loop (Core AI)
    print("[Autonomy Boot] 🚀 Starting all core autonomy systems...")
    master_autonomy_loop()

    # === Mark status as running
    log_state("ptm_status", "running")
    print("[BOOT] ✅ All background services launched.\n")

# === Local startup test ===
if __name__ == "__main__":
    boot_all_systems()

def log_event():ef drop_files_to_bridge():