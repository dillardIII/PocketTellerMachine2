from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: backtest_plotter.py ===

import matplotlib.pyplot as plt
from datetime import datetime

def plot_trade_signals(trades, ticker="AAPL"):
    if not trades:
        print("[Plotter] No trades to plot.")
        return

    dates = [datetime.strptime(t['date'], "%Y-%m-%d") for t in trades]
    prices = [t['close'] for t in trades]
    signals = [t['signal'] for t in trades]

    buy_dates = [dates[i] for i, s in enumerate(signals) if s == "buy"]:
    buy_prices = [prices[i] for i, s in enumerate(signals) if s == "buy"]:
:
    sell_dates = [dates[i] for i, s in enumerate(signals) if s == "sell"]:
    sell_prices = [prices[i] for i, s in enumerate(signals) if s == "sell"]:
:
    plt.figure(figsize=(14, 6))
    plt.plot(dates, prices, label="Close Price", color="#00ffe5")

    plt.scatter(buy_dates, buy_prices, marker="^", color="lime", label="Buy", s=80, edgecolor="black")
    plt.scatter(sell_dates, sell_prices, marker="v", color="red", label="Sell", s=80, edgecolor="black")

    plt.title(f"{ticker} - Trade Signals")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.style.use("dark_background")
    plt.show()

def log_event():ef drop_files_to_bridge():