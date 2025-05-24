Sure, below is a simple scaffold of the Python code to implement different trading strategies. For demonstration, I'll create two simple naive strategies: 'buy_low_sell_high' and 'invest_fixed_amount'

```python
class TradingStrategy:
    def execute(self, market_data):
        pass

class BuyLowSellHighStrategy(TradingStrategy):
    def __init__(self, buy_threshold, sell_threshold):
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold

    def execute(self, market_data):
        if market_data['price'] < self.buy_threshold:
            # implement buy logic here
            print('Buy')

        elif market_data['price'] > self.sell_threshold:
            # implement sell logic here
            print('Sell')


class InvestFixedAmountStrategy(TradingStrategy):
    def __init__(self, amount):
        self.amount = amount

    def execute(self, market_data):
        # implement fixed amount investment logic here
        print('Investing fixed amount')


class TradingSystem:
    def __init__(self, strategies):
        self.strategies = strategies

    def process_market_data(self, market_data):
        for strategy in self.strategies:
            strategy.execute(market_data)


buy_low_sell_high_strategy = BuyLowSellHighStrategy(50, 100)
invest_fixed_amount_strategy = InvestFixedAmountStrategy(100)

trading_System = TradingSystem([buy_low_sell_high_strategy, invest_fixed_amount_strategy])

# Here's an example of how we might use this system
market_data = {'price': 60}
trading_System.process_market_data(market_data)
```

Please note that above is a basic example and doesn't represent a real-world trading system. A practical system would require much more complex strategies taking into account various factors such as Unit tests, exception handling, logging, market trend analysis, considerations for fees, API for executing trades, etc. Also, the market data would typically be fetched in real-time from a market data service.

Further, the implementation of `execute()` function for each strategy is left blank as this can get quite complex and requires knowledge of your trading API and the specifics of your trading rules.