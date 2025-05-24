Sure, here's a simple example of how you could set up a basic automated trading system using Python. This example uses the `yfinance` library to get stock data and the `pandas` library to handle the data. The trading strategy is a simple moving average crossover strategy.

Please note that this is a very basic example and real-world trading systems are much more complex and need to handle a lot more scenarios.

```python
import yfinance as yf
import pandas as pd

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def trading_strategy(data):
    # Buy when the short-term average crosses above the long-term average
    # Sell when the short-term average crosses below the long-term average
    buy_signals = (data['short'] > data['long']) & (data['short'].shift(1) < data['long'].shift(1))
    sell_signals = (data['short'] < data['long']) & (data['short'].shift(1) > data['long'].shift(1))
    data.loc[buy_signals, 'Buy_Signal'] = data.loc[buy_signals, 'Close']
    data.loc[sell_signals, 'Sell_Signal'] = data.loc[sell_signals, 'Close']

def backtest(data):
    # Assume we buy and sell at the closing price
    buy_prices = data['Buy_Signal'].dropna()
    sell_prices = data['Sell_Signal'].dropna()
    return sell_prices.sum() - buy_prices.sum()

# Get historical data
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')
data['short'] = calculate_sma(data['Close'], window=50)
data['long'] = calculate_sma(data['Close'], window=200)

# Apply the trading strategy
trading_strategy(data)

# Backtest the strategy
profit = backtest(data)
print(f'Profit: {profit}')
```

This code will download the historical data for the specified stock symbol (in this case, AAPL), calculate the short-term and long-term moving averages, apply the trading strategy to generate buy and sell signals, and then backtest the strategy by calculating the profit or loss.