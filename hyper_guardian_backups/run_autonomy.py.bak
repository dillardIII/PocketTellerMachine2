# === FILE: run_autonomy.py ===
# 🚀 PTM Launch Trigger – Activates full AI stack, autonomy modules, and monitoring systems

from autonomy_core import AutonomyCore
from sandbox_monitor import monitor_sandboxes
from guardian_watchdog import start_guardian
from executor_engine import ExecutorEngine
from hivemind_sync import sync_all
import threading

def boot_ptm():
    print("💥 Launching PocketTellerMachine Autonomy Mode...")

    # === Core AI Stack ===
    ptm = AutonomyCore()
    ptm.start_all_systems()

    # === Guardian Watchdog ===
    threading.Thread(target=start_guardian, daemon=True).start()

    # === Sandbox Monitor ===
    threading.Thread(target=monitor_sandboxes, daemon=True).start()

    # === Task Executor ===
    executor = ExecutorEngine()
    threading.Thread(target=executor.run, daemon=True).start()

    # === HiveMind Sync Loop ===
    threading.Thread(target=sync_all, daemon=True).start()

    print("✅ PTM Autonomy stack online. Ghosts are awake. Bridges active. Reflexes hot.")

if __name__ == "__main__":
    boot_ptm()