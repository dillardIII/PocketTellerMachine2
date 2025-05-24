The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a RSI strategy.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Fetching the data
def get_data(symbol, start_date, end_date):
    df = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)
    return df

# Calculating RSI
def calculate_RSI(data, window):
    delta = data['Adj Close'].diff()
    up_days = delta.copy()
    up_days[delta<=0]=0.0
    down_days = abs(delta.copy())
    down_days[delta>0]=0.0
    RS_up = up_days.rolling(window).mean()
    RS_down = down_days.rolling(window).mean()
    rsi= 100-100/(1+RS_up/RS_down)
    data['RSI'] = rsi
    return data

# Implementing the strategy
def implement_RSI_strategy(data, buy_level, sell_level):
    data['Buy_Signal'] = np.where(data['RSI']<buy_level, 1, 0)
    data['Sell_Signal'] = np.where(data['RSI']>sell_level, -1, 0)
    return data

# Plotting the strategy
def plot_data(data, symbol):
    plt.figure(figsize=(12,5))
    plt.title('Buy and Sell Plot')
    plt.plot(data['Adj Close'], label=symbol, color = 'blue', alpha = 0.35)
    plt.plot(data.index, data['Buy_Signal'] * data['Adj Close'], '^', markersize = 10, color = 'g', label = 'buy signal', alpha = 1)
    plt.plot(data.index, data['Sell_Signal'] * data['Adj Close'], 'v', markersize = 10, color = 'r', label = 'sell signal', alpha = 1)
    plt.xlabel('Date',fontsize=15)
    plt.ylabel('Price',fontsize=15)
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

# Main function
def main():
    symbol = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2021-12-31'
    df = get_data(symbol, start_date, end_date)
    df = calculate_RSI(df, window=14)
    df = implement_RSI_strategy(df, buy_level=30, sell_level=70)
    plot_data(df, symbol)

if __name__ == "__main__":
    main()
```

This script fetches historical price data for a given symbol, calculates the RSI, generates buy/sell signals based on the RSI levels, and plots the strategy. Please note that this is a simple strategy and may not be profitable in real trading. Always backtest your strategies before live trading.