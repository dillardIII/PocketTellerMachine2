from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code that uses the Alpaca API to initiate a trade. This code will buy 1 share of Apple stock. Please replace `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` with your own Alpaca account's API key and secret key.

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

This code will initiate a trade only if the account status is active. The order is a market order, which means it will be executed at the best available price in the market.

Please note that this is a paper trading API endpoint, which means it's for simulated trading and won't actually execute any trades in the real stock market. For real trading, you need to use the live trading endpoint and ensure you're aware of the risks involved in trading.

Also, you need to install the Alpaca Trade API Python SDK. You can install it via pip:

```bash
pip install alpaca-trade-api
```