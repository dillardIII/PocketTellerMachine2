Sure, here's a simple implementation of an RSI (Relative Strength Index) strategy generator using Python and the pandas library. This code assumes that you have a pandas DataFrame `df` with a 'Close' column for closing prices.

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
    df['Buy_Signal'] = (df['RSI'] < 30) # Buy when RSI is less than 30
    df['Sell_Signal'] = (df['RSI'] > 70) # Sell when RSI is greater than 70
    return df

# Usage:
# df = pd.read_csv('your_data.csv')
# df_with_signals = rsi_strategy(df)
```

This code calculates the RSI for a given window of days (default is 14) and adds it as a new column to the DataFrame. It then generates 'Buy_Signal' and 'Sell_Signal' columns, which are True on days where the RSI is below 30 (indicating the asset is oversold and may be a good time to buy) and above 70 (indicating the asset is overbought and may be a good time to sell), respectively.

Please replace `'your_data.csv'` with your actual data file path. Also, this is a very simple strategy and may not be profitable in real trading. Always backtest your strategies before live trading.