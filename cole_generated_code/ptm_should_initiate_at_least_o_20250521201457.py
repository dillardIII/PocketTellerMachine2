Sure, here is a simple Python code using the alpaca_trade_api which is a popular API for trading stocks. Please replace 'APCA-API-KEY-ID' and 'APCA-API-SECRET-KEY' with your own API keys.

```python
import alpaca_trade_api as tradeapi

# Setup
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

This code will initiate a trade to buy 1 share of Apple stock at the current market price. This is a 'good till cancelled' order which means it will stay active until it is manually cancelled.

Please note that this is a test trade on the paper trading platform of Alpaca Markets. For real trading, you would need to change the base_url to Alpaca's live trading url.

Also, please be aware that trading involves risk, and this code does not implement any risk management or trading strategy. It is important to understand the implications and risks of trading before executing any trades.