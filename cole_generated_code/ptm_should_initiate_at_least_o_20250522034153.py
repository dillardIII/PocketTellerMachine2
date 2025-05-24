Sure, here is a simple Python code that uses the `yfinance` library to download stock data and initiate a trade. Please note that this is a simulation and does not involve real money.

```python
import yfinance as yf

class PTM:
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol
        self.data = yf.download(ticker_symbol, start='2021-01-01', end='2021-12-31')
        self.balance = 10000  # initial balance
        self.shares = 0  # initial shares

    def trade(self):
        # Buy at the start of the year
        opening_price = self.data.iloc[0]['Open']
        self.shares = self.balance // opening_price
        self.balance -= self.shares * opening_price
        print(f'Bought {self.shares} shares at {opening_price} each.')

        # Sell at the end of the year
        closing_price = self.data.iloc[-1]['Close']
        self.balance += self.shares * closing_price
        print(f'Sold {self.shares} shares at {closing_price} each.')

        print(f'Final balance: {self.balance}')

# Test the PTM class
ptm = PTM('AAPL')
ptm.trade()
```

This script simulates buying shares of a company (in this case, Apple) at the opening price of the first trading day of 2021 and selling them at the closing price of the last trading day of 2021. The final balance is printed out at the end.

Please note that this is a very simplistic trading strategy and is unlikely to yield good results in real trading. It's just a demonstration of how one might use Python to interact with stock market data.