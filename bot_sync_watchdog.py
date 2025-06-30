from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bot_sync_watchdog.py ===
# 🐶 Bot Sync Watchdog – Monitors bot loops, restarts any that crash or stop.

import threading
import time

def monitor_bot(bot_fn, bot_name):
    while True:
        try:
            print(f"[Watchdog] 🧠 Starting {bot_name}...")
            bot_fn()
        except Exception as e:
            print(f"[Watchdog] ⚠️ {bot_name} crashed: {e}")
            time.sleep(3)
            print(f"[Watchdog] 🔁 Restarting {bot_name}...")

def start_watchdog():
    from replit_bot_installer import install_files
    from mission_dispatcher import dispatch_loop

    threading.Thread(target=monitor_bot, args=(install_files, "Installer"), daemon=True).start()
    threading.Thread(target=monitor_bot, args=(dispatch_loop, "Dispatcher"), daemon=True).start()

if __name__ == "__main__":
    print("[Watchdog] 🐺 Replit-side sync watchdog online.")
    start_watchdog()
    while True:
        time.sleep(10)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():