from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple implementation of a Relative Strength Index (RSI) strategy generator using Python and pandas library. The RSI is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market.

```python
import pandas as pd
import numpy as np

def calculate_rsi(data, period):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    average_gain = up.rolling(window=period).mean()
    average_loss = abs(down.rolling(window=period).mean())
    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def generate_rsi_strategy(data, rsi_period, rsi_upper, rsi_lower):
    # Calculate RSI
    data['RSI'] = calculate_rsi(data['Close'], rsi_period)
    
    # Create signals
    data['Buy_Signal'] = np.where((data['RSI'] < rsi_lower), 1, 0)
    data['Sell_Signal'] = np.where((data['RSI'] > rsi_upper), -1, 0)
    
    # Generate strategy
    data['Strategy'] = data['Buy_Signal'] + data['Sell_Signal']
    
    return data

# Load data
data = pd.read_csv('data.csv')

# Generate RSI strategy
rsi_strategy = generate_rsi_strategy(data, rsi_period=14, rsi_upper=70, rsi_lower=30)

print(rsi_strategy)
```

In this code, the `calculate_rsi` function calculates the RSI for a given data series and period. The `generate_rsi_strategy` function generates buy and sell signals based on the RSI. A buy signal is generated when the RSI is below the lower threshold (oversold condition), and a sell signal is generated when the RSI is above the upper threshold (overbought condition). The final strategy is the sum of the buy and sell signals. 

Please replace `'data.csv'` with your actual data file path. The data file should contain a 'Close' column for closing prices. The RSI period, upper, and lower thresholds can be adjusted to fit your strategy.