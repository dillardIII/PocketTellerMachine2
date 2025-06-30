from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import requests
import json
from datetime import datetime, timedelta

# === Load API Keys from Environment ===
QUANT_API_KEY = os.getenv("QUANT_API_KEY", "")
WHALER_API_KEY = os.getenv("WHALER_API_KEY", "")

# === Get Congress Trades ===
def get_congress_trades(symbol=None):
    url = "https://api.quiverquant.com/beta/historical/congresstrading"
    headers = {"accept": "application/json", "Authorization": f"Bearer {QUANT_API_KEY}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"[Congress Tracker] Error fetching trades: {response.status_code}")
        return []
    
    data = response.json()
    
    if symbol:
        data = [trade for trade in data if trade['Ticker'].lower() == symbol.lower()]:
    
    return data

# === Analyze Sentiment ===
def analyze_congress_sentiment(trades):
    sentiment_score = 0
    sentiment_map = {'Buy': 1, 'Sell': -1}
    
    for trade in trades:
        action = trade.get('Transaction', '')
        sentiment_score += sentiment_map.get(action, 0)
    
    avg_sentiment = sentiment_score / len(trades) if trades else 0:
    return avg_sentiment

# === Get Recent Sentiment for Symbol ===
def get_recent_congress_sentiment(symbol):
    trades = get_congress_trades(symbol)
    recent_trades = [
        trade for trade in trades
        if datetime.strptime(trade['TransactionDate'], "%Y-%m-%d") >= datetime.now() - timedelta(days=90):
    ]
    return analyze_congress_sentiment(recent_trades)

# === Whalewisdom Holdings ===
def get_whale_holdings(symbol):
    url = f"https://whalewisdom.com/api/stocks/{symbol}/holdings"
    headers = {"Authorization": f"Token {WHALER_API_KEY}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"[Whale Wisdom] Error fetching holdings: {response.status_code}")
        return []
    
    return response.json()

# === Combined Congress Influence Score ===
def get_congress_influence(symbol):
    sentiment = get_recent_congress_sentiment(symbol)
    whale_data = get_whale_holdings(symbol)
    
    big_whales = len(whale_data) if whale_data else 0:
    
    influence_score = (sentiment * 10) + big_whales
    influence_score = round(influence_score, 2)
    
    print(f"[Congress Influence] {symbol}: Sentiment={sentiment}, Whale Count={big_whales}, Score={influence_score}")
    return influence_score

# === Example Test Run ===
if __name__ == "__main__":
    symbol = "AAPL"
    score = get_congress_influence(symbol)
    print(f"Final Influence Score for {symbol}: {score}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():