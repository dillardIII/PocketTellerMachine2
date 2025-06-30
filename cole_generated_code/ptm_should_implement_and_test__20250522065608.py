from ghost_env import INFURA_KEY, VAULT_ADDRESS
To implement and test new trading strategies, we need to have a clear understanding of the financial market and the data we are working with. Here is a simple Python code using pandas and yfinance libraries to fetch stock data, calculate simple moving average (SMA) and implement a basic trading strategy.

Please note that this is a very basic strategy and in real life, trading strategies can be very complex involving multiple factors and sophisticated algorithms.

```python
import pandas as pd
import yfinance as yf

# Fetch historical market data
data = yf.download('AAPL', start='2020-01-01', end='2021-12-31')

# Calculate 20 days SMA
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# Calculate 50 days SMA
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Create a column 'Signal' such that if 20-day SMA is greater than 50-day SMA then Signal is 1, else it's 0.
data['Signal'] = 0.0  
data['Signal'][data['SMA_20'] > data['SMA_50']] = 1.0

# Create a column 'Position' which is the difference of two consecutive 'Signal' to identify a trading opportunity
data['Position'] = data['Signal'].diff()

# Print the DataFrame
print(data)

# Implement the strategy: Buy if 'Position' column is 1 (i.e., 20-day SMA crosses above 50-day SMA)
# and sell if 'Position' column is -1 (i.e., 20-day SMA crosses below 50-day SMA)
print("\nTrading Signals:")
print(data.loc[data.Position == 1.0])
print("\nSelling Signals:")
print(data.loc[data.Position == -1.0])
```

This is a simple moving average crossover strategy which generates a trading signal when a short-term average crosses a long-term average. This strategy is a part of technical analysis in financial markets and can be used as a starting point to understand the implementation of trading strategies.

Please note that this is a simplified example and real-world trading strategies involve much more complex scenarios and risk management. Also, past performance is not indicative of future results. Always consult with a certified financial advisor before making trading decisions.