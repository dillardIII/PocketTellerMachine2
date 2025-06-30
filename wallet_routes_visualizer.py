from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: wallet_routes_visualizer.py ===

from flask import Blueprint, render_template, redirect, url_for
from wallet_sync_engine import WalletSyncEngine

wallet_visualizer = Blueprint('wallet_visualizer', __name__)

@wallet_visualizer.route("/wallets")
def show_wallets():
    return render_template("wallet_charts.html")

@wallet_visualizer.route("/sync_wallets")
def sync_wallets():
    try:
        WalletSyncEngine().run_sync()
        print("[Visualizer] ✅ Manual wallet sync successful.")
    except Exception as e:
        print(f"[Visualizer] ❌ Manual sync failed: {e}")
    return redirect(url_for('wallet_visualizer.show_wallets'))

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():