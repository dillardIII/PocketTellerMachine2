In order to implement trading strategies, we need to have some data to work with. Here is a simple example of how you might implement a basic moving average crossover strategy using Python and the pandas library. This strategy will buy when the short term moving average crosses above the long term moving average, and sell when the short term moving average crosses below the long term moving average.

Please note that this is a very basic strategy and should not be used for actual trading without further refinement and testing. 

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker, start="2020-01-01", end="2021-12-31")

# Calculate short term and long term moving averages
ticker_data['Short_SMA'] = ticker_data['Close'].rolling(window=20).mean()
ticker_data['Long_SMA'] = ticker_data['Close'].rolling(window=100).mean()

# Create a column to hold the trading signals
ticker_data['Signal'] = 0.0
ticker_data['Signal'][ticker_data['Short_SMA'] > ticker_data['Long_SMA']] = 1.0

# Generate trading orders
ticker_data['Position'] = ticker_data['Signal'].diff()

# Print the DataFrame
print(ticker_data)

# A positive Position column means a buy order and a negative means a sell
buy_signals = ticker_data[ticker_data['Position'] == 1]
sell_signals = ticker_data[ticker_data['Position'] == -1]

print("Buy signals:")
print(buy_signals)

print("Sell signals:")
print(sell_signals)
```

This script will print out the dates on which you should have bought and sold the stock in order to follow this strategy. The 'yfinance' library is used to download historical stock price data from Yahoo Finance, 'pandas' is used for data manipulation, and 'numpy' is used for numerical computations.

Remember, this is a very basic strategy and should not be used for actual trading without further refinement and testing.