Sure, here is a simple Python code for a Mean Reversion trading strategy. This strategy assumes that the price of a stock will revert to its mean or average price over time. If the stock price is below the mean, it's a good time to buy. If it's above the mean, it's a good time to sell.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the stock symbol
symbol = 'AAPL'

# Get the stock data
df = pdr.get_data_yahoo(symbol, start="2020-01-01", end="2021-12-31")

# Calculate the mean of the close prices
mean_close = df['Close'].mean()

# Calculate the standard deviation of the close prices
std_close = df['Close'].std()

# Define an empty DataFrame for the signals
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0

# Generate trading signals based on the mean reversion strategy
signals['signal'][df['Close'] < mean_close - std_close] = 1.0
signals['signal'][df['Close'] > mean_close + std_close] = -1.0

# Print the signals
print(signals)
```

This code will print a DataFrame with trading signals. A signal of 1.0 means it's a good time to buy the stock, and a signal of -1.0 means it's a good time to sell the stock.

Please note that this is a very basic trading strategy and may not be profitable in real trading. It's recommended to use more sophisticated strategies and consider more factors, such as volume, momentum, and other technical indicators. Also, always backtest your strategies before using them in real trading.