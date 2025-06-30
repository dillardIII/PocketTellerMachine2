from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code that uses pandas and yfinance libraries to implement two trading strategies: Moving Average Crossover and Relative Strength Index (RSI). 

Please note that this is a very basic implementation and real-world trading strategies would be much more complex and would also consider many other factors.

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr
from datetime import datetime
import matplotlib.pyplot as plt
from ta.trend import SMAIndicator
from ta.momentum import RSIIndicator

# Download historical data for required stocks
ticker = "AAPL"
yf.pdr_override()
start_date = datetime(2020, 1, 1)
end_date = datetime(2021, 12, 31)
data = pdr.get_data_yahoo(ticker, start_date, end_date)

# Moving Average Crossover Strategy
def MA_crossover(data, short_window, long_window):
    SMA1 = SMAIndicator(data['Close'], short_window)
    SMA2 = SMAIndicator(data['Close'], long_window)
    data['SMA1'] = SMA1.sma_indicator()
    data['SMA2'] = SMA2.sma_indicator()
    data['Buy_Signal'] = (data['SMA1'] > data['SMA2']).astype(int)
    data['Sell_Signal'] = (data['SMA1'] < data['SMA2']).astype(int)
    return data

# Relative Strength Index (RSI) Strategy
def RSI_strategy(data, period):
    rsi = RSIIndicator(data['Close'], period)
    data['RSI'] = rsi.rsi()
    data['Buy_Signal'] = (data['RSI'] < 30).astype(int)
    data['Sell_Signal'] = (data['RSI'] > 70).astype(int)
    return data

# Implementing the strategies
data_MA = MA_crossover(data.copy(), 50, 200)
data_RSI = RSI_strategy(data.copy(), 14)

# Print the data
print(data_MA)
print(data_RSI)
```

In this code, the Moving Average Crossover strategy generates a buy signal when the short-term moving average crosses above the long-term moving average, and a sell signal when the short-term moving average crosses below the long-term moving average.

The RSI strategy generates a buy signal when the RSI drops below 30 (indicating oversold conditions) and a sell signal when the RSI rises above 70 (indicating overbought conditions).

Please note that this code does not include any risk management or portfolio optimization techniques, and it does not take into account transaction costs or slippage. It is intended to serve as a basic example of how one might implement trading strategies in Python.