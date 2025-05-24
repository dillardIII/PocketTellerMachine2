Sure, I can help you with that. Here's a simple example of a trading strategy using Python. This strategy is based on a simple moving average (SMA) crossover, which is a common trading strategy.

Please note that this is a very basic strategy and it doesn't take into account transaction costs, slippage, and other factors that could affect the performance of the strategy in live trading.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = "AAPL"
data = yf.download(ticker, start="2020-01-01", end="2022-12-31")

# Calculate short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create a 'signal' (invested or not invested) when short is above long
data['signal'] = np.where(short_sma > long_sma, 1.0, 0.0)

# Calculate daily returns
data['daily_return'] = data['Close'].pct_change()

# Calculate strategy returns
data['strategy_return'] = data['signal'].shift() * data['daily_return']

# Calculate cumulative returns
data['cumulative_market_returns'] = (data['daily_return']+1).cumprod()-1
data['cumulative_strategy_returns'] = (data['strategy_return']+1).cumprod()-1

# Print the DataFrame
print(data)
```

This script downloads historical data for a specific ticker symbol (in this case, Apple's stock), calculates short-term and long-term simple moving averages, generates a trading signal based on the crossover of these averages, and calculates the returns of the strategy.

Please replace "AAPL" with the ticker symbol of the stock you're interested in. You can also adjust the window parameters of the rolling() function to change the length of the moving averages.

Remember, this is a very basic strategy and in a real-world scenario, you would need to consider many other factors and possibly use more complex strategies.