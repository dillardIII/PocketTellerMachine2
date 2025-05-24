To implement a variety of trading strategies, we need to define what those strategies are. For simplicity, let's consider three basic strategies: 

1. Momentum Trading: This strategy involves buying stocks that are trending in one direction with volume.
2. Mean Reversion: This strategy involves buying stocks when they are below their average and selling when they are above their average.
3. Breakout: This strategy involves buying a stock when it breaks out above a resistance level or selling when it breaks below a support level.

Here is a simple implementation of these strategies in Python:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

class TradingStrategies:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.get_data()

    def get_data(self):
        df = web.DataReader(self.ticker, 'yahoo', self.start_date, self.end_date)
        return df

    def momentum(self, lookback_period):
        momentum = self.data['Close'] - self.data['Close'].shift(lookback_period)
        self.data['Momentum'] = momentum
        return self.data

    def mean_reversion(self, lookback_period):
        mean = self.data['Close'].rolling(window=lookback_period).mean()
        std_dev = self.data['Close'].rolling(window=lookback_period).std()
        self.data['Z-Score'] = (self.data['Close'] - mean) / std_dev
        return self.data

    def breakout(self, lookback_period):
        self.data['High'] = self.data['High'].rolling(window=lookback_period).max()
        self.data['Low'] = self.data['Low'].rolling(window=lookback_period).min()
        return self.data

# Example usage:
trading = TradingStrategies('AAPL', '2020-01-01', '2021-12-31')
momentum_data = trading.momentum(14)
mean_reversion_data = trading.mean_reversion(14)
breakout_data = trading.breakout(14)
```

This code first fetches the stock data for a given ticker symbol and date range. Then it calculates the momentum, mean reversion, and breakout for the stock using a specified lookback period. The results are added as new columns to the DataFrame.

Please note that this is a very basic implementation and real-world trading strategies would be much more complex and take many other factors into account. Also, this code does not actually execute any trades, it just calculates values that could be used to make trading decisions.