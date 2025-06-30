from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python code using the `alpaca-trade-api` library to initiate a trade. This code will buy 1 share of Apple stock. Please replace `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` with your actual Alpaca API key and secret.

```python
import alpaca_trade_api as tradeapi

# Set up the API connection
api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

# Get account information
account = api.get_account()

# Check if the account is active
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
    print("Account is not active, cannot initiate trade.")
```

This code will initiate a trade in a paper trading account (simulated trading with fake money for practice), so it's perfect for gaining practical experience. If you want to trade in a real account, you should change the `base_url` to `'https://api.alpaca.markets'`.

Please note that trading involves risks, you should only trade with money that you can afford to lose. Also, this code does not include any error handling or trading strategy, it's a very basic example just to show how to use the API to initiate a trade.