Sure, I can provide a simple example of a pair trading strategy using Python. This strategy involves finding two stocks that are historically correlated, then trading them when they deviate from their normal correlation.

Please note that this is a simplified example and real-world trading strategies would be much more complex, involving many more factors and sophisticated algorithms.

```python
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the stocks to be used in the pair trading strategy
stock1 = 'AAPL'
stock2 = 'MSFT'

# Download historical data as dataframe
df1 = pdr.get_data_yahoo(stock1, start="2020-01-01", end="2021-12-31")
df2 = pdr.get_data_yahoo(stock2, start="2020-01-01", end="2021-12-31")

# Compute the correlation between the two stocks
correlation = df1['Close'].rolling(60).corr(df2['Close'])

# Compute the 60 day rolling standard deviation of the difference in closing prices
std_deviation = (df1['Close'] - df2['Close']).rolling(60).std()

# Compute the z-score of the difference in closing prices
z_score = (df1['Close'] - df2['Close']) / std_deviation

# Define entry/exit conditions for long & short positions
entry_long = (z_score < -1)
exit_long = (z_score >= 0)
entry_short = (z_score > 1)
exit_short = (z_score <= 0)

# Create signals for long and short positions
num_units_long = np.where(entry_long, 1, 0) + np.where(exit_long, -1, 0)
num_units_short = np.where(entry_short, -1, 0) + np.where(exit_short, 1, 0)

# Combine long and short signals
num_units = num_units_long + num_units_short

# Compute daily portfolio returns
returns = num_units.shift() * (df1['Close'].pct_change() - df2['Close'].pct_change())

# Compute cumulative portfolio returns
cum_returns = (1 + returns).cumprod()

# Plot the cumulative returns
cum_returns.plot()
```

This code will plot the cumulative returns of the pair trading strategy. The strategy goes long when the z-score is less than -1 and goes short when the z-score is greater than 1. It exits positions when the z-score crosses 0.