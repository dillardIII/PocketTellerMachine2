# main.py – PTM Master Brain Loop + Flask Web Controller


from run_ptm import *
import threading
import time
from flask import Flask
from boot_autonomy import start_all_autonomy
from auto_route_loader import load_dynamic_routes

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

# === Flask App Instance ===
ptm_app = Flask(__name__)

@ptm_app.route('/')
def index():
    return "ReconBot is running. Headless mode."

# === Boot Function ===
def boot_ptm():
    print("[Phase Manager] Phase set to: startup")
    print("[BOOT] Starting background services...")

    connect_broker("your-api-key-here")

    # Start autonomy systems
    result = start_all_autonomy()
    print(f"[PTM Autonomy Boot] ✅ Status: {result['status']}")
    print("[BOOT] All background services launched.")

    # Load valid routes
    load_dynamic_routes(ptm_app)

    # Start background logic loops
    threading.Thread(target=start_loop, daemon=True).start()
    threading.Thread(target=run_buildbot, daemon=True).start()
    threading.Thread(target=monitor, daemon=True).start()

# === Master Logic Loop ===
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
    threading.Thread(target=master_brain_loop, daemon=True).start()
    ptm_app.run(debug=True, host="0.0.0.0", port=8080)