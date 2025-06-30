from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple example of a Python code for a trading strategy. This strategy is called Moving Average Crossover. It's one of the simplest and most widely used strategies in trading.

Please note that this is a very basic example and real-world trading strategies can be much more complex and involve many other factors.

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

def moving_average_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = calculate_sma(data, short_window)
    # Long moving average
    signals['long_mavg'] = calculate_sma(data, long_window)

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Fetch data
data = web.DataReader('AAPL', 'yahoo', start='01/01/2010', end='01/01/2022')

# Use moving average strategy
signals = moving_average_strategy(data['Close'], 40, 100)

print(signals)
```

In this code, we are using the Moving Average Crossover strategy on the closing prices of Apple's stock. The strategy generates a "buy" signal when the short-term moving average crosses above the long-term moving average, and a "sell" signal when the short-term moving average crosses below the long-term moving average.

Please note that you'll need to install `pandas_datareader` library to fetch the data. You can install it using pip:

```bash
pip install pandas_datareader
```

Also, please be aware that trading in the stock market involves risk, and this code is provided as an example and should not be used for real trading without proper knowledge and research.