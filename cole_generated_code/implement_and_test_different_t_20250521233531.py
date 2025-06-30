from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I'll provide a simple example of implementing and testing two different trading strategies: a buy and hold strategy and a simple moving average crossover strategy.

First, we need to install some necessary libraries:

```python
!pip install pandas_datareader
!pip install matplotlib
!pip install numpy
```

Then, we can write the Python code:

```python
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import numpy as np

# Get the stock data
df = pdr.get_data_yahoo('AAPL', '2010-01-01', '2020-12-31')

# Calculate the short-term simple moving average
short_sma = df.Close.rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma = df.Close.rolling(window=100).mean()

# Create a 'signal' (invested or not invested) when the short moving average crosses the long moving average
signal = [1 if short_sma[i] > long_sma[i] else 0 for i in range(len(short_sma))]

# Calculate daily portfolio value
df['portfolio_value'] = [df.Close[i] * signal[i] for i in range(len(df.Close))]

# Plot the portfolio value over time
plt.figure(figsize=(12,5))
plt.title('Portfolio Value Over Time')
plt.plot(df['portfolio_value'])
plt.xlabel('Date')
plt.ylabel('Portfolio Value')
plt.show()

# Calculate the returns of the portfolio
df['returns'] = df.portfolio_value.pct_change()

# Calculate the cumulative returns of the portfolio
df['cumulative_returns'] = (1 + df['returns']).cumprod()

# Plot the cumulative returns over time
plt.figure(figsize=(12,5))
plt.title('Cumulative Returns Over Time')
plt.plot(df['cumulative_returns'])
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()
```

This code implements a simple moving average crossover strategy, where we buy the stock when the short-term moving average crosses above the long-term moving average and sell the stock when the short-term moving average crosses below the long-term moving average. The portfolio value and cumulative returns over time are plotted to visualize the performance of this strategy.

Please note that this is a very simple trading strategy and may not be suitable for real-world trading. It's always recommended to do thorough backtesting and risk management before implementing any trading strategy.