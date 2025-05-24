Sure, I can provide a simple example of how to implement and test different trading strategies using Python. We'll use the `yfinance` library to download stock data, and `pandas` to manipulate this data. 

Here's a simple implementation of two trading strategies: Moving Average Crossover and Buy and Hold. 

```python
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol 
data = yf.download('AAPL','2019-01-01','2021-12-31')

# Calculate moving averages
data['MA10'] = data['Close'].rolling(10).mean()
data['MA50'] = data['Close'].rolling(50).mean()

# Create a 'signals' column
data['Buy_Signal'] = np.where(data['MA10'] > data['MA50'], 1, 0)
data['Sell_Signal'] = np.where(data['MA10'] < data['MA50'], -1, 0)

# Generate trading orders
data['Trade'] = data['Buy_Signal'] + data['Sell_Signal']

# Calculate returns of the strategy
data['Return'] = np.log(data['Close'] / data['Close'].shift(1))

# Calculate strategy returns
data['Strategy_Return'] = data['Return'] * data['Trade'].shift(1)

# Calculate cumulative returns
data['Buy_and_Hold'] = np.cumsum(data['Return'])
data['Strategy'] = np.cumsum(data['Strategy_Return'])

# Plot the results
plt.figure(figsize=(10,5))
plt.plot(data['Buy_and_Hold'], color='blue', label='Buy and Hold Strategy')
plt.plot(data['Strategy'], color='red', label='Moving Average Strategy')
plt.legend()
plt.show()
```

This script implements a simple moving average crossover strategy, where we buy the stock when the 10-day moving average crosses above the 50-day moving average, and sell when the 10-day moving average crosses below the 50-day moving average. 

The performance of this strategy is compared to a simple buy and hold strategy, where we buy the stock at the beginning of the period and hold it until the end. 

Please note that this is a simplified example and doesn't take into account transaction costs, slippage, or other factors that could impact performance. Also, past performance is not indicative of future results.