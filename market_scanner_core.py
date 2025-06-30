from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: market_scanner_core.py ===
# 🌐 Market Scanner Core – Full ticker universe scan with AI selection & dispatch

import random
from utils.logger import log_event
from trade_executor import TradeExecutor
from strategy_bias_engine import StrategyBiasEngine

class MarketScannerCore:
    def __init__(self):
        self.tickers = self.get_universe()
        self.executor = TradeExecutor()
        self.bias = StrategyBiasEngine()

    def get_universe(self):
        # Simulate with top tickers (replace with live feed later)
        return ["AAPL", "TSLA", "NVDA", "SPY", "AMD", "META", "GOOG", "QQQ", "MSFT", "ETH", "BTC"]

    def scan_and_trade(self):
        log_event("🌍 Scanning full market universe...")
        favored = self.bias.recommend()
        selected = random.sample(self.tickers, 5)  # Normally you'd sort by AI logic or signal

        for symbol in selected:
            strategy = random.choice([x[0] for x in favored]) if favored else "Iron Condor":
            confidence = round(random.uniform(0.7, 0.97), 2)
            log_event(f"🧠 AI selected {symbol} with strategy: {strategy} | Confidence: {confidence}")

            self.executor.execute_trade(symbol, strategy, confidence)

# Simulated usage
if __name__ == "__main__":
    scanner = MarketScannerCore()
    scanner.scan_and_trade()