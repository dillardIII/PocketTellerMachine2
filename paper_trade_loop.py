# === FILE: paper_trade_loop.py ===

import os
import json
import time
from datetime import datetime
from threading import Thread
from random import uniform, choice

os.makedirs("data", exist_ok=True)
TRADE_LOG = "data/brain_trades.json"

TICKERS = ["AAPL", "TSLA", "NVDA", "AMZN", "META"]

def generate_price_data(length=50):
    base = uniform(100, 300)
    return [round(base + uniform(-5, 5), 2) for _ in range(length)]

def calc_rsi(prices, period=14):
    gains, losses = [], []
    for i in range(1, period + 1):
        diff = prices[-i] - prices[-i - 1]
        (gains if diff > 0 else losses).append(abs(diff))
    avg_gain = sum(gains) / period if gains else 0.01
    avg_loss = sum(losses) / period if losses else 0.01
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def calc_sma(prices, period=10):
    return sum(prices[-period:]) / period

def calc_ema(prices, period=10):
    k = 2 / (period + 1)
    ema = prices[0]
    for price in prices[1:]:
        ema = price * k + ema * (1 - k)
    return ema

def calc_macd(prices):
    ema12 = calc_ema(prices[-12:], 12)
    ema26 = calc_ema(prices[-26:], 26)
    return ema12 - ema26

def calc_stochastic(prices, k_period=14):
    high = max(prices[-k_period:])
    low = min(prices[-k_period:])
    current = prices[-1]
    return 100 * ((current - low) / (high - low)) if high != low else 0

def detect_support_resistance(prices):
    support = min(prices[-10:])
    resistance = max(prices[-10:])
    return support, resistance

def score_confidence(indicators):
    score = 0
    if indicators["RSI"] < 30 or indicators["RSI"] > 70:
        score += 20
    if indicators["MACD"] > 0:
        score += 15
    if indicators["Stochastic"] < 20 or indicators["Stochastic"] > 80:
        score += 15
    if indicators["EMA Fast"] > indicators["EMA Slow"]:
        score += 20
    if indicators["Current Price"] < indicators["Support"] + 3 or indicators["Current Price"] > indicators["Resistance"] - 3:
        score += 30
    return min(score, 100)

def check_trade_signal(prices):
    current = prices[-1]
    rsi = calc_rsi(prices)
    sma = calc_sma(prices)
    ema_fast = calc_ema(prices[-12:], 5)
    ema_slow = calc_ema(prices[-26:], 20)
    macd = calc_macd(prices)
    stochastic = calc_stochastic(prices)
    support, resistance = detect_support_resistance(prices)

    indicators = {
        "RSI": rsi, "SMA": sma, "MACD": macd,
        "Stochastic": stochastic,
        "EMA Fast": ema_fast, "EMA Slow": ema_slow,
        "Support": support, "Resistance": resistance,
        "Current Price": current
    }

    action = None
    if rsi < 30 and current > sma and macd > 0 and stochastic < 20 and ema_fast > ema_slow:
        action = "BUY"
    elif rsi > 70 and current < sma and macd < 0 and stochastic > 80 and ema_fast < ema_slow:
        action = "SELL"

    return action, indicators

def log_trade(trade):
    if os.path.exists(TRADE_LOG):
        with open(TRADE_LOG, "r") as f:
            data = json.load(f)
    else:
        data = {"trades": []}
    data["trades"].append(trade)
    with open(TRADE_LOG, "w") as f:
        json.dump(data, f, indent=2)

# === LOCAL VOICE FILE VERSION ===
def trigger_trade_recap(trade):
    persona = "Mo Cash" if trade["action"] == "BUY" else "Mentor"

    voice_paths = {
        "Mo Cash": "static/audio/male/mo_cash_preview.mp3",
        "Mentor": "static/audio/male/mentor_preview.mp3"
    }

    voice_line = (
        f"{persona} says: {trade['action']} {trade['quantity']} share of {trade['ticker']} "
        f"at ${trade['price']:.2f}. Confidence: {trade['confidence']}%. "
        f"RSI {trade['indicators']['RSI']:.2f}, MACD {trade['indicators']['MACD']:.2f}."
    )

    trade["voice_recap"] = voice_paths.get(persona, "N/A")

    print(f"[VOICE] {voice_line}")
    print(f"[AUDIO] Preview voice: {trade['voice_recap']}")

def run_trade_loop():
    trade_count = 1
    while True:
        ticker = choice(TICKERS)
        prices = generate_price_data(50)
        action, indicators = check_trade_signal(prices)
        current_price = prices[-1]

        if action:
            confidence = score_confidence(indicators)
            trade = {
                "id": f"{trade_count:04}",
                "timestamp": datetime.utcnow().isoformat(),
                "ticker": ticker,
                "price": current_price,
                "action": action,
                "quantity": 1,
                "indicators": {k: round(v, 2) for k, v in indicators.items()},
                "confidence": confidence
            }
            log_trade(trade)
            print(f"[PTM] {action} {ticker} @ {current_price} | Confidence: {confidence}%")
            trigger_trade_recap(trade)
            trade_count += 1
        else:
            print(f"[PTM] No valid signal. Waiting...")

        time.sleep(30)

def start_paper_trade_thread():
    thread = Thread(target=run_trade_loop)
    thread.daemon = True
    thread.start()