Here is a simple Python code that uses the Alpaca API for trading. This code will initiate a trade by buying one share of Apple stock.

```python
import alpaca_trade_api as tradeapi

# You need to sign up on Alpaca and get your API keys
API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'
BASE_URL = 'https://paper-api.alpaca.markets' # Use paper trading URL for practice

# Initialize the API
api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

# Define the symbol and quantity
symbol = 'AAPL'
qty = 1

# Submit a market order to buy 1 share of Apple stock
order = api.submit_order(
    symbol=symbol,
    qty=qty,
    side='buy',
    type='market',
    time_in_force='gtc'
)

print(f"Submitted order to buy {qty} share of {symbol}")
```

Please note that this is a very basic example and real-world trading involves more complexities like handling market data, risk management, etc. Also, replace `'your_api_key'` and `'your_secret_key'` with your actual Alpaca API keys.

This code will only work when the market is open. If you want to place an order while the market is closed, you can use a limit order and set the `time_in_force` to `'gtc'` (Good-Til-Cancelled), which means the order will remain active until it is filled or cancelled.