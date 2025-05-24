Sure, here's a simple example of a Python trading bot using the Moving Average Crossover strategy. This strategy is based on the principle that if the short-term moving average of a stock price crosses above its long-term moving average, it's a buy signal, and if it crosses below, it's a sell signal.

Please note that this is a simplified example and doesn't include important aspects like error handling, logging, or sophisticated order management. Also, it assumes that you have an account with Alpaca (a commission-free API-first stock brokerage) and you have set your API key and secret key as environment variables.

```python
import os
import alpaca_trade_api as tradeapi
import pandas as pd

class MovingAverageCrossover:
    def __init__(self, symbol, short_window, long_window):
        self.symbol = symbol
        self.short_window = short_window
        self.long_window = long_window

        # Connect to the Alpaca API
        self.api = tradeapi.REST()

    def calculate_moving_average(self, data):
        # Calculate the short and long window simple moving averages
        data['short_sma'] = data['close'].rolling(window=self.short_window).mean()
        data['long_sma'] = data['close'].rolling(window=self.long_window).mean()

        return data

    def generate_signals(self, data):
        # Generate trading signals based on the moving averages
        data['signal'] = 0.0
        data['signal'][self.short_window:] = np.where(data['short_sma'][self.short_window:] > data['long_sma'][self.short_window:], 1.0, 0.0)

        # Generate trading orders based on the signals
        data['order'] = data['signal'].diff()

        return data

    def execute_trades(self):
        # Get the latest data
        data = self.api.get_barset(self.symbol, 'day', limit=self.long_window).df[self.symbol]

        # Calculate the moving averages and generate signals
        data = self.calculate_moving_average(data)
        data = self.generate_signals(data)

        # If the latest signal is a buy signal
        if data['order'].iloc[-1] == 1.0:
            # If we're not already in a long position
            if not self.api.get_position(self.symbol):
                # Buy the stock
                self.api.submit_order(
                    symbol=self.symbol,
                    qty=1,
                    side='buy',
                    type='market',
                    time_in_force='gtc'
                )

        # If the latest signal is a sell signal
        elif data['order'].iloc[-1] == -1.0:
            # If we're in a long position
            if self.api.get_position(self.symbol):
                # Sell the stock
                self.api.submit_order(
                    symbol=self.symbol,
                    qty=1,
                    side='sell',
                    type='market',
                    time_in_force='gtc'
                )

if __name__ == "__main__":
    # Initialize the bot
    bot = MovingAverageCrossover('AAPL', 50, 200)

    # Run the bot
    bot.execute_trades()
```

Please be aware that trading involves risk, and this script is provided without any guarantees or warranty. In no event shall the author or service provider be liable for any loss.