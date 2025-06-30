from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code using the `yfinance` library to initiate a trade. This example will buy 1 share of Apple Inc. (AAPL). Please note that this is a simulated trade and does not involve real money.

```python
import yfinance as yf

def buy_stock(symbol, num_shares):
    stock = yf.Ticker(symbol)
    current_price = stock.info['regularMarketPrice']
    total_cost = current_price * num_shares
    print(f"Bought {num_shares} shares of {symbol} at {current_price} each, for a total of {total_cost}")

buy_stock("AAPL", 1)
```

This script will print out a message indicating that a purchase was made. However, it's important to note that this is a simulation and doesn't actually buy any stock. For actual trading, you'd need to use a trading API like Alpaca, TD Ameritrade, or Interactive Brokers. These APIs require you to have an account with them and they have their own Python libraries that you can use to place trades.

Also, please be aware that trading involves risk and you should only trade with money that you can afford to lose. It's recommended to understand the basics of stock trading and the specific rules and fees of the trading platform you're using before you start trading.