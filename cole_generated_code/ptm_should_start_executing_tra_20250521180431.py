To start creating and executing trading strategies, a trading bot using Python can be implemented. This bot will use the Python library 'Alpaca', which connects to Alpaca's trade API, allowing trading on U.S. markets using the account.

To illustrate, below is a simple Python script that runs a basic trading strategy. Note that you need to install the Alpaca trade API by running `pip install alpaca-trade-api`.

```Python
import alpaca_trade_api as tradeapi
import time

api = tradeapi.REST('<insert your API key>', '<insert your secret key>', base_url='https://paper-api.alpaca.markets') 

symbol = 'AAPL'  # stock to monitor
quantity = 10  # number of shares to trade

while True:
    # Get current price of the stock
    barset =api.get_barset(symbol, 'minute', 1)
    current_price = barset[symbol][0].c

    # Get current account information
    account = api.get_account()

    # Buy the stock if our cash balance is higher than the current price
    if float(account.cash) > current_price:
        api.submit_order(
            symbol=symbol,
            qty=quantity,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        print(f"Bought {quantity} shares of {symbol}")

    # Sell the stock if we have more than 1 share in our portfolio
    elif api.get_position(symbol).qty > 1:
        api.submit_order(
            symbol=symbol,
            qty=quantity,
            side='sell',
            type='market',
            time_in_force='gtc'
        )
        print(f"Sold {quantity} shares of {symbol}")

    time.sleep(60)   # Pause the script for a minute
```

This is an oversimplified trading bot that buys a specific stock if there is enough cash in the account, and sells it if there are more than 1 share of it in the portfolio. For a real trading strategy, you will likely need to execute more sophisticated steps, like doing market analysis or incorporating machine learning algorithms. 

Remember, trading involves financial risk, always double check the strategies and execute them in a paper trading account to minimize possible risk.
