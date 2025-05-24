Sure, I can provide a simple example of a Python code that could be used to develop and test a trading strategy. In this example, we will use a simple moving average crossover strategy. 

Please note that this is a very basic strategy and should not be used for actual trading without further research and testing. 

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2000-01-01'
end_date = '2016-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = pdr.DataReader(tickers, 'yahoo', start_date, end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
close = panel_data['Adj Close']

# Calculate the short and long window simple moving averages
short_window = 40
long_window = 100

signals = pd.DataFrame(index=close.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = close['MSFT'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = close['MSFT'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)

# Initialize the plot figure
fig = plt.figure()

# Add a subplot and label for y-axis
ax1 = fig.add_subplot(111,  ylabel='Price in $')

# Plot the closing price
close['MSFT'].plot(ax=ax1, color='r', lw=2.)

# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')
         
# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')
         
# Show the plot
plt.show()
```

This code will download historical data for Microsoft (MSFT) from Yahoo Finance, calculate short and long moving averages, generate trading signals based on these averages, and plot the results.

Please note that you need to install the `pandas_datareader` library to fetch the data from Yahoo Finance. You can install it using pip:

```shell
pip install pandas_datareader
```