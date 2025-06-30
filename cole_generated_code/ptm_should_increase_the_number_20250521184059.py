from ghost_env import INFURA_KEY, VAULT_ADDRESS
To increase the number of trades made by PTM (Presumed to be a trading bot or algorithm), we would need to modify the trading logic in the Python code. However, without the original code, it's impossible to provide an accurate modification. 

But here is a simple example of how a trading bot might decide to make trades. In this example, the bot makes a trade if the current price is higher than the average price over the last 10 periods. To make the bot trade more often, we could decrease the number of periods used to calculate the average price. 

```python
import pandas as pd
import numpy as np

class PTM:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance
        self.holdings = 0

    def trade(self, data):
        # Calculate the average price over the last 10 periods
        avg_price = data['price'].rolling(window=10).mean()

        # Make a trade if the current price is higher than the average price
        for i in range(len(data)):
            if data['price'].iloc[i] > avg_price.iloc[i]:
                self.buy(data['price'].iloc[i])
            else:
                self.sell(data['price'].iloc[i])

    def buy(self, price):
        if self.balance > 0:
            self.holdings += self.balance / price
            self.balance = 0

    def sell(self, price):
        if self.holdings > 0:
            self.balance += self.holdings * price
            self.holdings = 0
```

In this code, you can change the window size in the `avg_price = data['price'].rolling(window=10).mean()` line to a smaller number to make the bot trade more often. 

Please note that this is a very simplified example and real trading bots would use much more complex logic to decide when to trade. Also, increasing the number of trades doesn't necessarily increase the chances of winning, it could also increase the chances of losing if the trades are not profitable.