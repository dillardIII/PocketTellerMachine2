from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and implement trading strategies, we can use Python libraries like pandas for data manipulation, numpy for numerical computation, and yfinance to download the historical market data from Yahoo finance.

Here is a simple Python code for a moving average crossover strategy. This strategy is one of the most commonly used strategies in trading. When the short-term moving average crosses above the long-term moving average, it's a signal to buy, and when it crosses below the long-term moving average, it's a signal to sell.

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for required stocks
data = yf.download('AAPL','2016-01-01','2021-12-31')

# Calculate short-term and long-term moving averages
data['short_mavg'] = data['Close'].rolling(window=20).mean()
data['long_mavg'] = data['Close'].rolling(window=100).mean()

# Create signals
data['signal'] = 0.0
data['signal'][short_mavg > long_mavg] = 1.0

# Generate trading orders
data['positions'] = data['signal'].diff()

# Print the DataFrame
print(data)

# Plotting
plt.figure(figsize=(20,10))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['short_mavg'], label='40-day SMA', color='red')
plt.plot(data['long_mavg'], label='100-day SMA', color='green')
plt.plot(data.loc[data.positions == 1.0].index, 
         data.short_mavg[data.positions == 1.0],
         '^', markersize=10, color='m', label='buy')
plt.plot(data.loc[data.positions == -1.0].index, 
         data.short_mavg[data.positions == -1.0],
         'v', markersize=10, color='k', label='sell')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.legend()
plt.grid()
plt.show()
```

Please note that this is a very basic trading strategy and may not always result in wins. It's always recommended to use more sophisticated strategies and consider other factors like trading volume, market sentiment, etc. Also, always backtest your strategy before live trading.