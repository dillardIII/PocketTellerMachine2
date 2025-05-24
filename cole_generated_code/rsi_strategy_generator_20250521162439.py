To generate a Relative Strength Index (RSI) strategy, we will first require data on which we will calculate the RSI, and then we will decide a strategy based on this RSI. 

To calculate RSI, we will use the `pandas` library which is great for time series analysis, and for data we will use the `yfinance` library to download the stock data.

**Here's the python code to accomplish this task:**

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# Define the ticker symbol
tickerSymbol = 'GOOG'

# Get data on this ticker
tickerData = pdr.get_data_yahoo(tickerSymbol, start='2019-01-01', end='2021-12-31')

# Calculate the RSI
delta = tickerData['Close'].diff()
delta = delta[1:] 
up = delta.clip(lower=0)
down = -1 * delta.clip(upper=0)
ema_up = up.ewm(com=13, adjust=False).mean()
ema_down = down.ewm(com=13, adjust=False).mean()
rs = ema_up/ema_down
tickerData['RSI'] = 100 - (100/(1 + rs))

# RSI Strategy
# If the RSI is less than 30 then the stock is oversold and buy the stock
# If the RSI is higher than 70 then the stock is overbought and sell the stock

tickerData['Buy_Signal'] = (tickerData['RSI'] < 30)
tickerData['Sell_Signal'] = (tickerData['RSI'] > 70)

print(tickerData)
```

This script downloads historical stock prices of Google (GOOG) and computes the RSI. Based on the RSI, it generates two signals - Buy signal and Sell signal. If RSI is higher than 70, it is considered overbought condition and generates a Sell signal. Similarly, if RSI is less than 30, it is considered oversold condition and generates a Buy signal.

This is a rudimentary strategy. For example, it does not account for transaction costs and limit the order quantity. Also, it does not account for existing positions in the portfolio. The Buy/Sell signals are meant to illustrate the use of technical indicators and are not a recommendation to buy or sell securities. Please use this code as a building block for your strategy.