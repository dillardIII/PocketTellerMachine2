from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autonomy_daemon.py ===
# 🔁 Autonomy Daemon – Boots and loops all core systems

import threading
from guardian_watchdog import start_guardian_loop
from rebuild_deployer import deploy_all_rebuilders
from ptm_task_orchestrator import orchestrate_tasks
from recovery_launcher import launch_recovery_sweep

def run_autonomy():
    print("[AutonomyDaemon] 🔁 Starting full autonomy engine...")
    threading.Thread(target=start_guardian_loop).start()
    threading.Thread(target=deploy_all_rebuilders).start()
    threading.Thread(target=orchestrate_tasks).start()
    threading.Thread(target=launch_recovery_sweep).start()

if __name__ == "__main__":
    run_autonomy()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():