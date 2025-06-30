from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple example of how you might implement a new trading strategy in Python using the pandas library. This strategy is known as a moving average crossover, which is when the price of an asset moves above or below its moving average, indicating a potential buy or sell opportunity.

```python
import pandas as pd
import numpy as np

# Assuming we have a DataFrame 'df' with 'Close' prices
df = pd.read_csv('your_trading_data.csv')

# Calculate the short-term simple moving average
short_sma = df['Close'].rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma = df['Close'].rolling(window=100).mean()

# Create a column in the DataFrame to hold the trading signals
df['signal'] = 0.0

# Generate trading signals based on the crossover strategy
df['signal'][short_sma > long_sma] = 1.0
df['signal'][short_sma < long_sma] = -1.0

# Calculate the daily returns of the strategy
df['strategy_returns'] = df['signal'].shift() * df['Close'].pct_change()

# Print the total return of the strategy
total_return = df['strategy_returns'].cumsum()[-1]
print(f'Total return: {total_return * 100:.2f}%')
```

This script will read in your trading data, calculate the short-term and long-term simple moving averages, generate trading signals based on these averages, calculate the daily returns of the strategy, and print the total return.

Please note that this is a very basic trading strategy and should not be used for actual trading without further refinement and testing. Always do your own research and consider the risks before trading.