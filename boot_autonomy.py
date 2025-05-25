# === FILE: boot_autonomy.py ===

from master_autonomy_loop import master_autonomy_loop
from autonomy_loop_controller import start_autonomy_daemon
from auto_cycle_builder import run_build_autonomy_cycle
from cole_self_healing_error_watcher import run_self_healing_autofix

import threading

def start_all_autonomy():
    print("[Autonomy Boot] 🚀 Starting all core autonomy systems...")

    threading.Thread(target=master_autonomy_loop, daemon=True).start()
    print("[Autonomy Boot] ✅ Master Autonomy Loop running.")

    threading.Thread(target=start_autonomy_daemon, daemon=True).start()
    print("[Autonomy Boot] ✅ Autonomy Loop Controller running.")

    threading.Thread(target=run_build_autonomy_cycle, daemon=True).start()
    print("[Autonomy Boot] ✅ Auto Cycle Builder running.")

    threading.Thread(target=run_self_healing_autofix, daemon=True).start()
    print("[Autonomy Boot] 🧠 Self-Healing Watcher running.")

    print("[Autonomy Boot] ✅✅✅ All core systems launched.")