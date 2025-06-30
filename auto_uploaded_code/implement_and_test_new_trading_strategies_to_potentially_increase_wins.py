from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy using Python. This strategy is called Moving Average Crossover. It's a very basic strategy that involves buying when the short term moving average crosses above the long term moving average and selling when the short term moving average crosses below the long term moving average.

Please note that this is a very simplified strategy and real-world trading involves many more factors.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    sma = calculate_sma(data, short_window)
    ema = calculate_ema(data, long_window)

    buying_signals = []
    selling_signals = []

    for i in range(1, len(data)):
        if sma[i] > ema[i] and sma[i - 1] < ema[i - 1]:
            buying_signals.append(data[i])
            selling_signals.append(np.nan)
        elif sma[i] < ema[i] and sma[i - 1] > ema[i - 1]:
            selling_signals.append(data[i])
            buying_signals.append(np.nan)
        else:
            buying_signals.append(np.nan)
            selling_signals.append(np.nan)

    return buying_signals, selling_signals

# Test the strategy with historical data
data = web.DataReader('AAPL', 'yahoo', start='01-01-2020', end='12-31-2020')['Close']
buying_signals, selling_signals = trading_strategy(data, 50, 200)

# Print results
print("Buying signals: ", buying_signals)
print("Selling signals: ", selling_signals)
```

This script will print out the buying and selling signals for the Apple stock during the year 2020. Please replace 'AAPL' with the ticker symbol of the stock you want to test. Also, you can adjust the short_window and long_window parameters to test different strategies.