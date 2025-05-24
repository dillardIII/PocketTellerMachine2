Sure, I can provide a simple example of a Python code for a trading strategy. This strategy is a simple moving average crossover strategy. It is a basic strategy where a short-term moving average crosses above (bullish) or below (bearish) a long-term moving average.

Please note that this is a very basic strategy and in real trading scenarios, strategies can get very complex involving multiple indicators, machine learning models, and risk management techniques.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

# Download historical data for required stocks
ticker = "AAPL"
tickerData = yf.Ticker(ticker)
data = tickerData.history(period='1d', start='2010-1-1', end=datetime.today().strftime('%Y-%m-%d'))

# Calculate short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create a column 'Signal' such that if short-term sma is greater than long-term sma then 1 else 0
data['Signal'] = 0.0  
data['Signal'][short_sma > long_sma] = 1.0

# Create a column 'Position' which is a day-to-day difference of the 'Signal' column
data['Position'] = data['Signal'].diff()

# Print the DataFrame
print(data)

# Create a trading order: if 'Position' is 1 then 'Buy' else if 'Position' is -1 then 'Sell'
for i in range(len(data)):
    if data['Position'].iloc[i] == 1:
        print("Buy on date: ", data.index[i])
    elif data['Position'].iloc[i] == -1:
        print("Sell on date: ", data.index[i])
```

This code uses the `yfinance` library to download historical stock price data, calculates short-term and long-term simple moving averages, generates a trading signal based on the crossover of these averages, and finally generates trading orders based on these signals.

Please install necessary libraries by using `pip install pandas yfinance numpy` if they are not installed yet.

Remember, this is a very basic trading strategy and should not be used for actual trading without proper backtesting and risk management.