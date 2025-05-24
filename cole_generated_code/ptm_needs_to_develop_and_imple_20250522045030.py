Sure, here's a simple example of a trading strategy implemented in Python using the pandas library for data manipulation and analysis. This strategy is based on moving averages, a common indicator in technical analysis.

Please note that this is a very basic strategy and should not be used for actual trading without further refinement and testing. Also, this code assumes that you have historical trading data in a pandas DataFrame called `df` with 'Close' prices.

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and it has a 'Close' column
# df = pd.read_csv('your_data.csv')

# Define the lookback period for slow and fast moving averages
slow_ma_period = 50
fast_ma_period = 25

# Calculate slow and fast moving averages
df['slow_ma'] = df['Close'].rolling(window=slow_ma_period).mean()
df['fast_ma'] = df['Close'].rolling(window=fast_ma_period).mean()

# Create a column for the trading signals
df['signal'] = 0.0

# Generate trading signals based on moving averages (buy if fast MA is above slow MA, sell if below)
df.loc[df['fast_ma'] > df['slow_ma'], 'signal'] = 1.0
df.loc[df['fast_ma'] < df['slow_ma'], 'signal'] = -1.0

# Calculate daily returns
df['daily_returns'] = df['Close'].pct_change()

# Calculate strategy returns
df['strategy_returns'] = df['signal'].shift() * df['daily_returns']

# Calculate cumulative returns
df['cumulative_returns'] = (1 + df['strategy_returns']).cumprod()

# Print the DataFrame
print(df)
```

This code will generate trading signals based on the relationship between a fast and a slow moving average of the closing prices. When the fast moving average is above the slow one, it generates a buy signal (1.0), and when it's below, a sell signal (-1.0). Then it calculates the daily and strategy returns, as well as the cumulative returns of the strategy.