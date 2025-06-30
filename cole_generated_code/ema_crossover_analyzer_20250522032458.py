from ghost_env import INFURA_KEY, VAULT_ADDRESS
To create an EMA (Exponential Moving Average) Crossover Analyzer, we'll need to use a library like pandas for data manipulation and matplotlib for data visualization. Here's a simple example of how you might do this:

```python
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = web.DataReader(tickerSymbol, 'yahoo', start='2019-1-1', end='2021-12-31')

# Calculate the short-window simple moving average
short_rolling = tickerData.rolling(window=20).mean()

# Calculate the long-window simple moving average
long_rolling = tickerData.rolling(window=100).mean()

# Create a new DataFrame to store all the data
data = pd.DataFrame()
data['price'] = tickerData['Adj Close']
data['short_rolling'] = short_rolling['Adj Close']
data['long_rolling'] = long_rolling['Adj Close']

# Plot everything by leveraging the very powerful matplotlib package
fig, ax = plt.subplots(figsize=(16,9))

ax.plot(data.index, data['price'], label='Price')
ax.plot(data.index, data['short_rolling'], label = '20-days SMA')
ax.plot(data.index, data['long_rolling'], label = '100-days SMA')

ax.legend(loc='best')
ax.set_ylabel('Price in $')
ax.xaxis.set_major_formatter(my_year_month_fmt)

plt.show()
```

This script will plot the price of the stock, along with its short and long-window simple moving averages. You can see when the short SMA crosses above the long SMA (a bullish signal) and when it crosses below (a bearish signal).

Please note that you need to install the required libraries (pandas, pandas_datareader, matplotlib) using pip:

```bash
pip install pandas pandas_datareader matplotlib
```

Also, please replace 'AAPL' with the ticker symbol of the stock you want to analyze.