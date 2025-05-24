Sure, here's a simple Python script that uses the Alpaca API to initiate a trade. Please note that you need to replace `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` with your actual API keys.

```python
import alpaca_trade_api as tradeapi

# Set up the API connection
api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets')

# Get account information
account = api.get_account()
print(account)

# Check if the market is open
clock = api.get_clock()
if clock.is_open:
    # Initiate a trade
    api.submit_order(
        symbol='AAPL',
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
else:
    print("The market is closed")
```

This script checks if the market is open and if it is, it initiates a market order to buy 1 share of Apple (AAPL). This is a very basic example and real trading algorithms can be much more complex. Also, please note that this script uses a paper trading API endpoint which means it's for simulation and no real money is involved.