The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a trading strategy based on RSI.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from ta.momentum import RSIIndicator

# Download historical data for required stocks
ticker = "AAPL"
df = yf.download(ticker, start="2020-01-01", end="2021-12-31")

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

# Create a buy signal when RSI is oversold (below 30)
df['Buy_Signal'] = np.where(df['RSI'] < 30, 1, 0)

# Create a sell signal when RSI is overbought (above 70)
df['Sell_Signal'] = np.where(df['RSI'] > 70, 1, 0)

print(df)
```

This script downloads the historical data for a specific stock (in this case, Apple Inc.), calculates the RSI for a 14-day period (which is the most commonly used period), and generates buy and sell signals based on the RSI. The signals are added as new columns in the dataframe. The buy signal is set to 1 when the RSI is below 30 (indicating that the stock is oversold), and the sell signal is set to 1 when the RSI is above 70 (indicating that the stock is overbought).