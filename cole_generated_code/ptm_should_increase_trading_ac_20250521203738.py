To increase trading activity, you can create a Python script that uses an algorithm to make trades. Here's a simple example of how you might do this using a random trading strategy. This is a very basic example and real trading algorithms would be much more complex and based on various factors.

```python
import random
import pandas as pd

class PTM:
    def __init__(self):
        self.balance = 10000  # Starting balance
        self.stocks = 0  # Starting stocks
        self.trading_history = []  # History of trading activity

    def trade(self):
        # Randomly decide to buy or sell
        action = random.choice(['buy', 'sell'])

        if action == 'buy':
            # Randomly decide how many stocks to buy (between 1 and 10)
            quantity = random.randint(1, 10)

            # Check if we have enough balance to buy
            if self.balance >= quantity * 100:  # Assume each stock costs $100
                self.balance -= quantity * 100
                self.stocks += quantity
                self.trading_history.append(('buy', quantity))
        elif action == 'sell':
            # Randomly decide how many stocks to sell (between 1 and 10)
            quantity = random.randint(1, 10)

            # Check if we have enough stocks to sell
            if self.stocks >= quantity:
                self.balance += quantity * 100
                self.stocks -= quantity
                self.trading_history.append(('sell', quantity))

    def start_trading(self, num_trades):
        for _ in range(num_trades):
            self.trade()

        # Convert trading history to DataFrame for analysis
        df = pd.DataFrame(self.trading_history, columns=['Action', 'Quantity'])
        return df


ptm = PTM()
trading_history = ptm.start_trading(1000)

print(trading_history)
```

This script creates a PTM object with a starting balance and number of stocks. It then makes trades (either buying or selling stocks) and records the trading activity. The `start_trading` method starts the trading process and makes a specified number of trades.

Please note that this is a very simplified simulation and doesn't take into account many factors that would be important in real trading, such as stock prices, market trends, etc. It's also using a random strategy, which is not recommended for real trading. This is just for demonstration purposes.