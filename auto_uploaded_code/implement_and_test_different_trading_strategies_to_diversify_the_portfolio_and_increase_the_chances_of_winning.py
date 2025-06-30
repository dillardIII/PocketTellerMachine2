from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I'll provide a simple example of two trading strategies in Python: Moving Average Crossover and Mean Reversion. Please note that this is a simplified version and real-world trading strategies are much more complex and require a deep understanding of financial markets.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Fetching data
def fetch_data(stock, start, end):
    df = pdr.get_data_yahoo(stock, start, end)
    return df

# Moving Average Crossover
def moving_average_crossover(df, short_window, long_window):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Mean Reversion
def mean_reversion(df, window):
    signals = pd.DataFrame(index=df.index)
    signals['distance'] = 0.0

    # Calculate z-score
    signals['z_score'] = (df['Close'] - df['Close'].rolling(window=window).mean()) / df['Close'].rolling(window=window).std()

    # Create signals
    signals['distance'][window:] = np.where(signals['z_score'][window:] > 1, 1.0, 0.0)
    signals['distance'][window:] = np.where(signals['z_score'][window:] < -1, -1.0, signals['distance'])

    # Generate trading orders
    signals['positions'] = signals['distance'].diff()

    return signals

# Fetch data
df = fetch_data('AAPL', '2010-01-01', '2020-12-31')

# Implement Moving Average Crossover
mac_signals = moving_average_crossover(df, 40, 100)

# Implement Mean Reversion
mr_signals = mean_reversion(df, 30)

# Plotting
plt.figure(figsize=(15,10))
plt.plot(df['Close'], label='Close Price')
plt.plot(mac_signals['short_mavg'], label='40-days SMA')
plt.plot(mac_signals['long_mavg'], label='100-days SMA')
plt.plot(mr_signals['z_score'], label='Z-Score')
plt.title('AAPL Close Prices & Trading Signals')
plt.legend()
plt.show()
```

This code implements two trading strategies: Moving Average Crossover and Mean Reversion. It fetches historical data for Apple Inc. (AAPL) from Yahoo Finance, calculates trading signals, and plots the close prices along with the trading signals.

Please note that this is a simple example and doesn't include transaction costs, slippage, risk management, or other important factors for a real trading strategy. Also, using this code in real trading requires a thorough understanding of financial markets and Python programming.