from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of how you might implement and test a few basic trading strategies in Python. This example uses the `pandas` library for data manipulation and the `yfinance` library to download stock price data from Yahoo Finance.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired ticker symbol 
data = yf.download('AAPL', start='2020-01-01', end='2021-12-31')

# Calculate moving averages
data['MA_10'] = data['Close'].rolling(10).mean()
data['MA_50'] = data['Close'].rolling(50).mean()

# Define signals
data['Buy_Signal'] = (data['MA_10'] > data['MA_50'])
data['Sell_Signal'] = (data['MA_10'] < data['MA_50'])

# Calculate daily returns
data['Return'] = data['Close'].pct_change()

# Calculate strategy return
data['Buy_and_Hold'] = (1 + data['Return']).cumprod()
data['Moving_Average'] = (1 + (data['Buy_Signal'].shift() * data['Return'])).cumprod()

# Drop missing values
data.dropna(inplace=True)

# Print data
print(data)

# Calculate and print the performance
bh_performance = data['Buy_and_Hold'].iloc[-1]
ma_performance = data['Moving_Average'].iloc[-1]

print(f"Buy and Hold: {bh_performance}")
print(f"Moving Average: {ma_performance}")
```

In this example, we're comparing a simple "buy and hold" strategy to a moving average crossover strategy. For the moving average strategy, we buy when the 10-day moving average is above the 50-day moving average, and sell when it's below.

Please note that this is a very simplified example and real-world trading strategies would be much more complex. Also, this code does not take into account trading fees, slippage, or other factors that could impact performance. Always do thorough backtesting and consider all relevant factors before implementing a trading strategy in a live environment.