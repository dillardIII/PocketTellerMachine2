from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code that uses the `pandas` library to calculate the RSI and generate a trading strategy:

```python
import pandas as pd
import numpy as np

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

def generate_rsi_strategy(data, window=14):
    rsi = calculate_rsi(data, window)
    data = pd.concat([data, rsi], axis=1)
    data.columns = ['price', 'rsi']

    data['long_entry'] = data.rsi < 30
    data['long_exit'] = data.rsi > 70
    data['short_entry'] = data.rsi > 70
    data['short_exit'] = data.rsi < 30

    data['positions_long'] = np.nan
    data.loc[data.long_entry,'positions_long']= 1
    data.loc[data.long_exit,'positions_long']= 0

    data['positions_short'] = np.nan
    data.loc[data.short_entry,'positions_short']= -1
    data.loc[data.short_exit,'positions_short']= 0

    data = data.fillna(method='ffill')
    data['positions'] = data.positions_long + data.positions_short

    return data

# Test the function with some price data
price_data = pd.DataFrame({'price': np.random.rand(100) * 100})
strategy = generate_rsi_strategy(price_data)
print(strategy)
```

This code first calculates the RSI for the given price data. Then, it generates a trading strategy based on the RSI. The strategy goes long when the RSI is below 30 (oversold condition) and exits the long position when the RSI is above 70 (overbought condition). Similarly, it goes short when the RSI is above 70 and exits the short position when the RSI is below 30. The final positions are calculated by adding the long and short positions.