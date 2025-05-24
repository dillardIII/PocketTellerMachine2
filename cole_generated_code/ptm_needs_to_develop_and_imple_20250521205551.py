Sure, I can provide a simple example of a Python code for a trading strategy. This strategy is called Moving Average Crossover, which is a popular strategy used in algorithmic trading. 

Please note that this is a very basic example and real-world trading strategies are much more complex and involve many more factors.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    sma = calculate_sma(data, short_window)
    ema = calculate_ema(data, long_window)

    buy_signal = (sma > ema)
    sell_signal = (sma < ema)

    data['Buy_Signal'] = np.where(buy_signal, 1, 0)
    data['Sell_Signal'] = np.where(sell_signal, -1, 0)

    return data

def fetch_data(ticker):
    data = web.DataReader(ticker, 'yahoo', start='01-01-2010', end='01-01-2022')
    return data['Close']

ticker = 'AAPL'
data = fetch_data(ticker)
trading_data = trading_strategy(data, 50, 200)
print(trading_data)
```

This script fetches the historical data for a given ticker symbol (in this case, 'AAPL' for Apple Inc.) and calculates the simple moving average (SMA) and exponential moving average (EMA) for the specified short and long windows. When the SMA crosses above the EMA, it generates a buy signal, and when it crosses below, it generates a sell signal.

Please note that you will need to install the `pandas_datareader` library to fetch the data from Yahoo Finance. You can install it using pip:

```
pip install pandas_datareader
```

Also, remember that this is a very basic strategy and in real-world scenarios, you would need to consider transaction costs, risk management, portfolio diversification, and many other factors. Always do thorough backtesting before implementing any trading strategy.