In order to increase the number of trades, you would need to adjust the trading strategy. However, without knowing the specifics of the current trading strategy, it's difficult to provide a specific code. 

Here is a simple example of a trading strategy in Python using the `yfinance` package to download stock data and `pandas` to handle the data. This strategy buys a stock when the 50-day moving average crosses above the 200-day moving average (a "golden cross") and sells when the 50-day moving average crosses below the 200-day moving average (a "death cross"). 

```python
import yfinance as yf
import pandas as pd

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def golden_cross(stock):
    data = yf.download(stock, start='2020-01-01', end='2022-12-31')
    data['50_SMA'] = calculate_sma(data['Close'], 50)
    data['200_SMA'] = calculate_sma(data['Close'], 200)
    buy_signals = (data['50_SMA'] > data['200_SMA']) & (data['50_SMA'].shift(1) < data['200_SMA'].shift(1))
    sell_signals = (data['50_SMA'] < data['200_SMA']) & (data['50_SMA'].shift(1) > data['200_SMA'].shift(1))
    data['Buy_Signal'] = buy_signals
    data['Sell_Signal'] = sell_signals
    return data

stock = 'AAPL'
data = golden_cross(stock)
```

This strategy will increase or decrease the number of trades based on the stock's price movements. If you want to increase the number of trades, you could use a shorter moving average. For example, you could use a 10-day and 50-day moving average instead of a 50-day and 200-day moving average. 

```python
def golden_cross(stock):
    data = yf.download(stock, start='2020-01-01', end='2022-12-31')
    data['10_SMA'] = calculate_sma(data['Close'], 10)
    data['50_SMA'] = calculate_sma(data['Close'], 50)
    buy_signals = (data['10_SMA'] > data['50_SMA']) & (data['10_SMA'].shift(1) < data['50_SMA'].shift(1))
    sell_signals = (data['10_SMA'] < data['50_SMA']) & (data['10_SMA'].shift(1) > data['50_SMA'].shift(1))
    data['Buy_Signal'] = buy_signals
    data['Sell_Signal'] = sell_signals
    return data

stock = 'AAPL'
data = golden_cross(stock)
```

This will generate more trades because the stock's price is more likely to cross a shorter moving average. However, keep in mind that more trades does not necessarily mean better performance. It's important to evaluate the performance of the trading strategy and adjust it as necessary.