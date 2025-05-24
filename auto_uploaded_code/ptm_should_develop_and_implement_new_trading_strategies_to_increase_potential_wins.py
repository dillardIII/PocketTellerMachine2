As a language model AI developed by OpenAI, I can provide you with a basic example of a Python code that simulates a simple trading strategy. However, please note that this is a very simplified version and real-world trading involves many more factors and complexities. This code is for educational purposes only and should not be used for real trading without proper knowledge and understanding.

```python
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Assume we have a DataFrame 'df' with 'Date' and 'Close' columns
df = pd.read_csv('stock_data.csv')  # replace with your actual data file
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculate the short-term (fast) and long-term (slow) moving averages
df['Fast_MA'] = df['Close'].rolling(window=10).mean()  # 10-day MA
df['Slow_MA'] = df['Close'].rolling(window=50).mean()  # 50-day MA

# Create a column 'Buy_Signal' where if fast MA is greater than slow MA then True else False
df['Buy_Signal'] = np.where(df['Fast_MA'] > df['Slow_MA'], True, False)

# Create a column 'Sell_Signal' where if fast MA is less than slow MA then True else False
df['Sell_Signal'] = np.where(df['Fast_MA'] < df['Slow_MA'], True, False)

# Assume we start with no stock and $10000 cash
stock = 0
cash = 10000

# Go through the DataFrame row by row
for index, row in df.iterrows():
    # If we get a buy signal and we don't hold the stock
    if row['Buy_Signal'] and stock == 0:
        # Buy as much as we can
        stock = cash / row['Close']
        cash = 0
    # If we get a sell signal and we hold the stock
    elif row['Sell_Signal'] and stock > 0:
        # Sell all our stock
        cash = stock * row['Close']
        stock = 0

# Calculate the total value (cash + stock value)
total_value = cash + stock * df.iloc[-1]['Close']

print(f'Total value: ${total_value:.2f}')
```

This code implements a simple moving average crossover strategy, where we buy the stock when the 10-day moving average crosses above the 50-day moving average, and sell when it crosses below. This strategy assumes that upward momentum will continue when the short-term average becomes higher than the long-term average, and vice versa.

Please note that this is a very simplistic strategy and in real trading you would need to consider transaction costs, risk management, diversification, and many other factors. Always consult with a financial advisor before making trading decisions.