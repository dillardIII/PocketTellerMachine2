Sure, here is a simple Python code that uses the alpaca trade API to initiate a trade. Please replace `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` with your actual API keys.

```python
import alpaca_trade_api as tradeapi

# Set up the API connection
api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

# Get account information
account = api.get_account()
print(account)

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we have to work with.
print('${} is available as cash'.format(account.cash))

# Submit a market order to buy 1 share of Apple stock (symbol: AAPL)
api.submit_order(
    symbol='AAPL',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc'
)
```

This code will initiate a trade to buy 1 share of Apple stock at the current market price. Please note that this is a simple example and doesn't include any logic for making trading decisions. You would need to implement your own trading strategy for a real-world application.

Also, please note that this code uses Alpaca's paper trading API, which simulates trades but doesn't actually execute them in the real market. This is a good way to gain practical experience without risking real money.