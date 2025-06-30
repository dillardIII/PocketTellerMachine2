from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: boot_autonomy.py ===
# 🚀 Boot Autonomy – Starts all core systems in background threads and registers Flask blueprints

from threading import Thread
from flask import Flask

# === PTM Core Imports ===
from master_autonomy_loop import master_autonomy_loop
from cole_autopilot_cycle import cole_autopilot_cycle
from auto_cycle_builder import run_build_autonomy_cycle
from log_merger_bot import start_merger_bot
from ptm_watchdog import start_watchdog
from ptm_brain_sync import run_brain_sync
from auto_error_repair_loop import auto_error_repair_loop
from self_rebuilder import self_rebuilder_loop
from bridge_heartbeat_sync import start_bridge_sync
from bots.cole_bot_listener import cole_listen_loop
from ptm.inter_bot_router import start_relay_loop

# === Flask Routes / Blueprints ===
from market_trend_route import market_trend_bp
from command_center_route import command_center_bp
from ai_recon_route import ai_recon_bp
from recovery_reporter import recovery_reporter_bp
from trade_execution_route import trade_execution_bp

# === PTM Initializer ===
from ptm_initializer import PTMInitializer

app = Flask(__name__)
ptm_initializer = PTMInitializer()

# Register API blueprints
app.register_blueprint(market_trend_bp)
app.register_blueprint(command_center_bp)
app.register_blueprint(ai_recon_bp)
app.register_blueprint(recovery_reporter_bp)
app.register_blueprint(trade_execution_bp)

def start_all_autonomy():
    """
    Central boot method for PTM autonomy engine.
    Kicks off all core threads and initializes blueprint(services.)
    """
    print("[BOOT AUTONOMY] 🚀 Launching autonomy services...")
    boot_result = ptm_initializer.boot_sequence()

    Thread(target=master_autonomy_loop, daemon=True).start()
    Thread(target=cole_autopilot_cycle, daemon=True).start()
    Thread(target=run_build_autonomy_cycle, daemon=True).start()
    Thread(target=start_merger_bot, daemon=True).start()
    Thread(target=start_watchdog, daemon=True).start()
    Thread(target=run_brain_sync, daemon=True).start()
    Thread(target=auto_error_repair_loop, daemon=True).start()
    Thread(target=self_rebuilder_loop, daemon=True).start()
    Thread(target=start_bridge_sync, daemon=True).start()
    Thread(target=cole_listen_loop, daemon=True).start()
    Thread(target=start_relay_loop, daemon=True).start()

    print(f"[PTM Autonomy Boot] ✅ Status: {boot_result['status']}")
    return boot_result

def log_event():ef drop_files_to_bridge():