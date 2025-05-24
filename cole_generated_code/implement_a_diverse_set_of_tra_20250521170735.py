To implement different trading strategies, we first need to install the backtrading module via pip.

In the Python environment:

```python
!pip install backtrader
```

Then, we proceed with a simple implementation of moving average crossover strategy:

```python
import backtrader as bt

# Define a Moving Average Crossover strategy
class MACrossover(bt.Strategy):
    params = (('short_period', 12), ('long_period', 26), )

    def __init__(self):
        # Initialize two moving averages
        self.short_mav = bt.indicators.EMA(period=self.params.short_period)
        self.long_mav = bt.indicators.EMA(period=self.params.long_period)

    def next(self):
        # If the short moving average crosses above the long moving average, issue a buy order
        if self.short_mav > self.long_mav and not self.position:
            self.buy()

        # If the short moving average crosses below the long moving average, issue a sell order
        if self.short_mav < self.long_mav and self.position:
            self.sell()

# Initialize the Cerebro engine
cerebro = bt.Cerebro()

# Set up the backtest
data = bt.feeds.YahooFinanceData(dataname='YHOO', fromdate=datetime(2011, 1, 1), todate=datetime(2012, 12, 31))
cerebro.adddata(data)
cerebro.addstrategy(MACrossover)

# Run the backtest
cerebro.run()

```
Please note that you would need actual data and to tweak the parameters of the moving averages based on the asset you are dealing with. The above strategy is just a starting point, please conduct a proper backtest and validate it's effectiveness before using them in live trading.

This script is using Moving Average Crossover strategy only. To try other strategies, you would need to replace `MACrossover` strategy class with different strategy logic. For example, you could implement RSI based strategy, Bollinger Band based strategy etc.

Always remember, that code alone will not give you the most effective strategy, it always depends on various factors like market condition, asset selection, risk management etc. Also, past performance is not always indicative of future results.