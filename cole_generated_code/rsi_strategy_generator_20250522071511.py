from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code to generate a RSI (Relative Strength Index) strategy. This strategy is used in technical analysis in trading to measure the speed and change of price movements.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def calculate_rsi(data, time_window):
    diff = data.diff(1).dropna()        
    up_chg = 0 * diff
    down_chg = 0 * diff
    up_chg[diff > 0] = diff[ diff>0 ]
    down_chg[diff < 0] = diff[ diff < 0 ]
    up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    rs = abs(up_chg_avg/down_chg_avg)
    rsi = 100 - 100/(1+rs)
    return rsi

def rsi_strategy(data, rsi_period=14, rsi_upper=70, rsi_lower=30):
    data['RSI'] = calculate_rsi(data['Close'], rsi_period)
    data['Buy_Signal'] = (data['RSI'] < rsi_lower)
    data['Sell_Signal'] = (data['RSI'] > rsi_upper)
    return data

# Fetching data
df = web.DataReader('AAPL', 'yahoo', start='01-01-2019', end='31-12-2019')

# Applying RSI strategy
df = rsi_strategy(df)
print(df)
```

This code fetches historical data for Apple Inc. from Yahoo Finance. It calculates the RSI for the closing prices and generates buy signals when the RSI is less than 30 and sell signals when the RSI is greater than 70. 

Please note that this is a very basic strategy and might not be profitable in real trading. Always backtest your strategies before using them in live trading.