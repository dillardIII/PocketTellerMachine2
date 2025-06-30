from ghost_env import INFURA_KEY, VAULT_ADDRESS
As an AI model, I can provide you with a few basic examples of trading strategies implemented in Python. However, please note that these are simplified examples and real-world trading strategies would require a more comprehensive approach, including data analysis, risk management, and possibly machine learning algorithms.

1. Simple Moving Average Crossover Strategy:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def SMA_strategy(symbol, short_window, long_window):
    # Fetch daily data
    df = web.DataReader(symbol, 'yahoo', start='01/01/2010', end='01/01/2022')
    df['short_SMA'] = df['Close'].rolling(window=short_window).mean()
    df['long_SMA'] = df['Close'].rolling(window=long_window).mean()

    # Create signals
    df['signal'] = 0.0
    df['signal'][short_window:] = np.where(df['short_SMA'][short_window:] 
                                            > df['long_SMA'][short_window:], 1.0, 0.0)   
    df['positions'] = df['signal'].diff()
    return df

# Test the strategy
df = SMA_strategy('AAPL', 50, 200)
```

2. Mean Reversion Strategy:

```python
def mean_reversion_strategy(symbol, window):
    # Fetch daily data
    df = web.DataReader(symbol, 'yahoo', start='01/01/2010', end='01/01/2022')
    df['mean'] = df['Close'].rolling(window=window).mean()
    df['std'] = df['Close'].rolling(window=window).std()
    df['z_score'] = (df['Close'] - df['mean']) / df['std']

    # Create signals
    df['signal'] = np.where(df['z_score'] > 1, 1, 0)
    df['signal'] = np.where(df['z_score'] < -1, -1, df['signal'])
    df['positions'] = df['signal'].diff()
    return df

# Test the strategy
df = mean_reversion_strategy('AAPL', 20)
```

Remember, these are just basic examples and real-world trading involves many other factors. Always backtest your strategies before live trading.