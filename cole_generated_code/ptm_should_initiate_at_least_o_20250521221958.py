from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that uses the Alpaca API to initiate a trade. This code will buy 1 share of Apple stock. Please replace `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` with your actual Alpaca API key and secret.

```python
import alpaca_trade_api as tradeapi

# Set up the API connection
api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

# Get account info
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

This code will print out the account information, check if the account is restricted from trading, and then submit a market order to buy 1 share of Apple stock. The `time_in_force` parameter is set to 'gtc', which stands for 'Good Till Cancelled', meaning the order will stay open until it is filled or cancelled.

Please note that this is a very basic example of a trading bot and doesn't include any strategy for when to buy or sell stocks. It's recommended to use this code in a paper trading account for testing purposes.