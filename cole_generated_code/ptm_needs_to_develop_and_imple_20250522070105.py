from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I'll provide a simple example of a trading strategy using Python. This strategy will use a simple moving average crossover strategy, which is a common technique in algorithmic trading. 

Please note that this is a very basic example and real-world trading strategies can be much more complex. Also, it's important to understand that trading in financial markets involves significant risk.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Collect data on this ticker
data = pdr.get_data_yahoo(tickerSymbol, start="2020-01-01", end="2021-12-31")

# Calculate the short-term simple moving average (SMA)
short_sma = data['Close'].rolling(window=20).mean()

# Calculate the long-term SMA
long_sma = data['Close'].rolling(window=100).mean()

# Create a column in the DataFrame to hold the trading signals
data['signal'] = 0.0

# Generate trading signals based on the SMA crossover strategy
data['signal'][short_sma > long_sma] = 1.0

# Calculate the daily returns
data['daily_returns'] = data['Close'].pct_change()

# Calculate the strategy returns
data['strategy_returns'] = data['daily_returns'] * data['signal'].shift()

# Print the DataFrame
print(data)
```

In this code, we first fetch the historical data for a particular stock (in this case, Apple Inc.). Then, we calculate the short-term and long-term simple moving averages (SMA) of the closing prices. A trading signal is generated when the short-term SMA crosses above the long-term SMA. Finally, we calculate the daily and strategy returns.

Please note that you will need to install the `pandas_datareader` and `yfinance` libraries to run this code. You can install them using pip:

```
pip install pandas_datareader yfinance
```