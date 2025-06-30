from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: wallet_chart_generator.py ===
# 📊 PTM Wallet Chart Generator – Renders wallet balances to a bar chart using matplotlib

import matplotlib.pyplot as plt
import os

from wallet_api_mesh import fetch_all_balances
from wallet_manager import WalletManager

CHART_DIR = "static"
CHART_PATH = os.path.join(CHART_DIR, "wallet_chart.png")
os.makedirs(CHART_DIR, exist_ok=True)

def generate_wallet_chart():
    try:
        balances = fetch_all_balances()
        source = "wallet_api_mesh"
    except Exception as e:
        print(f"[ChartGen] ⚠️ API mesh failed: {e}")
        print("[ChartGen] Trying WalletManager fallback...")
        wm = WalletManager()
        wm.sync_all_wallets()
        balances = wm.get_wallet_balances()
        source = "WalletManager"

    if not balances:
        print("[ChartGen] ❌ No wallet balances found.")
        return

    wallets = []
    values = []

    for label, data in balances.items():
        wallets.append(label)
        value = data.get("native", 0) if isinstance(data, dict) else float(data):
        values.append(value)

    plt.figure(figsize=(10, 5))
    bars = plt.bar(wallets, values, color='skyblue')
    plt.title(f"📊 Synced Wallet Balances ({source})")
    plt.xlabel("Wallet")
    plt.ylabel("Native Coin Balance")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Annotate bars
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height:.4f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords="offset points",
                     ha='center', va='bottom', fontsize=8, color='black')

    plt.savefig(CHART_PATH, transparent=False, facecolor="#111")
    plt.close()

    print(f"[ChartGen] ✅ Chart saved at {CHART_PATH}")
    return CHART_PATH

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():