This task requires a lot of steps and a lot of code, but here is a simplified example of how you could approach it using Python and the pandas library. This example uses a simple moving average crossover strategy, which is a common strategy for stock trading.

```python
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Collect data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end=datetime.now().strftime("%Y-%m-%d"))

# Calculate the short-term simple moving average
tickerDf['SMA_20'] = tickerDf['Close'].rolling(window=20).mean()

# Calculate the long-term simple moving average
tickerDf['SMA_50'] = tickerDf['Close'].rolling(window=50).mean()

# Create a column where 1 indicates the short-term SMA is greater than the long-term SMA
tickerDf['Buy_Signal'] = (tickerDf['SMA_20'] > tickerDf['SMA_50']).astype(int)

# Shift the signals down by one day (as we can only act on signals based on yesterday's data)
tickerDf['Buy_Signal'] = tickerDf['Buy_Signal'].shift()

# Drop the missing values
tickerDf.dropna(inplace=True)

# Calculate the daily returns
tickerDf['Return'] = tickerDf['Close'].pct_change()

# Calculate the strategy return
tickerDf['Strategy_Return'] = tickerDf['Return'] * tickerDf['Buy_Signal']

# Print the last few rows of the DataFrame
print(tickerDf.tail())
```

This code will print out the last few rows of the DataFrame, which includes the close price, the short-term and long-term SMAs, the buy signal, the daily return, and the strategy return. 

Please note that this is a very simplified example and real trading strategies would need to consider many other factors. Also, this does not include the code to actually make trades, as that would require access to a trading API and would involve real money.