Here is a simple Python code that implements two basic trading strategies: Moving Average Crossover and Mean Reversion. 

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# Fetching historical data
def fetch_data(stock, start, end):
    df = pdr.get_data_yahoo(stock, start, end)
    return df

# Moving Average Crossover Strategy
def moving_average_crossover(df, short_window, long_window):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0.0
    signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)   
    signals['positions'] = signals['signal'].diff()
    return signals

# Mean Reversion Strategy
def mean_reversion(df, window):
    signals = pd.DataFrame(index=df.index)
    signals['distance'] = df['Close'] - df['Close'].rolling(window=window).mean()
    std_dev = df['Close'].rolling(window=window).std()
    signals['signal'] = np.where(signals['distance'] < -std_dev, 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    return signals

# Fetching data
data = fetch_data('AAPL', '2010-01-01', '2020-12-31')

# Implementing strategies
mac_signals = moving_average_crossover(data, 40, 100)
mr_signals = mean_reversion(data, 20)

# Plotting the strategies
plt.figure(figsize=(15,10))
plt.plot(data['Close'], label='Close Price')
plt.plot(mac_signals['short_mavg'], label='40-days SMA')
plt.plot(mac_signals['long_mavg'], label='100-days SMA')
plt.plot(mr_signals['distance'], label='Distance')
plt.title('Apple Stock Price with Trading Signals')
plt.legend()
plt.show()
```

This code fetches historical data for Apple's stock, calculates trading signals for both strategies and plots the results. The Moving Average Crossover strategy generates a trading signal when a short-term moving average crosses a long-term moving average. The Mean Reversion strategy generates a trading signal when the price deviates significantly from the mean.

Please note that these are very basic strategies and may not be profitable in real trading. They are used here for illustrative purposes only. Always backtest your strategies before live trading.