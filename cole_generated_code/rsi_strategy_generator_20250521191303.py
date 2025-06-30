from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market.

Here is a simple Python code to generate an RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Download historical data for required stocks
ticker = "AAPL"
yf.pdr_override()
start_date = datetime(2020, 1, 1)
end_date = datetime(2021, 1, 1)
df = pdr.get_data_yahoo(ticker, start_date, end_date)

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

# Design strategy: Buy when RSI < 30 and sell when RSI > 70
df['Buy_Signal'] = np.where(df['RSI'] < 30, 1, 0)
df['Sell_Signal'] = np.where(df['RSI'] > 70, 1, 0)

df[['Close','RSI','Buy_Signal','Sell_Signal']].plot(subplots=True, figsize=(10,8))
plt.show()
```

This script calculates the RSI for the closing price of a given stock (in this case, Apple Inc.) and generates buy signals when the RSI is below 30 (oversold condition) and sell signals when the RSI is above 70 (overbought condition). The signals are then plotted on a graph. 

Please note that this is a very basic trading strategy and should not be used for actual trading without further refinement and risk management.