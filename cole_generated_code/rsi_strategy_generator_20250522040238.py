The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here's a simple Python code to generate a trading strategy based on RSI:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from ta.momentum import RSIIndicator

def compute_RSI(data, time_window):
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

def RSI_Strategy(data):
    # Calculate RSI
    data['RSI'] = compute_RSI(data['Close'], 14)

    # Create signals
    data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0) # Oversold level
    data['Sell_Signal'] = np.where((data['RSI'] > 70), 1, 0) # Overbought level

    return data

# Download historical data as dataframe
data = yf.download('AAPL','2020-01-01','2022-12-31')

# Generate RSI strategy
RSI_Strategy(data)
```

This script will generate a trading strategy for Apple Inc. (AAPL) stock. It will buy when the RSI is below 30 (oversold) and sell when the RSI is above 70 (overbought). Please note that this is a very simplistic strategy and may not be profitable in real trading. Always backtest your strategies before using them in live trading.