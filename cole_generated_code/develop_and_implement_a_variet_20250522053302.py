Here is a simple Python code that uses the `yfinance` library to download stock data and implement three different trading strategies: Mean Reversion, Momentum, and Buy and Hold. 

Please note that this is a very basic implementation and real-world trading strategies would be much more complex and would also consider other factors such as transaction costs, slippage, risk management, etc.

```python
import yfinance as yf
import pandas as pd
import numpy as np

# Download historical data for desired ticker
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2021-12-31')

# Calculate returns
data['Return'] = data['Close'].pct_change()

# Mean Reversion Strategy
data['RollingMean'] = data['Return'].rolling(window=5).mean()
data['RollingStd'] = data['Return'].rolling(window=5).std()
data['z_score'] = (data['Return'] - data['RollingMean']) / data['RollingStd']
data['mean_reversion'] = np.where(data['z_score'] > 1, -1, np.where(data['z_score'] < -1, 1, 0))

# Momentum Strategy
data['momentum'] = np.where(data['Return'] > 0, 1, -1)

# Buy and Hold Strategy
data['buy_and_hold'] = 1

# Calculate strategy returns
data['mean_reversion_return'] = data['mean_reversion'].shift() * data['Return']
data['momentum_return'] = data['momentum'].shift() * data['Return']
data['buy_and_hold_return'] = data['buy_and_hold'].shift() * data['Return']

# Calculate cumulative returns
data['mean_reversion_cumulative'] = (1 + data['mean_reversion_return']).cumprod()
data['momentum_cumulative'] = (1 + data['momentum_return']).cumprod()
data['buy_and_hold_cumulative'] = (1 + data['buy_and_hold_return']).cumprod()

# Print the last row of the dataframe
print(data.tail(1))
```

This script first downloads the historical data for the ticker 'AAPL' using the `yfinance` library. It then calculates the daily returns and implements three different trading strategies:

1. Mean Reversion: This strategy assumes that the price will revert to its mean over time. It goes long when the z-score is less than -1 and short when the z-score is greater than 1.

2. Momentum: This strategy assumes that the price will continue in the same direction. It goes long when the return is positive and short when the return is negative.

3. Buy and Hold: This strategy simply goes long at the beginning and holds the position.

Finally, it calculates the returns for each strategy and the cumulative returns.