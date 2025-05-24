Sure, here is a very basic example of how you might initiate a trade using the python-binance API. This example will buy 100 BNB coins at market price. Please note that you need to replace `api_key` and `api_secret` with your actual Binance API key and secret.

```python
from binance.client import Client

# Initialize the Binance client
client = Client(api_key, api_secret)

# Define the symbol and quantity
symbol = 'BNBBTC'
quantity = 100

# Place a market buy order
order = client.order_market_buy(
    symbol=symbol,
    quantity=quantity)

print(order)
```

Please note that this code is for educational purposes only and should not be used for real trading without proper error handling and additional features. Also, make sure you are aware of the risks associated with trading cryptocurrencies.