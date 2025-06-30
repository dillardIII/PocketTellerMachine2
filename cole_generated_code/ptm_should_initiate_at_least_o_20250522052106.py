from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code to simulate a trading activity. This code uses a random number generator to simulate the price of a stock and then decides whether to buy or sell based on the price.

```python
import random

class PTM:
    def __init__(self):
        self.cash = 10000
        self.stocks = 0
        self.trade_history = []

    def trade(self):
        price = random.uniform(50, 150)  # Simulate price
        if price < 100:
            # Buy
            stocks_to_buy = self.cash // price
            self.stocks += stocks_to_buy
            self.cash -= stocks_to_buy * price
            self.trade_history.append(('buy', stocks_to_buy, price))
        elif self.stocks > 0:
            # Sell
            self.cash += self.stocks * price
            self.trade_history.append(('sell', self.stocks, price))
            self.stocks = 0

    def print_trade_history(self):
        for action, stocks, price in self.trade_history:
            print(f"{action} {stocks} stocks at {price}")

# Create PTM and initiate a trade
ptm = PTM()
ptm.trade()
ptm.print_trade_history()
```

This code creates a PTM (Portfolio Trading Model) with an initial cash of $10,000. The `trade` method simulates a stock price between $50 and $150. If the price is less than $100, it buys as many stocks as possible with the available cash. If the price is more than $100 and it has some stocks, it sells all the stocks. The `print_trade_history` method prints all the trades made.

Please note that this is a very simplified trading model and real-world trading involves a lot more factors and complexities.