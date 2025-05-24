Sure, I'll provide you with a simple Python code that implements a basic trading strategy. This strategy is called Moving Average Crossover. It's a popular strategy used in algorithmic trading. 

Please note that this is a very basic strategy and may not yield profitable results. It's always recommended to use more sophisticated strategies and also consider transaction costs, slippage, etc.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the ticker list
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data):
    # Create a 'signals' DataFrame with signal information
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Create short simple moving average over the short window
    signals['short_mavg'] = calculate_sma(data, window=20)

    # Create long simple moving average over the long window
    signals['long_mavg'] = calculate_sma(data, window=100)

    # Create signals
    signals['signal'][20:] = np.where(signals['short_mavg'][20:] > signals['long_mavg'][20:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Fetch the data
for ticker in tickers_list:
    data = pdr.get_data_yahoo(ticker, start="2020-01-01", end="2022-12-31")
    signals = trading_strategy(data['Close'])
    print(f"Signals for {ticker}")
    print(signals)
```

This Python code uses Yahoo Finance to fetch the stock price data, calculates the short-term (20 days) and long-term (100 days) moving averages, and generates trading signals based on the crossover of these moving averages. A buy signal is generated when the short-term average crosses above the long-term average, and a sell signal is generated when the short-term average crosses below the long-term average.