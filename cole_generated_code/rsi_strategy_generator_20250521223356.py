from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a trading strategy based on RSI:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
from pyti.relative_strength_index import relative_strength_index as rsi

# Download historical data for required stocks
ticker = "AAPL"
ohlcv = yf.download(ticker, datetime.today()-timedelta(365),datetime.today())

def computeRSI (data, time_window):
    diff = data.diff(1).dropna()        # diff in one field(one day)

    #this preservers dimensions off diff values
    up_chg = 0 * diff
    down_chg = 0 * diff
    
    # up change is equal to the positive difference, otherwise equal to zero
    up_chg[diff > 0] = diff[ diff>0 ]
    
    # down change is equal to negative deifference, otherwise equal to zero
    down_chg[diff < 0] = diff[ diff < 0 ]
    
    # check pandas documentation for ewm
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html
    # values are related to exponential decay
    # we set com=time_window-1 so we get decay alpha=1/time_window
    up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    
    rs = abs(up_chg_avg/down_chg_avg)
    rsi = 100 - 100/(1+rs)
    return rsi

ohlcv['RSI'] = computeRSI(ohlcv['Adj Close'], 14)

# Create a strategy: if RSI < 30, buy. If RSI > 70, sell.
ohlcv['Buy_Signal'] = np.where(ohlcv['RSI'] < 30, 1, 0)
ohlcv['Sell_Signal'] = np.where(ohlcv['RSI'] > 70, 1, 0)
```

This code downloads the historical data for a stock (in this case, Apple Inc.), computes the RSI, and generates buy/sell signals based on the RSI. If the RSI is less than 30, it indicates that the stock is oversold and it might be a good time to buy. If the RSI is greater than 70, it indicates that the stock is overbought and it might be a good time to sell.