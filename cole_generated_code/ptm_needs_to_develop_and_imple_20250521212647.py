from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code for a trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in trading. It's a strategy where two moving averages of different lengths are calculated, and a trade is made when these two averages cross.

Please note that this is a very basic strategy and in real trading scenarios, strategies can get very complex. Also, this code assumes that you have a pandas DataFrame 'df' that contains 'Close' prices of a stock.

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and it has a column 'Close' 
# which represents the close price of each trading day

# Calculate short-term simple moving average
short_sma = df['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = df['Close'].rolling(window=100).mean()

# Create a column 'Signal' such that if short-term moving average is 
# greater than long-term moving average then set Signal as 1 else 0
df['Signal'] = 0.0  
df['Signal'][short_sma > long_sma] = 1.0

# Create a column 'Position' which is the difference of present and 
# previous day's 'Signal' column. This column will give us actual 
# trading orders
df['Position'] = df['Signal'].diff()

# Print DataFrame
print(df)
```

In this code, 'Signal' 1 means "Buy" and 'Signal' 0 means "Sell". 'Position' 1 means "Enter" and 'Position' -1 means "Exit".

Please replace the window parameters in short_sma and long_sma as per your strategy. Also, you may want to use Exponential Moving Average (EMA) instead of Simple Moving Average (SMA), depending on your strategy.

Remember, this is a very basic strategy and might not be profitable. In real-world scenarios, trading strategies involve a lot more factors like volume, bid-ask spread, market trends, etc. Also, it's important to backtest any strategy before live trading.