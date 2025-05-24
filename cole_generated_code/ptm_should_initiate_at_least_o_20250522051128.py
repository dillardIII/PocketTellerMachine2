Sure, I can provide a simple Python code for a trading bot using the Alpaca API. This bot will initiate a trade based on a simple strategy: buy a stock when its price goes up by 1% and sell it when its price goes down by 1%.

Please replace `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` with your actual Alpaca API key and secret.

```python
import alpaca_trade_api as tradeapi

api = tradeapi.REST('APCA-API-KEY-ID', 'APCA-API-SECRET-KEY', base_url='https://paper-api.alpaca.markets') 

symbol = 'AAPL'  # Apple stock
qty = 1  # number of shares to buy/sell

# Get the latest quote
last_quote = api.get_last_quote(symbol)

# Buy if the price goes up by 1%
buy_price = last_quote.askprice * 1.01
if last_quote.askprice >= buy_price:
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='limit',
        time_in_force='gtc',
        limit_price=buy_price
    )

# Sell if the price goes down by 1%
sell_price = last_quote.bidprice * 0.99
if last_quote.bidprice <= sell_price:
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='limit',
        time_in_force='gtc',
        limit_price=sell_price
    )
```

Please note that this is a very simple trading bot and the strategy used here is not guaranteed to make a profit. It's just for gaining experience and potentially increasing wins. You should develop a more sophisticated strategy for a real trading bot. Also, this code does not handle any errors that might occur during trading. You should add error handling code for a production-ready bot.