The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a basic RSI trading strategy.

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Download historical data for required stocks
ticker = "AAPL"
yf.pdr_override()
df = pdr.get_data_yahoo(ticker, start="2020-01-01", end=datetime.now())

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

# Create a plot
plt.figure(figsize=(12,5))
plt.title('RSI plot over time')
plt.plot(df.index, df['RSI'])
plt.axhline(0, linestyle='--', alpha=0.5, color='#ff0080')
plt.axhline(10, linestyle='--', alpha=0.5, color='#2E8B57')
plt.axhline(20, linestyle='--', alpha=0.5, color='#2E8B57')
plt.axhline(30, linestyle='--', alpha=0.5, color='#2E8B57')
plt.axhline(70, linestyle='--', alpha=0.5, color='#2E8B57')
plt.axhline(80, linestyle='--', alpha=0.5, color='#2E8B57')
plt.axhline(90, linestyle='--', alpha=0.5, color='#2E8B57')
plt.axhline(100, linestyle='--', alpha=0.5, color='#ff0080')
plt.fill_between(df.index, df['RSI'], 30, where=(df['RSI'] <= 30), color='C1', alpha=0.1)
plt.fill_between(df.index, df['RSI'], 70, where=(df['RSI'] >= 70), color='C1', alpha=0.1)
plt.ylabel('RSI Values')
plt.show()
```

This script fetches the historical data for the specified ticker symbol (in this case, Apple Inc.), calculates the RSI, and then plots it over time. The horizontal lines at 30 and 70 are typically used as signals to buy (when the RSI is below 30) or sell (when the R