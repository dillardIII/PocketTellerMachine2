The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market.

Here is a simple Python code to generate a trading strategy based on RSI:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Fetching the data
def fetch_data(stock, start, end):
    df = pdr.get_data_yahoo(stock, start, end)
    return df

# Calculating RSI
def computeRSI (data, time_window):
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

# Define the strategy
def RSI_Strategy(df):
    df['RSI'] = computeRSI(df['Adj Close'], 14)
    df['Buy_Signal'] = (df['RSI'] < 30)
    df['Sell_Signal'] = (df['RSI'] > 70)
    return df

# Fetch the data
df = fetch_data('AAPL', '2020-01-01', '2021-12-31')

# Apply the strategy
df = RSI_Strategy(df)
print(df)
```

In this code, we first fetch the data for a given stock (in this case, 'AAPL') for a specified time period. Then we calculate the RSI for the 'Adj Close' prices with a time window of 14 days (which is the most commonly used period). We then generate a 'Buy_Signal' when the RSI is less than 30 (indicating that the stock is oversold) and a 'Sell_Signal' when the RSI is greater than 70 (indicating that the stock is overbought).