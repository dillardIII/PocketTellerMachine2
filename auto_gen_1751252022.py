```python
# dark_liquidity_watcher.py

import time
import logging
from typing import List

# Configure logging
logging.basicConfig(filename='liquidity_watcher.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MockMarketDataFeed:
    """Mock class to simulate market data feed."""
    
    @staticmethod
    def get_order_book() -> dict:
        # Simulating a market order book with potential dark liquidity walls
        order_book = {
            'bids': [
                {'price': 100.0, 'quantity': 10},
                {'price': 99.5, 'quantity': 5},
                # Large bid point acting as a dark liquidity wall
                {'price': 99.0, 'quantity': 1000},
            ],
            'asks': [
                {'price': 101.0, 'quantity': 8},
                {'price': 102.0, 'quantity': 10},
                # Large ask point acting as a dark liquidity wall
                {'price': 102.5, 'quantity': 1200},
            ]
        }
        return order_book

class LiquidityWallWatcher:
    """Class to watch for dark liquidity walls in the market."""
    
    def __init__(self, threshold: float = 100.0):
        self.threshold = threshold
        self.market_data_feed = MockMarketDataFeed()

    def analyze_order_book(self, order_book: dict) -> List[str]:
        suspicious_activities = []
        for side in ['bids', 'asks']:
            for order in order_book.get(side, []):
                if order['quantity'] >= self.threshold:
                    activity = f"Suspicious {side[:-1]} at {order['price']} with quantity {order['quantity']}"
                    suspicious_activities.append(activity)
        return suspicious_activities
                
    def log_suspicious_activities(self, suspicious_activities: List[str]) -> None:
        if suspicious_activities:
            for activity in suspicious_activities:
                logging.info(activity)
        else:
            logging.info("No suspicious activity detected in this cycle.")

    def watch(self, interval: float = 5.0) -> None:
        while True:
            order_book = self.market_data_feed.get_order_book()
            suspicious_activities = self.analyze_order_book(order_book)
            self.log_suspicious_activities(suspicious_activities)
            time.sleep(interval)

if __name__ == "__main__":
    watcher = LiquidityWallWatcher(threshold=100.0)
    watcher.watch(interval=10.0)
```
