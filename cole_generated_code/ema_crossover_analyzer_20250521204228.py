Sure, here is a simple Python code to analyze the EMA (Exponential Moving Average) crossover. This code uses the `pandas` library for data manipulation and `yfinance` to download historical stock data from Yahoo Finance.

```python
import pandas as pd
import yfinance as yf

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(stock_symbol, short_window, long_window):
    # Download historical data as dataframe
    data = yf.download(stock_symbol, start='2020-01-01', end='2022-12-31')

    # Calculate short and long EMA
    data['short_ema'] = calculate_ema(data['Close'], short_window)
    data['long_ema'] = calculate_ema(data['Close'], long_window)

    # Create signals
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_ema'][short_window:] > data['long_ema'][short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    # Print data
    print(data)

# Test the function
ema_crossover_analyzer('AAPL', 12, 26)
```

This script downloads the historical data for the given stock symbol, calculates the short and long EMA, and then generates trading signals and positions based on the crossover of these two EMAs. When the short EMA is above the long EMA, it generates a buy signal (1.0), and when it's below, it generates a sell signal (0.0). The positions are calculated by taking the difference of these signals.

Please note that you need to install `pandas`, `yfinance` and `numpy` libraries to run this script. You can install them using pip:

```
pip install pandas yfinance numpy
```