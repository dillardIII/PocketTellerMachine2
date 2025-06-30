from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I will provide a simple Python code to implement and test a few trading strategies using the pandas library. However, please note that this is a simplified example and real-world trading involves more complex factors.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', 'SPY']

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates
start_date = '2017-01-01'
end_date = '2021-12-31'

# Use pandas_datareader.data.DataReader to load the desired data
panel_data = pdr.get_data_yahoo(tickers, start_date, end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
adj_close = panel_data['Adj Close']

# Check the head of the output
print(adj_close.head())

# Simple Moving Average strategy
def SMA_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = data.rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = data.rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Test the strategy with different moving average windows
for ticker in tickers:
    print(f"Testing SMA strategy for {ticker}")
    signals = SMA_strategy(adj_close[ticker], 40, 100)
    print(signals)
```

This script downloads historical data for Apple, Microsoft, and the S&P500 index from Yahoo Finance, and then tests a simple moving average (SMA) trading strategy on each of them. The strategy generates a "buy" signal when the short-term moving average crosses above the long-term moving average, and a "sell" signal when the short-term moving average crosses below the long-term moving average. The effectiveness of the strategy can be evaluated by examining the resulting signals and positions. 

Please note that you need to install the `pandas_datareader` and `yfinance` libraries to run this script. You can install them using pip:

```
pip install pandas_datareader yfinance
```

Also, keep in mind that this is a very basic strategy and doesn't take into account transaction costs, slippage, risk management, or other important factors for a real trading system.