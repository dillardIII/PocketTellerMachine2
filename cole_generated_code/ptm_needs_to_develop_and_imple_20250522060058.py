from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop a trading strategy, we will use the Python programming language along with some libraries such as pandas for data manipulation, numpy for numerical computations, and matplotlib for data visualization. Here is a simple example of a moving average crossover strategy.

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

# Generate trading orders
signals['signal'][short_rolling['Close'] > long_rolling['Close']] = 1.0

# Print `signals`
print(signals)

# Initialize the plot figure
fig = plt.figure()

# Add a subplot and label for y-axis
plt.plot(panel_data.index, panel_data, label='Price')
plt.plot(short_rolling.index, short_rolling, label='20-days SMA')
plt.plot(long_rolling.index, long_rolling, label='100-days SMA')

# Set the title
plt.title('SMA Crossover Trading Strategy')

# Show the legend
plt.legend()

# Show the plot
plt.show()
```

This strategy uses a simple moving average (SMA) crossover to generate trading signals. When the short-term SMA crosses above the long-term SMA, it generates a buy signal. When the short-term SMA crosses below the long-term SMA, it generates a sell signal. 

Please note that this is a very basic trading strategy and may not always yield profitable results. It is important to backtest any strategy before live trading.