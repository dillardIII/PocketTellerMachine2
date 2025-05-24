Sure, here's a simple example of how you might initiate a trade using a Python library called `alpaca-trade-api` which is a REST API for stock trading. Please note that you need to have an Alpaca account and API keys to use this.

```python
import alpaca_trade_api as tradeapi

# Define your API keys
API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use paper trading URL for testing

# Initialize the API
api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

# Define the symbol and quantity you want to trade
symbol = 'AAPL'
qty = 1

# Submit a market order to buy 1 share of Apple stock (symbol 'AAPL')
order = api.submit_order(
    symbol=symbol,
    qty=qty,
    side='buy',
    type='market',
    time_in_force='gtc'
)

print(f"Submitted order to buy {qty} share(s) of {symbol}")
```

This code will submit a market order to buy 1 share of Apple stock. The `time_in_force='gtc'` parameter means that the order will remain active until it is filled or cancelled.

Please replace `'your_api_key'` and `'your_secret_key'` with your actual Alpaca API keys.

Remember, trading involves risk and this code is a very basic example. In real trading, you would want to implement more sophisticated strategies, risk management, error handling, etc.