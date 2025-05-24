Sure, here is a simple Python code that simulates a trading strategy. This strategy is based on moving averages. When the short-term average is greater than the long-term average, it's a signal to buy. When the short-term average is less than the long-term average, it's a signal to sell.

```python
import pandas as pd
import numpy as np

# Assuming we have a DataFrame 'df' with 'Close' prices
df = pd.DataFrame(np.random.randint(100,200,size=(100, 1)), columns=['Close'])

# Calculate short-term simple moving average
short_sma = df['Close'].rolling(window=5).mean()

# Calculate long-term simple moving average
long_sma = df['Close'].rolling(window=20).mean()

# Create a column 'Signal' such that if short-term sma is greater than long-term sma then 1 else 0
df['Signal'] = 0.0  
df['Signal'][short_sma > long_sma] = 1.0

# Create a column 'Position' which is the difference of the 'Signal' column
df['Position'] = df['Signal'].diff()

# Print the DataFrame
print(df)
```

In this code, we are using a random data for the 'Close' prices. In a real-world scenario, you would replace this with actual closing prices of the stocks you are interested in.

Please note that this is a very basic trading strategy and might not be profitable in a real-world scenario. Always backtest your strategies with historical data before you start trading with real money.

Also, the code doesn't actually execute any trades. It just gives signals when to buy and when to sell. You would need to integrate this with a trading platform API in order to actually execute trades.