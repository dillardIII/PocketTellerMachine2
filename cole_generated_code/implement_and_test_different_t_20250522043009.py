To implement and test different trading strategies, we can use the `backtrader` library in Python. This library allows us to backtest trading strategies, analyze the results, and optimize the strategies. 

Here's a simple example of how you can implement and test a moving average crossover strategy:

```python
import backtrader as bt

# Create a subclass of bt.Strategy to define the indicators and logic
class MovingAverageStrategy(bt.Strategy):
    params = (('short_period', 20), ('long_period', 50),)

    def __init__(self):
        self.short_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.short_period)
        self.long_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.long_period)

    def next(self):
        if self.short_ma[0] > self.long_ma[0] and self.short_ma[-1] < self.long_ma[-1]:
            self.buy()
        elif self.short_ma[0] < self.long_ma[0] and self.short_ma[-1] > self.long_ma[-1]:
            self.sell()

# Create a cerebro entity
cerebro = bt.Cerebro()

# Add a strategy
cerebro.addstrategy(MovingAverageStrategy)

# Create a data feed
data = bt.feeds.YahooFinanceCSVData(dataname='AAPL.csv')

# Add the data to Cerebro
cerebro.adddata(data)

# Set our desired cash start
cerebro.broker.setcash(100000.0)

# Run over everything
cerebro.run()

# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
```

This code implements a simple moving average crossover strategy where we buy when the short-term moving average crosses above the long-term moving average and sell when the short-term moving average crosses below the long-term moving average.

You can implement different strategies by changing the logic in the `next` method and compare their performance by running them and checking the final portfolio value.

Note: Please make sure you have the historical data (like 'AAPL.csv' in this case) available in your directory. You can download it from Yahoo Finance or any other reliable source.