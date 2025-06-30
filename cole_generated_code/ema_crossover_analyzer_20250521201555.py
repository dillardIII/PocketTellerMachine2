from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python script that uses the pandas library to calculate the Exponential Moving Average (EMA) and analyze the crossover points. This script assumes that you have a pandas DataFrame `df` with a 'Close' column representing the closing prices of a stock.

```python
import pandas as pd
import numpy as np

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def analyze_crossovers(data, short_window, long_window):
    short_ema = calculate_ema(data['Close'], short_window)
    long_ema = calculate_ema(data['Close'], long_window)

    data['Short_EMA'] = short_ema
    data['Long_EMA'] = long_ema

    # Create column to hold the Buy/Sell signals
    data['Buy_Signal'] = np.where(short_ema > long_ema, 1, 0)
    data['Sell_Signal'] = np.where(short_ema < long_ema, 1, 0)

    buy_signals = data[data['Buy_Signal'] == 1]
    sell_signals = data[data['Sell_Signal'] == 1]

    return buy_signals, sell_signals

# Assuming df is your DataFrame and 'Close' is your column with closing prices
buy_signals, sell_signals = analyze_crossovers(df, 12, 26)

print("Buy Signals:")
print(buy_signals)

print("Sell Signals:")
print(sell_signals)
```

This script calculates the EMA for a short window and a long window. It then creates two new columns in the DataFrame: 'Buy_Signal' and 'Sell_Signal'. A buy signal is generated when the short EMA crosses above the long EMA, and a sell signal is generated when the short EMA crosses below the long EMA. The script then prints out the data points where these crossovers occur. 

Please replace `df` with your actual data frame and 'Close' with the actual column name of closing prices. Also, you can adjust the short and long window periods as per your requirements. The values 12 and 26 are commonly used for EMA crossover analysis.