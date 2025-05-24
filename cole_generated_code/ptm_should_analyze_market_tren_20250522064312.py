To complete this task, we would need to use a library like pandas for data analysis and manipulation, yfinance to download historical market data from Yahoo finance, and matplotlib for data visualization. 

Here's a simple example of how you might set up a system to analyze market trends and set up alerts for potential trading opportunities. This example only considers simple moving averages as a trading signal, but you could incorporate more complex algorithms or machine learning models to make more accurate predictions.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def analyze_trends(symbol):
    # Download historical data as dataframe
    data = yf.download(symbol, start='2020-01-01', end='2022-12-31')

    # Calculate 50-day and 200-day simple moving averages
    data['SMA_50'] = calculate_sma(data['Close'], 50)
    data['SMA_200'] = calculate_sma(data['Close'], 200)

    # Plot closing price and moving averages
    plt.figure(figsize=(12,6))
    plt.plot(data['Close'], label='Close')
    plt.plot(data['SMA_50'], label='50-day SMA')
    plt.plot(data['SMA_200'], label='200-day SMA')
    plt.title('Stock price and SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

    # Generate trading signals and alerts
    buy_signals = (data['SMA_50'] > data['SMA_200']) & (data['SMA_50'].shift() < data['SMA_200'].shift())
    sell_signals = (data['SMA_50'] < data['SMA_200']) & (data['SMA_50'].shift() > data['SMA_200'].shift())

    if buy_signals.any():
        print(f"Buy signal for {symbol} on {buy_signals.idxmax().date()}")
    if sell_signals.any():
        print(f"Sell signal for {symbol} on {sell_signals.idxmax().date()}")

analyze_trends('AAPL')
```

This script downloads historical data for the specified symbol (in this case, AAPL), calculates 50-day and 200-day simple moving averages, plots the closing price and moving averages, and then generates buy and sell signals based on when the 50-day SMA crosses the 200-day SMA. 

Please note that this is a very basic example and real-world trading systems are much more complex and take many more factors into account. Also, this script does not actually perform any trades, it only analyzes data and generates signals.