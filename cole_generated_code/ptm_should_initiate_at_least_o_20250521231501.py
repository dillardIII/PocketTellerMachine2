from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python code that simulates a trading bot using a simple strategy. This bot will buy when the price goes above the moving average and sell when it goes below. 

Please note that this is a very simple example and real trading bots use much more complex strategies and risk management. Also, this code assumes that you have a data frame `df` with the price data.

```python
import pandas as pd
import numpy as np

class PTM:
    def __init__(self):
        self.position = 0  # 1 for long position, -1 for short position, 0 for no position
        self.balance = 10000  # starting balance
        self.data = None  # price data

    def moving_average(self, window_size):
        return self.data['Close'].rolling(window=window_size).mean()

    def trade(self, data):
        self.data = data
        ma = self.moving_average(10)  # calculate 10-day moving average

        for i in range(len(self.data)):
            if self.data['Close'][i] > ma[i]:  # if price goes above moving average, buy
                if self.position == 0:  # if no position, buy
                    self.position = 1
                    self.balance -= self.data['Close'][i]
                    print(f'Bought at {self.data["Close"][i]}')
                elif self.position == -1:  # if short position, close short and buy
                    self.position = 1
                    self.balance += 2 * self.data['Close'][i]
                    print(f'Closed short and bought at {self.data["Close"][i]}')
            elif self.data['Close'][i] < ma[i]:  # if price goes below moving average, sell
                if self.position == 0:  # if no position, sell short
                    self.position = -1
                    self.balance += self.data['Close'][i]
                    print(f'Sold short at {self.data["Close"][i]}')
                elif self.position == 1:  # if long position, close long and sell short
                    self.position = -1
                    self.balance += 2 * self.data['Close'][i]
                    print(f'Closed long and sold short at {self.data["Close"][i]}')

        print(f'Final balance: {self.balance}')

# Assume df is the DataFrame with price data
ptm = PTM()
ptm.trade(df)
```

This script will print the trades made and the final balance. It's a very basic script and doesn't take into account trading fees or slippage. It also doesn't do any risk management. For real trading, you would need to consider these factors and probably use a more sophisticated strategy.