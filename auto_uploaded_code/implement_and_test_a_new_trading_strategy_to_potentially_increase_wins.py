from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python code that implements a basic moving average crossover strategy. This strategy is based on the concept that if the short-term average is above the long-term average, it may be a good time to buy, and vice versa.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Download historical data for required stocks
ticker = "AAPL"
ohlcv = pdr.get_data_yahoo(ticker, start="2020-01-01", end="2022-12-31")

# function to calculate SMA
def SMA(data, period=30, column='Close'):
    return data[column].rolling(window=period).mean()

# function to calculate EMA
def EMA(data, period=20, column='Close'):
    return data[column].ewm(span=period, adjust=False).mean()

# create new columns for SMA & EMA
ohlcv['SMA'] = SMA(ohlcv)
ohlcv['EMA'] = EMA(ohlcv)

# function to buy and sell stock (The trading strategy)
def trade(data, buy, sell):
    flag = -1 # flag to track buy or sell
    lastBuy = 0 # to store the price of the last buy order
    x = [] # to store the profit or loss percentage
    
    # loop through the data
    for i in range(len(data)):
        # buy order
        if data[EMA][i] > data[SMA][i] and flag != 1:
            lastBuy = data['Close'][i]
            flag = 1
        # sell order
        if data[EMA][i] < data[SMA][i] and flag != 0:
            flag = 0
            x.append((data['Close'][i] - lastBuy)/lastBuy * 100)
    return x

# call the trading strategy
pnl = trade(ohlcv, 'EMA', 'SMA')

# calculate the total PnL
total_pnl = sum(pnl)
print(f'Total profit/loss: {total_pnl}%')
```

This is a simple trading strategy and may not be profitable in all scenarios. It's important to backtest any strategy before live trading. Also, this script does not take into account trading fees or slippage.