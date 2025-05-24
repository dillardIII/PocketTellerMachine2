While I can't write a full trading strategy for you (as it would require knowledge of your current trading strategies, risk tolerance, and other factors), I can provide you with a simple Python code that uses a moving average crossover strategy. This strategy is a common one where a short-term average crosses a long-term average, often used as a signal to buy or sell.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the ticker symbol
tickerSymbol = 'AAPL' # for example

# Get data on this ticker
df = pdr.get_data_yahoo(tickerSymbol, start="2020-01-01", end="2022-12-31")

# Calculate the short-term exponential moving average (EMA)
ShortEMA = df.Close.ewm(span=12, adjust=False).mean() 

# Calculate the long-term EMA
LongEMA = df.Close.ewm(span=26, adjust=False).mean() 

# Calculate the MACD line
MACD = ShortEMA - LongEMA

# Calculate the signal line
signal = MACD.ewm(span=9, adjust=False).mean()

# Create a new column in the dataframe to hold the trading strategy signals
df['Buy_Signal_Price'] = np.where(MACD > signal, df['Close'], np.nan)
df['Sell_Signal_Price'] = np.where(MACD < signal, df['Close'], np.nan)

# Print the dataframe
print(df)
```

This code downloads historical data for a given ticker (in this case, AAPL), calculates the short-term and long-term EMA, calculates the MACD line and the signal line, and then creates a new column in the dataframe to hold the trading signals. If the MACD line is greater than the signal line, it's a buy signal, and if it's less, it's a sell signal.

Please note that this is a very simple trading strategy and may not be suitable for your needs. You should always backtest any new trading strategies before implementing them.