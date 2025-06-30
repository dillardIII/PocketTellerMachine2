from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple implementation of a Relative Strength Index (RSI) strategy generator in Python. This code assumes that you have a pandas DataFrame `df` with a 'Close' column for the closing prices.

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

def generate_rsi_strategy(df, window=14):
    df['RSI'] = calculate_rsi(df['Close'], window)
    df['Buy_Signal'] = (df['RSI'] < 30)
    df['Sell_Signal'] = (df['RSI'] > 70)
    return df

# Usage:
# df = pd.read_csv('your_data.csv')
# df_with_signals = generate_rsi_strategy(df)
```

In this code, `calculate_rsi` function calculates the RSI for the given data and window. The `generate_rsi_strategy` function adds the RSI to the DataFrame and generates Buy and Sell signals based on the RSI. A Buy signal is generated when the RSI goes below 30 (oversold condition) and a Sell signal is generated when the RSI goes above 70 (overbought condition).

Please replace `'your_data.csv'` with your actual data file. Also, make sure that your data is sorted in ascending order by date.