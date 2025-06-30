from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple example of a Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in stock trading. 

Please note that this is a very basic strategy and in real-world trading, you would need more complex strategies that consider multiple factors.

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
    # Calculate the short and long window simple moving average
    sma_short = calculate_sma(data, short_window)
    sma_long = calculate_sma(data, long_window)

    # Create a 'signal' (invested or not invested) data series
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Generate trading signals (long entry)
    signals['signal'][short_window:] = np.where(sma_short[short_window:] > sma_long[short_window:], 1.0, 0.0)

    # Generate trading signals (short entry)
    signals['signal'][short_window:] = np.where(sma_short[short_window:] < sma_long[short_window:], -1.0, signals['signal'])

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Define the stock to be used in the strategy
stock = 'AAPL'

# Get the stock data
data = web.DataReader(stock, 'yahoo', start='01/01/2010', end='01/01/2022')

# Define the short and long window
short_window = 40
long_window = 100

# Run the trading strategy
signals = trading_strategy(data['Close'], short_window, long_window)

print(signals)
```

This code fetches the historical data for a specific stock symbol (in this case, 'AAPL' for Apple Inc.) and calculates the short and long window simple moving averages (SMA). When the short SMA is greater than the long SMA, it generates a buy signal (1.0), and when the short SMA is less than the long SMA, it generates a sell signal (-1.0). The 'positions' column represents the trading orders based on the change in signals.