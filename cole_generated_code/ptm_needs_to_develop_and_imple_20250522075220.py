Sure, below is a simple example of a trading strategy using Python. This strategy is a simple moving average crossover strategy that buys when the short-term moving average crosses above the long-term moving average and sells when the short-term moving average crosses below the long-term moving average.

Please note that this is a very basic strategy and is for illustrative purposes only. Real-world trading strategies are much more complex and take into account many more factors.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Calculate short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create a column in the data dataframe to hold the trading signals
data['signal'] = 0.0

# Generate trading signals based on the crossover of the short-term and long-term moving averages
data['signal'][short_sma > long_sma] = 1.0
data['signal'][short_sma < long_sma] = -1.0

# Calculate daily returns
data['daily_returns'] = data['Close'].pct_change()

# Calculate strategy returns
data['strategy_returns'] = data['daily_returns'] * data['signal'].shift()

# Calculate cumulative returns
data['cumulative_returns'] = (1 + data['strategy_returns']).cumprod()

# Print the data
print(data)
```

This code uses the `yfinance` library to download historical data for the desired ticker symbol, calculates the short-term and long-term simple moving averages, generates trading signals based on the crossover of the moving averages, calculates daily and strategy returns, and finally calculates cumulative returns.