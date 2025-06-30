from ghost_env import INFURA_KEY, VAULT_ADDRESS
# strategy_generator.py – Generates Basic Trade Strategies

import random

def generate_strategy():
    print("[Strategy Generator] 🔄 Generating strategy...")

    symbols = ["AAPL", "TSLA", "AMZN", "NVDA", "GOOGL"]
    actions = ["BUY", "SELL"]
    types = ["stock", "options", "forex", "crypto"]

    strategy = {
        "type": random.choice(types),
        "symbol": random.choice(symbols),
        "action": random.choice(actions),
    }

    print(f"[Strategy Generator] 🎯 Strategy created: {strategy}")
    return strategy

def log_event():ef drop_files_to_bridge():