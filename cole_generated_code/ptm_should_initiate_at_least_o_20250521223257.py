Here's a simple example of how you could implement a trading bot in Python using the Alpaca API. This bot will buy a stock when its price goes up and sell it when its price goes down.

Please replace `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` with your own Alpaca API keys.

```python
import alpaca_trade_api as tradeapi

# Set up the API
api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets')

# Define the stock we want to trade and the amount of shares
symbol = 'AAPL'
qty = 1

# Get the current price of the stock
current_price = api.get_last_trade(symbol).price

# Get the last 5 minute's worth of historical data
barset = api.get_barset(symbol, 'minute', limit=5)
bars = barset[symbol]

# Calculate the average price over the last 5 minutes
avg_price = sum([bar.c for bar in bars]) / len(bars)

# If the current price is higher than the average price, buy the stock
if current_price > avg_price:
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    print(f"Bought {qty} shares of {symbol}")

# If the current price is lower than the average price, sell the stock
elif current_price < avg_price:
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
    print(f"Sold {qty} shares of {symbol}")
```

This is a very basic trading bot and should not be used for real trading without further improvements. It does not take into account any risk management strategies or market conditions. It simply buys or sells based on the average price over the last 5 minutes.