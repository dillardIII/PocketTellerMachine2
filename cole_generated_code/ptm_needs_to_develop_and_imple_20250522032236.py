from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a Python code for a basic trading strategy using moving average crossover. This strategy is one of the most common systematic trading strategies that uses two moving averages, one short-term (fast) and one long-term (slow). When the fast moving average crosses above the slow moving average, it generates a buy signal. Conversely, when the fast moving average crosses below the slow moving average, it generates a sell signal.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

# Define the ticker list
tickers = ['AAPL', 'GOOG', 'MSFT']

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = calculate_sma(data, short_window)

    # Long moving average
    signals['long_mavg'] = calculate_sma(data, long_window)

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Get the data
data = {}
for ticker in tickers:
    data[ticker] = web.DataReader(ticker, 'yahoo', start='01/01/2010', end='01/01/2022')

# Apply the strategy
for ticker in tickers:
    signals = trading_strategy(data[ticker]['Close'], 50, 200)
    print(f"Trading signals for {ticker}:")
    print(signals)
```

Please note that this is a simple example and real trading strategies involve much more considerations and complex algorithms. Also, this code requires the pandas, numpy and pandas_datareader libraries. If you don't have these libraries installed, you can install them using pip:

```bash
pip install pandas numpy pandas_datareader
```

Also, please replace '01/01/2010' and '01/01/2022' with the actual start and end dates you want to use.