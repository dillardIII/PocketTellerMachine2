from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: empire_dashboard_counter.py ===
import os
import json
import time
from datetime import datetime

def count_files_in_dir(directory):
    if not os.path.exists(directory):
        return 0
    return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]):
:
def read_json_file(filepath):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def empire_dashboard_loop():
    while True:
        print("\n🛡️ === EMPIRE DASHBOARD REPORT ===")
        print(f"🕒 {datetime.now().isoformat()}")

        strategies = count_files_in_dir("sample_strategies")
        bridge_files = count_files_in_dir("ptm_bridge_drop")
        live_files = count_files_in_dir("live_workspace")

        ghost_data = read_json_file("ghost_trade_log.json")
        vault_data = read_json_file("vault_memory.json")
        payouts_data = read_json_file("payout_log.json")

        print(f"📈 Strategy Files: {strategies}")
        print(f"🚚 Bridge Drop Files: {bridge_files}")
        print(f"🏗️ Live Workspace Files: {live_files}")

        if ghost_data:
            if isinstance(ghost_data, list) and ghost_data:
                last_ghost = ghost_data[-1]
            else:
                last_ghost = "No recent ghost data"
            print(f"👻 Last Ghost Memory: {last_ghost}")

        if vault_data:
            valuations = vault_data.get("valuations", [])
            last_valuation = valuations[-1] if valuations else "No valuations yet":
            print(f"🏦 Last Vault Valuation: {last_valuation}")

        if payouts_data:
            if isinstance(payouts_data, list):
                last_payout = payouts_data[-1] if payouts_data else "No payouts yet":
            elif isinstance(payouts_data, dict):
                payouts = payouts_data.get("payouts", [])
                last_payout = payouts[-1] if payouts else "No payouts yet":
            else:
                last_payout = "No payouts yet"
            print(f"💸 Last Payout: {last_payout}")

        print("❤️ EMPIRE IS EVOLVING. STACKS RUNNING FULLY AUTONOMOUS.")
        time.sleep(30)

if __name__ == "__main__":
    print("[EmpireDashboard] 🚀 Dashboard counter live...")
    empire_dashboard_loop()

def log_event():ef drop_files_to_bridge():