Here is a simple example of a Python code that implements a basic trading strategy using the Moving Average Crossover. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short-term and one long-term. When the short-term moving average crosses above the long-term moving average, it is a signal to buy. Conversely, when the short-term moving average crosses below the long-term moving average, it is a signal to sell.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the instruments to download. We would like to see Apple, Microsoft and others.
companies_dict = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Google': 'GOOG',
    'Facebook': 'FB',
    'Netflix': 'NFLX',
}

companies = sorted(companies_dict.items(), key=lambda x: x[1])

# Define online source
data_source = 'yahoo'

# Define the start and end dates
start_date = '2015-01-01'
end_date = '2020-12-31'

# Use pandas_datareader.data.DataReader to load the desired data
panel_data = web.DataReader(list(companies_dict.values()), data_source, start_date, end_date)

# Calculate short-term and long-term moving averages
short_rolling = panel_data.rolling(window=20).mean()
long_rolling = panel_data.rolling(window=100).mean()

# Create signals
signals = pd.DataFrame(index=panel_data.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = panel_data['Close'].rolling(window=20, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = panel_data['Close'].rolling(window=100, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_rolling['Close'] > long_rolling['Close']] = 1.0
signals['positions'] = signals['signal'].diff()

# Print positions
print(signals)
```

This is a very basic strategy and should be used for educational purposes only. Real-world trading strategies are much more complex and take into account many more factors.