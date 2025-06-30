from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bot.py ===
# 🤖 PTM Master Bot – Oversees execution, coordination, and persona flow

import threading
import time
from assistants import get_active_assistants
from ghost_intel_announcer import announce_ghost_intel
from trade_loop import execute_trade_cycle
from bot_status import update_bot_status
from scheduler import schedule_daily_tasks

# ⏱️ Core loop interval (in seconds)
LOOP_INTERVAL = 30

def master_bot_loop():
    print("[BOT] 🤖 Master bot loop initiated...")

    while True:
        try:
            update_bot_status("Running")

            # 🔁 Cycle through key systems
            assistants = get_active_assistants()
            if "Mentor" in assistants:
                print("[BOT] 🧠 Mentor is active – Initiating market summary.")
                announce_ghost_intel(["market summary", "economic news"])

            if "Mo Cash" in assistants:
                print("[BOT] 💰 Mo Cash is active – Running trade loop.")
                execute_trade_cycle()

            if "Strategist" in assistants:
                print("[BOT] 📊 Strategist is active – Scheduling strategic analysis.")
                schedule_daily_tasks()

            update_bot_status("Idle")

        except Exception as e:
            print(f"[BOT ERROR] ❌ {e}")
            update_bot_status(f"Error: {str(e)}")

        time.sleep(LOOP_INTERVAL)

# 🧵 Launch the bot in a background thread
def launch_bot():
    print("[BOT] 🚀 Launching PTM Bot in a separate thread...")
    bot_thread = threading.Thread(target=master_bot_loop, daemon=True)
    bot_thread.start()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():