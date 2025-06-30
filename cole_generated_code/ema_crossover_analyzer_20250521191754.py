from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that uses pandas library to calculate Exponential Moving Average (EMA) and analyze its crossover.

```python
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def plot_graph(data, short_ema, long_ema):
    plt.figure(figsize=(12,5))
    plt.title('Close Price', fontsize = 18)
    plt.plot(data['Close'], label='Close Price', color = 'blue')
    plt.plot(short_ema, label='Short/Fast EMA', color = 'red')
    plt.plot(long_ema, label='Long/Slow EMA', color = 'green')
    plt.xlabel('Date', fontsize = 18)
    plt.ylabel('Close Price USD ($)', fontsize = 18)
    plt.legend(loc='upper left')
    plt.show()

def ema_crossover_analyzer(stock, short_window, long_window):
    # Fetch the data
    data = pdr.get_data_yahoo(stock)

    # Calculate short and long EMA
    short_ema = calculate_ema(data['Close'], short_window)
    long_ema = calculate_ema(data['Close'], long_window)

    # Create signals
    data['Buy_Signal'] = (short_ema > long_ema)
    data['Sell_Signal'] = (short_ema < long_ema)

    # Plot the close price and EMAs
    plot_graph(data, short_ema, long_ema)

    return data

# Analyze EMA crossover for Apple stock with short EMA window of 12 days and long EMA window of 26 days
ema_crossover_analyzer('AAPL', 12, 26)
```

This script fetches the stock data, calculates the short and long EMA, generates buy and sell signals based on the crossover of these EMAs, and plots the close price along with the EMAs. 

Please note that you need to install pandas_datareader library to fetch the stock data. You can install it using pip:

```python
pip install pandas_datareader
```

Also, this is a very basic script and may not be suitable for real trading. You should consider factors like transaction costs, slippage, risk management, etc. before using such a strategy for trading.