Sure, here is a simple example of how you might implement a trading bot in Python using the Alpaca API. Please note that you need to replace `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` with your own Alpaca API keys.

```python
import alpaca_trade_api as tradeapi

# Authenticate with the Alpaca API
api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

# Define the symbol to trade and the amount of shares
symbol = 'AAPL'
qty = 1

# Check if the market is open
clock = api.get_clock()
if clock.is_open:
    # Check if we own any shares of the symbol
    positions = api.list_positions()
    if any([position.symbol == symbol for position in positions]):
        # If we do, sell it
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='sell',
            type='market',
            time_in_force='gtc'
        )
    else:
        # If we don't, buy it
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
```

This script will initiate a trade of 1 share of Apple stock (AAPL) whenever the market is open. If we already own a share of AAPL, it will sell it; otherwise, it will buy one.

Please note that this is a very basic example and real trading algorithms should be much more sophisticated, taking into account various factors such as market conditions, current portfolio, risk tolerance, etc. Also, please be aware of the risks involved in trading and only trade with money you can afford to lose.