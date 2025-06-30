from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and test new trading strategies, we need to consider a few things:

1. Data: We need historical stock price data. We can use Python's `pandas_datareader` to fetch data from various Internet sources into a pandas DataFrame.

2. Strategy: We need to define a trading strategy. For simplicity, let's use a simple moving average (SMA) crossover strategy. When the short-term average crosses above the long-term average, it may be a good time to buy. When the short-term average crosses below the long-term average, it may be a good time to sell.

3. Backtesting: We need to test our strategy on historical data to see how it would have performed. We can use Python's `backtrader` library for this.

Here is a simple example of how we might implement this:

```python
import pandas as pd
import pandas_datareader.data as web
import backtrader as bt
import datetime

# Define the trading strategy
class SmaCross(bt.Strategy):
    params = (('pfast', 10), ('pslow', 30),)
    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)
        sma2 = bt.ind.SMA(period=self.p.pslow)
        self.crossover = bt.ind.CrossOver(sma1, sma2)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0:
            self.close()

# Fetch historical data
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2020, 12, 31)
data = web.DataReader('AAPL', 'yahoo', start, end)

# Create a backtester
cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)
data = bt.feeds.PandasData(dataname=data)
cerebro.adddata(data)
cerebro.run()

# Plot the result
cerebro.plot()
```

This code fetches historical data for AAPL from Yahoo Finance, applies the SMA crossover strategy, and backtests it over the specified time period. It then plots the portfolio value over time. 

Please note that this is a very simple strategy and is unlikely to be profitable without further refinement. It's just a starting point. You should consider other factors such as transaction costs, slippage, risk management, etc. when developing a real trading strategy.