Sure, I can provide a simple example of a Python code that could be used to develop and implement trading strategies. However, please note that this is a very basic example and actual trading strategies can be very complex, involving advanced algorithms and machine learning techniques.

```python
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Define the instruments to download
tickers = ['AAPL', 'MSFT', 'GOOGL']

# Define the online source to be used
data_source = 'yahoo'

# Define the start and end dates
start_date = '2017-01-01'
end_date = '2022-12-31'

# Use pandas_datareader to load the desired data
panel_data = pdr.get_data_yahoo(tickers, start_date, end_date)

# Calculate simple moving average
def SMA(data, window):
    sma = data.rolling(window = window).mean()
    return sma

# Calculate exponential moving average
def EMA(data, window):
    ema = data.ewm(span = window).mean()
    return ema

# Define a signal for trading strategy
def generate_signals(data):
    # Create a 'signals' DataFrame with signal information
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Create short simple moving average over short window
    signals['short_mavg'] = SMA(data['Close'], window=20)

    # Create long simple moving average over long window
    signals['long_mavg'] = SMA(data['Close'], window=100)

    # Create signals
    signals['signal'][20:] = np.where(signals['short_mavg'][20:] > signals['long_mavg'][20:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Implement the trading strategy for each ticker
for ticker in tickers:
    data = panel_data['Adj Close'][ticker]
    signals = generate_signals(data)
    print(f"Trading signals for {ticker}:")
    print(signals)
```

This code will generate trading signals based on a simple moving average (SMA) crossover strategy. When the short-term average is above the long-term average, it generates a buy signal, and when the short-term average is below the long-term average, it generates a sell signal.