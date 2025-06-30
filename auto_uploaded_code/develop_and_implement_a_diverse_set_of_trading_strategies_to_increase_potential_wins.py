from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code implementing two trading strategies: Moving Average Crossover and Mean Reversion. 

Please note that this is a very basic implementation and real-world trading strategies would require much more sophisticated algorithms, risk management, and data analysis.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', 'SPY']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2000-01-01'
end_date = '2016-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = pdr.get_data_yahoo(tickers, start_date, end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
close = panel_data['Adj Close']

# Moving Average Crossover Strategy
def moving_average_crossover(close, short_window=40, long_window=100):
    signals = pd.DataFrame(index=close.index)
    signals['signal'] = 0.0

    # Create short simple moving average over the short window
    signals['short_mavg'] = close.rolling(window=short_window, min_periods=1, center=False).mean()

    # Create long simple moving average over the long window
    signals['long_mavg'] = close.rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Mean Reversion Strategy
def mean_reversion(close, window=40):
    signals = pd.DataFrame(index=close.index)
    signals['signal'] = 0.0

    # Create moving average and standard deviation over the window
    signals['mavg'] = close.rolling(window=window, min_periods=1, center=False).mean()
    signals['std'] = close.rolling(window=window, min_periods=1, center=False).std()

    # Create signals based on the condition that if the price is 1 standard deviation above the mean, we short, if it's 1 standard deviation below the mean, we long.
    signals['signal'] = np.where(signals['mavg'] - close > signals['std'], 1.0, 0.0)
    signals['signal'] = np.where(signals['mavg'] - close < -signals['std'], -1.0, signals['signal'])

    return signals

# Apply strategies to the data
for ticker in tickers:
    print(f"Moving Average Crossover Strategy for {ticker}:")
    print(moving_average_crossover(close[ticker]))
    print(f"Mean Reversion Strategy for {ticker}:")
    print(mean_reversion(close[ticker]))
```

This code fetches historical data for Apple, Microsoft, and the S&P500 index from Yahoo Finance and applies two trading strategies to this data. 

The Moving Average Crossover strategy generates a long signal when the short-term moving average crosses above the long-term moving average, and a short signal when the short-term moving average crosses below the long-term moving average.

The Mean Reversion strategy generates a long signal when the price is one standard deviation below the mean, and a short signal when the price is one standard deviation