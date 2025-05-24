Sure, here's a simple example of a trading strategy using Python. This strategy is based on moving averages, a common indicator used in technical analysis. The strategy buys when the short-term moving average crosses above the long-term moving average and sells when the short-term moving average crosses below the long-term moving average.

Please note that this is a simple example and real trading strategies can be much more complex. Also, trading in financial markets involves risk, and this code is provided for educational purposes only. It should not be used for real trading without further improvements and testing.

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
    # Calculate the short and long-term moving averages
    sma_short = calculate_sma(data, short_window)
    sma_long = calculate_sma(data, long_window)

    # Create a 'signal' (invested or not invested) data series
    signal = pd.Series(index=data.index)
    signal[short_window:] = np.where(sma_short[short_window:] > sma_long[short_window:], 1.0, 0.0)   

    # Generate trading orders
    orders = signal.diff()

    return orders

# Define the stock to be used
stock = 'AAPL'

# Define the online source to be used
data_source = 'yahoo'

# Define the start and end dates
start_date = '2010-01-01'
end_date = '2020-12-31'

# Use pandas_datareader.data.DataReader to load the desired data
data = web.DataReader(stock, data_source, start_date, end_date)

# Use adjusted closing prices for the analysis
data = data['Adj Close']

# Define the short and long moving average windows
short_window = 40
long_window = 100

# Generate trading signals
orders = trading_strategy(data, short_window, long_window)

# Print the resulting DataFrame
print(orders)
```

This code will print a series of 1.0, -1.0, and 0.0 values, representing buy, sell, and hold signals, respectively.