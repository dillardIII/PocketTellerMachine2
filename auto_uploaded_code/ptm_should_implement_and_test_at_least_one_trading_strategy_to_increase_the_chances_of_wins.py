from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that implements a basic moving average crossover strategy. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy. When the short moving average crosses below the long moving average, it's a signal to sell.

Please note that this is a very basic strategy and may not always result in wins. It's always recommended to use more complex strategies and consider more factors for actual trading.

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

def implement_strategy(data):
    # Calculate short-term simple moving average
    sma_short = calculate_sma(data['Close'], window=20)
    # Calculate long-term simple moving average
    sma_long = calculate_sma(data['Close'], window=50)

    # Create a column 'Signal' such that if 20-day SMA is greater than 50-day SMA then Signal is 1, else it's 0.
    data['Signal'] = 0.0  
    data['Signal'] = np.where(sma_short > sma_long, 1.0, 0.0)

    # Create a column 'Position' which is a day-to-day difference of the 'Signal' column
    data['Position'] = data['Signal'].diff()

def test_strategy(data):
    # Fetch data
    data = pdr.get_data_yahoo('AAPL', start='2020-01-01', end='2021-12-31')
    implement_strategy(data)

    # Plotting
    import matplotlib.pyplot as plt
    plt.figure(figsize=(20,10))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(sma_short, label='20-day SMA', color='red')
    plt.plot(sma_long, label='50-day SMA', color='green')
    plt.plot(data.loc[data['Position'] == 1.0].index, 
             data['Close'][data['Position'] == 1.0], 
             '^', markersize=10, color='m', label='buy')
    plt.plot(data.loc[data['Position'] == -1.0].index, 
             data['Close'][data['Position'] == -1.0], 
             'v', markersize=10, color='k', label='sell')
    plt.title('Apple Inc. - Moving Average Crossover Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

test_strategy('AAPL')
```

This script fetches the historical data for Apple Inc. ('AAPL') from Yahoo Finance, calculates the short-term (20-day) and long-term (50-day) simple moving averages (SMA), and generates trading signals based on the crossover of these SMAs. It also plots the closing price, SMAs, and trading signals for visualization.