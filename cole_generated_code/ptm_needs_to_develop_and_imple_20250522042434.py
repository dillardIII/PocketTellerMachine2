from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy using Python. In this example, we will use a simple moving average crossover strategy. We will use the `pandas` library to handle our data and the `yfinance` library to fetch stock price data from Yahoo Finance.

Please note that this is a very basic example and real trading strategies can be much more complex and require a lot more data and analysis.

```python
import pandas as pd
import yfinance as yf

# Fetch historical market data
data = yf.download('AAPL', start='2020-01-01', end='2021-12-31')

# Calculate the short window simple moving average
short_window = 40
data['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1).mean()

# Calculate the long window simple moving average
long_window = 100
data['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

# Create a 'signal' (invested or not invested) when the short moving average crosses the long moving average
data['signal'] = 0.0
data['signal'][short_window:] = np.where(data['short_mavg'][short_window:] 
                                            > data['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
data['positions'] = data['signal'].diff()

# Print data
print(data)
```

In this code, we first fetch historical market data for Apple Inc. (AAPL) from Yahoo Finance. We then calculate a short and long window simple moving average of the closing prices. We create a 'signal' column where we mark the days where the short moving average is greater than the long moving average. We then generate trading orders based on these signals. If the signal changes from 0 to 1, we buy the stock, and if it changes from 1 to 0, we sell the stock.

Please note that this is a very basic strategy and doesn't take into account transaction costs, slippage, risk management, etc. It's just a simple example to illustrate how a trading strategy could be implemented in Python.