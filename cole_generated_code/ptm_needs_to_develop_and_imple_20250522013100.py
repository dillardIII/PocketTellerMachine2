from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop a trading strategy, we will use Python and a few libraries such as pandas and yfinance to fetch the stock data. We will implement a simple moving average crossover strategy for this task.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    data['short_sma'] = calculate_sma(data['Close'], short_window)
    data['long_sma'] = calculate_sma(data['Close'], long_window)

    # Create signals based on the crossover of short and long moving average
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_sma'][short_window:] 
                                            > data['long_sma'][short_window:], 1.0, 0.0)

    # Generate trading orders based on the signals
    data['positions'] = data['signal'].diff()

    return data

# Fetch the stock data
data = yf.download('AAPL', start='2020-01-01', end='2021-12-31')

# Implement the trading strategy
trading_data = trading_strategy(data, 50, 200)

# Plot the stock price, short and long window simple moving averages and the buy/sell signals
plt.figure(figsize=(10,5))
plt.plot(trading_data['Close'], label='Close Price', color='blue')
plt.plot(trading_data['short_sma'], label='50-day SMA', color='red')
plt.plot(trading_data['long_sma'], label='200-day SMA', color='green')
plt.plot(trading_data.loc[trading_data.positions == 1.0].index, 
         trading_data.short_sma[trading_data.positions == 1.0],
         '^', markersize=10, color='m', label='buy')
plt.plot(trading_data.loc[trading_data.positions == -1.0].index, 
         trading_data.short_sma[trading_data.positions == -1.0],
         'v', markersize=10, color='k', label='sell')
plt.title('AAPL - Moving Average Crossover Trading Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
```

This script fetches the historical stock data of Apple Inc. (AAPL) from Yahoo Finance, calculates the 50-day and 200-day simple moving averages (SMA), generates buy/sell signals based on the crossover of these SMAs, and plots the stock price, SMAs, and the buy/sell signals.

Please note that this is a simple trading strategy and may not be profitable in real trading. Always use trading strategies with caution and consider other factors such as market conditions, risk tolerance, etc.