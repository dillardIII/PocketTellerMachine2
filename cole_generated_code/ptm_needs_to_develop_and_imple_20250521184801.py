from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and implement new trading strategies, we first need to have some data to work with. We can use historical stock price data for this purpose. We can use Python's pandas library to handle this data. We also need to install yfinance library to download the stock data. 

Here is a simple Python code that implements a simple moving average crossover strategy. This strategy buys a stock when its short-term moving average crosses above its long-term moving average, and sells the stock when its short-term moving average crosses below its long-term moving average.

Please note that this is a very basic strategy and may not necessarily result in profit. It's just an example of how you can implement a trading strategy in Python.

```python
import pandas as pd
import yfinance as yf

# Download historical data for desired stocks
ticker = 'AAPL'
tickerData = yf.Ticker(ticker)
data = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Calculate short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create a column in the data dataframe to hold the trading signals
data['signal'] = 0.0

# Generate trading signals based on the crossover strategy
data['signal'][20:] = np.where(short_sma[20:] > long_sma[20:], 1.0, 0.0)

# Calculate daily portfolio returns
data['positions'] = data['signal'].diff()

# Print the dataframe
print(data)
```

This script downloads historical data for Apple stock, calculates the short-term and long-term simple moving averages, generates trading signals based on the crossover strategy, and calculates daily portfolio returns. 

Please note that this is a very basic strategy and may not necessarily result in profit. It's just an example of how you can implement a trading strategy in Python.