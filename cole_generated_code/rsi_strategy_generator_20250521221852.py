from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple implementation of a Relative Strength Index (RSI) strategy generator using Python and the pandas library. This code assumes that you have a pandas DataFrame `df` with a 'Close' column representing the closing prices of a stock.

```python
import pandas as pd
import numpy as np

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

def generate_rsi_strategy(df, rsi_window=14, rsi_upper=70, rsi_lower=30):
    df['RSI'] = calculate_rsi(df['Close'], rsi_window)
    df['Buy_Signal'] = (df['RSI'] < rsi_lower)
    df['Sell_Signal'] = (df['RSI'] > rsi_upper)
    return df

# Use the function on your DataFrame
df = generate_rsi_strategy(df)
```

This code first calculates the RSI for each day in the DataFrame. Then, it generates a 'Buy_Signal' whenever the RSI drops below a certain lower threshold (indicating the stock may be oversold and is a good time to buy), and a 'Sell_Signal' whenever the RSI goes above a certain upper threshold (indicating the stock may be overbought and is a good time to sell).

Please note that this is a very simple strategy and may not be profitable in real trading. Always backtest your strategies before live trading.