from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code using pandas library to generate RSI strategy:

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

def generate_rsi_strategy(data, window=14):
    # Calculate RSI
    data['RSI'] = calculate_rsi(data['Close'], window)

    # Create signals
    data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0)  # oversold condition
    data['Sell_Signal'] = np.where((data['RSI'] > 70), -1, 0)  # overbought condition

    # Generate strategy
    data['RSI_Strategy'] = data['Buy_Signal'] + data['Sell_Signal']
    return data

# Load data
data = pd.read_csv('data.csv')  # replace with your data file
data = generate_rsi_strategy(data)

# Print data with RSI strategy
print(data)
```

This script calculates the RSI of the closing prices and generates a trading strategy based on it. A buy signal is generated when the RSI is below 30 (oversold condition) and a sell signal is generated when the RSI is above 70 (overbought condition). The strategy is then calculated by adding the buy and sell signals.

Please replace `'data.csv'` with your actual data file path and make sure that your data has a 'Close' column for closing prices. If your data uses different column name, please adjust the code accordingly.