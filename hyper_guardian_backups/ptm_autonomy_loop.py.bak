# === FILE: ptm_autonomy_loop.py ===
# 🧠 PTM Autonomy Loop – Orchestrates all background bots and system repair

import threading
import time
from log_watcher import watch_logs_and_trigger_rebuild
from self_rebuilder import self_rebuilder_loop
from persona_watcher import monitor_persona_loop
from status_overlay import update_overlay_loop

def run_thread(name, target):
    try:
        thread = threading.Thread(target=target, name=name, daemon=True)
        thread.start()
        print(f"[LOOP LAUNCHER] 🚀 Started: {name}")
    except Exception as e:
        print(f"[LOOP LAUNCHER ERROR] ❌ {name}: {e}")

def start_autonomy_loops():
    print("[AUTONOMY LOOP] 🔁 Starting all background loops...")
    run_thread("SelfRebuilder", self_rebuilder_loop)
    run_thread("LogWatcher", watch_logs_and_trigger_rebuild)
    run_thread("OverlayUpdater", update_overlay_loop)
    run_thread("PersonaWatcher", monitor_persona_loop)

    # Add other bot loops below if needed in future phases
    # run_thread("TradeWatcher", trade_strategy_loop)
    # run_thread("BotSync", bot_heartbeat_sync)

    print("[AUTONOMY LOOP] ✅ All core systems launched.")

# Optional direct run
if __name__ == "__main__":
    start_autonomy_loops()
    while True:
        time.sleep(60)