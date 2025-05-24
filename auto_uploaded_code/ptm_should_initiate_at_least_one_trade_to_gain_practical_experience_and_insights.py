To initiate a trade, you will need to use a trading API. In this example, I'll use the Alpaca API which is a commission-free trading platform that allows you to trade stocks programmatically. You will need to sign up on Alpaca's website and get your API key and secret key.

Here is a simple Python script that initiates a trade:

```python
import alpaca_trade_api as tradeapi

# Replace these with your API connection info from the dashboard
api_key = 'your_api_key'
api_secret = 'your_api_secret'
base_url = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# Submit a market order to buy 1 share of Apple stock (symbol: AAPL)
api.submit_order(
    symbol='AAPL',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc'
)
```

This script will initiate a trade to buy 1 share of Apple stock. Please replace 'your_api_key' and 'your_api_secret' with your actual API key and secret key.

Please note that this is a very basic example and real trading involves a lot more complexity. You should also handle exceptions and errors properly in your code.