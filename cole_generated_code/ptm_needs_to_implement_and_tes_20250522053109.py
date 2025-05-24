Sure, here's a simple example of a Python code that implements a basic moving average crossover strategy. This strategy is one of the most common systematic strategies used in trading. It uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy. When the short moving average crosses below the long moving average, it's a signal to sell.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = 'AAPL'
ticker_data = yf.download(ticker, start='2020-01-01', end='2021-12-31')

# Calculate short and long moving averages
short_window = 20
long_window = 100

signals = pd.DataFrame(index=ticker_data.index)
signals['signal'] = 0.0

# Short moving average
signals['short_mavg'] = ticker_data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Long moving average
signals['long_mavg'] = ticker_data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print DataFrame
print(signals)
```

This code uses the `yfinance` library to download historical data for a given ticker symbol. It then calculates short and long moving averages of the closing prices, and generates trading signals based on these moving averages. When the short moving average is above the long moving average, the signal is 1 (indicating a buy), and when it's below, the signal is 0 (indicating a sell).

Please note that this is a very basic trading strategy and should not be used for actual trading without further improvements and adjustments. It's merely an example of how you could implement a trading strategy in Python.