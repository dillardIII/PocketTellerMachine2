Sure, here's a simple example of a Python code implementing a basic trading strategy. This strategy is called Moving Average Crossover, which is one of the most commonly used strategies in trading. 

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def implement_strategy(data):
    # Calculate the short term exponential moving average
    ShortEMA = calculate_ema(data['Close'], window=12)
    # Calculate the long term exponential moving average
    LongEMA = calculate_ema(data['Close'], window=26)

    # Create signals
    data['Buy_Signal'] = np.where(ShortEMA > LongEMA, 1, 0)
    data['Sell_Signal'] = np.where(ShortEMA < LongEMA, -1, 0)

    return data

# Fetch the data
df = web.DataReader('AAPL', data_source='yahoo', start='01-01-2020', end='01-01-2021')
df = df.reset_index()

# Implement the strategy
df = implement_strategy(df)

# Print the dataframe
print(df)
```

This code fetches the data for Apple Inc. from Yahoo finance. It then calculates the short term and long term exponential moving averages. If the short term average is greater than the long term average, it indicates a buy signal. If the short term average is less than the long term average, it indicates a sell signal.

Please note that this is a very basic strategy and might not be profitable in real trading. It's always recommended to backtest any strategy before using it in live trading. Also, this code does not include any risk management or portfolio optimization techniques.