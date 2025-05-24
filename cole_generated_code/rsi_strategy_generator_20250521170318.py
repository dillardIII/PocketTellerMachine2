The Relative Strength Index (RSI) is a momentum oscillator that can help us to identify the general market trend. Below is a Python code to generate RSI and make trading decisions based on it.

You will require `pandas` and `yfinance` to fetch historical stock data, and `matplotlib` library to visualize the output.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

def RSI(df, period = 14, column = 'Close'):

    # Calculate price differences
    delta = df[column].diff()

    # Separate positive and negative differences
    gain, loss = delta.copy(), delta.copy()
    gain[gain < 0] = 0
    loss[loss > 0] = 0
    
    # Calculate average gain and average loss over given period
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = abs(loss.rolling(window=period).mean())

    # Calculate RSI
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

# Fetch historical data
ticker = 'AAPL'
df = yf.download(ticker, start='2022-01-01', end='2023-01-01')

# Calculate RSI
df['RSI'] = RSI(df)

# RSI strategy: buy when RSI < 30 (oversold), sell when RSI > 70 (overbought)
df['Buy_Signal'] = np.where(df['RSI'] < 30, 1, 0)
df['Sell_Signal'] = np.where(df['RSI'] > 70, 1, 0)

# Plot RSI, buy signals and sell signals
plt.figure(figsize=(12, 9))
plt.plot(df['RSI'], label='RSI', color='blue')
plt.axhline(30, color='red', linestyle='--') # oversold line
plt.axhline(70, color='green', linestyle='--') # overbought line
plt.legend(loc='upper left')
plt.show()
```

In this code:

- Fetches historical data for any given ticker
- Calculates RSI of the close prices
- Generates a "Buy_Signal" whenever the RSI goes below 30 (indicating the stock might be oversold)
- Generates a "Sell_Signal" whenever the RSI goes above 70 (indicating the stock might be overbought)
- Plots the RSI values and the levels at which we considered the stock oversold or overbought.

Please install necessary libraries using pip if not installed,
```
pip install pandas yfinance matplotlib numpy
```