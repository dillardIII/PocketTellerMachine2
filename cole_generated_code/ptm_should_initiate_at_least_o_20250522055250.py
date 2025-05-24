Sure, I can provide a simple example of a Python code that uses the Alpaca API to initiate a trade. Please note that you need to replace 'APCA-API-KEY-ID' and 'APCA-API-SECRET-KEY' with your actual Alpaca API keys.

```python
import alpaca_trade_api as tradeapi

# Set up the API connection
api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

# Get account info
account = api.get_account()

# Check if our account is active
if account.status == 'ACTIVE':
    # Initiate a trade
    api.submit_order(
        symbol='AAPL',
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
else:
    print("Account is not active")
```

This script will buy 1 share of Apple Inc. (AAPL) at the current market price. The order type is 'gtc' (good-till-cancelled), which means the order will remain active until it is manually cancelled or the trade is executed.

Please note that this is a very basic example and real-world trading algorithms are much more complex. They take into account various factors such as current portfolio, market conditions, risk tolerance, etc. Also, keep in mind that trading involves risk and it's possible to lose money.