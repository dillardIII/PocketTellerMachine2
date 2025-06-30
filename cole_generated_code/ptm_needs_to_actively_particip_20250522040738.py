from ghost_env import INFURA_KEY, VAULT_ADDRESS
It seems like you want to create a trading bot in Python. Here's a simple example of how you might create a trading bot using the Alpaca API, which allows for commission-free trading. This bot will buy a stock when its price decreases by a certain percentage and sell when its price increases by a certain percentage.

Please note that this is a very basic example and real trading bots need to consider many more factors.

```python
import alpaca_trade_api as tradeapi

class TradingBot:
    def __init__(self, base_url, api_key, api_secret):
        self.api = tradeapi.REST(api_key, api_secret, base_url)
        self.symbol = 'AAPL'  # The stock to trade
        self.buy_threshold = -0.02  # Buy if the price drops 2%
        self.sell_threshold = 0.02  # Sell if the price rises 2%
        self.last_price = self.get_price()

    def get_price(self):
        return self.api.get_last_trade(self.symbol).price

    def trade(self):
        current_price = self.get_price()
        change_percent = (current_price - self.last_price) / self.last_price

        if change_percent <= self.buy_threshold:
            self.api.submit_order(
                symbol=self.symbol,
                qty=1,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            print(f'Bought {self.symbol}')

        elif change_percent >= self.sell_threshold:
            self.api.submit_order(
                symbol=self.symbol,
                qty=1,
                side='sell',
                type='market',
                time_in_force='gtc'
            )
            print(f'Sold {self.symbol}')

        self.last_price = current_price

# Initialize the bot
bot = TradingBot('<base_url>', '<api_key>', '<api_secret>')

# Run the bot
while True:
    bot.trade()
```

Replace `<base_url>`, `<api_key>`, and `<api_secret>` with your actual Alpaca API credentials.

Please note that this bot will run indefinitely until you stop it, and it will make a trade every time the price changes by the specified threshold. This is a very basic bot and there are many ways it could be improved, such as by adding more sophisticated trading strategies, error handling, logging, etc. Also, keep in mind that trading involves risk and you should only trade with money you can afford to lose.