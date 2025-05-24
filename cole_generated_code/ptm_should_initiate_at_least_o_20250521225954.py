Sure, here is a simple example of a Python code that uses the Alpaca API to initiate a trade. Please note that you need to replace `'APCA-API-KEY-ID'` and `'APCA-API-SECRET-KEY'` with your own Alpaca API key and secret key.

```python
import alpaca_trade_api as tradeapi

# Set up Alpaca API environment
api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

# Submit a market order to buy 1 share of Apple stock (symbol: AAPL)
api.submit_order(
    symbol='AAPL',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc'
)
```

This code will initiate a trade to buy 1 share of Apple stock at the current market price. The order is a 'good till cancelled' (gtc) order, which means it will remain active until it is filled or manually cancelled.

Please note that this is a simple example and real trading involves a lot more considerations like risk management, position sizing, etc. Also, make sure to handle exceptions and errors properly in your actual trading code.