Sure, I can provide a basic example of a trading strategy using Python. This strategy will be a simple moving average crossover strategy. 

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the lookback periods for the fast and slow moving averages
fast_period = 10
slow_period = 50

# Get the stock data
df = web.DataReader(stock, 'yahoo', start='01/01/2010', end='01/01/2022')

# Calculate the fast and slow moving averages
df['Fast_MA'] = df['Close'].rolling(window=fast_period).mean()
df['Slow_MA'] = df['Close'].rolling(window=slow_period).mean()

# Create a column to hold the trading signals
df['Signal'] = 0.0

# Generate the trading signals (1 for buy, -1 for sell)
df['Signal'][fast_period:] = np.where(df['Fast_MA'][fast_period:] > df['Slow_MA'][fast_period:], 1.0, -1.0)

# Calculate the daily returns of the strategy
df['Return'] = df['Signal'].shift() * df['Close'].pct_change()

# Calculate the cumulative returns of the strategy
df['Cumulative Return'] = (1 + df['Return']).cumprod()

# Print the last few rows of the DataFrame
print(df.tail())
```

This strategy buys the stock when the fast moving average is above the slow moving average and sells the stock when the fast moving average is below the slow moving average. The returns of the strategy are calculated based on these trading signals.

Please note that this is a very simple strategy and is unlikely to be profitable without further refinement. It's also important to consider transaction costs and slippage in a real trading environment. 

Also, this strategy is not meant to diversify risk. Diversification typically involves holding a portfolio of different assets that are not perfectly correlated. This could be achieved by running this strategy on multiple stocks and combining the results, or by using a different strategy altogether.