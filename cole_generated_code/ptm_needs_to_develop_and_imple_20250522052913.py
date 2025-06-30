from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a basic structure of a Python code for a simple trading strategy. However, please note that this is a very simplified version of what a real trading strategy might look like. Also, you need to have a good understanding of financial markets and Python programming to develop and implement effective trading strategies.

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
    # Create signals
    data['sma_signal'] = 0.0
    data['ema_signal'] = 0.0
    data['sma_signal'][window:] = np.where(data['sma'][window:] > data['Close'][window:], 1.0, 0.0)
    data['ema_signal'][window:] = np.where(data['ema'][window:] > data['Close'][window:], 1.0, 0.0)

    # Generate trading orders
    data['sma_trading_orders'] = data['sma_signal'].diff()
    data['ema_trading_orders'] = data['ema_signal'].diff()
    return data

# Fetch the data
data = pdr.get_data_yahoo(tickers_list, start="2020-01-01", end="2022-12-31")['Adj Close']

window = 14

# Compute SMA and EMA
data['sma'] = calculate_sma(data, window)
data['ema'] = calculate_ema(data, window)

# Create and implement the trading strategy
trading_data = trading_strategy(data)
print(trading_data)
```

This code fetches historical stock price data for the specified tickers, calculates the Simple Moving Average (SMA) and Exponential Moving Average (EMA) for each stock, and generates trading signals and orders based on these indicators. 

A signal to buy is generated when the price is above the moving average and a signal to sell is generated when the price is below the moving average. The trading orders are the differences between the current and previous signals.

Please note that this is a very basic trading strategy and may not be profitable in real trading. You should always backtest your strategies before implementing them.