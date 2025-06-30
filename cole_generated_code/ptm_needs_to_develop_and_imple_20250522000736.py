from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a trading strategy using Python. This strategy is based on moving averages, a common indicator used in trading. 

Please note that this is a very basic strategy and is not recommended for actual trading. It's just an example to illustrate how a trading strategy might be implemented in Python.

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
    # Calculate SMA and EMA
    data['SMA'] = calculate_sma(data['Close'], 14)
    data['EMA'] = calculate_ema(data['Close'], 14)

    # Create a column 'Signal' such that if EMA is greater than SMA then buy else sell
    data['Signal'] = np.where(data['EMA'] > data['SMA'], 'Buy', 'Sell')

    return data

# Fetch the data
for ticker in tickers_list:
    data = pdr.get_data_yahoo(ticker, start="2020-01-01", end="2022-12-31")
    data = trading_strategy(data)
    print(f"Data for {ticker} from 2020 to 2022")
    print(data)
```

This script fetches historical data for a list of tickers using the Yahoo Finance API. It then calculates the Simple Moving Average (SMA) and Exponential Moving Average (EMA) for each ticker. If the EMA is greater than the SMA, it generates a 'Buy' signal; otherwise, it generates a 'Sell' signal.

Please note that you need to install the `pandas_datareader` and `yfinance` libraries to run this script. You can install them using pip:

```
pip install pandas_datareader yfinance
```