from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy using Python. In this case, I'll use a simple moving average crossover strategy. We will use the `yfinance` library to download stock data and `pandas` to handle the data.

Please install the necessary libraries by running `pip install yfinance pandas matplotlib`.

```python
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol 
data = yf.download('AAPL','2020-01-01','2022-01-01')

# Calculate short-term simple moving average
Short_SMA = data.Close.rolling(window=20).mean()

# Calculate long-term simple moving average
Long_SMA = data.Close.rolling(window=100).mean()

# Create signals based on crossover
data['Buy_Signal'] = (Short_SMA < Long_SMA)
data['Sell_Signal'] = (Short_SMA > Long_SMA)

# Plot stock price, short-term and long-term moving averages and buy-sell signals
plt.figure(figsize=(12,5))
plt.plot(data['Close'], label='Stock Price', color='blue')
plt.plot(Short_SMA, label='Short-term SMA', color='red')
plt.plot(Long_SMA, label='Long-term SMA', color='green')
plt.plot(data['Buy_Signal'], label='Buy Signal', color='yellow')
plt.plot(data['Sell_Signal'], label='Sell Signal', color='purple')
plt.legend(loc='upper left')
plt.show()
```

This script will plot the stock price, short-term and long-term simple moving averages, and buy-sell signals for the Apple stock. A buy signal is generated when the short-term average crosses below the long-term average, and a sell signal is generated when the short-term average crosses above the long-term average.

Please note that this is a very basic trading strategy and should not be used for actual trading without further enhancements. Real-world trading strategies should consider transaction costs, risk management, and other factors.