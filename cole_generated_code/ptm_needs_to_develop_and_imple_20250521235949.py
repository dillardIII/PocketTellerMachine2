Sure, I can provide a simple example of a trading strategy using Python. This strategy is based on moving averages. Please note that this is a simplified example and real-world trading strategies are much more complex and take into account many more factors.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the ticker list
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Fetch the data
data = pdr.get_data_yahoo(tickers_list, start="2017-01-01", end="2021-12-31")['Adj Close']

# Print first 5 rows of the data
print(data.head())

# Calculate the 20 days moving averages of the closing prices
short_rolling = data.rolling(window=20).mean()

# Calculate the 200 days moving averages of the closing prices
long_rolling = data.rolling(window=200).mean()

# Create a 'signals' DataFrame with the `sign` of the difference of short and long window
signals = pd.DataFrame(index=data.index)
for ticker in tickers_list:
    signals[ticker] = np.sign(short_rolling[ticker] - long_rolling[ticker])

# Print `signals`
print(signals)

# Create a 'positions' DataFrame
positions = signals.shift()

# Fill NaN values
positions.fillna(0, inplace=True)

# Print `positions`
print(positions)

# Calculate daily portfolio returns
returns = data.pct_change() * positions.shift()

# Print `returns`
print(returns)

# Calculate cumulative portfolio returns
cumulative_returns = (1 + returns).cumprod()

# Print `cumulative_returns`
print(cumulative_returns)
```

In this code, we first fetch the data for some selected tickers. Then, we calculate the 20 days and 200 days moving averages of the closing prices. If the short moving average is above the long moving average, we take a long position (buy), and if it's below, we take a short position (sell). We then calculate the daily and cumulative portfolio returns based on these positions.

Please note that this is a very simple strategy and doesn't take into account transaction costs, slippage, risk management, etc. Also, past performance is not indicative of future results.