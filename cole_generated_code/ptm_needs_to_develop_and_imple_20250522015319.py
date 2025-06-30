from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy using Python. Here we will use a simple moving average crossover strategy. This strategy buys/sells when a short-term moving average crosses a long-term moving average. 

Please note that this is a very basic strategy and should be used for educational purposes only. Real-world trading involves many more factors.

```python
import pandas as pd
import numpy as np
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

    # Create a 'signals' DataFrame with the signal information
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Generate trading signals (1 for buy, -1 for sell)
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

# Print the signals
print(signals)
```

This script fetches historical stock price data for Apple Inc. from Yahoo Finance, calculates the 40-day and 100-day simple moving averages (SMA), and generates trading signals based on the crossover of these SMAs. The 'positions' column in the 'signals' DataFrame indicates the trading orders: a 1 means buy and a -1 means sell.