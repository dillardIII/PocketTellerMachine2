from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, below is a simple Python code that implements and tests two trading strategies: Moving Average Crossover and Mean Reversion.

Please note that this is a basic implementation and should run with appropriate trading data.

``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Strategy 1: Moving Average Crossover
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

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()
    
    return signals

# Strategy 2: Mean Reversion
def mean_reversion(data, window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    
    # Calculate mean and standard deviation
    signals['mean'] = data['Close'].rolling(window=window, min_periods=1, center=False).mean()
    signals['std'] = data['Close'].rolling(window=window, min_periods=1, center=False).std()
    
    # Create signals
    signals['signal'] = np.where(data['Close'] > signals['mean'] + 2*signals['std'], 1.0, 0.0)
    signals['signal'] = np.where(data['Close'] < signals['mean'] - 2*signals['std'], -1.0, signals['signal']) 

    return signals

# Assume 'data' is a DataFrame that contains trading data, with 'Close' prices.

# Implementing Moving Average Crossover strategy with short window = 40 and long window = 100
mac_signals = moving_average_crossover(data, 40, 100)

# Implementing Mean Reversion strategy with window = 20
mr_signals = mean_reversion(data, 20)

# Test the strategies by plotting the 'Close' prices and the trading signals 
plt.figure(figsize=(12,5))
plt.title('Moving Average Crossover & Mean Reversion')
plt.plot(data['Close'], color='blue', label='Close')
plt.plot(mac_signals['short_mavg'], color='red', linestyle='--', label='MA short')
plt.plot(mac_signals['long_mavg'], color='green', linestyle='--', label='MA long')
plt.plot(mr_signals['mean'], color='purple', linestyle='--', label='Mean')
plt.plot(mr_signals['mean'] + 2* signals['std'], color='pink', linestyle='--', label='Mean + 2sd')
plt.plot(mr_signals['mean'] - 2* signals['std'], color='yellow', linestyle='--', label='Mean - 2sd')
plt.legend()
plt.show()
```

This code assumes that short-term moving averages crossing above long-term ones is a buy signal, while the opposite is a sell signal. For mean reversion, prices more than 2 standard deviations above the mean are sold (betting they will fall toward the mean), while those more than 2 standard deviations below the mean are bought (betting they will rise toward the mean).