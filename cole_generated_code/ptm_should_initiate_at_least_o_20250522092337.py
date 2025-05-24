In order to initiate a trade, we first need to have a trading API. For this example, I will use the Alpaca API, a popular choice for algorithmic trading. Here's a simple Python script that initiates a trade:

```python
import alpaca_trade_api as tradeapi

# Use your own keys here
API_KEY = 'YOUR_API_KEY'
SECRET_KEY = 'YOUR_SECRET_KEY'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use paper trading URL

# Initialize the API
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# Define the symbol and quantity
symbol = 'AAPL'  # Apple Inc.
qty = 1  # Buy 1 share

# Submit the order
order = api.submit_order(
    symbol=symbol,
    qty=qty,
    side='buy',
    type='market',
    time_in_force='gtc'
)

print(f"Submitted order to buy {qty} share(s) of {symbol}")
```

This script will initiate a trade to buy 1 share of Apple Inc. (AAPL) at the current market price. Please replace `'YOUR_API_KEY'` and `'YOUR_SECRET_KEY'` with your own Alpaca API keys.

Note: This is a paper trading URL, which means it's a simulated trading environment used for practice. No real trades will be made. If you want to do real trading, you need to replace the `BASE_URL` with the live trading URL and be aware of the financial risks involved.