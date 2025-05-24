Sure, I can provide a basic example of a simple trading strategy using Python. Here, we will use the Moving Average Crossover strategy. This strategy is one of the most commonly used strategies in the trading world. It's based on the principle of buying a security when its short-term moving average crosses above its long-term moving average, and selling the security when its short-term moving average crosses below its long-term moving average.

Please note that this is a simplified example and real-world trading strategies can be much more complex. Also, this code will not run unless you have the necessary data and the pandas library.

```python
import pandas as pd
import numpy as np

# Assuming we have a DataFrame 'df' with 'Close' prices
df = pd.read_csv('path_to_your_file.csv')

# Calculate the short-term moving average
short_window = 10
df['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Calculate the long-term moving average
long_window = 30
df['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create a 'signals' DataFrame with the signal strategy
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0

# Create signals
signals['signal'][short_window:] = np.where(df['short_mavg'][short_window:] 
                                            > df['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)
```

In this code, we first calculate the short-term and long-term moving averages. Then, we create a signal when the short moving average crosses the long moving average. A buy signal is generated when the short moving average is greater than the long moving average, and a sell signal is generated when the short moving average is less than the long moving average. 

Remember, this is a very basic strategy and doesn't take into account transaction costs, slippage, risk management, or other important factors for a real trading strategy. Also, the choice of moving average periods (10 and 30 in this case) can significantly affect the strategy performance, and they should be optimized based on historical data.