from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple implementation of two trading strategies using Python. We'll use the `pandas_datareader` library to fetch historical stock data from Yahoo Finance, and `pandas` to handle the data. The two strategies we'll implement are:

1. Moving Average Crossover Strategy: This strategy is based on the idea that a short-term moving average crossing above a long-term moving average is a buy signal, and vice versa.

2. Mean Reversion Strategy: This strategy assumes that prices will revert to their mean over time. If a stock price is significantly above its mean, it's a sell signal, and if it's significantly below its mean, it's a buy signal.

```python
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

# Fetch historical data
start = datetime(2020, 1, 1)
end = datetime(2021, 12, 31)
data = pdr.get_data_yahoo('AAPL', start, end)

# Moving Average Crossover Strategy
def moving_average_crossover(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   
    signals['positions'] = signals['signal'].diff()

    return signals

# Mean Reversion Strategy
def mean_reversion(data, window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Calculate mean and standard deviation
    signals['mean'] = data['Close'].rolling(window=window, min_periods=1, center=False).mean()
    signals['std'] = data['Close'].rolling(window=window, min_periods=1, center=False).std()

    # Create signals
    signals['signal'] = np.where(data['Close'] < (signals['mean'] - 1.5*signals['std']), 1.0, 0.0)
    signals['signal'] = np.where(data['Close'] > (signals['mean'] + 1.5*signals['std']), -1.0, signals['signal'])
    signals['positions'] = signals['signal'].diff()

    return signals

# Test the strategies
mac_signals = moving_average_crossover(data, 20, 100)
mr_signals = mean_reversion(data, 20)

print(mac_signals)
print(mr_signals)
```

Please note that these are very basic implementations of these strategies and real-world trading systems would be much more complex. Also, this code doesn't take into account trading costs or slippage. Always backtest your strategies before live trading.