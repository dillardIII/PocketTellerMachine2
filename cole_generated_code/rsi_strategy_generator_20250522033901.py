from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple implementation of a Relative Strength Index (RSI) strategy generator using Python and the pandas library. This code assumes that you have a pandas DataFrame `df` with a 'Close' column representing the closing prices of a stock.

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

def rsi_strategy(df, window=14):
    df['RSI'] = calculate_rsi(df['Close'], window)
    df['Buy_Signal'] = (df['RSI'] < 30)
    df['Sell_Signal'] = (df['RSI'] > 70)
    return df

# Assuming df is your DataFrame with a 'Close' column
df = rsi_strategy(df)
```

This code adds two new columns to the DataFrame: 'RSI' and 'Buy_Signal', 'Sell_Signal'. 'RSI' is the calculated Relative Strength Index. 'Buy_Signal' is True on days where the RSI is below 30 (indicating the stock is oversold and might be a good time to buy), and 'Sell_Signal' is True on days where the RSI is above 70 (indicating the stock is overbought and might be a good time to sell).

Please note that this is a very simple strategy and might not be profitable in real trading. Always backtest your strategies before using them in live trading.