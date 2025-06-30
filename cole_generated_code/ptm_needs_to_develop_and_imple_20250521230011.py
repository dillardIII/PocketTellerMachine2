from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy using Python. This strategy will be a simple Moving Average Crossover strategy. This strategy is a trend-following strategy that is based on the crossover of two moving averages of different lengths.

Please note that this is a very basic strategy and real-world trading strategies can be much more complex and involve many other factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Download historical data (monthly) for DJI constituent stocks
tickers = ["AAPL","MSFT","JPM","V","PG","JNJ","WMT","MA","INTC","VZ"]

all_data = {}
for ticker in tickers:
    all_data[ticker] = pdr.get_data_yahoo(ticker, start="2000-01-01", end="2010-12-31")

# Calculate 6-month SMA for all stocks
for ticker in tickers:
    all_data[ticker]["SMA_6"] = all_data[ticker]["Adj Close"].rolling(window=6).mean()

# Calculate 12-month SMA for all stocks
for ticker in tickers:
    all_data[ticker]["SMA_12"] = all_data[ticker]["Adj Close"].rolling(window=12).mean()

# Create a DataFrame to store the trading strategy signals
signals = pd.DataFrame(index=all_data["AAPL"].index)
for ticker in tickers:
    signals[ticker] = np.where(all_data[ticker]["SMA_6"] > all_data[ticker]["SMA_12"], 1.0, 0.0)

# Create a DataFrame to store the trading strategy returns
returns = pd.DataFrame(index=all_data["AAPL"].index)
for ticker in tickers:
    returns[ticker] = all_data[ticker]["Adj Close"].pct_change() * signals[ticker].shift()

# Plot the strategy returns
(returns+1).cumprod().plot()
plt.show()
```

This script first downloads historical data for a few stocks. It then calculates 6-month and 12-month Simple Moving Averages (SMA) for these stocks. A signal to buy a stock is generated when its 6-month SMA is greater than its 12-month SMA. The script then calculates the returns for this strategy and plots the cumulative returns.

Please note that this script requires the `pandas_datareader` package to download data from Yahoo Finance. You can install it using pip:

```bash
pip install pandas-datareader
```

Also, this script does not take into account transaction costs and other factors that could affect the performance of a trading strategy in a real-world scenario.