The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a trading strategy based on the RSI.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr

# Download historical data for required stocks
ticker = "AAPL"
yf.pdr_override()
df = pdr.get_data_yahoo(ticker, start="2020-01-01", end="2021-12-31")

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

df['RSI'] = computeRSI(df['Close'], 14)

# Trading strategy
# Buy when RSI < 30 (oversold)
# Sell when RSI > 70 (overbought)

df['Buy_Signal'] = np.where(df['RSI'] < 30, 1, 0)
df['Sell_Signal'] = np.where(df['RSI'] > 70, 1, 0)

print(df)
```

This script first downloads the historical data for a specific stock (in this case, Apple Inc.). It then computes the RSI based on the closing prices and a time window of 14 days. Finally, it generates trading signals based on the RSI: a buy signal when the RSI is below 30 (indicating that the stock is oversold) and a sell signal when the RSI is above 70 (indicating that the stock is overbought).