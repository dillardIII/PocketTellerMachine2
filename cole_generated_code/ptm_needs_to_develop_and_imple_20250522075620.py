from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is often used in stock trading where you buy/sell when short-term average crosses the long-term average.

Please note that this is a simple example and real-world trading strategies can be much more complex and involve many other factors.

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
    short_sma = calculate_sma(data, short_window)
    long_sma = calculate_sma(data, long_window)

    # Create a 'signals' DataFrame with the signal information
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Generate trading signals based on the crossover strategy
    signals['signal'][short_window:] = np.where(short_sma[short_window:] > long_sma[short_window:], 1.0, 0.0)

    # Generate trading orders based on the signals
    signals['positions'] = signals['signal'].diff()

    return signals

# Define the stock symbol and the data range
symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'

# Get the stock data
data = web.DataReader(symbol, 'yahoo', start_date, end_date)

# Implement the trading strategy
signals = trading_strategy(data['Close'], 50, 200)

# Print the signals
print(signals)
```

In this code, we first calculate the short and long window simple moving averages (SMA). Then we create a 'signals' DataFrame to store the trading signals. We generate the trading signals based on the crossover strategy: if the short-term SMA is greater than the long-term SMA, we generate a 'buy' signal (1.0), otherwise we generate a 'sell' signal (0.0). Finally, we generate trading orders based on the signals: a positive difference means a 'buy' order and a negative difference means a 'sell' order.