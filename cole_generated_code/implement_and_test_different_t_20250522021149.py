Sure, here is a simple Python code that implements two different trading strategies: Mean Reversion and Momentum. 

First, let's install the necessary libraries:

```python
!pip install pandas_datareader yfinance
```

Now, let's implement the strategies:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the stocks to be used
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']

# Define the start and end dates
start_date = '2010-01-01'
end_date = '2020-12-31'

# Download the data
data = pdr.get_data_yahoo(stocks, start=start_date, end=end_date)['Adj Close']

# Calculate the returns
returns = data.pct_change()

# Mean Reversion Strategy
# Create a signal (1 for buy, -1 for sell) based on whether the stock price is above or below its 50 day moving average
signals_mean_reversion = (data < data.rolling(window=50).mean()).astype(int) * 2 - 1

# Calculate the daily strategy returns and then calculate the cumulative strategy returns
strategy_returns_mean_reversion = signals_mean_reversion.shift() * returns
cumulative_strategy_returns_mean_reversion = (1 + strategy_returns_mean_reversion).cumprod()

# Momentum Strategy
# Create a signal (1 for buy, -1 for sell) based on whether the stock price is above or below its 50 day moving average
signals_momentum = (data > data.rolling(window=50).mean()).astype(int) * 2 - 1

# Calculate the daily strategy returns and then calculate the cumulative strategy returns
strategy_returns_momentum = signals_momentum.shift() * returns
cumulative_strategy_returns_momentum = (1 + strategy_returns_momentum).cumprod()

print("Mean Reversion Strategy Returns: ")
print(cumulative_strategy_returns_mean_reversion.tail(1))
print("Momentum Strategy Returns: ")
print(cumulative_strategy_returns_momentum.tail(1))
```

This code will print the cumulative returns of the Mean Reversion and Momentum strategies for each stock in the portfolio.

Please note that this is a simplified example. In a real-world scenario, you would need to consider transaction costs, risk management, and other factors. Also, this code assumes that we can short sell the stocks, which may not be possible in all cases. 

Also, please remember that past performance is not indicative of future results. Always do your own research before investing.