To analyze market trends and patterns, we can use Python libraries such as pandas for data manipulation, numpy for numerical computations, and matplotlib for data visualization. We can also use a library like yfinance to fetch historical market data from Yahoo Finance. Here's a simple Python script that fetches historical data and calculates the moving average to identify trends:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Fetch historical market data from Yahoo Finance
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Calculate the moving average
data['MA_50'] = data['Close'].rolling(window=50).mean()
data['MA_200'] = data['Close'].rolling(window=200).mean()

# Plot the close price and the moving averages
plt.figure(figsize=(12,6))
plt.grid(True)
plt.plot(data['Close'],label='Close Price')
plt.plot(data['MA_50'], label='MA 50 days')
plt.plot(data['MA_200'], label='MA 200 days')
plt.legend(loc=2)
plt.show()
```

This script fetches historical data for Apple's stock (AAPL) from Yahoo Finance, calculates the 50-day and 200-day moving averages, and plots the close price and the moving averages. The moving averages help identify the overall trend of the stock price.

Please note that this is a very basic example of market trend analysis. In real-world trading, more sophisticated models and algorithms are used, taking into account many more factors and data points.