from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code using Alpaca API to initiate a trade. Please replace the placeholders with your actual API keys and desired stock symbol.

```python
import alpaca_trade_api as tradeapi

# Set up API keys
api = tradeapi.REST('<Your-API-Key>', '<Your-Secret-Key>', base_url='https://paper-api.alpaca.markets') 

# Define the stock symbol and quantity
symbol = '<Your-Stock-Symbol>'
qty = 1

# Submit a market order to buy 1 share of the stock
order = api.submit_order(
    symbol=symbol,
    qty=qty,
    side='buy',
    type='market',
    time_in_force='gtc'
)

print(f"Successfully submitted order to buy {qty} share(s) of {symbol}")
```

This code will initiate a trade to buy 1 share of the specified stock using a market order. Please note that this code is for educational purposes only and should not be used for actual trading without proper risk management.

Also, please ensure that you have the necessary permissions and funds in your account to carry out the trade.