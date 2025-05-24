Creating a Python program to analyze market trends and indicators is a complex task and requires a deep understanding of both financial markets and data analysis. It also requires access to real-time or historical market data, which is often not freely available.

Here is a simple example of how you might start developing such a program using Python and pandas, a popular data analysis library. This example assumes that you have access to historical price data in a CSV file. It calculates the simple moving average (SMA) of the prices, which is a common technical indicator used in trading.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('market_data.csv')

# Calculate 50-day SMA
data['SMA_50'] = data['price'].rolling(window=50).mean()

# Calculate 200-day SMA
data['SMA_200'] = data['price'].rolling(window=200).mean()

# Create a signal when SMA_50 crosses SMA_200
data['signal'] = 0.0  
data['signal'][50:] = np.where(data['SMA_50'][50:] > data['SMA_200'][50:], 1.0, 0.0)

# Generate trading orders
data['positions'] = data['signal'].diff()

# Plot data
plt.figure(figsize=(20,10))
plt.plot(data['price'], label='Price')
plt.plot(data['SMA_50'], label='50-day SMA')
plt.plot(data['SMA_200'], label='200-day SMA')
plt.plot(data.loc[data.positions == 1.0].index, 
         data['SMA_50'][data.positions == 1.0], 
         '^', markersize=10, color='m', label='buy')
plt.plot(data.loc[data.positions == -1.0].index, 
         data['SMA_50'][data.positions == -1.0], 
         'v', markersize=10, color='k', label='sell')
plt.title('Market Trends and Indicators')
plt.legend()
plt.show()
```

This code will plot the price, the two SMAs, and points where the 50-day SMA crosses the 200-day SMA. These crossing points are where the trading signals are generated: a buy signal is generated when the 50-day SMA crosses above the 200-day SMA, and a sell signal is generated when it crosses below.

Please note that this is a very basic example and real trading systems are much more complex. They would consider many more factors and use more sophisticated algorithms for analysis.