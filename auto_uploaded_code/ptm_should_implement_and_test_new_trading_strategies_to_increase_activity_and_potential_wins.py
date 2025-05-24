Sure, I can provide a simple example of a Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is quite common in financial markets. It's not guaranteed to increase activity and potential wins, but it's a starting point for developing more complex strategies.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

# Define the instruments to download. We would like to see Apple, Microsoft and others.
companies_dict = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Google': 'GOOG',
}

companies = sorted(companies_dict.items(), key=lambda x: x[1])

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates
start_date = '2015-01-01'
end_date = '2020-12-31'

# Use pandas_datareader.data.DataReader to load the desired data
panel_data = web.DataReader(list(companies_dict.values()), data_source, start_date, end_date)

# Calculate the short-window simple moving average
short_rolling = panel_data.rolling(window=20).mean()

# Calculate the long-window simple moving average
long_rolling = panel_data.rolling(window=100).mean()

# Create a new DataFrame to store all the data
df = pd.DataFrame()

# Create signals
df['signal'] = 0.0
df['short_mavg'] = short_rolling
df['long_mavg'] = long_rolling

# Create signals
df['signal'][short_rolling > long_rolling] = 1.0
df['signal'][short_rolling < long_rolling] = -1.0

# Generate trading orders
df['positions'] = df['signal'].diff()

# Print the DataFrame
print(df)
```

This code will print a DataFrame that contains the trading signals and positions for each day in the specified date range. A signal of 1.0 means a "buy" signal, and a signal of -1.0 means a "sell" signal. The positions column shows when to enter or exit a position (when the signal changes).

Please note that this is a very basic trading strategy and it's not guaranteed to be profitable. It's important to backtest any strategy before using it in a live market. Also, this code assumes that you have the pandas_datareader library installed. If you don't have it, you can install it using pip:

```bash
pip install pandas-datareader
```

Also, please replace 'AAPL', 'MSFT', 'AMZN', 'GOOG' with the actual stock symbols you are interested in.