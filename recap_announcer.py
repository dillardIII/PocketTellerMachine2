# Recap Announcer
from voice_engine import speak

def announce_trade_recap(trade):
    summary = f"Trade executed: {trade['action']} {trade['quantity']} shares of {trade['symbol']} at ${trade['price']}"
    print(f"[Recap] {summary}")
    speak(summary)