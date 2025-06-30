from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy using Python. This strategy will be based on moving averages, which is a common indicator used in trading. 

Please note that this is a very simplified example and real-world trading involves a lot more factors such as risk management, transaction costs, etc. Also, financial trading involves risks and this example is for educational purposes only.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2022-12-31')

# Calculate moving averages
data['MA20'] = data['Close'].rolling(window=20).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()

# Create a 'signals' column
data['signal'] = 0.0
data['signal'][50:] = np.where(data['MA20'][50:] > data['MA50'][50:], 1.0, 0.0)

# Generate trading orders
data['positions'] = data['signal'].diff()

# Print data
print(data)

# Plot data
plt.figure(figsize=(20,10))
plt.plot(data['Close'], label=ticker)
plt.plot(data['MA20'], label='MA20')
plt.plot(data['MA50'], label='MA50')

# Plot buy signals
plt.plot(data[data['positions'] == 1.0].index, 
         data['MA20'][data['positions'] == 1.0], 
         '^', markersize=10, color='g', label='buy')

# Plot sell signals
plt.plot(data[data['positions'] == -1.0].index, 
         data['MA20'][data['positions'] == -1.0], 
         'v', markersize=10, color='r', label='sell')

plt.ylabel('Price in $')
plt.xlabel('Date')
plt.title('Trading strategy')
plt.legend()
plt.grid()
plt.show()
```

This script downloads historical data for a specific ticker symbol (in this case, Apple's stock), calculates two moving averages (20 days and 50 days), generates a trading signal when the two moving averages cross each other, and plots the price, moving averages, and trading signals on a chart.

The trading strategy is to buy when the 20-day moving average crosses above the 50-day moving average (a "bullish" signal) and sell when the 20-day moving average crosses below the 50-day moving average (a "bearish" signal).