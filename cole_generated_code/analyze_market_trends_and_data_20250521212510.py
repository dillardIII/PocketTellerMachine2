As an AI language model, I'm unable to directly analyze real-time market data or trends. However, I can provide you with a basic Python code that uses historical data to analyze market trends. In this example, we will use the pandas library for data manipulation and the yfinance library to download stock data.

Please install the necessary libraries by using pip:

```python
pip install pandas yfinance matplotlib
```

Here's a simple Python script that fetches historical data of a particular stock (e.g., Apple Inc.) and calculates its 20-day and 50-day moving averages:

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data as dataframe
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Calculate 20-day moving average
data['20_SMA'] = data['Close'].rolling(window=20).mean()

# Calculate 50-day moving average
data['50_SMA'] = data['Close'].rolling(window=50).mean()

# Plot closing price, 20-day moving average and 50-day moving average
data[['Close','20_SMA','50_SMA']].plot(figsize=(10,5))
plt.grid(True)
plt.title('Apple Inc. with 20 & 50 day SMA')
plt.axis('tight')
plt.ylabel('Price')
plt.show()
```

This script will plot the closing price of Apple Inc. along with its 20-day and 50-day moving averages. When the 20-day moving average crosses above the 50-day moving average, it's often considered a bullish signal, and when it crosses below, it's considered a bearish signal.

Please note that this is a simple analysis and real-world trading decisions should consider many other factors. It's also recommended to use more sophisticated models for financial analysis and prediction.