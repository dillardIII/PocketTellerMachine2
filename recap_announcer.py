# recap_announcer.py – Announces completed trade summaries

def announce_trade_recap(trade_info):
    print("[Trade Recap] 📣 Summary of executed trade:")
    print(f"  Symbol: {trade_info.get('symbol')}")
    print(f"  Action: {trade_info.get('action')}")
    print(f"  Price: ${trade_info.get('price'):.2f}")
    print(f"  Quantity: {trade_info.get('quantity')}")