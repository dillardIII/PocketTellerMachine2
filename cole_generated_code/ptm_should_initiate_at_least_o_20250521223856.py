from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple example of a Python code that uses the Alpaca API to initiate a trade. Please note that this is a simulated trade and you need to replace 'APCA-API-KEY-ID' and 'APCA-API-SECRET-KEY' with your actual API keys to execute real trades.

```python
import alpaca_trade_api as tradeapi

# setup
api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

# get account information
account = api.get_account()
print(account)

# check if the market is open
clock = api.get_clock()
print('The market is {}'.format('open.' if clock.is_open else 'closed.'))

# initiate a trade
if clock.is_open:
    api.submit_order(
        symbol='AAPL',
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
```

This script first checks if the market is open. If it is, it initiates a trade to buy 1 share of Apple Inc. (AAPL) at the current market price. The order is a 'Good Till Cancelled' order, meaning it will remain active until it is filled or cancelled.

Please remember that trading involves risks and you should only trade with what you can afford to lose. This script is a very basic example and does not include any risk management or trading strategy.