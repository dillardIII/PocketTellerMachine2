The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a basic RSI trading strategy:

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

def implement_RSI_strategy(data, window=14):
    data['RSI'] = calculate_RSI(data['Close'], window)
    data['Buy_Signal'] = (data['RSI'] < 30)
    data['Sell_Signal'] = (data['RSI'] > 70)
    return data

# Download historical data
ticker = 'AAPL'
start_date = datetime(2020, 1, 1)
end_date = datetime(2021, 12, 31)
data = yf.download(ticker, start=start_date, end=end_date)

# Implement RSI strategy
data = implement_RSI_strategy(data)

# Plotting
plt.figure(figsize=(12,5))
plt.plot(data['RSI'], label='RSI', color='red')
plt.axhline(0, linestyle='--', alpha=0.5, color='black')
plt.axhline(10, linestyle='--', alpha=0.5, color='blue')
plt.axhline(20, linestyle='--', alpha=0.5, color='orange')
plt.axhline(30, linestyle='--', alpha=0.5, color='green')
plt.axhline(70, linestyle='--', alpha=0.5, color='green')
plt.axhline(80, linestyle='--', alpha=0.5, color='orange')
plt.axhline(90, linestyle='--', alpha=0.5, color='blue')
plt.axhline(100, linestyle='--', alpha=0.5, color='black')
plt.title('RSI plot')
plt.show()
```

In this code, we first define a function to calculate the RSI. We then define another function to implement the RSI strategy, where we generate a buy signal when the RSI is below 30 (oversold condition) and a sell signal when the RSI is above 70 (overbought condition). We then download historical data for a specific ticker using the `yfinance` library, implement the RSI strategy on this data, and plot the RSI values.