To implement and test new trading strategies, you would typically use a backtesting framework. Here is a simple example of how you might do this using Python's pandas library for data manipulation and backtrader library for backtesting.

```python
import pandas as pd
import backtrader as bt

# Define a new trading strategy
class NewStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        if self.dataclose[0] < self.dataclose[-1]:
            if self.dataclose[-1] < self.dataclose[-2]:
                self.buy()

# Load some market data
data = bt.feeds.YahooFinanceData(dataname='AAPL', fromdate=datetime(2017, 1, 1), todate=datetime(2022, 12, 31))

# Create a backtest
cerebro = bt.Cerebro()
cerebro.addstrategy(NewStrategy)
cerebro.adddata(data)
cerebro.broker.setcash(100000.0)

# Run the backtest
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
```

This code defines a simple trading strategy that buys when the price has decreased for two days in a row. It then backtests this strategy on Apple's stock price from 2017 to 2022.

Please note that this is a very simple example and real trading strategies would be much more complex. Also, backtesting has many pitfalls and just because a strategy performs well in a backtest does not mean it will do so in the future.