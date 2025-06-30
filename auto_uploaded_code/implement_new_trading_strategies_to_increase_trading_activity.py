from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, let's assume that the trades are executed with respect to a basic moving average crossover strategy which can be implemented as following:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def moving_average_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Create short simple moving average over the short window
    signals['short_mavg'] = calculate_sma(data, short_window)

    # Create long simple moving average over the long window
    signals['long_mavg'] = calculate_sma(data, long_window)

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Fetch data
data = yf.download('AAPL','2016-01-01','2019-08-01')

# Define the short and long windows
short_window = 40
long_window = 100

# Initialize the signals DataFrame
signs = moving_average_strategy(data['Adj Close'], short_window, long_window)

print(signs)
```

Here, the trading strategy is based on the moving average crossover, i.e. the short window moving average crossing above (buy signal) or below (sell signal) the long window moving average.

Please note that you'll have to install 'yfinance' and 'pandas_datareader' Python packages to fetch the data.

Make sure to adjust your short window and long window values accordingly as they ultimately decide how sensitive your trading strategy will be. Also, this is a very basic strategy and real world implementation would require considering other factors as well.