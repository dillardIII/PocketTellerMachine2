from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a basic example of a simple trading strategy using Python. This strategy will be a simple moving average crossover strategy. 

Please note that this is a very basic strategy and real-world trading strategies can be much more complex. Also, this code assumes that you have pandas, numpy and yfinance libraries installed in your Python environment.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for desired ticker symbol
def download_data(stock, start_date, end_date):
    data = yf.download(stock, start=start_date, end=end_date)
    return data

# Calculate the short-term simple moving average
def calculate_SMA(data, window):
    sma = data.rolling(window=window).mean()
    return sma

# Create a function to signal when to buy and sell an asset
def generate_signals(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short simple moving average
    signals['short_sma'] = calculate_SMA(data, short_window)

    # Long simple moving average
    signals['long_sma'] = calculate_SMA(data, long_window)

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_sma'][short_window:] 
                                                > signals['long_sma'][short_window:], 1.0, 0.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Download data
data = download_data('AAPL', '2020-01-01', '2021-12-31')

# Generate signals
signals = generate_signals(data['Close'], 50, 200)

# Print signals
print(signals)
```

In this code, we first download the historical data for the desired ticker symbol using the `yfinance` library. We then calculate the short-term and long-term simple moving averages (SMA) for the closing prices. We generate a signal when the short-term SMA crosses above the long-term SMA, and vice versa.

This strategy is known as a moving average crossover strategy and is one of the simplest trading strategies. It is a type of trend-following strategy.

Please note that this is a very basic strategy and real-world trading strategies can be much more complex. Also, this code assumes that you have pandas, numpy and yfinance libraries installed in your Python environment.