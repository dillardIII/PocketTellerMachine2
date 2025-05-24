Sure, I can help you to write a basic Python code for a simple trading strategy. However, please note that in real-world scenarios, trading strategies can be very complex and require a deep understanding of financial markets and data analysis. 

Here's a simple moving average crossover strategy using Python:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker, start='2020-01-01', end=datetime.today().strftime('%Y-%m-%d'))

# Calculate moving averages
short_sma = ticker_data.Close.rolling(window=20).mean()
long_sma = ticker_data.Close.rolling(window=100).mean()

# Create signals based on crossover
ticker_data['Buy_Signal'] = np.where(short_sma > long_sma, 1, 0)
ticker_data['Sell_Signal'] = np.where(short_sma < long_sma, -1, 0)

# Generate trading orders
ticker_data['Trade'] = ticker_data['Buy_Signal'] + ticker_data['Sell_Signal']

# Print the DataFrame
print(ticker_data)

# Plotting
plt.figure(figsize=(12,5))
plt.title('Close Price', fontsize=18)
plt.plot(ticker_data['Close'], label='Close Price', color='blue', alpha=0.35)
plt.plot(short_sma, label='Short/Fast EMA', color='red',alpha=0.35)
plt.plot(long_sma, label='Middle/Medium EMA', color='orange', alpha=0.35)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.legend(loc='upper left')
plt.show()
```

This script downloads historical data for a specific stock (in this case, Apple Inc.), calculates short-term and long-term simple moving averages (SMA), generates buy/sell signals based on the crossover of these SMAs, and plots the close price and SMAs. 

Please note that this is a very basic strategy and may not be profitable in real trading. It's always recommended to backtest any strategy before live trading. Also, this script doesn't take into account trading fees or slippage. 

You would need to install the `yfinance`, `pandas`, `numpy`, and `matplotlib` libraries to run this script.