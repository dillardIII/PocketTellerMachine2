In order to evaluate and optimize the current trading algorithms, we first need to have access to the existing algorithms. However, as a text-based AI model developed by OpenAI, I don't have the ability to access or interact with external systems or databases, including your trading algorithms. 

However, I can provide you with a general example of how you might evaluate and optimize a simple trading algorithm using Python. This example uses a simple moving average crossover strategy.

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import ParameterGrid
import backtrader as bt

# Define the trading strategy
class MovingAverageStrategy(bt.Strategy):
    params = (('short_period', 20), ('long_period', 50))

    def __init__(self):
        self.data_close = self.datas[0].close
        self.order = None
        self.price = None
        self.comm = None
        self.short_sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.short_period)
        self.long_sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.long_period)

    def next(self):
        if self.order:
            return

        if not self.position:
            if self.short_sma[0] > self.long_sma[0]:
                self.order = self.buy()
        else:
            if self.short_sma[0] < self.long_sma[0]:
                self.order = self.sell()

# Evaluate the strategy with different parameters
param_grid = {'short_period': range(10, 31), 'long_period': range(50, 71)}
grid = ParameterGrid(param_grid)

for params in grid:
    cerebro = bt.Cerebro()
    cerebro.addstrategy(MovingAverageStrategy, **params)
    cerebro.broker.setcash(100000.0)
    data = bt.feeds.YahooFinanceData(dataname='AAPL', fromdate=datetime(2019, 1, 1), todate=datetime(2020, 12, 31))
    cerebro.adddata(data)
    cerebro.run()

    final_value = cerebro.broker.getvalue()
    print('Final Portfolio Value: ${}'.format(final_value))
```

This code will evaluate the MovingAverageStrategy with different short and long period parameters. The final portfolio value for each set of parameters will be printed out. You can then choose the parameters that give the best results.

Please replace 'AAPL' with your stock symbol and adjust the date range as per your needs. Also, install necessary libraries by using pip install backtrader pandas numpy sklearn.