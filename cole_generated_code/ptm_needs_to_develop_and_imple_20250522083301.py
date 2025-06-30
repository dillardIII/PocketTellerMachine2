from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple Python code example of a trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in trading, it's simple and effective. 

Please note that this is a basic example and real-world trading strategies can be much more complex, involving many more factors and sophisticated algorithms.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data):
    # Calculate SMA and EMA
    sma = calculate_sma(data['Close'], 50)
    ema = calculate_ema(data['Close'], 50)
    
    # Create a 'Signal' column
    data['Signal'] = 0.0  
    data['Signal'][50:] = np.where(sma[50:] > ema[50:], 1.0, 0.0)

    # Generate trading orders
    data['Position'] = data['Signal'].diff()

def plot(data):
    # Plot the closing price, SMA, EMA
    plt.figure(figsize=(10,5))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['SMA'], label='50-day SMA', color='red')
    plt.plot(data['EMA'], label='50-day EMA', color='green')
    plt.title('Stock Price with SMA and EMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

# Fetch data
data = web.DataReader('AAPL', data_source='yahoo', start='01-01-2020', end='31-12-2020')

# Implement the trading strategy
trading_strategy(data)

# Plot the data
plot(data)
```

This code fetches historical stock price data for Apple Inc. (AAPL) from Yahoo Finance, calculates the 50-day Simple Moving Average (SMA) and Exponential Moving Average (EMA), generates trading signals based on the crossover of SMA and EMA, and plots the closing price, SMA, and EMA.

Please note that you need to install pandas_datareader library to fetch data from Yahoo Finance. You can install it using pip:

```bash
pip install pandas_datareader
```

Also, this is a very basic strategy and might not be profitable in real trading. Always backtest your strategy before live trading.