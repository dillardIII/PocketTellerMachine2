The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code that uses the `pandas` and `yfinance` libraries to generate a basic RSI strategy for a given stock.

```python
import pandas as pd
import yfinance as yf

def calculate_rsi(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window=window).mean()
    average_loss = abs(down.rolling(window=window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def rsi_strategy(ticker, start_date, end_date, rsi_window, overbought, oversold):
    data = yf.download(ticker, start=start_date, end=end_date)
    data['RSI'] = calculate_rsi(data['Close'], rsi_window)
    data['Buy_Signal'] = (data['RSI'] < oversold)
    data['Sell_Signal'] = (data['RSI'] > overbought)
    return data

ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-12-31'
rsi_window = 14
overbought = 70
oversold = 30

data = rsi_strategy(ticker, start_date, end_date, rsi_window, overbought, oversold)
print(data)
```

This code downloads historical data for a given stock using the `yfinance` library, calculates the RSI for each day, and generates buy and sell signals based on the RSI. The `rsi_strategy` function takes as input a ticker symbol, a start and end date for the historical data, a window for the RSI calculation, and thresholds for overbought and oversold conditions. The function returns a DataFrame that includes the original data, the calculated RSI, and the buy and sell signals.