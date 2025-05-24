Here is a simple Python code that uses the `pandas` library to calculate the Exponential Moving Average (EMA) and analyze the crossover points. This code assumes that you have a `pandas` DataFrame `df` that contains the prices. 

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'Price' is the column with prices
# Calculate the EMA for short and long windows
short_ema = df['Price'].ewm(span=12, adjust=False).mean()
long_ema = df['Price'].ewm(span=26, adjust=False).mean()

# Create a DataFrame to hold the calculated EMAs
ema_df = pd.DataFrame()
ema_df['Short EMA'] = short_ema
ema_df['Long EMA'] = long_ema

# Function to detect the crossover
def detect_crossover(short_ema, long_ema):
    crossover_points = []
    
    for i in range(1, len(short_ema)):
        if short_ema[i] > long_ema[i] and short_ema[i-1] < long_ema[i-1]:
            crossover_points.append(i)
        elif short_ema[i] < long_ema[i] and short_ema[i-1] > long_ema[i-1]:
            crossover_points.append(i)
    
    return crossover_points

# Detect the crossover points
crossover_points = detect_crossover(ema_df['Short EMA'], ema_df['Long EMA'])

# Print the crossover points
for point in crossover_points:
    print(f"Crossover point at index {point}, price: {df['Price'][point]}")
```

This code calculates the EMA for short (12 periods) and long (26 periods) windows, then it checks for crossover points. A crossover point is detected when the short EMA crosses the long EMA. If the short EMA is above the long EMA and it was below in the previous period, it's a bullish crossover. If the short EMA is below the long EMA and it was above in the previous period, it's a bearish crossover. The crossover points are then printed out.