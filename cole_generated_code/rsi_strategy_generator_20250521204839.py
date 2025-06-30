from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code using the `pandas` and `yfinance` libraries to generate an RSI strategy.

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

    data['Buy_Signal_Price'] = buy_signals
    data['Sell_Signal_Price'] = sell_signals

    return data

ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2022-12-31')
rsi_strategy(data)
```

This code first calculates the RSI for the given data and window period (default is 14 days as it is commonly used in RSI calculation). Then it generates buy signals when the RSI is below 30 (indicating oversold conditions) and sell signals when the RSI is above 70 (indicating overbought conditions). The prices at these points are added to the data frame. 

Please note that this is a very basic RSI strategy and might not be profitable without further optimization and risk management. Always backtest your strategies before live trading.