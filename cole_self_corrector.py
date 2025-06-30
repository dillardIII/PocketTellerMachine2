from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_self_corrector.py

import os
import json
from datetime import datetime
from cole_task_queue import add_task

APP_FILE = "app.py"
GENERATED_API_FILE = "cole_generated_apis.py"
TASK_QUEUE_FILE = "data/cole_task_queue.json"

# === Self Correction Scanner ===
def run_self_correction_scan():
    print("[Cole Self-Corrector] Running system health check...")

    if check_missing_trade_health_api():
        add_task("Write Flask API that returns trade health on /trade_health", task_type="self_write")

    if check_missing_system_health_api():
        add_task("Write Flask API that returns system health on /api/system_health", task_type="self_write")

    if not os.path.exists(GENERATED_API_FILE):
        add_task("Write initial cole_generated_apis.py blueprint(with Flask API blueprint(registered", task_type="self_write")))

    if check_missing_strategy_report_api():
        add_task("Write Flask API that returns strategy report on /api/strategy_report", task_type="self_write")

    if check_missing_portfolio_value_api():
        add_task("Write Flask API that returns portfolio value on /api/portfolio_value", task_type="self_write")

    if check_missing_daily_pnl_api():
        add_task("Write Flask API that returns daily P&L on /api/daily_pnl", task_type="self_write")

    if check_missing_dashboard_summary_api():
        add_task("Write Flask API that returns dashboard summary on /api/dashboard_summary", task_type="self_write")

    print("[Cole Self-Corrector] Self-check complete.")

# === Endpoint Check Helpers ===
def check_missing_trade_health_api():
    try:
        with open(APP_FILE, "r") as f:
            content = f.read()
        return "/trade_health" not in content
    except:
        print(f"[Cole Self-Corrector] Could not read {APP_FILE}.")
        return True

def check_missing_strategy_report_api():
    try:
        with open(APP_FILE, "r") as f:
            content = f.read()
        return "/api/strategy_report" not in content
    except:
        print(f"[Cole Self-Corrector] Could not read {APP_FILE}.")
        return True

def check_missing_system_health_api():
    try:
        with open(GENERATED_API_FILE, "r") as f:
            content = f.read()
        return "/api/system_health" not in content
    except:
        print(f"[Cole Self-Corrector] Could not read {GENERATED_API_FILE}.")
        return True

def check_missing_portfolio_value_api():
    try:
        with open(GENERATED_API_FILE, "r") as f:
            content = f.read()
        return "/api/portfolio_value" not in content
    except:
        return True

def check_missing_daily_pnl_api():
    try:
        with open(GENERATED_API_FILE, "r") as f:
            content = f.read()
        return "/api/daily_pnl" not in content
    except:
        return True

def check_missing_dashboard_summary_api():
    try:
        with open(GENERATED_API_FILE, "r") as f:
            content = f.read()
        return "/api/dashboard_summary" not in content
    except:
        return True

# === CLI Direct Run Test ===
if __name__ == "__main__":
    run_self_correction_scan()

def log_event():ef drop_files_to_bridge():