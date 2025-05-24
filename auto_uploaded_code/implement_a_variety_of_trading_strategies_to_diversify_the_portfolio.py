Here are some basic examples of trading strategies implemented in Python. Note that these are very simplified versions of the strategies and real-world implementation would require much more complexity and risk management.

1. Buy and Hold Strategy: This strategy involves buying a stock and holding it for a long period of time, regardless of fluctuations in the market.

```python
def buy_and_hold(data, symbol):
    data['Buy and Hold'] = data[symbol]
    return data
```

2. Simple Moving Average Crossover: This strategy involves buying a stock when its short-term moving average crosses above its long-term moving average, and selling it when the short-term moving average crosses below the long-term moving average.

```python
def simple_moving_average(data, symbol, short_window, long_window):
    data['Short MA'] = data[symbol].rolling(window=short_window).mean()
    data['Long MA'] = data[symbol].rolling(window=long_window).mean()
    data['Buy Signal'] = (data['Short MA'] > data['Long MA']).astype(int)
    data['Sell Signal'] = (data['Short MA'] < data['Long MA']).astype(int)
    return data
```

3. Mean Reversion Strategy: This strategy involves buying a stock when it falls below its mean price over a certain period, and selling it when it rises above its mean price.

```python
def mean_reversion(data, symbol, window):
    data['Mean'] = data[symbol].rolling(window=window).mean()
    data['Buy Signal'] = (data[symbol] < data['Mean']).astype(int)
    data['Sell Signal'] = (data[symbol] > data['Mean']).astype(int)
    return data
```

Remember, these are just basic examples and real trading strategies would involve much more complexity, including risk management, position sizing, and possibly the use of derivatives. Also, these strategies do not take into account transaction costs, which can significantly impact the profitability of a strategy.