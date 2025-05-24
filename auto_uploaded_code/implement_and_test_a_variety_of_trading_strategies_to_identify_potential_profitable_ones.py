In order to implement and test a variety of trading strategies, we will need to use a backtesting library such as `bt` or `backtrader`. Here, we will use `backtrader` for its flexibility and features.

Here is a simple example of a moving average crossover strategy:

```python
import backtrader as bt

# Create a subclass of bt.Strategy to define the indicators and logic
class MovingAverageCrossover(bt.Strategy):
    params = (('pfast', 20), ('pslow', 50),)

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

# Create a cerebro entity
cerebro = bt.Cerebro()

# Add a strategy
cerebro.addstrategy(MovingAverageCrossover)

# Create a Data Feed
data = bt.feeds.YahooFinanceData(dataname='AAPL', fromdate=datetime(2011, 1, 1), todate=datetime(2022, 12, 31))
cerebro.adddata(data)

# Set our desired cash start
cerebro.broker.setcash(100000.0)

# Run over everything
cerebro.run()

# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
```

This code implements a simple moving average crossover strategy, where we buy when the fast moving average crosses above the slow moving average, and sell when the fast moving average crosses below the slow moving average.

Please note that this is a very basic strategy and is unlikely to be profitable without further refinement. It's also important to note that past performance is not indicative of future results, and this code does not take into account transaction costs or slippage.

You can implement and test a variety of other trading strategies in a similar way, by subclassing bt.Strategy and defining your own indicators and logic in the `__init__` and `next` methods.