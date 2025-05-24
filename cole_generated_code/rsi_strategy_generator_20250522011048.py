Sure, Here is a simple implementation of the RSI (Relative Strength Index) strategy generator in Python using the pandas library for data manipulation and the yfinance library to download the stock data.

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# Download historical data as dataframe
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

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

print(df)
```

This code will calculate the RSI for the stock symbol "AAPL" for the years 2020 and 2021. The RSI is calculated over a period of 14 days, which is the most commonly used period for this indicator. The RSI values are then added to the dataframe.

Please note that you need to install yfinance and pandas_datareader libraries if you haven't already. You can install them using pip:

```python
pip install yfinance pandas_datareader
```

Also, please replace "AAPL" with the symbol of the stock you want to analyze.