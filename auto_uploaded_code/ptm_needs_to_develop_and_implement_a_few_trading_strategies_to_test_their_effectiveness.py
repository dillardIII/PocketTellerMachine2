Sure, I'll provide a simple example of a trading strategy using Python. This strategy will be a simple moving average crossover strategy. This strategy generates a buy signal when the short-term moving average crosses above the long-term moving average, and a sell signal when the short-term moving average crosses below the long-term moving average.

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol
def download_data(stock, start='2010-01-01', end='2020-12-31'):
    data = yf.download(stock, start, end)
    return data

# Calculate short-term moving average and long-term moving average
def calculate_SMA(data, window_short, window_long):
    SMA_short = data['Close'].rolling(window=window_short).mean()
    SMA_long = data['Close'].rolling(window=window_long).mean()
    data = data.assign(SMA_short=SMA_short, SMA_long=SMA_long).dropna()
    return data

# Generate signals based on crossover strategy
def generate_signals(data):
    buy_signal = (data['SMA_short'] > data['SMA_long'])
    sell_signal = (data['SMA_short'] < data['SMA_long'])
    return buy_signal, sell_signal

# Implement the strategy
def implement_strategy(ticker_symbol, window_short=50, window_long=200):
    data = download_data(ticker_symbol)
    data = calculate_SMA(data, window_short, window_long)
    buy_signal, sell_signal = generate_signals(data)

    # Plotting
    plt.figure(figsize=(10,5))
    plt.plot(data['Close'], label=ticker_symbol)
    plt.plot(data['SMA_short'], label='SMA_short')
    plt.plot(data['SMA_long'], label='SMA_long')
    plt.legend(loc='upper left')
    plt.title('Moving Average Crossover Strategy')
    plt.show()

    return buy_signal, sell_signal

# Example usage
buy_signal, sell_signal = implement_strategy('AAPL')
```

This code will download historical data for the AAPL stock, calculate the short-term and long-term moving averages, generate buy and sell signals based on the crossover strategy, and plot the results.

Please note that this is a simple example and real trading strategies should take into account many other factors such as transaction costs, risk management, etc. Also, you need to install the `yfinance` package to download the historical data from Yahoo Finance. You can install it using pip:

```shell
pip install yfinance
```