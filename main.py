# PTM Main Brain Loop – Final Phase Wiring ✅

import threading
import time

# === Phase Boot Modules ===
from autonomy_loop_controller import start_loop
from phase_status_monitor import monitor
from buildbot_loop import run_buildbot

# === Intelligence & Strategy ===
from strategy_generator import generate_strategy
from strategy_validator import validate
from strategy_router import route_strategy

# === Trading & Error Handling ===
from trading_execution_engine import execute_trade
from trade_error_handler import handle_trade_error
from trade_logger import log_trade
from recap_announcer import announce_trade_recap

# === Market & Broker ===
from market_data_fetcher import fetch_market_data
from broker_connector import connect_broker

# === Features & Mood ===
from feature_toggle_manager import is_enabled
from mood_engine import set_mood

# === UI & Sync ===
from ui_controller_sync import update_ui

# === Boot ===
def boot_ptm():
    print("[PTM Boot] 🔧 Starting PTM Brain...")
    connect_broker("your-api-key-here")

    threading.Thread(target=start_loop, daemon=True).start()
    threading.Thread(target=run_buildbot, daemon=True).start()
    threading.Thread(target=monitor, daemon=True).start()

# === Master Loop ===
def master_brain_loop():
    print("[PTM Brain] 🧠 Running main logic loop...")
    while True:
        if is_enabled("strategy_autogen"):
            strategy = generate_strategy()
            if validate(strategy):
                market_data = fetch_market_data("AAPL")
                success = execute_trade("AAPL", "BUY", market_data["price"], 10)
                if success:
                    log_trade("AAPL", "BUY", market_data["price"], 10)
                    announce_trade_recap({
                        "symbol": "AAPL",
                        "action": "BUY",
                        "price": market_data["price"],
                        "quantity": 10
                    })
                else:
                    handle_trade_error("Trade failed", strategy)
        set_mood("neutral")
        update_ui({"status": "loop running"})
        time.sleep(15)

# === GO TIME ===
if __name__ == "__main__":
    boot_ptm()
    master_brain_loop()