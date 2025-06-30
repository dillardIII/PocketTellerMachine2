from ghost_env import INFURA_KEY, VAULT_ADDRESS
In order to accomplish this task, we need to create a PTM (Portfolio Trading Model) and apply a strategy that actively increases trading volume. Here is a simple example considering only buying of stocks. It doesn't consider other factors such as market trends or company fundamentals which should be considered in a real trading strategy.

```python
class Portfolio:
    def __init__(self):
        self.stocks = {}  # stores bought stock information

    def buy_stock(self, ticker, volume, price):
        if ticker in self.stocks:
            self.stocks[ticker]['volume'] += volume
            self.stocks[ticker]['total_cost'] += volume * price
        else:
            self.stocks[ticker] = {'volume': volume, 'total_cost': volume * price}

class PTM:
    def __init__(self, portfolio, threshold):
        self.portfolio = portfolio
        self.threshold = threshold

    def increase_trading_volume(self, ticker, current_price):
        target_volume = self.threshold / current_price
        self.portfolio.buy_stock(ticker, target_volume, current_price)

portfolio = Portfolio()
ptm = PTM(portfolio, threshold=1000)  # threshold is the amount of money you are ready to spend in every transaction

# Imagine that these prices arrive dynamically (for instance from a stock market API)
stock_prices = {
    "AAPL": 135.69,
    "GOOGL": 2110.7,
    "MSFT": 234.65,
    # other stocks...
}

for ticker, price in stock_prices.items():
    ptm.increase_trading_volume(ticker, price)
``` 

The PTM class introduces a method `increase_trading_volume` that allows to buy a certain volume of a given stock at its current price. The volume to buy is calculated as the threshold (a pre-determined amount of money you are ready to invest in every transaction) divided by the current stock price. Thus, if the stock price decreases, you will buy more volume, essentially increasing the trading volume.