from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought and oversold conditions in a market. Here is a simple Python code to generate a trading strategy based on the RSI.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr

# Download historical data for required stocks
ticker = "AAPL"
yf.pdr_override()
df = pdr.get_data_yahoo(ticker, start="2020-01-01", end="2021-12-31")

def calculate_RSI(data, time_window):
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

df['RSI'] = calculate_RSI(df['Close'], 14)

# Create a column in the DataFrame showing "TRUE" if sell entry signal is given and "FALSE" otherwise. 
# A sell is initiated when the RSI crosses above 70
df['Sell Entry'] = ((df['RSI'] < 70) & (df['RSI'].shift(1) > 70)) 

# Create a column in the DataFrame showing "TRUE" if buy entry signal is given and "FALSE" otherwise. 
# A buy is initiated when the RSI crosses below 30
df['Buy Entry'] = ((df['RSI'] > 30) & (df['RSI'].shift(1) < 30)) 

print(df)
```

This code calculates the RSI based on the closing price of the stock and generates buy and sell signals based on the RSI. A buy signal is generated when the RSI crosses below 30 (oversold condition) and a sell signal is generated when the RSI crosses above 70 (overbought condition). Please note that this is a very basic strategy and should not be used for live trading without further optimization.