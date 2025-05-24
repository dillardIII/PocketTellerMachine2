Sure, here is a simple example of how you might implement and test a few basic trading strategies in Python. We'll use pandas for data manipulation and backtrader for backtesting.

```python
import pandas as pd
import backtrader as bt

# Load data
data = pd.read_csv('your_data.csv')

# Create a subclass of bt.Strategy to define the indicators and logic
class MovingAverageCrossStrategy(bt.Strategy):
    params = (('fast', 10), ('slow', 50),)

    def __init__(self):
        self.fast_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.fast)
        self.slow_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.slow)

    def next(self):
        if self.fast_ma[0] > self.slow_ma[0] and self.fast_ma[-1] < self.slow_ma[-1]:
            self.buy()
        elif self.fast_ma[0] < self.slow_ma[0] and self.fast_ma[-1] > self.slow_ma[-1]:
            self.sell()

# Create a cerebro entity
cerebro = bt.Cerebro()

# Add a strategy
cerebro.addstrategy(MovingAverageCrossStrategy)

# Create a Data Feed
data_feed = bt.feeds.PandasData(dataname=data)

# Add the Data Feed to Cerebro
cerebro.adddata(data_feed)

# Set our desired cash start
cerebro.broker.setcash(100000.0)

# Print out the starting conditions
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Run over everything
cerebro.run()

# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
```

This is a simple moving average crossover strategy. It buys when the fast moving average crosses above the slow moving average, and sells when the fast moving average crosses below the slow moving average.

You can implement and test other strategies in a similar way, by creating a new subclass of bt.Strategy and defining your own indicators and logic in the __init__ and next methods.

Please replace 'your_data.csv' with your actual data file. The data should contain columns for 'open', 'high', 'low', 'close' and 'volume'.