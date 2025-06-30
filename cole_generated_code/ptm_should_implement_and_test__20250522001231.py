from ghost_env import INFURA_KEY, VAULT_ADDRESS
In order to implement and test new trading strategies, we first need to define what our trading strategy will be. For simplicity, let's implement a simple moving average crossover strategy. This strategy will buy when the short-term moving average crosses above the long-term moving average, and sell when the short-term moving average crosses below the long-term moving average.

Here is a simple implementation in Python using pandas:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_lma(data, window):
    lma = data.rolling(window=window).mean()
    return lma

def implement_strategy(data, short_window, long_window):
    # Calculate short term and long term moving averages
    sma = calculate_sma(data, short_window)
    lma = calculate_lma(data, long_window)

    # Create a 'signals' DataFrame with signal information
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Generate trading signals based on moving averages
    signals['signal'][short_window:] = np.where(sma[short_window:] > lma[short_window:], 1.0, 0.0)

    # Generate trading orders based on signals
    signals['positions'] = signals['signal'].diff()

    return signals

# Load data
data = web.DataReader('AAPL', 'yahoo', start='01/01/2010', end='01/01/2022')

# Implement strategy
signals = implement_strategy(data['Close'], 50, 200)

# Print resulting signals
print(signals)
```

This code will print a DataFrame with trading signals for each day. A positive value in the 'positions' column means a buy order, and a negative value means a sell order.

Please note that this is a very basic strategy and should not be used for real trading without further improvements and risk management. It also does not take into account trading fees or other costs.