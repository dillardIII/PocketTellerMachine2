RSI (Relative Strength Index) is a popular technical analysis indicator used in trading. It is used to measure the speed and change of price movements. Here is a simple Python code for generating RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
from pandas_datareader import data as pdr

# Download historical data as dataframe
yf.pdr_override()
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end=datetime.today().strftime('%Y-%m-%d'))

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

# Buy when RSI < 30 and sell when RSI > 70
df['Buy_Signal'] = np.where(df['RSI'] < 30, 1, 0)
df['Sell_Signal'] = np.where(df['RSI'] > 70, 1, 0)

print(df)
```

In this code, we first download the historical data for a specific stock (in this case, AAPL). Then, we compute the RSI based on the closing prices. The RSI is calculated with a time window of 14 days, which is a common choice in trading. Finally, we generate buy and sell signals based on the RSI. If the RSI is below 30, this is considered an oversold condition and generates a buy signal. If the RSI is above 70, this is considered an overbought condition and generates a sell signal.