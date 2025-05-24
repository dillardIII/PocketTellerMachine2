Sure, here's a basic example of a trading strategy implemented in Python. This strategy is known as a simple moving average crossover strategy. It's a very basic strategy where a position is taken based on whether the short term moving average is above or below the long term moving average.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for desired ticker symbol
def download_data(stock, start='2000-01-01', end='2020-12-31'):
    data = yf.download(stock, start, end)
    return data

# Calculate short-term simple moving average
def calculate_SMA(data, window):
    sma = data.rolling(window=window).mean()
    return sma

# Create trading signals based on short-term and long-term SMAs
def create_trading_signals(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short simple moving average
    signals['short_SMA'] = calculate_SMA(data['Close'], short_window)

    # Long simple moving average
    signals['long_SMA'] = calculate_SMA(data['Close'], long_window)

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_SMA'][short_window:] > signals['long_SMA'][short_window:], 1.0, 0.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Define the ticker symbol and SMA windows
ticker = "AAPL"
short_window = 40
long_window = 100

# Download the data
data = download_data(ticker)

# Generate trading signals
signals = create_trading_signals(data, short_window, long_window)

# Print the DataFrame
print(signals)
```

In this code, we first download the historical data for the desired ticker symbol using the `yfinance` library. We then calculate the short-term and long-term simple moving averages (SMA) for the closing prices. A trading signal is generated when the short-term SMA crosses the long-term SMA. A buy signal is generated when the short-term SMA is greater than the long-term SMA, and a sell signal is generated when the short-term SMA is less than the long-term SMA.

Please note that this is a very basic trading strategy and may not be profitable in real-world trading. It's important to consider other factors such as transaction costs and slippage, and to thoroughly backtest any strategy before live trading.