Sure, I can provide a simple Python code that simulates a trading strategy. This strategy will be based on a simple moving average (SMA) crossover, which is a popular strategy in algorithmic trading. 

Please note that this is a very basic strategy and real-world trading strategies can be much more complex and require careful backtesting and risk management.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for required stocks
data = yf.download('AAPL','2016-01-01','2021-12-31')

# Calculate short-term simple moving average
ShortEMA = data.Close.ewm(span=12, adjust=False).mean()

# Calculate long-term simple moving average
LongEMA = data.Close.ewm(span=26, adjust=False).mean()

# Create signals based on crossover
data['Buy_Signal_Flag'] = np.where(ShortEMA > LongEMA, 1, 0)
data['Sell_Signal_Flag'] = np.where(ShortEMA < LongEMA, 1, 0)

# Generate trading orders
Buy_Signals = data[data['Buy_Signal_Flag'] == 1]
Sell_Signals = data[data['Sell_Signal_Flag'] == 1]

print("Buy signals:\n", Buy_Signals)
print("Sell signals:\n", Sell_Signals)
```

This Python script uses the `yfinance` library to download historical data for Apple Inc. (AAPL) from Yahoo Finance. It then calculates the short-term and long-term exponential moving averages (EMA) of the closing prices. A buy signal is generated when the short-term EMA crosses above the long-term EMA, and a sell signal is generated when the short-term EMA crosses below the long-term EMA.

Please note that this script does not take into account transaction costs or slippage, and it assumes that you can trade at the closing price of each day, which may not be possible in reality.