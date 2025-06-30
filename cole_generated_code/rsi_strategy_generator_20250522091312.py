from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple implementation of a Relative Strength Index (RSI) strategy generator in Python using the pandas library for data manipulation and the yfinance library to get stock data:

```python
import pandas as pd
import yfinance as yf

def calculate_rsi(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window).mean()
    average_loss = abs(down.rolling(window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def rsi_strategy(ticker, window=14):
    data = yf.download(ticker, start='2020-01-01', end='2022-12-31')
    data['RSI'] = calculate_rsi(data['Close'], window)

    buy_signals, sell_signals = [], []
    for i in range(len(data)):
        if data['RSI'].iloc[i] < 30:
            buy_signals.append(data['Close'].iloc[i])
            sell_signals.append(float('nan'))
        elif data['RSI'].iloc[i] > 70:
            sell_signals.append(data['Close'].iloc[i])
            buy_signals.append(float('nan'))
        else:
            buy_signals.append(float('nan'))
            sell_signals.append(float('nan'))

    data['Buy_Signal_Price'] = buy_signals
    data['Sell_Signal_Price'] = sell_signals

    return data

data = rsi_strategy("AAPL")
print(data)
```

This script downloads historical data for a given ticker (in this case, AAPL), calculates the RSI, and generates buy and sell signals. A buy signal is generated when the RSI goes below 30 (indicating oversold conditions), and a sell signal is generated when the RSI goes above 70 (indicating overbought conditions).

Please note that this is a very basic implementation of an RSI strategy and may not be suitable for live trading without further refinement.