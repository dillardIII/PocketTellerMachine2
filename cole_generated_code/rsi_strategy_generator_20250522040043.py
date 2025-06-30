from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate an RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

def calculate_RSI(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window=window).mean()
    average_loss = abs(down.rolling(window=window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def implement_RSI_strategy(data, window):
    data['RSI'] = calculate_RSI(data['Close'], window)
    data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0) 
    data['Sell_Signal'] = np.where((data['RSI'] > 70), -1, 0) 
    return data

# Download historical data
ticker = "AAPL"
start_date = datetime(2020, 1, 1)
end_date = datetime.now()
data = yf.download(ticker, start=start_date, end=end_date)

# Implement the strategy
window = 14
data = implement_RSI_strategy(data, window)

# Plot the data
plt.figure(figsize=(12,5))
plt.plot(data['RSI'], label='RSI')
plt.axhline(0, linestyle='--', alpha=0.5, color='gray')
plt.axhline(10, linestyle='--', alpha=0.5, color='orange')
plt.axhline(20, linestyle='--', alpha=0.5, color='green')
plt.axhline(30, linestyle='--', alpha=0.5, color='red')
plt.axhline(70, linestyle='--', alpha=0.5, color='red')
plt.axhline(80, linestyle='--', alpha=0.5, color='green')
plt.axhline(90, linestyle='--', alpha=0.5, color='orange')
plt.axhline(100, linestyle='--', alpha=0.5, color='gray')
plt.title('RSI strategy')
plt.show()
```

This code first calculates the RSI for a given window of days. Then it generates buy signals when the RSI is less than 30 (oversold condition) and sell signals when the RSI is greater than 70 (overbought condition). The signals are plotted on a graph for visualization.