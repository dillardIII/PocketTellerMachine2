Sure, here is a simple example of a Python trading bot using the Alpaca API. This bot will buy a stock when its price goes up and sell when its price goes down.

Please note that this is a very basic bot and real trading bots require a lot more considerations such as error handling, logging, configuration, testing, etc.

```python
import alpaca_trade_api as tradeapi

class PTM:
    def __init__(self):
        self.api = tradeapi.REST('<APCA-API-KEY-ID>', '<APCA-API-SECRET-KEY>', base_url='https://paper-api.alpaca.markets') 

    def get_price(self, symbol):
        barset = self.api.get_barset(symbol, 'minute', 1)
        return barset[symbol][0].c

    def trade(self, symbol):
        current_price = self.get_price(symbol)
        last_price = 0

        while True:
            current_price = self.get_price(symbol)

            if current_price > last_price:  # price is going up
                self.api.submit_order(
                    symbol=symbol,
                    qty=1,
                    side='buy',
                    type='market',
                    time_in_force='gtc'
                )
            elif current_price < last_price:  # price is going down
                self.api.submit_order(
                    symbol=symbol,
                    qty=1,
                    side='sell',
                    type='market',
                    time_in_force='gtc'
                )

            last_price = current_price

ptm = PTM()
ptm.trade('AAPL')
```

Please replace '<APCA-API-KEY-ID>' and '<APCA-API-SECRET-KEY>' with your actual Alpaca API key ID and secret key.

Also, please note that this bot will run indefinitely until it's manually stopped. It's recommended to add some sort of condition to stop the bot after a certain period of time or after a certain profit/loss threshold is reached.

Lastly, this bot doesn't consider any trading fees or slippage, and it assumes that the market is always open and the orders are always filled immediately, which might not be the case in a real trading scenario.