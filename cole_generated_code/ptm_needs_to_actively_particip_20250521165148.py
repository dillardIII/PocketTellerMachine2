from ghost_env import INFURA_KEY, VAULT_ADDRESS
Your task requires a lot of detailed specifications that you haven't provided yet. Trading involves various strategies and approaches which can be quite complex when it comes to coding them. A simple Python code for active trading involves sending buy/sell orders to an exchange, using an algorithmic trading library such as Backtrader.

Here's a simple example of a Python code which uses Backtrader to create a trading bot. In this sample, we'll just make a bot that buys/sells on simple Moving Average Crossover strategy:

```python
import backtrader as bt

class MAcrossover(bt.Strategy):
    params = (('fastlength', 5), ('slowlength', 25))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None

        self.sma1 = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.fastlength)
        self.sma2 = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.slowlength)

    def next(self):
        if self.order:
            return
        if not self.position:
            if self.sma1[0] > self.sma2[0]:
                self.order = self.buy()
        else:
            if self.sma1[0] < self.sma2[0]:
                self.order = self.sell()

cerebro = bt.Cerebro()
data = bt.feeds.YahooFinanceCSVData(dataname='FB.csv')
cerebro.adddata(data)
cerebro.addstrategy(MAcrossover)
cerebro.run()
```

This sample code creates a simple bot to buy/sell Facebook's stock (FB.csv file needs to be in the same directory or else provide the full path to the file) based on Moving Average Crossover strategy. It uses Backtrader's built in SimpleMovingAverage indicator for the same. This bot buys when the fast simple moving average crosses above the slow simple moving average, and sells when the fast simple moving average crosses below the slow simple moving average.

Real life trading involves many more complexities like commission, slippage, order types, risk management etc. Also, real life trading requires live data feed and execution environment which can't be shown in an example. It's recommended to thoroughly study algorithmic trading before implementing it. 

Please note this is a very simplistic version of a trading system used for demonstration purposes only, and should not be used for live trading without appropriate modifications and testing.