Sure, here is a simple implementation of a Relative Strength Index (RSI) strategy generator in Python using the `pandas` and `yfinance` libraries. This strategy buys when the RSI is below 30 (oversold) and sells when the RSI is above 70 (overbought).

Please replace `TICKER` with the actual stock symbol you are interested in.

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# Define the RSI function
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

# Download historical data as dataframe
data = pdr.get_data_yahoo("TICKER", period="1y")

# Compute RSI
data['RSI'] = computeRSI(data['Close'], 14)

# Create signals
data['Buy_Signal'] = (data['RSI'] < 30)
data['Sell_Signal'] = (data['RSI'] > 70)

print(data)
```

This code will print a dataframe with the historical data of the specified ticker, the computed RSI, and two new columns indicating the buy and sell signals. Please note that this is a very basic strategy and should not be used for real trading without further adjustments and testing.