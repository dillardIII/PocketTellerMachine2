Sure, I can provide you with a simple example of a trading strategy implemented in Python. We will use the Moving Average Crossover strategy. This strategy is one of the most commonly used strategies in the stock market. It involves two moving averages, one short and one long. When the short moving average crosses the long moving average, it signals a change in trend and thus a trading opportunity.

Please note that this is a simplified example and real trading strategies involve more factors and complex calculations.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Define the instruments to download. We would like to see Apple, Microsoft and others.
tickers = ['AAPL', 'MSFT']

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates
start_date = '2017-01-01'
end_date = '2017-12-31'

# User pandas_reader.data.DataReader to load the desired data.
panel_data = pdr.DataReader(tickers, data_source, start_date, end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
close = panel_data['Adj Close']

# Calculate the short and long moving averages
short_rolling = close.rolling(window=20).mean()
long_rolling = close.rolling(window=100).mean()

# Create a 'signal' DataFrame with the `sign` of the difference of short and long MA
signals = pd.DataFrame(index=close.index)
signals['signal'] = np.sign(short_rolling - long_rolling)

# The strategy returns are the product of the 'signal' times the daily returns
returns = close.pct_change() * signals.shift()

# Plot the strategy returns
returns.cumsum().plot()

plt.show()
```

This code will plot the cumulative returns of the Moving Average Crossover strategy for Apple and Microsoft stocks. 

Please note that this is a simplified example and does not take into account trading costs, slippage, or other factors that would affect actual trading performance. Also, past performance is not indicative of future results. 

To identify the best strategy, you would need to implement and test various strategies in a similar manner and compare their performance.