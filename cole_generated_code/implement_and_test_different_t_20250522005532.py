Sure, here's a simple Python code that simulates two different trading strategies: Buy and Hold, and Simple Moving Average Crossover. We will use the `yfinance` library to download stock data and `pandas` for data manipulation.

Please note that this is a very basic implementation and real trading strategies are much more complex and involve more factors.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol 
def download_data(stock, start='2000-01-01', end='2020-12-31'):
    data = yf.download(stock, start, end)
    return data

# Implement Buy and Hold strategy
def buy_and_hold(data, cash):
    shares = cash / data['Close'].iloc[0]
    ending_value = shares * data['Close'].iloc[-1]
    return ending_value

# Implement Simple Moving Average Crossover strategy
def SMA_crossover(data, cash, short_window=50, long_window=200):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1).mean()
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    shares = 0
    for i in range(len(signals)):
        if signals['positions'].iloc[i] == 1:
            shares += cash / data['Close'].iloc[i]
            cash = 0
        elif signals['positions'].iloc[i] == -1:
            cash += shares * data['Close'].iloc[i]
            shares = 0
    ending_value = cash + shares * data['Close'].iloc[-1]
    return ending_value

# Test the strategies
data = download_data('AAPL')
cash = 10000  # Starting cash
print("Buy and Hold: ", buy_and_hold(data, cash))
print("SMA Crossover: ", SMA_crossover(data, cash))
```

This code first downloads historical data for the specified ticker symbol. Then it implements two strategies: Buy and Hold, which simply buys the stock at the beginning and sells at the end; and a Simple Moving Average Crossover, which buys the stock when the short-term moving average crosses above the long-term moving average and sells when it crosses below. The ending value of the portfolio is printed for each strategy.