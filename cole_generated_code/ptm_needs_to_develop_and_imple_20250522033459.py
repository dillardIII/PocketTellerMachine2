from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here's a simple Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is commonly used in trading, where you buy when a short-term moving average crosses above a long-term moving average, and sell when the opposite happens.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    sma_short = calculate_sma(data, short_window)
    sma_long = calculate_sma(data, long_window)

    # Create a 'signals' DataFrame with signal values
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Generate trading signals (buy=1 , sell=-1)
    signals['signal'][short_window:] = np.where(sma_short[short_window:] > sma_long[short_window:], 1.0, -1.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Fetch the data
start_date = '2010-01-01'
end_date = '2020-12-31'
data = web.DataReader('AAPL', 'yahoo', start_date, end_date)

# Implement the strategy
short_window = 40
long_window = 100
signals = trading_strategy(data['Close'], short_window, long_window)

# Plot the results
plt.figure(figsize=(10,5))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(calculate_sma(data['Close'], short_window), label=f'SMA {short_window}', color='red', linestyle='--')
plt.plot(calculate_sma(data['Close'], long_window), label=f'SMA {long_window}', color='green', linestyle='--')
plt.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], '^', markersize=10, color='m')
plt.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 'v', markersize=10, color='k')
plt.title('AAPL SMA Crossover Trading Signals')
plt.ylabel('Price')
plt.xlabel('Date')
plt.legend(loc='best')
plt.grid(True)
plt.show()
```

Please note that this is a very basic trading strategy and should be used for educational purposes only. Real-world trading involves many more factors and complexities. Also, you need to install pandas, pandas_datareader, numpy, and matplotlib libraries to run this code.