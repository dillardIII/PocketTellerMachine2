from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python code that uses pandas library to calculate Exponential Moving Average (EMA) and analyze the crossover points. 

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Function to calculate EMA
def EMA(df, period, column='Close'):
    return df[column].ewm(span=period, adjust=False).mean()

# Function to determine when crossover occurs
def crossover(df, column1, column2):
    # Create an empty list to store the crossover points
    crossover_points = []
    
    # Loop through the DataFrame
    for i in range(1, len(df)):
        # If the fast EMA crosses above the slow EMA
        if df[column1].iloc[i] > df[column2].iloc[i] and df[column1].iloc[i-1] < df[column2].iloc[i-1]:
            crossover_points.append(df.index[i])
        # If the fast EMA crosses below the slow EMA
        elif df[column1].iloc[i] < df[column2].iloc[i] and df[column1].iloc[i-1] > df[column2].iloc[i-1]:
            crossover_points.append(df.index[i])
    return crossover_points

# Fetching historical data
df = pdr.get_data_yahoo('AAPL', '2020-01-01', '2022-12-31')

# Calculate the fast and slow EMA
df['Fast_EMA'] = EMA(df, 12)
df['Slow_EMA'] = EMA(df, 26)

# Determine the crossover points
crossover_points = crossover(df, 'Fast_EMA', 'Slow_EMA')

# Plotting
plt.figure(figsize=(12,5))
plt.plot(df.index, df['Close'], label='Close Price', color='blue')
plt.plot(df.index, df['Fast_EMA'], label='Fast EMA', color='red')
plt.plot(df.index, df['Slow_EMA'], label='Slow EMA', color='green')
plt.scatter(crossover_points, [df['Close'][x] for x in crossover_points], color='black', marker='o')
plt.legend(loc='upper left')
plt.show()
```

This script fetches historical data for Apple Inc. (AAPL) from Yahoo Finance, calculates the 12-day and 26-day EMA, determines the crossover points, and plots the close price, fast EMA, slow EMA, and crossover points.

Please note that you need to install pandas_datareader, matplotlib and pandas libraries to run this script. You can install them using pip:

```
pip install pandas_datareader matplotlib pandas
```