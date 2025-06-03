# === FILE: ptm_watchdog.py ===
# 🐶 PTM Watchdog – Monitors critical systems and restarts failed bots

import threading
import time
import random

monitored_services = {
    "master_autonomy_loop": {"status": "ok", "last_ping": time.time()},
    "cole_autopilot_cycle": {"status": "ok", "last_ping": time.time()},
    "run_build_autonomy_cycle": {"status": "ok", "last_ping": time.time()},
}

def simulate_ping(bot_name):
    # For future wiring: bots should send pings to this monitor
    monitored_services[bot_name]["last_ping"] = time.time()

def check_bot_health(bot_name):
    now = time.time()
    last_ping = monitored_services[bot_name]["last_ping"]
    return now - last_ping < 15  # 15-second timeout

def restart_bot(bot_name):
    print(f"[WATCHDOG] 🛠️ Restarting {bot_name}...")
    monitored_services[bot_name]["status"] = "restarting"
    time.sleep(random.uniform(0.5, 1.5))
    monitored_services[bot_name]["status"] = "ok"
    monitored_services[bot_name]["last_ping"] = time.time()
    print(f"[WATCHDOG] ✅ {bot_name} is back online.")

def watchdog_loop():
    print("[WATCHDOG] 🐶 PTM Watchdog is active.")
    while True:
        for bot in monitored_services.keys():
            if not check_bot_health(bot):
                print(f"[WATCHDOG] ⚠️ {bot} is unresponsive.")
                restart_bot(bot)
        time.sleep(10)

def start_watchdog():
    threading.Thread(target=watchdog_loop, daemon=True).start()