from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here's a simple Python code that uses a moving average crossover strategy. This strategy is one of the most common systematic trading strategies that uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it means that recent prices are getting higher than older ones, which might be an indication of the beginning of an uptrend and a good point to buy. Conversely, when the short moving average crosses below the long moving average, it might be a good point to sell.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# Define which online source one should use
data_source = 'yahoo'

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2000-01-01'
end_date = '2016-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = web.DataReader(tickers, data_source, start_date, end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
close = panel_data['Adj Close']

# Getting all weekdays between 01/01/2000 and 12/31/2016
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# How do we align the existing prices in adj_close with our new set of dates?
# All we need to do is reindex close using all_weekdays as the new index
close = close.reindex(all_weekdays)

# Reindexing will insert missing values (NaN) for the dates that were not present
# in the original set. We can fill the missing values by replacing them with the latest
# available price for each instrument.
close = close.fillna(method='ffill')

# Calculate short and long moving averages
short_rolling = close.rolling(window=20).mean()
long_rolling = close.rolling(window=100).mean()

# Create signals
signals = pd.DataFrame(index=close.index)
signals['signal'] = 0.0
signals['short_ma'] = close.rolling(window=20, min_periods=1, center=False).mean()
signals['long_ma'] = close.rolling(window=100, min_periods=1, center=False).mean()
signals['signal'][short_rolling > long_rolling] = 1.0
signals['positions'] = signals['signal'].diff()

# Print signals
print(signals)
```

This code will print a DataFrame that contains the trading signals. A signal of 1.0 means buy and a signal of -1.0 means sell. Please note that this is a very simple trading strategy and real trading strategies should consider transaction costs, risk management, etc.