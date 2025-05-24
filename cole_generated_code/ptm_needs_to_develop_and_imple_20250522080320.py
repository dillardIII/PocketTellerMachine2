Sure, I can provide a simple example of a trading strategy using Python. This strategy will be a basic moving average crossover strategy. 

Here's the code:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Collect data on this ticker
df = pdr.get_data_yahoo(tickerSymbol, start="2020-01-01", end="2021-12-31")

# Calculate the short-term exponential moving average (EMA)
ShortEMA = df.Close.ewm(span=12, adjust=False).mean()

# Calculate the long-term exponential moving average (EMA)
LongEMA = df.Close.ewm(span=26, adjust=False).mean()

# Create a new column for the signal
df['Buy_Signal'] = np.where(ShortEMA > LongEMA, 1, 0)

# Create a new column for the positions
df['Position'] = df['Buy_Signal'].diff()

# Print the DataFrame
print(df)
```

In this strategy, we buy when the short-term EMA crosses above the long-term EMA (signaled by a 1 in the 'Position' column), and sell when the short-term EMA crosses below the long-term EMA (signaled by a -1 in the 'Position' column).

Please note that this is a very basic strategy and should not be used for actual trading without further refinement and risk management. Also, this code requires the `pandas_datareader`, `yfinance`, `pandas`, and `numpy` libraries.