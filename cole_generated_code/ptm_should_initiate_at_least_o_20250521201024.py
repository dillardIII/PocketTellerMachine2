Sure, here is a simple example of a Python code that uses the Alpaca API to initiate a trade. This code will buy 1 share of Apple stock. Please replace 'YourAPCA-API-KEY-ID' and 'YourAPCA-API-SECRET-KEY' with your actual Alpaca API key and secret.

```python
import alpaca_trade_api as tradeapi

# Set up the API connection
api = tradeapi.REST('YourAPCA-API-KEY-ID', 'YourAPCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

# Get account information
account = api.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we have to work with.
print('${} is available as cash.'.format(account.cash))

# Submit a market order to buy 1 share of Apple stock (symbol: AAPL)
api.submit_order(
    symbol='AAPL',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc'
)
```

Please note that this is a very basic example and real trading involves a lot more considerations like market conditions, risk management, etc. Also, this code will work only during the market hours. 

Make sure you have the `alpaca-trade-api` package installed in your Python environment. You can install it using pip:

```bash
pip install alpaca-trade-api
```

Also, remember that trading involves risk and you should only trade with what you can afford to lose.