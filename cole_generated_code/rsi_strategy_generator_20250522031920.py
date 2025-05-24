The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here's a simple Python code to generate an RSI trading strategy using the `pandas` and `yfinance` libraries.

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

def rsi_strategy(data, window=14):
    rsi = calculate_rsi(data['Close'], window)
    data['RSI'] = rsi

    buy_signals, sell_signals = [], []

    for i in range(len(data)):
        if data['RSI'].iloc[i] < 30:  # oversold condition
            buy_signals.append(data['Close'].iloc[i])
            sell_signals.append(float('nan'))
        elif data['RSI'].iloc[i] > 70:  # overbought condition
            sell_signals.append(data['Close'].iloc[i])
            buy_signals.append(float('nan'))
        else:
            buy_signals.append(float('nan'))
            sell_signals.append(float('nan'))

    return buy_signals, sell_signals

ticker = yf.Ticker("AAPL")
data = ticker.history(period="1y")

buy_signals, sell_signals = rsi_strategy(data)
data['Buy_Signal_Price'] = buy_signals
data['Sell_Signal_Price'] = sell_signals

print(data)
```

This script calculates the RSI for the closing prices of AAPL over the past year. It generates buy signals when the RSI drops below 30 (indicating oversold conditions) and sell signals when the RSI rises above 70 (indicating overbought conditions). The buy and sell signal prices are then added to the data frame.