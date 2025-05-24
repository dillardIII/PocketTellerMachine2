Sure, here's a simple example of a Python trading bot using the Moving Average Crossover strategy. It's a basic strategy where the bot buys when the short term moving average crosses above the long term moving average and sells when the short term moving average crosses below the long term moving average.

Please note that this is a simplified version and real trading bots will require much more complexity including error handling, more sophisticated strategies, and use of real-time data.

```python
import pandas as pd
import yfinance as yf

class TradingBot:
    def __init__(self, symbol, short_window, long_window):
        self.symbol = symbol
        self.short_window = short_window
        self.long_window = long_window

    def calculate_sma(self, data, window):
        return data.rolling(window=window).mean()

    def execute_trading_strategy(self):
        # Download historical data as dataframe
        data = yf.download(self.symbol, start='2020-01-01', end='2022-12-31')

        # Calculate short and long term moving averages
        data['short_mavg'] = self.calculate_sma(data['Close'], self.short_window)
        data['long_mavg'] = self.calculate_sma(data['Close'], self.long_window)

        # Create signals
        data['signal'] = 0.0
        data['signal'][self.short_window:] = np.where(data['short_mavg'][self.short_window:] > data['long_mavg'][self.short_window:], 1.0, 0.0)

        # Generate trading orders
        data['positions'] = data['signal'].diff()

        # Print data
        print(data)

        # Initialize the plot figure
        fig = plt.figure()

        # Add a subplot and label for y-axis
        ax1 = fig.add_subplot(111, ylabel='Price in $')

        # Plot the closing price
        data['Close'].plot(ax=ax1, color='r', lw=2.)

        # Plot the short and long moving averages
        data[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

        # Plot the buy signals
        ax1.plot(data.loc[data.positions == 1.0].index, data.short_mavg[data.positions == 1.0], '^', markersize=10, color='m')

        # Plot the sell signals
        ax1.plot(data.loc[data.positions == -1.0].index, data.short_mavg[data.positions == -1.0], 'v', markersize=10, color='k')

        # Show the plot
        plt.show()

# Initialize and run the trading bot
bot = TradingBot('AAPL', 40, 100)
bot.execute_trading_strategy()
```

This code uses `yfinance` to download historical data from Yahoo Finance, `pandas` to manipulate the data, and `matplotlib` to visualize the data and trading signals. The bot is initialized with a stock symbol and two window lengths for calculating the short and long term moving averages. The `execute_trading_strategy` method downloads the historical data, calculates the moving averages, generates trading signals and orders, and visualizes the data and signals.