Sure, here is a simple Python code that implements a basic moving average crossover trading strategy. This strategy is one of the most common systematic trading strategies that uses two moving averages, one short and one long. The strategy goes long when the short moving average crosses above the long moving average and goes short when the short moving average crosses below the long moving average.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Collect data on this ticker
df = pdr.get_data_yahoo(tickerSymbol, start="2020-01-01", end="2021-12-31")

# Calculate the short-term simple moving average
short_sma = df.Close.rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma = df.Close.rolling(window=100).mean()

# Create signals based on crossover
df['signal'] = 0.0
df['signal'][short_sma > long_sma] = 1.0
df['signal'][short_sma < long_sma] = -1.0

# Generate trading orders
df['position'] = df['signal'].diff()

# Print the DataFrame
print(df)

# Plotting
plt.figure(figsize=(10,5))
plt.grid(True)
plt.plot(df['Close'],label='Close Price')
plt.plot(short_sma, label='Short SMA', color='red')
plt.plot(long_sma, label='Long SMA', color='blue')
plt.plot(df.loc[df.position == 1.0].index, 
         short_sma[df.position == 1.0],
         '^', markersize=10, color='g', label='buy')
plt.plot(df.loc[df.position == -1.0].index, 
         short_sma[df.position == -1.0],
         'v', markersize=10, color='r', label='sell')
plt.legend()
plt.show()
```

This is a very basic trading strategy and is meant for illustrative purposes. In practice, trading strategies can be significantly more complex and take into account many other factors.

Please note that this code requires pandas, numpy, matplotlib, pandas_datareader, and yfinance libraries. If these are not installed, you can install them using pip:

```bash
pip install pandas numpy matplotlib pandas_datareader yfinance
```

Also, please remember that investing in the stock market involves risk, and this code does not constitute investment advice.