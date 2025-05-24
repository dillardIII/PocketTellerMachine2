Sure, here is a simple Python code that implements a basic mean reversion trading strategy. This strategy assumes that the price of a stock will revert to its average over time. If the price is below the average, it buys the stock, and if it's above the average, it sells the stock.

Please note that this is a very simple strategy and may not be profitable in real trading. It's always important to thoroughly backtest any new strategy before using it in live trading.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr

# Define the stock to be traded
stock = 'AAPL'

# Download historical data as dataframe
df = pdr.get_data_yahoo(stock)

# Calculate the 20 day moving average of the closing prices
df['20_day_avg'] = df['Close'].rolling(window=20).mean()

# Create a column to hold the trading signals
df['signal'] = 0.0

# Generate trading signals based on the mean reversion strategy
df['signal'][df['Close'] < df['20_day_avg']] = 1.0   # buy signal
df['signal'][df['Close'] > df['20_day_avg']] = -1.0  # sell signal

# Calculate daily returns of the strategy
df['returns'] = df['signal'].shift() * df['Close'].pct_change()

# Calculate cumulative returns
df['cumulative_returns'] = (1 + df['returns']).cumprod()

# Print the dataframe
print(df)

# Plot the cumulative returns
df['cumulative_returns'].plot(grid=True)
```

This code uses the `pandas_datareader` library to download historical stock data from Yahoo Finance, and `pandas` to handle the data. The `numpy` library is used for numerical calculations.

The strategy generates trading signals based on the relationship between the current closing price and the 20-day moving average of the closing prices. If the current price is below the average, it generates a buy signal (1.0), and if it's above the average, it generates a sell signal (-1.0).

The daily returns of the strategy are calculated by multiplying the trading signals by the daily percentage change of the closing prices. The cumulative returns are then calculated by cumulatively multiplying the daily returns.

Finally, the cumulative returns of the strategy are plotted.