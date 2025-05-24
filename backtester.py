# === FILE: backtester.py ===

import os
import json
import numpy as np
import yfinance as yf
from datetime import datetime  # <- FIXED import

from price_data import get_historical_prices
from indicators import calc_rsi, calc_macd, calc_bollinger_bands
from backtest_plotter import plot_trade_signals

# === Strategy Grading ===
def calculate_grade(return_pct):
    if return_pct >= 30:
        return "A"
    elif return_pct >= 20:
        return "B"
    elif return_pct >= 10:
        return "C"
    elif return_pct >= 0:
        return "D"
    else:
        return "F"

# === RSI Strategy Signal Only ===
def rsi_strategy(data, window=14):
    delta = data['Close'].diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = np.mean(gain[-window:])
    avg_loss = np.mean(loss[-window:])
    if avg_loss == 0:
        rsi = 100
    else:
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

    if rsi < 30:
        return "buy"
    elif rsi > 70:
        return "sell"
    else:
        return "hold"

# === Yahoo-Based RSI Backtester ===
def backtest_strategy_yahoo(ticker, strategy_func, period="6mo", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval)
    data.dropna(inplace=True)

    if len(data) < 30:
        print(f"Not enough data for {ticker}")
        return None

    results = []
    cash = 10000
    position = 0
    entry_price = 0

    for i in range(20, len(data)):
        slice = data.iloc[:i]
        today = data.iloc[i]
        signal = strategy_func(slice)

        if signal == "buy" and position == 0:
            position = cash // today['Close']
            entry_price = today['Close']
            cash -= position * entry_price
        elif signal == "sell" and position > 0:
            cash += position * today['Close']
            position = 0

        results.append({
            "date": today.name.strftime("%Y-%m-%d"),
            "close": float(today['Close']),
            "signal": signal,
            "cash": round(cash, 2),
            "position": int(position)
        })

    final_value = cash + (position * data.iloc[-1]['Close'])
    return_pct = round((final_value - 10000) / 10000 * 100, 2)
    grade = calculate_grade(return_pct)
    voice_summary = f"Backtest on {ticker} returned {return_pct} percent. Grade: {grade}."

    return {
        "ticker": ticker,
        "final_value": round(final_value, 2),
        "return_pct": return_pct,
        "grade": grade,
        "voice_summary": voice_summary,
        "trades": results
    }

# === Internal Multi-Strategy Backtest (PTM-style) ===
def backtest_strategy(strategy_name, symbol="AAPL", prices=None):
    if prices is None:
        prices = get_historical_prices(symbol)
    if not prices or len(prices) < 50:
        return {"error": "Not enough price data"}

    trades = []
    position = None
    entry_price = 0

    for i in range(30, len(prices)):
        price_window = prices[:i+1]
        current_price = prices[i]
        rsi = calc_rsi(price_window)

        if strategy_name == "rsi_reversal":
            if rsi < 30 and position is None:
                position = "long"
                entry_price = current_price
            elif rsi > 70 and position == "long":
                pnl = current_price - entry_price
                trades.append(pnl)
                position = None

        elif strategy_name == "macd_trend_follow":
            macd_line, signal_line, _ = calc_macd(price_window)
            if macd_line > signal_line and position is None:
                position = "long"
                entry_price = current_price
            elif macd_line < signal_line and position == "long":
                pnl = current_price - entry_price
                trades.append(pnl)
                position = None

        elif strategy_name == "bollinger_bounce":
            lower, upper = calc_bollinger_bands(price_window)
            if not lower or not upper:
                continue
            if current_price <= lower and position is None:
                position = "long"
                entry_price = current_price
            elif current_price >= upper and position == "long":
                pnl = current_price - entry_price
                trades.append(pnl)
                position = None

    wins = [t for t in trades if t > 0]
    losses = [t for t in trades if t <= 0]
    total_pnl = sum(trades)

    return {
        "strategy": strategy_name,
        "symbol": symbol,
        "trades": len(trades),
        "wins": len(wins),
        "losses": len(losses),
        "win_rate": round(len(wins) / len(trades) * 100, 2) if trades else 0,
        "total_pnl": round(total_pnl, 2)
    }

# === Run All Yahoo RSI Backtests ===
def run_all_backtests():
    tickers = ["AAPL", "TSLA", "MSFT", "NIO", "SPY", "AMC", "PLTR", "NVDA", "BBBY", "GME"]
    all_results = []

    for ticker in tickers:
        result = backtest_strategy_yahoo(ticker, rsi_strategy)
        if result:
            all_results.append(result)

    os.makedirs("data", exist_ok=True)
    with open("data/backtest_results.json", "w") as f:
        json.dump(all_results, f, indent=2)

    print("Backtest complete. Results saved to data/backtest_results.json")

# === Run on Execution ===
if __name__ == "__main__":
    run_all_backtests()

    # === NEW: Plot AAPL Trade Signals Visually ===
    result = backtest_strategy_yahoo("AAPL", rsi_strategy)
    if result:
        plot_trade_signals(result["trades"], ticker="AAPL")