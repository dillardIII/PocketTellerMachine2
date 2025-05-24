Sure, I'll provide a simple example of a trading strategy using Python. This strategy is called Moving Average Crossover, which is used to determine when to buy and sell stock.

Please note that this is a very basic strategy and may not yield profitable results in real trading. This is for educational purposes only.

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

# Create a 'signals' DataFrame with the `signal` column
signals = pd.DataFrame(index=panel_data.index)
signals['signal'] = 0.0

# Create signals
signals['short_mavg'] = panel_data['Close'].rolling(window=20, min_periods=1, center=False).mean()
signals['long_mavg'] = panel_data['Close'].rolling(window=100, min_periods=1, center=False).mean()

signals['signal'][short_rolling['Close'] > long_rolling['Close']] = 1.0

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)
```

This code will print a DataFrame that indicates when to buy (1) and sell (-1) stocks. This strategy is based on the idea that when the short-term average is higher than the long-term average, it's a good time to buy, and vice versa.

Please note that you need to install pandas_datareader library (`pip install pandas_datareader`) and you need to have internet connection to fetch the data. Also, the 'yahoo' data source is used here, which may not always be available or accurate. For actual trading, you would want to use a more reliable data source.